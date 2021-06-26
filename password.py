import random
import string
# import string_utils         ---> first do--> pip install python-string-utils library


letters = string.ascii_letters 
symbols = string.punctuation 
numbers = string.digits

purpose = input("Where do you want to use this password? \n")

letters_no = int(input("Enter no of letters you want: "))     # enter required no of letters,digits,symbols
symbols_no = int(input("Enter no of symbols you want: "))
numbers_no = int(input("Enter no of numbers you want: "))





pletters="".join(random.choice(letters) for x in range(0,letters_no))   # string.join(iterable)
psymbols="".join(random.choice(symbols) for x in range(0,symbols_no))
pnumbers="".join(random.choice(numbers) for x in range(0,numbers_no))
password = pletters+psymbols+pnumbers
l = list(password)
random.shuffle(l)
password = "".join(l)


# print(string_utils.shuffle(password)) ---> it shuffles the string
