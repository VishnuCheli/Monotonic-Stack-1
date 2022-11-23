#Monotonic Stack
#Time Complexity:: O(n)-all indexes are visited twice in the worst case as we are pushing into mstack and comparing
#Space Complexity:: O(n)-a monotonic stack is used and in worst case the temp increases at the nth index
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = [] #initialize a monotonic stack+
        result = [0]*len(temperatures) #allocate a fixed result array with '0' as the lowest temperature is 30 and '0' indicates no future warmer days
        
        for i in range(len(temperatures)): #traverse all temps once as you're pushing them into the monotonic stack
            while mstack and temperatures[mstack[-1]]<temperatures[i]: #if the mstack is !empty compare the top of the stack with the current days temp
                result[mstack[-1]] = i - mstack[-1] #next warmer temperature's index is appended to the result after popping monotonic stack
                mstack.pop() #pop the monotonic stack as a higher temperature day has come
            mstack.append(i) #keep appending the current day temperature to the mstack as it will pop if a warmer day arrives
            
        return result #return the array of increased temperature days indexes