def minDiff(arr, m):
    n = len(arr)

    arr.sort()
    min = float('inf')

    for i in range(n-m+1):
        diff = arr[i+m-1]-arr[i]
        if diff < min:
            min = diff

    return min

if __name__ == "__main__":
    arr = [7,3,2,4,9,12,56]
    m = 3

    print(minDiff(arr,m))