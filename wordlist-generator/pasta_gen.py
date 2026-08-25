import sys

# Base Intelligence gathered from the website
pastas = ["Bucatini", "Farfalle", "Fettuccine", "Linguine", "Pappardelle", "Penne", "Rigatoni", "Spaghetti", "Ziti", "Fusilli", "Tortellini"]
names = ["Alessandra", "Alanzo", "Adriano", "Ferruccio", "Giovanni", "Leo", "Mario", "Sonia", "Luigi", "Zia"]
phrases = ["AlDente", "Pastabilities", "Mentors", "PastaMentors", "Pasta", "Noodles", "Dream", "Cooking", "Smile", "Family", "Tradition", "Password", "Admin"]
seasons = ["Spring", "Summer", "Autumn", "Fall", "Winter"]

# Modifiers
years = ["2021", "2022", "2023", "2024", "2025", "2026", "21", "22", "23", "24", "25", "26", ""]
symbols = ["!", "@", "#", "$", "*", "?", ""]

# Compile all base words
base_words = pastas + names + phrases + seasons

# Add First+Last name combinations
base_words.extend(["AlessandraFettuccini", "AlanzoBucatini", "AdrianoPenne", "FerruccioTortellini", "GiovanniRigatoni", "LeoFusilli", "MarioLinguine"])

def apply_leet(word):
    """Translates a word into standard leetspeak based on P@55w0rd!"""
    leet_map = {'a': '@', 'A': '@', 'e': '3', 'E': '3', 'o': '0', 'O': '0', 's': '5', 'S': '5', 'i': '1', 'I': '1'}
    return "".join(leet_map.get(c, c) for c in word)

passwords = set()

print("[+] Generating permutations...")

for base in base_words:
    # We want three main formats for the base word: Normal, lowercase, and leetspeak
    formats = [base, base.lower(), apply_leet(base)]
    
    for fmt in formats:
        for year in years:
            for sym in symbols:
                # Add the combination to the set (sets automatically remove duplicates)
                passwords.add(f"{fmt}{year}{sym}")

# Write the final list to a text file
output_file = "ultimate_pasta.txt"
with open(output_file, "w") as f:
    for pwd in passwords:
        f.write(f"{pwd}\n")

print(f"[+] Done! Generated {len(passwords)} highly targeted passwords.")
print(f"[+] Saved to {output_file}")
