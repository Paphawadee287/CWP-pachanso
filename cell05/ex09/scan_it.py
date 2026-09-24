import sys
import re

params = sys.argv

if len(params) != 3:
    print("none")
else:
    keyword = params[1]
    text = params[2]

    matches = re.findall(keyword, text)
    print(len(matches))
