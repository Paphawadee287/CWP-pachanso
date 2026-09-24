import sys

params = sys.argv

if len(params) < 2:
    print("none")
else:
    print(f"parameters: {len(params) - 1}")
    for i in params[1:]:
        print(f"{i}: {len(i)}")
