from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left = left + 1
        elif total > target:
            right = right - 1
    return []


if __name__ == "__main__":
    print(pair_sum_sorted([], 0))
    print(pair_sum_sorted([1], 1))
    print(pair_sum_sorted([2, 3], 5))
    print(pair_sum_sorted([2, 4], 5))
    print(pair_sum_sorted([2, 2, 3], 5))
    print(pair_sum_sorted([-1, 2, 3], 2))
    print(pair_sum_sorted([-3, -2, -1], -5))


