"""
link: https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        s_to_t_mapping = {}
        t_to_s_mapping = {}


        for i in range(n):
            s_to_t = s_to_t_mapping.get(s[i], False)
            t_to_s = t_to_s_mapping.get(t[i], False)

            if s_to_t and t_to_s:
                s_to_t_mapping[s[i]] = t[i]
                t_to_s_mapping[t[i]] = s[i]
            elif s_to_t is None and t_to_s is not None and t_to_s != s[i]:
                return False
            elif t[i] != s_to_t or t_to_s != s[i]:
                return False

        return True


s = Solution()
print(s.isIsomorphic("badc", "baba"))


