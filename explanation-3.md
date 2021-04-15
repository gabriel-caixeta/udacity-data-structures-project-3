# Algorithm
- Sort the array
- Using the sorted array `a`, generates the numbers in thw following manner:
  - first number: a[0] + 10*a[2] + 100*a[4] + ... + (10^n)*a[2n]
  - second number: a[1] + 10*a[3] + 100*a[5] + ... + (10^n)*a[2n+1]

# Time complexity
- Total time complexity:
  - Best and average case: `O(nlog(n))`
  - Worst (pivots already in position): `O(n^2`
- Analysis
  - Generating the numbers: `O(n)`
  - Sorting the array: using quicksort
    - Best and average case: `O(nlog(n))`
    - Worst (pivots already in position): `O(n^2`
