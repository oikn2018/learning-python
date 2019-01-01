# Simple right triangular pattern using for loops.
# Oikantik Nath, Dec 29, 2018

rows = int(input("How many rows of emojis do you want?"))
i = 1

while i != rows:
    print("\U0001f600\t"*i)
    i += 1