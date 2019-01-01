# A copying game. Computer repeats whatever you say till you say "stop copying me"
# Oikantik Nath, Dec 30, 2018

print("Hello!")
message = input().lower()

while message != "stop copying me":
    print(message)
    message = input().lower()