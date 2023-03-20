"""Игра угадай число. Компьютер сам загадывает и угадывает число
методом горячо-холодно через серединные отрезки"""

import numpy as np
def random_predict(n:int, number:int=1) -> int:
    """Угадывает число методом горячо-холодно через серединные отрезки
    путем прибавления и вычитания

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        n (int): предел числа
    Returns:
        count (int): Число попыток
    """
    
    count = 0
    a = int(n/2) #предполагаемое число

    while True:
        count += 1
        m = int(round(n/2**(count + 1))) #перменная для поиска середины
        if m < 1: m = 1 #костыли для наибольшего числа
        if a < number:
            a = a + m
        elif a > number:
            a = a - m
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