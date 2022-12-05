import math
from numpy import cumsum
from operator import itemgetter

def shennon(file, user_word):
    input_file = open(file, "r")
    list_of_user_word = list(user_word)
    print(list_of_user_word)
    letters = [line.rstrip() for line in input_file.readlines(2)]
    numbers = [line.rstrip() for line in input_file.readlines(1)]
    lines_of_letters = letters[0].split(' ')
    lines_of_numbers = numbers[0].split(' ')
    lines_of_numbers = list(map(float, lines_of_numbers))
    dict_n_l = dict(zip(lines_of_letters, lines_of_numbers))
    soted_dict = dict(sorted(dict_n_l.items(), key=itemgetter(1), reverse=True))
    
    symbols_of_sorted_dict = []
    lst_of_nmb = []
    for_log = []

    for key, values in soted_dict.items():
        lst_of_nmb.append(values)
        symbols_of_sorted_dict.append(key)

    for_log = lst_of_nmb.copy()

    summ_iter = cumsum(lst_of_nmb) - lst_of_nmb
    int_numbers_lst = []
    for elem in summ_iter:
         int_numbers_lst.append(int((elem % 1 * 100)))
    
    lst_for_binary = []
    
    for elem in int_numbers_lst:
        lst_for_binary.append('{0:b}'.format(elem))
    
    logged_lst = []    
    for elem in for_log:
        logged_lst.append(math.ceil(math.log2(1/elem)))

    prefinal_dict = dict(zip(lst_for_binary, logged_lst))
    final_dict = []
    for key, value in prefinal_dict.items():
        final_dict.append(str(key)[:value])
    
    new_dict = dict(zip(symbols_of_sorted_dict, final_dict))
    
    new_dict_for_elems = {e: new_dict[e] for e in list_of_user_word}
    return new_dict_for_elems
        
    
print(shennon('input.txt', 'acdbe'))
