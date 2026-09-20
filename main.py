from scrape import scrape_latest_codes
from target import get_target_vivillons, get_rare_countries, get_excluded_countries
from user import get_users
from notification import send
from insert import save_post

def main():
    users = get_users()
    posts = scrape_latest_codes()

    new_posts = []

    for post in posts:
        if save_post(post):
            new_posts.append(post)

    rare_countries = get_rare_countries()

    for user in users:
        user_id = user["user_id"]

        target_vivillons = get_target_vivillons(user_id)
        excluded_countries = get_excluded_countries(user_id)

        for i in new_posts:

            if i["vivillon"] in target_vivillons:
                send(user["discord_webhook_url"], i)

            elif i["country"] in excluded_countries:
                continue

            elif i["country"] in rare_countries:
                send(user["discord_webhook_url"], i)

if __name__ == "__main__":
    main()
