# Security Automation Tools

A curated collection of Python and Bash scripts for security automation, penetration testing, and credential assessment workflows.

These tools were developed during practical security assessments and demonstrate automation, scripting, and problem-solving skills.

---

## Tools Overview

| Tool | Language | Purpose |
| :--- | :--- | :--- |
| OSINT Wordlist Generator | Python | Generates targeted, context-aware password wordlists based on OSINT data |
| Pasta Wordlist Generator | Python | Creates focused wordlists using company-specific terminology |
| Web Login Bruteforcer | Python | Multi-threaded credential spraying against web login forms |
| iRedAdmin Credential Spray | Python | Refined credential spraying tool with progress tracking and rate limiting |
| Credential Spray Automation | Bash | Automates credential spraying using ffuf with multiple wordlists |

---

## Tools

### 1. OSINT Wordlist Generator (`wordlist-generator/massive_tpm_gen.py`)

Generates a massive, targeted wordlist using OSINT-derived keywords.

**Key Features:**
- Combines company names, employee names, industry terms, and locations
- Applies case variations, leetspeak, and common transformations
- Generates combinations with years, special characters, and number suffixes
- Outputs approximately 350,000+ password candidates

**Usage:**
python3 massive_tpm_gen.py

**Output:** massive_tpm_list.txt

---

### 2. Pasta Wordlist Generator (`wordlist-generator/pasta_gen.py`)

A focused wordlist generator using specific company terminology.

**Key Features:**
- Uses company-specific pasta names, employee names, and phrases
- Applies leetspeak transformations
- Adds year and symbol variations
- Deduplicates output for efficiency

**Usage:**
python3 pasta_gen.py

**Output:** ultimate_pasta.txt

---

### 3. Web Login Bruteforcer (`credential-spray/brute_iredadmin.py`)

A multi-threaded credential spraying tool for web login forms.

**Key Features:**
- Concurrent processing with ThreadPoolExecutor
- Detects successful logins via HTTP redirect analysis
- Terminates immediately upon finding valid credentials
- Handles SSL certificate warnings gracefully

**Usage:**
python3 brute_iredadmin.py

**Requirements:**
- master_usernames.txt (list of usernames, one per line)
- roe_filtered_compliant.txt (list of passwords, one per line)

**Output:** WINNER.txt (username:password)

---

### 4. iRedAdmin Credential Spray (`credential-spray/iredadmin_final.py`)

A refined credential spraying tool with progress tracking and rate limiting.

**Key Features:**
- Progress tracking with real-time status updates
- Rate limiting to avoid detection
- Multiple wordlist support
- Clear success/failure detection

**Usage:**
python3 iredadmin_final.py

**Requirements:**
- users.txt (list of usernames, one per line)
- Wordlist files (e.g., seasons.txt, months.txt, days.txt)

**Output:** iredadmin_real_credentials.txt

---

### 5. Credential Spray Automation (`automation-scripts/sweep.sh`)

A Bash script that automates credential spraying using ffuf.

**Key Features:**
- Iterates through multiple wordlists
- Tests username:password combinations
- Saves successful hits to a results file

**Usage:**
./sweep.sh

**Requirements:**
- ffuf installed
- overnight_targets.txt (list of usernames)
- Wordlist files in ROE-wordlists/ directory

**Output:** WINNER.txt

---

## Installation

Clone the repository:

git clone https://github.com/finnianmoore/security-automation-tools.git
cd security-automation-tools

**Python Dependencies:**
pip install requests concurrent.futures urllib3

**Bash Dependencies:**
sudo apt install ffuf

---

## Disclaimer

These tools are for educational and authorized security testing purposes only. Do not use these tools for any illegal or unauthorized activities. Always obtain explicit written permission before testing any system or network.

---

## Author

Finnian Moore
GitHub: https://github.com/finnianmoore
LinkedIn: https://linkedin.com/in/finnian-moore-4ba7093b

---

## License

This project is for educational purposes only. Use at your own risk.
