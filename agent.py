import os
from dotenv import load_dotenv
from openai import OpenAI
from tools.bitcoin import fetch_bitcoin_usd
from tools.currency import usd_to_czk

# Načtení API klíče z .env
load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def call_llm(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="Jsi AI asistent, odpovídej česky a věcně.",
        input=prompt,
    )
    return response.output_text.strip()

def respond_to_query(query):
    if "bitcoin" in query.lower():
        btc_usd = fetch_bitcoin_usd()
        rate = usd_to_czk()
        btc_czk = btc_usd * rate
        return (
            f"Aktuální cena Bitcoinu je {btc_usd:.2f} USD "
            f"({btc_czk:.2f} CZK při kurzu {rate:.2f} CZK/USD)."
        )
    return call_llm(query)

def main():
    print("=== AI Agent ===")
    while True:
        user_input = input(">> ")
        if user_input.lower() in ("exit", "quit"):
            break
        answer = respond_to_query(user_input)
        print(answer)

if __name__ == "__main__":
    main()

