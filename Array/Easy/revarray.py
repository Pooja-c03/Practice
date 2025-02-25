# To reverse an array

def revarray(A): # [1,2,3,4]
    n = len(A)
    temp = []
    for i in range(n-1,-1,-1):
        temp.append(A[i])

    for i in range(n):
        A[i] = temp[i]

    print("The reversed array is :", A)
if __name__ == "__main__":
    no = int(input("Enter no of elements you want to enter: "))
    arr = []
    print("Enter the elements:")
    for i in range(no):
        ele = int(input())
        arr.append(ele)

    revarray(arr)
    