"""Игра угадай число. Компьютер сам загадывает и угадывает число
методом горячо-холодно рандомно от середины"""

import numpy as np
def random_predict(n:int, number:int=1) -> int:
    """Угадывает число методом горячо-холодно рандомно от середины

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        n (int): предел числа
    Returns:
        count (int): Число попыток
    """
    count = 0
    min = 1 #начало диапазона поиска числа
    max = n + 1 #конец диапазона поиска числа
    a = n/2 #предполагаемое число
            
    while True:
        count += 1
        if a < number:
            min = a + 1
            a = np.random.randint(min, max)
        elif a > number:
            max = a
            a = np.random.randint(min, max)
        else:
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