class twoNumberSum:

    def __init__(self, array, targetSum):
         self.array = array
         self.targetSum = targetSum

    # O(n^2) time | O(1) space
    def twoNumberSum1(self):
        '''
        This code is using the nested for loops 
        '''
        for idx1 in range(len(self.array)-1):
            for idx2 in range(idx1+1, len(self.array)):
                if (self.array[idx1] + self.array[idx2]) == self.targetSum:
                    return [self.array[idx1] , self.array[idx2]]
        return []


    # O(nlog(n)) time | O(1) space
    def twoNumberSum2(self):
        '''
        This code is using two pointer concept where array is sorted
        '''
        self.array.sort()
        left = 0
        right = len(self.array)-1
        while(left < right): 
            currentSum = self.array[left] + self.array[right]
            if currentSum > self.targetSum:
                right = right - 1
            elif currentSum < self.targetSum: 
                left = left + 1
            else: 
                return [self.array[left], self.array[right]]

    #O(n) time | O(n) space
    def twoNumberSum3(self):
        '''
        This code is using the Hash table 
        '''
        nums = {}
        for num in self.array: 
            if self.targetSum - num in nums: 
                return [num,  self.targetSum - num]
            else:
                nums[num] = True
        return []



if __name__ == "__main__":

    obj = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(obj.twoNumberSum1())
    print(obj.twoNumberSum2())
    print(obj.twoNumberSum3())
