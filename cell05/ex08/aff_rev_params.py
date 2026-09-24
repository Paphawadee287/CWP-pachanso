import sys

params = sys.argv

if len(params) < 3:
    print("none")
else:
    for param in reversed(params[1:]):
        print(param)
