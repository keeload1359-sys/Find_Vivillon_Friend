import re
from datetime import datetime, timedelta, timezone

def estimate_time(time_text):
    now = datetime.now(timezone.utc)

    match = re.search(r"(\d+) minutes ago", time_text)
    
    if match:
        min = int(match.group(1))
        estimate =  now - timedelta(minutes = min)
    elif time_text == "just now":
        estimate = now
    elif time_text == "a minute ago":
        estimate = now - timedelta(minutes = 1) 

    return estimate.replace(microsecond=0)

def create_post_time_range(estimate):

    start_time = estimate - timedelta(minutes=1)
    end_time = estimate + timedelta(minutes=1)

    return (
        f'["{start_time.isoformat()}",'
        f'"{end_time.isoformat()}"]'
    )

