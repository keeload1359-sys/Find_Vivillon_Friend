from supabase_client import supabase

def get_target_vivillons(user_id):
    response = (
        supabase.table("target_vivillons")
        .select("vivillon_code")
        .eq("user_id", user_id)
        .execute()
    )

    return {row["vivillon_code"] for row in response.data}
