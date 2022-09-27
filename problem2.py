# this is the solution they accepted for the problem:
# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        size = len(nums)
        for i, v in enumerate(nums):
            for n in range(i+1, size):
                if v + nums[n] == target and i!= n:
                    result.append(i)
                    result.append(n)
                    break
            if result:
                break

        return result
