
# context manager
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

lines = data.split("\n")

number_counter = 0
letter_counter = 0

for line in lines:
    for char in line:
        if char.isnumeric():
            number_counter += 1
        elif char.isalpha():
            letter_counter +=1

print(number_counter)
print(letter_counter)