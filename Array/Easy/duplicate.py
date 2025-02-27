def dupe(A):
    flag = 0
    n = len(A)    #[1,2,3,1]      n=4
    for i in range(n-1):
        for j in (i+1, n-1):
            if A[i] == A[j]:
                flag = 1

    if flag == 1:
        print("Duplicate")
    else:
        print("No duplicate")

if __name__ == '__main__':
    no = int(input("Enter no of elements you want to enter: "))
    arr = []
    print("Enter the elements:")
    for i in range(no):
        ele = int(input())
        arr.append(ele)

    dupe(arr)