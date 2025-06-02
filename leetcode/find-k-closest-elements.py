"""
link: https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]



Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

"""

from typing import List


class Solution:
    def find_pos_of_x(self, arr: List[int], n: int, x: int) -> List[int|bool]:
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            elif arr[mid] > x:
                r = mid - 1
            else:
                return [mid, True]
        return [l, False]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        x_pos, exists = self.find_pos_of_x(arr, n, x)

        if (x_pos == 0 and exists) or x < arr[0]:
            return arr[:k]

        if (x_pos == n-1 and exists) or x > arr[-1]:
            return arr[n-k:]

        k_arr = []
        i = x_pos-1
        j = x_pos

        if exists:
            k_arr = [x]
            j += 1

        while len(k_arr) < k:
            if i >= 0 and j < n:
                # print(k_arr, i, j, arr[i], arr[j])

                if abs(x-arr[i]) > abs(x-arr[j]):
                    k_arr.append(arr[j])
                    j += 1
                    # print(k_arr, i, j, arr[i], arr[j])

                else:

                    k_arr.append(arr[i])
                    i -= 1
                    # print(k_arr, i, j, arr[i], arr[j])

            else:
                break

        while i >= 0 and len(k_arr) < k:
            k_arr.append(arr[i])
            i -= 1

        while j < n and len(k_arr) < k:
            k_arr.append(arr[j])
            j += 1

        return sorted(k_arr)




s = Solution()
print(s.findClosestElements([1,3] , 1, 2))