# opens ini file and assigns the content to data variable
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

# separates the lines in the file
lines = data.split("\n")

# initializes counter variables for letters and numbers
number_counter = 0
letter_counter = 0

# in each line, go through each character individually and assesses if it is a letter or number - returns boolean
for line in lines:
    for char in line:
        # increment counter for number or letter is boolean value is true
        if char.isnumeric():
            number_counter += 1
        elif char.isalpha():
            letter_counter +=1

# prints the results for user to see
print(f"There are {letter_counter} letter(s) and {number_counter} number(s)")