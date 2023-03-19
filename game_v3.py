"""Игра угадай число. Компьютер сам загадывает и угадывает число"""
import numpy as np
def random_predict(n:int, number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        n (int): предел числа
    Returns:
        int: Число попыток
    """
    count = 0
    a = int(round(n/2))
    while True:
        count += 1
        if number < a:
            a -= 1
        if number > a:
            a += 1
        if number == a:
            break
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    n = 100 #предел числа
    random_array = np.random.randint(1, n+1, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(n, number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)