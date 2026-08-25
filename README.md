# Security Automation Tools

A collection of Python and Bash scripts I developed for penetration testing and security automation. These tools focus on:

- **OSINT Wordlist Generation** - Creating targeted password lists
- **Web Credential Spraying** - Automating login form testing
- **Security Scanning Automation** - Scripting repetitive tasks

## Tools

### 1. OSINT Wordlist Generator (`wordlist-generator/`)

Python script that creates context-aware password wordlists based on company and employee information.

**Key Features:**
- Generates customized wordlists for targeted assessments
- Uses OSINT techniques to create focused attack lists
- Outputs massive, tailored password lists

### 2. Web Login Bruteforcer (`credential-spray/`)

Multi-threaded Python script for testing web login forms.

**Key Features:**
- Concurrent processing for speed
- Handles SSL certificate issues gracefully
- Clean termination upon finding a match

### 3. Credential Spraying Automation (`automation-scripts/`)

Bash script for automating credential spraying attacks.

**Key Features:**
- Runs multiple wordlists against a target
- Captures successful hits
- Provides real-time feedback

## Usage

Each tool has its own README with detailed usage instructions. Please review the individual tool documentation before use.

## Disclaimer

These tools are for educational and authorized testing purposes only. Always obtain explicit written permission before testing any system. Do not use these tools for any illegal or unauthorized activities.
