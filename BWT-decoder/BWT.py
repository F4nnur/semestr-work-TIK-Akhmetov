# def bwt(bwt):
#     #Пустой столбик
#     table = [""] * len(bwt)

#     for i in range(len(bwt)):
#         #Добавляем столбик
#         table = [bwt[i] + table[i] for i in range(len(bwt))]
#         print('unsorted = ', table)
#         table = sorted(table)
#         print('sorted    =', table)
    
#     # Ищем строку которая заканчивается на $   
#     inverse_bwt = [row for row in table if row.endswith("$")][0]

#     #Избавляемся от $
#     inverse_bwt = inverse_bwt.rstrip("$")

#     return(inverse_bwt)

# print(bwt("annb$aa"))

def bwt_decoder(encoded_word, position):
    decode_matrix = list(sorted(encoded_word))
    for _ in range(len(encoded_word) - 1):
        for i in range(len(encoded_word)):
            decode_matrix[i] = encoded_word[i] + decode_matrix[i]
        decode_matrix.sort()
    # print(*decode_matrix, sep='\n')
    # print('________________________________')
    return decode_matrix[position]

print('bwt decode ', bwt_decoder("рдакраааабб", 2))