for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    if n % 10 == 1 and n % 100 != 11:
        print(n, 'процент,', end=' ')
    elif 1 < n % 10 < 5 and not 11 < n % 100 < 15:
        print(n, 'процента,', end=' ')
    else:
        print(n, 'процентов,', end=' ')

