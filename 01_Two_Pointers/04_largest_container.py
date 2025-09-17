from typing import List


def largest_container(heights: List[int])-> int:
    left = 0
    right = len(heights) - 1
    max_water = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height
        max_water = max(max_water, area)
        if heights[left] == heights[right]:
            left = left + 1
            right = right - 1
        elif heights[left] < heights[right]:
            left = left + 1
        elif heights[right] < heights[left]:
            right = right - 1
    return max_water


if __name__ == "__main__":
    print(largest_container([]))
    print(largest_container([1]))
    print(largest_container([0, 1, 0]))
    print(largest_container([3, 3, 3, 3]))
    print(largest_container([1, 2, 3]))
    print(largest_container([3, 2, 1]))
