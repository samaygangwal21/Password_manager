import random, string, csv



def random_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

def password_strength(password):
    if password.isdigit():
        return "weak"
    length = len(password)
    score = 0
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in "!@#$%^&*()" for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if length >= 8: score += 1

    if score <= 2:
        return "weak"
    elif score == 3:
        return "medium"
    else:
        return "strong"



rows = [["password", "strength"]]
for _ in range(300):
    pwd = random_password(random.randint(6, 14))
    rows.append([pwd, password_strength(pwd)])

with open("password_strength.csv", "w", newline="") as f:
    csv.writer(f).writerows(rows)

print("✅ Generated 300 synthetic passwords.")
