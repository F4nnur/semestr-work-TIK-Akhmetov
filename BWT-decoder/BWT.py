def bwt(bwt):
    #Пустой столбик
    table = [""] * len(bwt)  

    for i in range(len(bwt)):
        #Добавляем столбик
        table = [bwt[i] + table[i] for i in range(len(bwt))]
        print('unsorted = ', table)
        table = sorted(table)
        print('sorted    =', table)
    
    # Ищем строку которая заканчивается на $   
    inverse_bwt = [row for row in table if row.endswith("$")][0]

    #Избавляемся от $
    inverse_bwt = inverse_bwt.rstrip("$")

    return(inverse_bwt)

print(bwt("annb$aa"))