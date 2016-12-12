def valueC(card):
    """ Функция оценки достоинства карты.
    Это достоинства станет параметром сортировки"""

    ret = 0

    if card[0] == 'T':
        ret = 10
    elif card[0] == 'J':
        ret = 11
    elif card[0] == 'Q':
        ret = 12
    elif card[0] == 'K':
        ret = 13
    elif card[0] == 'A':
        ret = 14
    else:
        ret = int(card[0])

    if card[1] == 'c':
        ret+=0
    elif card[1] == 's':
        ret+=0.1
    elif card[1] == 'h':
        ret+=0.2
    elif card[1] == 'd':
        ret+=0.3

    return ret

n = int(input())
string = input().strip()
D = dict()

for i in range(len(string)//2):
    card = string[2*i:2*i+2] # чтение по два символа
    D[card] = valueC(card) # забивается словарь

for card in sorted(list(D.items()), key=lambda item: item[1]): # сортируется словарь
    print(card[0], end='')

