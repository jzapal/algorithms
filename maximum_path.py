"""
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually
ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""
from typing import List


max_path = []


def find_maximum_path(triangle: List) -> List:
    if len(triangle) == 0:
        return []
    traveler = TriangleTraveler()
    return traveler.move_down(triangle, 0, 0, [])


class TriangleTraveler:
    max_path = []

    def move_down(self, triangle: List, current_level: int, current_position: int, path: List):
        path.append(triangle[current_level][current_position])
        print(path)
        if current_level == len(triangle) - 1:
            if sum(path) > sum(self.max_path):
                self.max_path = path
        else:
            if current_position > 0:
                self.move_down(triangle, current_level + 1, current_position - 1, path[0:current_level+1])
            self.move_down(triangle, current_level + 1, current_position, path[0:current_level+1])
            self.move_down(triangle, current_level + 1, current_position + 1, path[0:current_level+1])
        return self.max_path


def test_solution():
    assert find_maximum_path([]) == []
    assert find_maximum_path([[1], [2, 3], [1, 5, 1]]) == [1, 3, 5]
    assert find_maximum_path([[1], [2, 3], [1, 5, 1], [10, 10, 0, 1000]]) == [1, 3, 1, 1000]
