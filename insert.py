from estimate import estimate_time, create_post_time_range
from postgrest.exceptions import APIError
from supabase_client import supabase

def save_post(post):
    estimated_time = estimate_time(post["time"])
    try:
        response = (
            supabase.table("vivillon_data")
            .insert({
                    "trainer_code": post["trainer_code"],
                    "time": post["time"],
                    "country": post["country"],
                    "vivillon": post["vivillon"],
                    "estimated_time": estimated_time.isoformat(),
                    "post_time_range": create_post_time_range(estimated_time)
                })
            .execute()
        )
        return True

    except APIError as e:
        if e.code == "23P01":
            return False

