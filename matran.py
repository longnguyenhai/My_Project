import math

def make_list(size):
    list = []
    for i in range(size):
        list.append(0)
    return list

#print make_list(3)    #test

def make_matrix(rows,cols):
    matrix = []
    for i in range(rows):
        matrix.append(make_list(cols))
    return matrix



chuoi= raw_input ("Nhap vao chuoi: ")
x=chuoi.split()
val = int(math.sqrt(len(x)))
#print val
mx = make_matrix(int(val),int(val))
print (mx)


