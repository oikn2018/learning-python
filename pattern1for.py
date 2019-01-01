# Simple right triangular pattern using for loops.
# Oikantik Nath, Dec 29, 2018

rows = int(input("How many rows of emojis do you want?"))

for i in range(1,rows):
    print("\U0001f600\t"*i)