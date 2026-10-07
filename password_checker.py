# Password Strength Checker - By Ritik | Lucknow Toolkit

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ 8 characters se bada rakho")

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Capital aur Small dono letters use karo")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Number add karo (0-9)")

    if any(c in "!@#$%^&*()_+-=" for c in password):
        score += 1
    else:
        feedback.append("❌ Symbol add karo (!@#$)")

    if score == 4:
        return "✅ STRONG - Ekdum Safe Hai!"
    elif score == 3:
        return "⚠️ MEDIUM - Thoda aur strong banao\n" + "\n".join(feedback)
    else:
        return "❌ WEAK - Hack ho sakta hai!\n" + "\n".join(feedback)

# Test
print("=== Lucknow Toolkit - Password Checker ===")
pw = input("Apna password daalo check karne ke liye: ")
print(check_strength(pw))