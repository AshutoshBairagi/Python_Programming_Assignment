'''
Question 6:
Please write a binary search function which searches an item in a sorted list. The
function should return the index of element to be searched in the list.
'''

def binarySearch(arr,x):
    arr.sort()
    print("sorted array is ",arr)
    l = 0
    u = len(arr)-1
    while l<=u:
        mid = (l+u)//2
        if (x == arr[mid]):
           print("index of ",x," is ",mid+1)
           return
        else:
            if x>arr[mid]:
                l=mid+1
            else:
                u=mid-1
    else:
        print("element not found")


arr=[1,2,4,8,66,77,99,100]
binarySearch(arr,2)
