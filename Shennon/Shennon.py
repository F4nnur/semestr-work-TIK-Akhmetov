import math
from numpy import cumsum
from operator import itemgetter
# Python program to convert float
# decimal to binary number

# Function returns octal representation
def float_bin(number, places = 3):

    # split() separates whole number and decimal
    # part and stores it in two separate variables
    whole, dec = str(number).split(".")

    # Convert both whole number and decimal
    # part from string type to integer type
    whole = int(whole)
    dec = int(dec)
    
    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):

        # Multiply the decimal value by 2
        # and separate the whole number part
        # and decimal part
        whole, dec = str(decimal_converter(dec) * 2).split(".")

        # Convert the decimal part
        # to integer again
        dec = int(dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return str(res)[1:]

# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num if num != 0 else 0.0


def shennon(file, user_word):
    input_file = open(file, "r")
    list_of_user_word = list(user_word)
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
    
    lst_for_binary = []
    
    logged_lst = []    
    for elem in for_log:
        logged_lst.append(math.ceil(math.log2(1/elem)))

    for i in range(len(summ_iter)):
        lst_for_binary.append(float_bin(summ_iter[i], int(logged_lst[i])))

    prefinal_dict = dict(zip(lst_for_binary, logged_lst))
    final_dict = []
    for key, value in prefinal_dict.items():
        final_dict.append(str(key)[:value])
    
    new_dict = dict(zip(symbols_of_sorted_dict, final_dict))
    
    new_dict_for_elems = {e: new_dict[e] for e in list_of_user_word}
    encoded_word = ''.join([new_dict_for_elems[l] for l in user_word])
    return new_dict_for_elems, encoded_word
        
    
print(shennon('input.txt', 'bbaacd'))