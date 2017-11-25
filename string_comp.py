#Написать функцию, которая принимает на вход две строки.
#Если строки одинаковые, возвращает 1.
#Если строки разные и первая длиннее, возвращает 2.
#Если строки разные и вторая строка 'learn', возвращает 3.

str1=12345678
str2='123456'

def string_comp (string_1,string_2):
    string_1=str(string_1)
    string_2=str(string_2)
    print(string_1)
    print(type(string_1))
    print(string_2)
    print(type(string_2))
    try:
        if string_1 == string_2:
            return 1
        else:
            if len(string_1) > len(string_2):
                return 2
            elif string_2 =='learn':
                return 3
    except (TypeError):
        print('Неверный тип данных')

if __name__ == '__main__':
    val=string_comp(str1,str2)
    print(val)


