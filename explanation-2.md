# Algorithm
- Find the rotation point of the array (highest element in array)
- Do binary search on the two sorted non-rotated arrays. One until the rotation point, the other from the rotation point

# Time complexity
- Total time complexity: `O(log(n))`
  - both algorithms to find the pivot and search the succeeding arrays use binary search logic, so the total time complexity is the same as binary search
- finding the rotation point: uses a binary search like algorithm -> `O(log(n))`
- search the array: uses binary search -> `O(log(n))`