
def main():
    matrix= [[1,2,3],
             [4,5,6],
             [7,8,9],
             [10,11,12],
             [13,14,15]]
            
    transpose=[[1,4,7,10,13],
               [2,5,8,11,14],
               [3,6,9,12,15]]

    print(matrixMult(matrix,transpose))
        
def matrixMult(a,b):
    zip_b = zip(*b)
  
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]


main()


    
    
