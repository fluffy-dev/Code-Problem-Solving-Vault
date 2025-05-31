"""
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        max_now = 0
        for i in range(n):
            for j in range(i+1, n+1):
                temp = s[i: j]
                max_now = max(max_now, len(temp)) if len(temp) == len(set(temp)) else max_now

        return max_now


s = Solution()
print(s.lengthOfLongestSubstring("anviaj"))