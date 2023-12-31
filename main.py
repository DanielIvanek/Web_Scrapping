"""
WEB_Scapping: třetí projekt 
author: Daniel Ivánek 
email: ivanek.daniel99@gmail.com
discord: Notme#1275
"""
"""
Vytvoreno na rychlo s pomoci ai, kvuli uradu prace. Nasledne projekt predelam podle sebe. 
"""

import sys
import csv
from bs4 import BeautifulSoup
import requests
# import pandas

# arguments checks
def check_arguments():
    if len(sys.argv) != 3:
        print("You need to enter exactly two arguments")
        exit()
    elif not sys.argv[1].startswith("https://volby.cz"):
        print("Entered URL adress is not acceptable")
        exit()
    elif not sys.argv[2].endswith(".csv"):
        print("You must enter a .csv file to proceed")
        exit()


# retreive url adress from web
def get_url():
    main_url = sys.argv[1]
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

# retreive codes of towns from table
def get_town_codes():
    code_elements = get_url().find_all("td", {"class": "cislo"})
    codes = [code.get_text() for code in code_elements]
    return codes

# retreive names of towns from table
def get_town_names():
    town_elements = get_url().find_all("td", {"class": "overflow_name"})
    town_names = [town.get_text() for town in town_elements]
    return town_names

# Create a list with towns urls
def get_codes_url():
    url_towns = get_url().find_all("td", {"class": "cislo"})
    url_list = []
    for url in url_towns:
        url_list.append(url.find("a")["href"])
    sub_url = ["https://volby.cz/pls/ps2017nss/" + url_list[i] for i in range(len(url_list))]
    return sub_url

# získá informace z url jednotlivými obcí
def sub_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

# získá počet voličů v seznamu
def get_registered():
    register_list = []
    for url in get_codes_url():
        registered_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers="sa2")
        registered_list = [registered.get_text().replace("\xa0", "") for registered in registered_elements]
        register_list.extend(list(map(int, registered_list)))
    return register_list


# získá počet odevzdaných lístků
def get_envelopes():
    envelop_list = []
    for url in get_codes_url():
        envelopes_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers="sa3")
        envelopes_list = [envelopes.get_text().replace("\xa0", "") for envelopes in envelopes_elements]
        envelop_list.extend(list(map(int, envelopes_list)))
    return envelop_list

# získá počet platných hlasů
def get_valid_votes():
    validate_list = []
    for url in get_codes_url():
        valid_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers="sa6")
        valid_list = [valid.get_text().replace("\xa0", "") for valid in valid_elements]
        validate_list.extend(list(map(int, valid_list)))
    return validate_list

# získá první url s obcí
def sub_url_partis():
    response = requests.get(get_codes_url()[0])
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

# získá názvy všech stran
def get_party():
    party_elements = sub_url_partis().find_all("td", {"class": "overflow_name"})
    party_names = [party.get_text() for party in party_elements]
    return party_names

# vytvoří list se všemi hlasy v dané obci
def get_votes():
    votes_list = []
    for url in get_codes_url():
        votes_elements = sub_url(url).find_all("td", {"class": "cislo"}, headers=["t1sb3", "t2sb3"])
        get_votes = [votes.get_text().replace("\xa0", "") for votes in votes_elements]
        votes_list.append(list(map(int, get_votes)))
    return votes_list

# vytvoří se soubor dle druhého zadaného argumentu a vypíše se tabulka řádek po řádku
def csv_output():
    print("Downloading...")
    header = ["code", "location", "registered", "envelopes", "valid"] + get_party()

    rows = [header]
    town_codes = get_town_codes()
    town_names = get_town_names()
    registered = get_registered()
    envelopes = get_envelopes()
    valid_votes = get_valid_votes()
    party_votes = get_votes()

    for i in range(len(town_names)):
        row = [town_codes[i], town_names[i], registered[i], envelopes[i], valid_votes[i]] + party_votes[i]
        rows.append(row)

    with open(sys.argv[2], "w", newline="", encoding= "utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Download complete. Saved file: {sys.argv[2]}")


if __name__ == "__main__":
    check_arguments()
    csv_output()

