# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

class Solution:
    def threesum(self, arry:list, sum_total:int):
        length = len(arry)
        arry.sort()
        result = []
        for i in range(length-2):
            l = i+1
            r = length-1
            while l < r:
                sum_inside = arry[i] + arry[l] + arry[r]
                if sum_inside == sum_total:
                    if [arry[i] , arry[l] , arry[r]] not in result:
                        result.append([arry[i] , arry[l] , arry[r]])
                    l+=1
                    # r-=1
                elif sum_inside > sum_total:
                    r-=1
                else:
                    l+=1
        return result
        
three = Solution()
print(three.threesum([10, -6, 10, -2, -8, -3, 5, -8, -7, 0, 6, -4, 4, 7, 0, 7, 6, -9, -2, 1], 0))

