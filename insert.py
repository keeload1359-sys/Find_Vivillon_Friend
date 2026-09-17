from supabase import create_client
from estimate import estimate_time, create_post_time_range
from postgrest.exceptions import APIError
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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

