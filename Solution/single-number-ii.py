# from collections import Counter

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         n = Counter(nums)
#         for i in n:
#             if n[i] == 1:
#                 return i

# Python3 code to find the element
# that occur only once
INT_SIZE = 32


def singleNumber(nums):
    INT_SIZE = 32
    result = 0
    nresult = 0
    for i in range(INT_SIZE):
        mask = 1 << i
        sm = 0
        smn = 0
        for i in nums:

            if i < 0 and -i & mask:
                smn += 1

            elif i & mask:
                sm += 1
        
        if sm % 3 == 1:
            result |= mask
        
        if smn % 3 == 1:
            nresult |= mask

    print('result', result)
    print('nresult', nresult)

    return -nresult


def singleNumber(nums):
    
    b1, b2 = 0, 0

    for i in nums:

        # like C[b] += i
        b2 |= (b1 & i)  
        b1 ^= i

        # like C[b] %= 3
        shared = (b1 & b2)  
        b1 ^= shared
        b2 ^= shared

    return b1

    def singleNumber(nums):
        b1,b2 = 0,0
        for i in nums:
            b1 = (b1^i) & ~b2
            b2 = (b2^i) & ~b1
        
        return b1
        

nums = [2,2,-3,2]

print(singleNumber(nums))