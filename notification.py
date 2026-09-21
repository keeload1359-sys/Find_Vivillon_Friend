import requests
from master import VIVILLON_NAMES, COUNTRY_NAMES, VIVILLON_IMAGE_URLS

def country_to_flag(country_code):
    return "".join(
        chr(ord(c.upper()) + 127397)
        for c in country_code
    )

def send(webhook_url, post):

    country_display = COUNTRY_NAMES[post['country']]
    vivillon_display = VIVILLON_NAMES[post['vivillon']]
    flag = country_to_flag(post['country'])
    img_url = VIVILLON_IMAGE_URLS[post['vivillon']]

    embed = {
        "title": "🦋 Vivillon Friend",

        "fields": [
            {
                "name": "Trainer Code",
                "value": post["trainer_code"],
                "inline": False
            },
            {
                "name": "Country",
                "value": f"{flag} {country_display}",
                "inline": True
            },
            {
                "name": "Vivillon",
                "value": f"{vivillon_display}（{post['vivillon']}）",
                "inline": True
            },
            {
                "name": "Time",
                "value": post["time"],
                "inline": False
            }
        ],

        "footer": {
            "text": "pokemon-friends.eu"
        }
    }

    if img_url:
        embed["thumbnail"] = {
            "url": img_url
        }

    payload = {
        "content": (
            f"{flag} {country_display}｜"
            f"{vivillon_display}（{post['vivillon']}）\n"
            f"{post['trainer_code']}"
        ),

        "embeds": [
            embed
        ]
    }

    response = requests.post(
        webhook_url,
        json=payload
    )

    return response.raise_for_status()