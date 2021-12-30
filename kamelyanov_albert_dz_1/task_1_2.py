sum_list_1 = []
result_1 = 0
    for i in range(1, 1001, 2):  # формирую список  циклом
     sum_list_1.append(i ** 3)  # добовляю степень
    for ind, val in enumerate(sum_list_1):
     sum_digits = 0
    while val > 0:
        sum_digits = + val % 10
        val //= 10
if sum_digits % 7 == 0:
 result_1 += sum_list_1[ind]

