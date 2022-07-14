def birthday(type, name, value):
    str = f'В какой {type} родился {name}: '
    answer = None
    while answer != value:
        if answer != None:
            print("Не верно")
        answer = input(str)
    print('Верно')

birthday('год', 'А.С. Пушкин', '1799')
birthday('день', 'А.С. Пушкин', '6')
