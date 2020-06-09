import numpy as np

'''Сведем задачу к поиску позиции элемента в сортированном массиве'''
def game_core_v3(number):
    digit_list = [i for i in range (1, 101)] #Создаем массив на 100 элементов
    low = digit_list[0] #определяем меньший элемент массива
    high = digit_list[-1] #определяем больший элемент массива
    i = 0
    while low <= high: #повторяем пока меньший и больший элемент массива не совпадут
        i+=1
        middle = (low+high)//2 # находим средний элемент массива
        if middle > number:
            high = middle-1 #если искомое число меньше среднего элемента массива, определяем среднее значение в качестве большего
        elif middle < number:
            low = middle+1  #если искомое число больше среднего элемента массива, определяем среднее значение в качестве меньшего
        else:
            break # выходим из цикла
    return(i)

def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(100000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)
