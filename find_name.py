#Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
#Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.


list_names=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
find_name='Саша'

def find_valera (names):
    while True:
        name = names.pop()
        print(name)
        if name == "Валера":
            print("Валера нашелся!")
            break


def find_person (names, find_name):
    while True:
        name = names.pop()
        print(name)
        if name == find_name:
            print("{} нашелся!".format(find_name))
            break

if __name__ == '__main__':
    find_person(list_names, find_name)
