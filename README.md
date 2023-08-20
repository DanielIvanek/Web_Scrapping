# Web Scraping
# Volební Výsledky Scraper

Tento skript je určen k scrapování dat z volebních výsledků z webových stránek "[https://volby.cz/pls/ps2017nss/](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)". Získaná data jsou ukládána do CSV souboru.

## Použití

Před spuštěním skriptu ujistěte se, že máte nainstalované potřebné knihovny (requests, BeautifulSoup) a máte nainstalovaný Python.

1. Stažení repozitáře:

    ```bash
    Installing Python Packages From a Requirements File
    pip install -r requirements.txt
    ```

2. Spuštění skriptu s následujícími argumenty:

    ```bash
    python main.py <URL volebních výsledků> <Název výstupního CSV souboru>
    ```

   - `<URL volebních výsledků>` musí být platná URL adresa volebních výsledků na webu "[https://volby.cz/pls/ps2017nss/](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)".
   - `<Název výstupního CSV souboru>` musí být název souboru, do kterého chcete uložit data ve formátu CSV (např. "volebni_vysledky.csv").

3. Po dokončení scrapingu budete mít vytvořený CSV soubor s výsledky v aktuálním adresáři.



## Struktura Výstupního CSV Souboru

Výstupní CSV soubor bude mít následující strukturu:

- `code`: Kód obce
- `location`: Název obce
- `registered`: Počet voličů v seznamu
- `envelopes`: Počet vydaných obálek
- `valid`: Počet platných hlasů
- Každý sloupec pro jednotlivé kandidující strany bude obsahovat počet hlasů pro danou stranu.

## Poznámky

- Skript zpracovává pouze jednu stránku s volebními výsledky. Pokud chcete zpracovat více stránek, musíte upravit kód tak, aby procházel různé stránky výsledků.

- Skript může být rozšířen nebo upraven pro další analýzu dat podle vašich potřeb.

- Používejte tento skript zodpovědně a v souladu s právními předpisy.



