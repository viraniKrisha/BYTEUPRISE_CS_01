def check_strength(password):
  """
  Evaluates password strength based on length, character types,
  and deduction rules.

  Args:
      password (str): The password to be checked.

  Returns:
      str: A descriptive message about password strength.
  """

  score = 0
  strength_message = ""

  # Check password length
  if len(password) >= 12:
    score += 1
    strength_message += "Length is good (>= 12 characters).\n"
  elif len(password) >= 8:
    strength_message += "Length is fair (8-11 characters).\n"
  else:
    strength_message += "Length is weak (less than 8 characters).\n"

  # Check for lowercase, uppercase, digits, and special characters
  has_lowercase = any(char.islower() for char in password)
  has_uppercase = any(char.isupper() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_special = any(char in "!@#$" for char in password)

  characters = [has_lowercase, has_uppercase, has_digit, has_special]
  score += sum(characters)

  if characters.count(True) < 3:
    strength_message += "Missing character types (lowercase, uppercase, digit, special).\n"

  # Deduction rules for common patterns or keyboard sequences
  deductions = 0
  if password.lower() in password.upper():
    deductions += 1
    strength_message += "Password contains only lowercase or uppercase characters.\n"
  if password in password[::-1]:  # Check for reversed password
    deductions += 1
    strength_message += "Password is a reversed version of itself.\n"
  if password in ''.join(chr(ord(c) + 1) for c in password):  # Check for keyboard sequence
    deductions += 1
    strength_message += "Password resembles a keyboard sequence.\n"

  score -= deductions
  strength_message = strength_message.strip()  # Remove trailing newline

  strength_levels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
  return strength_levels[min(score, 4)]  # Cap score at 4 (Very Strong)

# Get password input from the user
password = input("Enter your password: ")

# Check password strength and print the result
strength = check_strength(password)
print(f"Your password strength is: {strength}")
