import random
import string

def generate_password(length):

  lowercase = string.ascii_lowercase
  uppercase = string.ascii_uppercase
  digits = string.digits
  punctuation = string.punctuation

  # Combine all character sets
  all_characters = lowercase + uppercase + digits + punctuation

  password = random.choice(lowercase) + random.choice(uppercase) + random.choice(digits) + random.choice(punctuation)

  # Fill remaining characters with random selection from all characters
  password += ''.join(random.choices(all_characters, k=length - 4))

  # Shuffle the characters for better randomness
  password_list = list(password)  # Convert password to a list
  random.shuffle(password_list)
  password = ''.join(password_list)  # Convert list back to a string

  return password

def main(): #Prompts user for password length and number, generates passwords, and displays them.

  while True:
    try:
      # Get user input for password length
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length must be at least 8 characters. Please try again.")
        continue

      # Get user input for number of passwords
      num_passwords = int(input("Enter the number of passwords to generate: "))
      if num_passwords <= 0:
        print("Please enter a positive number of passwords to generate.")
        continue

      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Generate and display passwords
  for _ in range(num_passwords):
    password = generate_password(length)
    print(password)

if __name__ == "__main__":
  main()
