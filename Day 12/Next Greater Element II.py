
def findNextGreater(nums):
    n = len(nums)
    stack = []
    result = [-1] * n
    for index in range(n - 1, -1, -1):
        # step-1 (Remove unnecessary values)
        while len(stack) > 0:
            if stack[-1] <= nums[index]:
                stack.pop()
            else:
                break 
                
        
        # step-2 (Update result if any element present)
        if len(stack) > 0:
            result[index] = stack[-1]
        
        
        # step-3 (Push current index element into stack)
        stack.append(nums[index])
    
    return result


nums = [10, 5, 2, 6, 11, -5, 100, 99, 88, 110]
       #[11, 6, 6, 11, 100, 100, 110, 110, 110, -1]
result = findNextGreater(nums)
print(result)
