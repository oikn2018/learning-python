# Simple looping through numbers categorizing them as even or odd,and for 4 and 13, classifying them
# as unlucky.
# Oikantik Nath, Dec 29, 2018

for i in range(1,21):
    if i == 4 or i == 13:
        print(f"NUMBER {i}: UNLUCKY!!!")
    elif i % 2 == 0:
        print(f"NUMBER {i}: EVEN")
    else:
        print(f"NUMBER {i}: ODD")