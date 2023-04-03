def check_rhythm(poem):
    phrases = poem.split()
    vowels_counts = []
    for phrase in phrases:
        vowels_count = sum(phrase.count(vowel) for vowel in "aeiouyAEIOUY")
        vowels_counts.append(vowels_count)
    if len(set(vowels_counts)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Введите стихотворение: ")
result = check_rhythm(poem)
print(result)