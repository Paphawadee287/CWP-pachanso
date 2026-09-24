original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for i in original_array:
    if i > 5:
        new.append(i + 2)

print(original_array)
print(set(new))
