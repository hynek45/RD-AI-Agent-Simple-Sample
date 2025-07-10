# AI Agent

Jednoduchý AI agent v Pythonu, který umí:
- odpovídat na běžné dotazy přes OpenAI API (`gpt-4o-mini`, endpoint `responses`)
- zjistit aktuální cenu Bitcoinu v USD a převést ji na CZK

## Požadavky

- Python 3.12+ (doporučeno)
- Testováno na WSL Ubuntu (Windows Subsystem for Linux)
- Virtuální prostředí (`venv`)
- OpenAI API klíč (uložený v `.env`)

## Instalace a spuštění (testováno na WSL Ubuntu)

1. **Otevři WSL Ubuntu terminál a přejdi do složky projektu:**

cd /mnt/c/Users/[tvůj_uzivatel]/Documents/ai_agent

2. **Nainstaluj modul pyth pro virtuální prostředí (pokud ještě není):**

sudo apt update
sudo apt install python3.12-venv

3. **Vytvoř a aktivuj virtuální prostředí:**

python3 -m venv .venv
source .venv/bin/activate

4. **Nainstaluj závislosti:**

pip install -r requirements.txt

5. **Vytvoř soubor `.env` ve složce projektu a vlož svůj OpenAI API klíč:**

OPENAI_API_KEY=sk-...tvůj_klíč...

6. **Spusť agenta:**

python agent.py

7. **Použití:**
- Pro dotaz na Bitcoin napiš například: `Jaká je aktuální cena bitcoinu?`
- Pro běžné dotazy napiš cokoliv jiného.
- Ukončení: napiš `exit` nebo `quit`.


## Struktura projektu

ai_agent/
- agent.py
- config.py
- .env
- requirements.txt
- tools/
  - bitcoin.py
  - currency.py
- README.md

## Poznámky

- **API klíč nikdy nesdílej veřejně!**
- Další nástroje lze přidávat do složky `tools` a rozšiřovat funkci `respond_to_query` v `agent.py`.

---
