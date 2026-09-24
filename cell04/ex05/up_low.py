msg = input()

for char in msg:
    if char.isupper():
        print(char.lower(), end="")
    elif char.islower():
        print(char.upper(), end="")
    else:
        print(char, end="")

print()
