def sparse(arr,n,m):
    s=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                s+=1
    
    sparse_matrix=[[0 for i in range(s)]for i in range(3)]
    
    k=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0:
                sparse_matrix[0][k]=i
                sparse_matrix[1][k]=j
                sparse_matrix[2][k]=arr[i][j]
                k+=1
    return sparse_matrix

def main():
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(input().split())
    for i in range(n):
        for j in range(m):
            arr[i][j]=int(arr[i][j])
    print("after sparse matrix")
    arr=sparse(arr,n,m)
    print(arr)
if __name__=="__main__":
    main()
    
