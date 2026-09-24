import sys

params = sys.argv

if len(params) != 2:
    print("none")
else:
    msg = input("What was the parameter? ")
    if msg == params[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
