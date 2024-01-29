def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] >= target:
            right = mid - 1

    upper_bound = None
    if left < len(arr):
        upper_bound = arr[left]

    return iterations, upper_bound


if __name__ == '__main__':
    arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    print(binary_search(arr, 0.5))
    print(binary_search(arr, 0.55))
    print(binary_search(arr, 0.6))
    print(binary_search(arr, 0.45))
