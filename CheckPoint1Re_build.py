import random

print('ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!')

bye_count = 0
while True:
    vnucheck = input('Поговори с бабулей: ')
    if vnucheck == 'ПОКА!':
        bye_count +=1
        if bye_count >= 3:
            print('ДО СВИДАНИЯ, МИЛЫЙ!')
            break
        else:
            year_random = random.randint(1930,1950)
            print(f'НЕТ, НИ РАЗУ С {year_random} ГОДА!')
    elif vnucheck.isupper():
        bye_count = 0
        year_random = random.randint(1930,1950)
        print(f'НЕТ, НИ РАЗУ С {year_random} ГОДА!')
    else:
        bye_count = 0
        print('АСЬ? ГОВОРИ ГРОМЧЕ, ВНУЧЕК!')
