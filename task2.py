text = '''В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера». Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты, где с ним было потеряна связь — он пролетел на расстоянии 100 000 км от поверхности. В 1965 году результат был уже лучше — 24 000 км. Венера-4 доставила спускаемый аппарат и смогла получить данные о давлении, что использовали при построении следующих аппаратов. Венера-7 впервые совершила мягкую посадку на другую планету — в 1970-м году. А Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.'''

words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_common_word = max(word_counts, key=word_counts.get)

longest_word = max(words, key=len)

print("Наиболее часто встречающееся слово: ", most_common_word)
print('Самое длинное слово:', longest_word)