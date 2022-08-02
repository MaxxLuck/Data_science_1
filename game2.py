""" Игра угадай число
    я загадываю число (аргумент у функции) а комп  сам угадывает число рандомным угадыванием
"""
import numpy as np
def random_predict(number:int=1) -> int:
    """рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
        """
    count = 0
    while True :
        count +=1
        predict_number=np.random.randint(1,101)
        if predict_number == number:
                break
    return count

def score_game(random_predict) -> int:
    """за какое количество попыток в среднем из 1000 раз наш алгоритм угадывает число

    Args:
        random_predict (_type_): функция угадывания (random_predict)

    Returns:
        int: среднее количество попыток из 100 раз
    """
    count_ls=[] #список для записи количества попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число за {score} попыток')
    return score
    
if __name__ == '__main__':
    score_game(random_predict)



    