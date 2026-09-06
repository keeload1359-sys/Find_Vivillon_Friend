import requests

def send(webhook_url, post):
    message = (
        "=================================\n"
        "**Vivillon通知**\n"
        f"Trainer Code: {post['trainer_code']}\n"
        f"Country: {post['country']}\n"
        f"Vivillon: {post['vivillon']}\n"
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