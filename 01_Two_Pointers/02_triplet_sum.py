from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    triplets = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        if nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                pair = pair_sum_sorted(nums[i+1:], -nums[i])
                if pair:
                    for el in pair:
                        el.append(nums[i])
                        triplets.append(el)
        elif nums[i] > 0:
            break
    return triplets


def pair_sum_sorted(nums: List[int], target: int) -> List[List[int]]:
    left = 0
    right = len(nums) - 1
    pair = []
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            pair.append([nums[left], nums[right]])
            left = left + 1
            while left < right and nums[left] == nums[left - 1]:
                left = left + 1
        elif total < target:
            left = left + 1
        elif total > target:
            right = right - 1
    return pair


if __name__ == "__main__":
    print(triplet_sum([]))
    print(triplet_sum([0]))
    print(triplet_sum([1, -1]))
    print(triplet_sum([0, 0, 0]))
    print(triplet_sum([1, 0, 1]))
    print(triplet_sum([1, 0, 1]))
    print(triplet_sum([0, 0, 1, -1, 1, -1]))
    print(triplet_sum([0, -1, 2, -3, 1]))
