#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


# def plusMinus(arr):
#     # Write your code here
#     length = len(arr)
#     pos = len([i for i in arr if i > 0])
#     zer = len([i for i in arr if i == 0])
#     neg = len([i for i in arr if i < 0])
#     print("{:.6f}".format(pos/length))
#     print("{:.6f}".format(neg/length))
#     print("{:.6f}".format(zer/length))


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)


# def miniMaxSum(arr):
#     # Write your code here
#     arr.sort()
#     print(sum(arr[:4]), sum(arr[1:]))


# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)


# def timeConversion(s):
#     # Write your code here
#     addHours = 12 if s[-2:] == 'PM' else 0
#     newHour = str(int(s[:2])+addHours) if (int(s[:2])+addHours) != 24 else '00'
#     newHour = '0'+newHour if len(newHour) < 2 else newHour
#     print(newHour+s[2:-2])
#     return newHour+s[2:-2]

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         if len(candidates) == 0 or min(candidates) > target:
#             return []
#         sortCand = sorted(candidates)
#         total = []
#         i = 0
#         while len(candidates) > i and sortCand[i] <= target:
#             if sortCand[i] == target:
#                 total.append([target])
#             else:
#                 res = self.combinationSum(sortCand, target-sortCand[i])
#                 for j in res:
#                     if len(res) > 0 and sorted([sortCand[i]]+j) not in total:
#                         total.append(sorted([sortCand[i]]+j))
#             i += 1
#         return total


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.zeroIsland(grid, row, col)

        return count

    def zeroIsland(self, grid: List[List[str]], row: int, col: int):
        num_rows = len(grid)
        num_cols = len(grid[0])
        if (row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] != '1'):
            return
        else:
            grid[row][col] = '#'
            self.zeroIsland(grid, row-1, col)
            self.zeroIsland(grid, row+1, col)
            self.zeroIsland(grid, row, col-1)
            self.zeroIsland(grid, row, col+1)
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones.sort()
#         while len(stones)>1:
#             print(stones)
#             left = stones[-2]
#             right = stones[-1]
#             if left == right:
#                 stones = stones[:-2]
#             else:
#                 stones = stones[:-2]+[right-left]
#             stones.sort()
#         return stones[0] if len(stones) else 0
        
        # heapq.heapify(self.heap)
        # heapq.heappop(self.heap)
        # heapq.heappush(self.heap, val)