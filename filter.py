import re

def within_15minutes(time_text):
    match = re.search(r"(\d+) minutes ago", time_text)
    
    if match:
        minutes = int(match.group(1))
        return minutes <= 30
    elif time_text == "just now":
        return True  
    elif time_text == "a minute ago":
        return True
    else:
        return False
