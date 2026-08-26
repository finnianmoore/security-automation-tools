# Security Automation Tools

A curated collection of Python and Bash scripts for security automation, penetration testing, and credential assessment workflows.

These tools were developed during practical security assessments and demonstrate automation, scripting, and problem-solving skills.

---

## Tools Overview

| Tool | Language | Purpose |
| :--- | :--- | :--- |
| OSINT Wordlist Generator | Python | Generates targeted, context-aware password wordlists based on OSINT data |
| Targeted Wordlist Generator | Python | Creates focused wordlists using company-specific terminology |
| Web Login Bruteforcer | Python | Multi-threaded credential spraying against web login forms |
| Credential Spray with Progress | Python | Refined credential spraying tool with progress tracking and rate limiting |
| Credential Spray Automation | Bash | Automates credential spraying using ffuf with multiple wordlists |

---

## Tools

### 1. OSINT Wordlist Generator (`wordlist-generator/osint-wordlist-generator.py`)

Generates a massive, targeted wordlist using OSINT-derived keywords.

**Key Features:**
- Combines company names, employee names, industry terms, and locations
- Applies case variations, leetspeak, and common transformations
- Generates combinations with years, special characters, and number suffixes
- Outputs approximately 350,000+ password candidates

**Usage:**
python3 osint-wordlist-generator.py

**Output:** massive_tpm_list.txt

---

### 2. Targeted Wordlist Generator (`wordlist-generator/targeted-wordlist-generator.py`)

A focused wordlist generator using specific company terminology.

**Key Features:**
- Uses company-specific names, phrases, and roles
- Applies leetspeak transformations
- Adds year and symbol variations
- Deduplicates output for efficiency

**Usage:**
python3 targeted-wordlist-generator.py

**Output:** ultimate_pasta.txt

---

### 3. Web Login Bruteforcer (`credential-spray/web-login-bruteforcer.py`)

A multi-threaded credential spraying tool for web login forms.

**Key Features:**
- Concurrent processing with ThreadPoolExecutor
- Detects successful logins via HTTP redirect analysis
- Terminates immediately upon finding valid credentials
- Handles SSL certificate warnings gracefully

**Usage:**
python3 web-login-bruteforcer.py

**Requirements:**
- master_usernames.txt (list of usernames, one per line)
- passwords.txt (list of passwords, one per line)

**Output:** WINNER.txt (username:password)

---

### 4. Credential Spray with Progress (`credential-spray/credential-spray-progress.py`)

A refined credential spraying tool with progress tracking and rate limiting.

**Key Features:**
- Progress tracking with real-time status updates
- Rate limiting to avoid detection
- Multiple wordlist support
- Clear success/failure detection

**Usage:**
python3 credential-spray-progress.py

**Requirements:**
- users.txt (list of usernames, one per line)
- Wordlist files (e.g., seasons.txt, months.txt, days.txt)

**Output:** credentials_found.txt

---

### 5. Credential Spray Automation (`automation-scripts/credential-spray-automation.sh`)

A Bash script that automates credential spraying using ffuf.

**Key Features:**
- Iterates through multiple wordlists
- Tests username:password combinations
- Saves successful hits to a results file

**Usage:**
./credential-spray-automation.sh

**Requirements:**
- ffuf installed
- targets.txt (list of usernames)
- Wordlist files in a wordlists/ directory

**Output:** WINNER.txt

---

## Installation

Clone the repository:

git clone https://github.com/finnianmoore/security-automation-tools.git
cd security-automation-tools

**Python Dependencies:**
pip install requests

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
