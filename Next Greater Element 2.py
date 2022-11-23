#Using Monotonic Stack
#Time Complexity:: O(n)-all indexes are visited twice in the worst case as we are pushing into mstack and searching circularly
#Space Complexity:: O(n)-a monotonic stack is used and in worst case the number never increases
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mstack = [] #initializing a monotonic stack
        result = [-1]*len(nums) #creating a result array with default value as -1 when there doesn't exist a greater element
        
        for i in range(len(nums)*2): #create 2*len of given array to search it circularly
            while mstack and nums[mstack[-1]] < nums[i%len(nums)]: #need to have both conditions in while otherwise infinite loop with element in mstack
                    result[mstack[-1]] = nums[i%len(nums)] #using mod as we are searching for greater number circularly, then we push it into result array
                    mstack.pop() #pop the top of the mstack after pushing element into it
            
            if i<len(nums): #condition to push numbers only once into the monotonic stack
                mstack.append(i)  
        return result #returning the next greater numbers