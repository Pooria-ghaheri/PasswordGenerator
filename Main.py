import string
from random import *
import random

UserUpperWords = input("choose any upper case: ").upper()
UserLowerWords = input("choose any lower case: ").lower()

Symbols = string.punctuation
RanSymbols = (''.join(random.choice(Symbols) for i in range(10)))

characters = UserUpperWords + UserLowerWords
password = "".join(choice(characters) for x in range(randint(8, 40)))

OriginalPass = password + RanSymbols
OriginalPassword = "".join(choice(OriginalPass) for x in range(randint(8, 40)))

print(f'{OriginalPassword}')
