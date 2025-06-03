"""
link: https://leetcode.com/problems/interval-list-intersections/description/

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].



Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

"""

# Stupid Version O(n*m),
from typing import List

class StupidSolution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output_intervals = []
        n = len(firstList)
        m = len(secondList)

        for i in range(n):
            first_interval = firstList[i]

            for j in range(m):
                second_interval = secondList[j]

                if first_interval[0] <= second_interval[0] <= first_interval[1] or second_interval[0] <= first_interval[0] <= second_interval[1]:
                    output_intervals.append([max(second_interval[0], first_interval[0]), min(second_interval[1], first_interval[1])])

        return output_intervals

# s = StupidSolution()
# print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))



class GoodSolution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)

        i, j = 0, 0

        output_intervals = []

        while i < n and j < m:
            print(i, j)
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif secondList[j][1] < firstList[i][0]:
                j += 1
            else:
                output_intervals.append([max(firstList[i][0], secondList[j][0]), min(secondList[j][1], firstList[i][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1

        return output_intervals

s = GoodSolution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]])) #[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

