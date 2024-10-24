# Given list
numbers = [1, 2, 4, 6, 7, 7, 7, 7, 4, 1]

# Create an empty dictionary to store frequencies
frequency = {}

# Count the frequency of each element
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# frequency = {num: numbers.count(num) for num in set(numbers)}

print(frequency)
