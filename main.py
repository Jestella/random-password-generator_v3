import random
import string

def randomPassword(stringLength=10):
  password_characters = string.ascii_letters + string.digits + string.punctuation

  return ''.join(random.choice(password_characters) for i in range(stringLength))

print("10 Passwords with letters, digits, and special characters!")
print("Password1: ",randomPassword())
print("Password2: ",randomPassword())
print("Password3: ",randomPassword())
print("Password4: ",randomPassword())
print("Password5: ",randomPassword())
print("Password6: ",randomPassword())
print("Password7: ",randomPassword())
print("Password8: ",randomPassword())
print("Password9: ",randomPassword())
print("Password10: ",randomPassword())


