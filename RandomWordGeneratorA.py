import requests
from random import randint

print("Welcome to personalised username/password generator")
city = input("What is your name ? \n")
word = input("Enter your favourite word \n")



url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text%2Fplain'

r = requests.get(url,headers={'User-Agent': 'Custom'})
text = r.text

set_of_words = text.split()
index = randint(0,len(set_of_words))
random_word = set_of_words[index]


print(f"Your username/password could be {city}{random_word}{word}")

