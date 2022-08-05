import numpy as np

def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """угадываем число через среднее между максимальным и минимальным в диапазоне

    Args:
        number (int, optional): _загаданное число. По умолчанию загадывает компьютер в диапазоне от 1 до 100. Defaults to np.random.randint(1, 101).

    Returns:
        int: число попыток
    """
    count = 0 # задаем счетчик
    min_num = 1
    max_num = 100
    
    while True:
        count +=1
        predict_num = int((min_num + max_num) / 2)  # загадываем число как среднее между 
                                                  # минимальным и максимальным и отбрасываем дробную часть
        
        if predict_num > number:
            max_num = predict_num
            
        elif predict_num < number:
            min_num = predict_num
            
        else:
            # print(f'Алгоритм рассчитал число {number} за {count} попыток') #активировал данную строку, 
            # если надо посмотреть все ли числа вылавливает алгоритм 
            # (сказали, что некоторые алгоритмы могут не ловить числа 1 и 99)
            break
    return count


def score_game(random_predict) -> int:
    """за какое количество попыток в среднем из 1000 раз наш алгоритм угадывает число

    Args:
        random_predict (_type_): функция угадывания (random_predict)

    Returns:
        int: среднее количество попыток из 100 раз
    """
    count_ls=[] # список для записи количества попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    count1 = 0
    
    for number in random_array:
        count_ls.append(random_predict(number))
        count1+=1
        # print(f"итерация номер {count1}") #активировал данную строку чтобы посмотреть количество итераций.
        # После 233 итерации работа алгоритма останавливалась.     
    score = int(np.mean(count_ls))
    print(f'Наш алгоритм угадывает число за {score} попыток')
    return score


score_game(random_predict)