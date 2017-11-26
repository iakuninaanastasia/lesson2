#Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
#При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
#Переписать функцию ask_user(), добавив обработку exception-ов
#Добавить перехват ctrl+C и прощание

answers={
    'привет': 'И тебе привет!',
    'как дела': 'Лучше всех',
    'что делаешь': 'разговариваю с тобой'
    }


def ask_user(): #Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
    while True:
        user_say = str(input('Скажи что-нибудь: \n')).lower()
        if user_say == 'Хорошо':
            break
        else:
            user_say = input ('Как дела? \n')


def get_answer(question):
    return answers.get(question)


def ask_user2(): #При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”
    try:
        while True:
            user_say = str(input('Скажи что-нибудь: \n')).lower()
            if user_say == 'Пока'.lower():
                print('Пока!')
                break
            else:
                print(get_answer(user_say))
    except EOFError:
        print('Жаль, что уже уходишь! Пока! ')
    except KeyboardInterrupt:
        print('Жаль, что уже уходишь! Пока! ')
       

       
if __name__ == '__main__':
    ask_user2()