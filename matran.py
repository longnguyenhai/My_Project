import math

# Create zero square matrix
def zero_matrix(N):
    zero_matrix = [[0 for row in range(N)] for col in range(N)]
    return zero_matrix

# Import value to matrix 
def matrix(L,N):
    k=0
    matrix= zero_matrix(N)
    for i in range(N):
        for j in range(N):
            matrix[i][j]= int (L[k])
            k +=1
    return matrix
    
def print_matrix(M):
    for row in M:
        print ("")#throw in a new line
        for item in row:
            print item,
                
                
if __name__ == '__main__':
        list_chain= raw_input ("Nhap gia tri cho ma tran N*N: ")
        words = list_chain.split()
        N = int(math.sqrt(len(words)))
        matrix=matrix(words,N)
        print ("Bieu dien ma tran:"),
        print_matrix(matrix)    #### Print matrix
        print ("\n")

#       Tinh tong
        sum = 0
        for i in range(N):
                sum += matrix[i][i]           # Duong cheo thu nhat
        for i in range(N):
                sum += matrix[N-i-1][i]               # Duong cheo thu hai
        print("Tong hai duong cheo chinh = %s" %sum )

#       Repleace X[][]:

        for i in range(N):
            for j in range(N):
                if (matrix[i][j] <=0) or (matrix[i][j]%2==1) :
                    matrix[i][j] = 'x'
        print ("Ma tran moi:"),
        print_matrix(matrix)