def count_vowels(text):
    vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    return sum(1 for char in text if char in vowels)

print(count_vowels("Hola mundo"))
print(count_vowels("Python"))
print(count_vowels("AEIOU"))
