# mileage calculator
# 1 km = 0.621371 miles

kms = input("Enter number of kilometres you ran today:")
miles = float(kms)/0.621371

print(f"You ran {kms}km or {round(miles, 2)}mi today.")