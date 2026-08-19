from dotenv import load_dotenv
import os

load_dotenv()


def build_short_url(short_name: str) -> str:
    base_url = os.getenv("BASE_URL")
    return f"{base_url}/r/{short_name}"