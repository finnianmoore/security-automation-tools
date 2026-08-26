import itertools

# Comprehensive OSINT Base Words
words = [
    # Seasons
    "spring", "summer", "autumn", "fall", "winter",
    # Pastas & Food
    "pasta", "fettuccini", "bucatini", "penne", "tortellini", "rigatoni", "fusilli", 
    "linguine", "noodles", "aldente", "macaroni", "spaghetti", "ravioli", "gnocchi",
    # Cheeses & Ingredients
    "parmesan", "mozzarella", "ricotta", "provolone", "pecorino", "sauce", "tomato", "garlic", "oliveoil",
    # Company Info
    "mentors", "thepastamentors", "tpm", "sanfrancisco", "california", "bayarea",
    # Employees
    "alessandra", "alanzo", "adriano", "ferruccio", "giovanni", "leo",
    # IT/Roles
    "chef", "trainer", "admin", "admin1", "root", "postmaster", "webadmin"
]

# Every year from 1990 to 2028 (e.g., 1995, 95, 2023, 23)
years = [str(y) for y in range(1990, 2029)] + [str(y)[-2:] for y in range(1990, 2029)]

# Common password suffixes
specials = ["!", "@", "#", "$", "%", "^", "&", "*", "!!", "!@", "1!", "123", "123!", "1234", ""]

def apply_cases(word):
    return [word.lower(), word.capitalize(), word.upper()]

def leet_speak(word):
    replacements = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    res = word.lower()
    for k, v in replacements.items():
        res = res.replace(k, v)
    return res

print("[+] Generating Massive TPM OSINT Wordlist...")
print("[+] This will generate roughly 350,000 contextual passwords. Please wait...")

with open("massive_tpm_list.txt", "w") as f:
    count = 0
    for w in words:
        # Get cases and leetspeak variations
        forms = apply_cases(w)
        forms.append(leet_speak(w))
        forms.append(leet_speak(w).capitalize())
        
        # Remove duplicates
        forms = list(set(forms))
        
        for form in forms:
            # Format: Word + Year + Special (e.g., Fusilli2023!)
            for y in years:
                for s in specials:
                    f.write(f"{form}{y}{s}\n")
                    count += 1
            
            # Format: Word + Special (e.g., Fusilli!)
            for s in specials:
                if s:
                    f.write(f"{form}{s}\n")
                    count += 1
            
            # Format: Word + Number (e.g., Fusilli1, Fusilli99!)
            for n in range(1, 101):
                f.write(f"{form}{n}\n")
                f.write(f"{form}{n}!\n")
                count += 2
                
    # Add combined names (e.g., LeoFusilli, lfusilli)
    combinations = [
        ("alessandra", "fettuccini"), ("alanzo", "bucatini"), ("adriano", "penne"), 
        ("ferruccio", "tortellini"), ("giovanni", "rigatoni"), ("leo", "fusilli")
    ]
    
    for first, last in combinations:
        combos = [
            first + last,
            first.capitalize() + last.capitalize(),
            first[0].lower() + last.lower(),
            first[0].upper() + last.capitalize()
        ]
        for c in combos:
            for y in years:
                for s in specials:
                    f.write(f"{c}{y}{s}\n")
                    count += 1

print(f"[+] Done! Successfully wrote {count} passwords to massive_tpm_list.txt")
