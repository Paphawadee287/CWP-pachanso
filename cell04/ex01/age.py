age = int(input("Please tell me your age: "))

print(f"You are currently {age} years old.")

for year in range(10, 31, 10):
    print(f"In {year} years, you'll be {age + year} years old.")
