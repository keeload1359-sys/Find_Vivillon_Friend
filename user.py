from supabase_client import supabase

def get_users():
    response = (
        supabase
        .table("profiles")
        .select("user_id, discord_webhook_url")
        .execute()
    )

    return response.data