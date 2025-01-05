import re

def assess_password_strength(password):
        return "Password Strength Level: Weak (Less than 3 criteria are met)."

def main():
    print("---------------- Password Complexity Checking Tool -----------------")
    print("Here are some quick tips for creating a secure password:")
    tips = [
        "1. Length: Aim for at least 12 characters.",
        "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
        "3. Avoid Common Words: Don't use easily guessable information.",
        "4. No Personal Info: Avoid using names, birthdays, or personal details.",
        "5. Use Passphrases: Consider combining multiple words or a sentence.",
        "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
        "7. Regular Updates: Change passwords periodically.",
        "8. Enable 2FA: Use Two-Factor Authentication where possible.",
        "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
        "10. Password Manager: Consider using one for secure and unique passwords."
    ]
    for tip in tips:
        print(tip)

    # Get user input for the password (visible to the user)
    password_input = input("\nEnter your password: ")

    # Masked password for display
    if len(password_input) > 2:
        masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]
    else:
        masked_password = password_input

    # Assess the password strength
    result = assess_password_strength(password_input)

    # Display the masked password and strength result
    print("\nEntered Password: {}".format(masked_password))
    print("")
    print(result)

if __name__ == "__main__":
    main()
