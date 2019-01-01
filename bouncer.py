
# ask for age
age = input("How old are you? ")
# age 18-21 wristband
# age 21+ drink, normal entry
# else too young
if age:
    age = int(age)
    if age >= 18:
        print("partying allowed")
        if age > 21:
            print("drinking allowed")
        else:
            print("no drinking")
    else:
        print("no partying and no drinking")
else:
    print("YOU DIDN'T ENTER AN AGE!")