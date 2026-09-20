from supabase_client import supabase
from collections import Counter

def get_target_vivillons(user_id):
    response = (
        supabase.table("target_vivillons")
        .select("vivillon_code")
        .eq("user_id", user_id)
        .execute()
    )

    return {row["vivillon_code"] for row in response.data}

def get_rare_countries():
    response = (
            supabase
            .table("vivillon_data")
            .select("country")
            .order("estimated_time", desc=True)
            .limit(1000)
            .execute()
        )

    countries = []
    for row in response.data:
        countries.append(row["country"])

    counts = Counter(countries)
    total = len(countries)
    rare_countries = set()

    for country, count in counts.items():
        per = count * 100 / total
        if per < 1.0:
            rare_countries.add(country)

    return rare_countries

#exclude
def get_excluded_countries(user_id):
    response = (
        supabase.table("excluded_countries")
        .select("country")
        .eq("user_id", user_id)
        .execute()
    )

    return {row["country"] for row in response.data}
