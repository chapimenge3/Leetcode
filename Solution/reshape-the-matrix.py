class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        nums = []
        for i in mat:
            nums.extend(i)
        
        final = []
        index = 0
        for i in range(r):
            row = []
            for ii in range(c):
                print(i, ii)
                row.append(nums[index])
                index += 1
            final.append(row)
        
        return final
        