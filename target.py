from supabase_client import supabase

def get_users():
    response = (
        supabase
        .table("profiles")
        .select("user_id, discord_webhook_url")
        .execute()
    )

    return response.data

def get_target_vivillons(user_id):
    response = (
        supabase.table("target_vivillons")
        .select("vivillon_code")
        .eq("user_id", user_id)
        .execute()
    )

    return {row["vivillon_code"] for row in response.data}

def target(post, user_id):
    target_vivillons = get_target_vivillons(user_id)

    return post["vivillon"] in target_vivillons
