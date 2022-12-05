import math
from numpy import cumsum
from operator import itemgetter

def shennon(file):
    input_file = open(file, "r")
    letters = [line.rstrip() for line in input_file.readlines(2)]
    numbers = [line.rstrip() for line in input_file.readlines(1)]
    lines_of_letters = letters[0].split(' ')
    lines_of_numbers = numbers[0].split(' ')
    lines_of_numbers = list(map(float, lines_of_numbers))
    dict_n_l = dict(zip(lines_of_letters, lines_of_numbers))
    soted_dict = dict(sorted(dict_n_l.items(), key=itemgetter(1), reverse=True))
    
    lst_of_nmb = []
    for_log = []

    for values in soted_dict.values():
        lst_of_nmb.append(values)
    for_log = lst_of_nmb.copy()

    summ_iter = cumsum(lst_of_nmb) - lst_of_nmb
    int_numbers_lst = []
    for elem in summ_iter:
         int_numbers_lst.append(int((elem % 1 * 100)))
    # print(int_numbers_lst)

    
    lst_for_binary = []
    
    for elem in int_numbers_lst:
        lst_for_binary.append('{0:b}'.format(elem))
    
    logged_lst = []    
    for elem in for_log:
        logged_lst.append(math.ceil(math.log2(1/elem)))
    print(logged_lst)

    prefinal_dict = dict(zip(lst_for_binary, logged_lst))
    final_dict = []
    for key, value in prefinal_dict.items():
        final_dict.append(str(key)[:value])
    
    return final_dict    
        
    
print(shennon('input.txt'))
