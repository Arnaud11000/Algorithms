def merge_sort(arr: list[int]) -> list[int]:

    #Turn any list composed of integers into a list in ascending order.
    #Time complexity O(n*logn), space complexity O(n)

    if len(arr)>1:
        mid=len(arr)//2
        left_arr: list[int] = arr[:mid]
        right_arr: list[int] =arr[mid:]

        #Recursively sort the two halves.
        #Each call pauses the current function until it finishes.
        #Once both functions return, left_arr and right_arr are sorted.
        #Their sorted merge can then appear.

        merge_sort(left_arr)
        merge_sort(right_arr)

        #We compare values of same index of the two halves and set the lowest first in arr.
        i, j, k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                arr[k]=left_arr[i]
                i+=1
            else:
                arr[k]=right_arr[j]
                j+=1
            k+=1

        #Taking any remaining elements from left_arr, aloready sorted, and give them to arr.
        while i < len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1

        #The same goes for any remaining elements of right_arr.
        while j < len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1        
    return arr
