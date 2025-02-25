# To find the min & max in an array 

def min(A):
    min = float('inf')
    for num in A:
        if num < min:
            min = num
    return min

def max(A):
    max = float('-inf')
    for num in A:
        if num > max:
            max = num
    return max

if __name__ == "__main__":
    no = int(input("Enter no of elements you want to enter: "))
    arr = []
    print("Enter the elements:")
    for i in range(no):
        ele = int(input())
        arr.append(ele)

    print(arr)
    print("The minimum element in array is: ", min(arr))
    print("The maximum element in array is: ", max(arr))