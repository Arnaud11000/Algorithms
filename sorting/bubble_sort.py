from typing import Optional

def bubble_sort(arr= Optional[list[int]]) -> Optional[list[int]]:

    if not arr or len(arr)<=1:
        return arr

    max_swapped=0
    to_check=True

    while to_check:

        to_check=False

        for i in range (len(arr) -1 -max_swapped):
            if arr[i]>arr[i+1]:
                to_check=True
                arr[i] , arr[i+1] = arr[i+1], arr[i]

        max_swapped+=1

    return arr
        
bubble_sort([1,7,6,5,4,2,6,7,8])
