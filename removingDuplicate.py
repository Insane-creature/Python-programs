# using set: as it doesn't contain duplicate values
l = [1, 2, 4, 6, 7, 1, 2]
unique_list = list(set(l))
# print(unique_list)

# using loops

l = [1, 2, 4, 6, 7, 1, 2]
unique_list = []
seen = set()

for item in l:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)

print(unique_list)
