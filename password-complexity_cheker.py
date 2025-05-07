import string
import math
import time


def password_strength(password):
    feedback = []
    score = 0

    # Character sets
    lowers = sum(1 for c in password if c.islower())
    uppers = sum(1 for c in password if c.isupper())
    digits = sum(1 for c in password if c.isdigit())
    specials = sum(1 for c in password if c in string.punctuation)
    length = len(password)

    # Scoring logic
    if length >= 8:
        score += 1
        feedback.append("Good length (8+ characters).")
    else:
        feedback.append("Password should be at least 8 characters long.")

    if lowers:
        score += 1
        feedback.append("Contains lowercase letter(s).")
    else:
        feedback.append("Add lowercase letters.")

    if uppers:
        score += 1
        feedback.append("Contains uppercase letter(s).")
    else:
        feedback.append("Add uppercase letters.")

    if digits:
        score += 1
        feedback.append("Contains digit(s).")
    else:
        feedback.append("Add digits.")

    if specials:
        score += 1
        feedback.append("Contains special character(s).")
    else:
        feedback.append("Add special characters (e.g., !, @, #).")

    # Entropy estimation
    charset = 0
    if lowers:
        charset += 26
    if uppers:
        charset += 26
    if digits:
        charset += 10
    if specials:
        charset += len(string.punctuation)

    entropy = math.log2(charset ** length) if charset else 0

    # Cracking time (based on 1 billion guesses/second)
    guesses = 2 ** entropy
    crack_time_seconds = guesses / 1e9

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback,
        "crack_time_seconds": crack_time_seconds
    }


# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to assess: ")
    result = password_strength(pwd)
    print(f"\nStrength: {result['strength']}")
    print("Feedback:")
    for note in result['feedback']:
        print(f"- {note}")
    print(f"Estimated time to crack: {result['crack_time_seconds']:.2e} seconds")
