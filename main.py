from scrape import scrape_latest_codes
from target import target
from notification import send

WEBHOOK_URL = "https://discord.com/api/webhooks/1545046400562241558/g5Co1qVAN-jMbEh4toQ-dqkUIzlmr3N_keAvX5VWbcd4HGIQDeei48_18t-Zqpdrt2k4"

def main():
    posts = scrape_latest_codes()

    for i in posts:
        if target(i):
            send(WEBHOOK_URL, i)

if __name__ == "__main__":
    main()
