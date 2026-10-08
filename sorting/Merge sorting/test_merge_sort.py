import random
from merge_sort import merge_sort


def run_tests():
    test_cases = [
        ([3, 1, 2], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([2, 2, 1], [1, 2, 2]),
        ([-3, 2, -1, 0], [-3, -1, 0, 2]),
    ]

    # Generate 100 random test cases
    for _ in range(100):
        nums = [random.randint(-1000, 1000)
                for _ in range(random.randint(0, 100))]

        test_cases.append((nums, sorted(nums)))

    # Check every test case
    for input_list, expected in test_cases:
        result = merge_sort(input_list.copy())
        assert result == expected, (
            f"Input: {input_list}\n"
            f"Expected: {expected}\n"
            f"Got: {result}"
        )

    print(f"All {len(test_cases)} tests passed!")


if __name__ == "__main__":
    run_tests()
