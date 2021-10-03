
input_words = input('new_words: ')

words = input_words.split()
for num, word in enumerate(words):
    print(f'#{num} - {word[:10]}')
    