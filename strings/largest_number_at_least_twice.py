"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.

Constraints:

2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
"""
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = (0,0)
        second_largest = (0,0)
        for i in range(len(nums)):
            if nums[i] > largest[1]:
                second_largest = largest
                largest = (i,nums[i])
            elif nums[i] > second_largest[1]:
                second_largest = (i,nums[i])
        if largest[1] >= 2*second_largest[1]:
            return largest[0]
        else:
            return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.dominantIndex([0,0,3,2]))
