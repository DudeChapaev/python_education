import random

year_random = random.randint(1940,1950)

word1 = 'АСЬ? ГОВОРИ ГРОМЧЕ ВНУЧЕК'
word2 = f'НЕТ, НИ РАЗУ С {year_random} ГОДА!'
last_words = 'ПОКА, ВНУЧЕК!'

bye_count = 0

while True:
    vnucheck = input('Поговори с бабулей: ')

    if vnucheck == 'ПОКА':
        bye_count +=1
        if bye_count >= 3:
            print(last_words)
            break
        else:
            print(word1)
    elif vnucheck == vnucheck.upper():
        print(word2)
        continue
    else:
        print(word1)