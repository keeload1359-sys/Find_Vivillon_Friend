from scrape import scrape_latest_codes
from target import target, get_users
from notification import send
from insert import save_post

def main():
    users = get_users()
    posts = scrape_latest_codes()

    for i in posts:
        if save_post(i):         
            for user in users:
                user_id = user["user_id"]

                if target(i, user_id):
                    send(user["discord_webhook_url"], i)

if __name__ == "__main__":
    main()
