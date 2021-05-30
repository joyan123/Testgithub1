import webbrowser
import random


file = open("P:/words.txt", "r")
x = file.readlines()
k=len(x)

i = random.randint(0,len(x))
file = open("P:/words.txt", "r")
for i in range(0,i):
    file.readline()
word = file.readline()
print(word)
file.close()
y=("https://www.yourdictionary.com/"+word)
print(y)
webbrowser.open(y)