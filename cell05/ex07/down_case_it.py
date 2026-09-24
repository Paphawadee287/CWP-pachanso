import sys

params = sys.argv

if len(params) < 2:
    print("none")
else:
    print(params[1].lower())
