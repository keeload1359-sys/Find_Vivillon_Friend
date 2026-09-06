TARGET_VIVILLON = {
    "SS",  # Sandstorm
    "TD",  # Tundra
    "IS",  # Icy Snow
    "PL",  # Polar
    "RV",  # River
    "SN",  # Sun
    "OC",  # Ocean
    "AP"   # Archipelago
}

def target(post):
    return post["vivillon"] in TARGET_VIVILLON
