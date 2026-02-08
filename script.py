import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor

FILE_URL = "https://upfiles.com/jPRo6AQ" # REPLACE THIS
DAILY_GOAL = random.randint(1900, 2100)
CONCURRENT_USERS = 5 

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3) Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0"
]

def simulate_user(user_id):
    headers = {"User-Agent": random.choice(USER_AGENTS), "Referer": "https://www.google.com"}
    try:
        # Step 1: Visit site home (Human behavior)
        requests.get("/".join(FILE_URL.split("/")[:3]), headers=headers, timeout=10)
        time.sleep(random.uniform(2, 5)) 

        # Step 2: Download file
        with requests.get(FILE_URL, headers=headers, stream=True, timeout=120) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=1024 * 128): pass 
        
        # Step 3: Quick Dwell Time (Saves GitHub minutes)
        time.sleep(random.randint(5, 15))
        print(f"User {user_id} success.")
    except Exception as e: print(f"User {user_id} error: {e}")

def main():
    with ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:
        executor.map(simulate_user, range(1, DAILY_GOAL + 1))

if name == "main":
    main()
