def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char not in vowels)
    return vowel_count, consonant_count


s = "anshika"
vowels, consonants = count_vowels_and_consonants(s)

print(f"String: {s}")
print(f"Vowel count: {vowels}")
print(f"Consonant count: {consonants}")