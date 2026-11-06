
import random
import time

# Deterministic Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Randomized Quick Sort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    return randomized_quick_sort(left) + equal + randomized_quick_sort(right)


# Main program
arr = list(map(int, input("Enter elements: ").split()))

start = time.time()
result1 = quick_sort(arr)
end = time.time()

print("Deterministic Quick Sort:", result1)
print("Time:", end - start, "seconds")

start = time.time()
result2 = randomized_quick_sort(arr)
end = time.time()

print("Randomized Quick Sort:", result2)
print("Time:", end - start, "seconds")
