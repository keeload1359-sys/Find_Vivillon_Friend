import requests
from master import VIVILLON_NAMES, COUNTRY_NAMES

def country_to_flag(country_code):
    return "".join(
        chr(ord(c.upper()) + 127397)
        for c in country_code
    )

def send(webhook_url, post):
    message = (
        "=================================\n"
        "**Vivillon通知**\n"
        f"Trainer Code: {post['trainer_code']}\n"
        f"Country: {COUNTRY_NAMES[post['country']]}{country_to_flag(post['country'])}\n"
        f"Vivillon: {VIVILLON_NAMES[post['vivillon']]} ({post['vivillon']})\n"
        f"Time: {post['time']}\n"
        "=================================\n"
    )

    response = requests.post(
        webhook_url,
        json={
        "content": message
        }
    )

    return response