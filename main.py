from fed_scraper import fetch_beige_book_fed, fetch_report_boe, fetch_bulletin_ecb
from prompt_runner import run_custom_prompt

def main():
    general_prompt = (
        "Analyze the general economic sentiment of this report. "
        "Return a numeric score from -2 (very negative) to 2 (very positive), and nothing else."
    )
    trade_prompt = (
        "Assess ONLY the effects of trade, tariff barriers, and supply-chain disruptions in this report. "
        "Return one numeric score from -2 (severe negative shock) to 2 (positive/no shock), and nothing else."
    )

    reports = [
        ("Fed Beige Book", fetch_beige_book_fed),
        ("BoE Monetary Policy Report", fetch_report_boe),
        ("ECB Economic Bulletin", fetch_bulletin_ecb),
    ]

    for name, fetch in reports:
        print(f"\n=== {name} ===")
        text = fetch()
        print("Fetched report, running sentiment analysis...")

        gen = run_custom_prompt(text, general_prompt)
        trd = run_custom_prompt(text, trade_prompt)

        print(f"General sentiment score: {gen['average']} (scores: {gen['scores']})")
        print(f"Trade/supply shock score: {trd['average']} (scores: {trd['scores']})")

if __name__ == "__main__":
    main()
