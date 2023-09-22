def arraymulti(MatA,MatB) : #Multiplication matrices carrees de taille n 
    MatC = []
    result = 0
    for i in range (len(MatA)):
        MatC.append([])
        for j in range(len(MatB[i])):
             MatC[i].append(0)
             
    for i in range (len(MatA)):
         for k in range(len(MatB[i])):
            for j in range (len(MatA[i])) : 
                result += MatA[i][j]*MatB[j][k]
            MatC[i][k] = result
            result = 0
    return MatC

def main():
    MatA = [[1,1,1],[1,1,1],[1,1,1]]
    MatB = [[1,1,1],[1,1,1],[1,1,1]]
    output = arraymulti(MatA,MatB)
    return output
 