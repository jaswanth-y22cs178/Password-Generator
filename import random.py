import random
l = int(input("Enter Lenght of Password:"))
password=""
for i in range(l):
    num = random.randint(33,127)
    password = password + chr(num)
print("Generated Password is {0}"
.format(password))
    