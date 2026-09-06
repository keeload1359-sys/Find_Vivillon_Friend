import os
from scrape import scrape_latest_codes
from target import target
from notification import send

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def main():
    posts = scrape_latest_codes()

    for i in posts:
        if target(i):
            send(WEBHOOK_URL, i)

if __name__ == "__main__":
    main()
