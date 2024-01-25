# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_serach(list1:list, key:int, start=0, end =None ) -> int:
    if end == None:
        end = len(list1)
    if start > end:
        return -1
    
    mid = (start+end)//2
    if list1[mid] == key:
        return(mid)
    if list1[mid] > key:
        return binary_serach(list1, key, start, mid-1)
    else:
        return binary_serach(list1, key, mid+1, end)

list1 = [x*2 for x in range(6)]
print(binary_serach(list1, 8))