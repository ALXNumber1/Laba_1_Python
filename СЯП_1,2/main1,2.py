text = input("Введите текст: ")
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0
vowel_letters = []

# Подсчет количества гласных и согласных букв
for letter in text:
    if letter.lower() in vowels:
        vowel_count += 1
        if letter not in vowel_letters:
            vowel_letters.append(letter)
    elif letter.isalpha():
        consonant_count += 1

# Вывод результатов
print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)

# Проверка на равенство количества гласных и согласных букв
if vowel_count == consonant_count:
    print("Гласные буквы в тексте:", ', '.join(vowel_letters))

# Подсчет количества слов в тексте
word_count = len(text.split())
print("Количество слов в тексте:", word_count)
