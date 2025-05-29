"""
link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/


Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.



Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        subarrays = []

        now_subarray_len = 0

        for i in range(n):
            if nums[i] == 1:
                now_subarray_len += 1
            else:
                subarrays.append(now_subarray_len)
                now_subarray_len = 0
        print(subarrays)

        if now_subarray_len != 0:
            subarrays.append(now_subarray_len)

        m = len(subarrays)

        if m == 1:
            return subarrays[0] - 1

        ans = 0
        for i in range(1, len(subarrays)):
            ans = max(ans, subarrays[i - 1] + subarrays[i])

        return ans

s = Solution()
print(s.longestSubarray([0,1,1,1,0,1,1,0,1]))


