# Algorithm
- Using a recursive divide and conquer algorithm to constantly divide the possible numbers in half until finding the best solution

# Time Analysis
## Time complexity
- Best case happens on square numbers
- Worst case, any other number, since there needs to be an approximation/finding the best solution logic
- As shown in the table below, the itterations of the recursion and the log2(n) follow a similar trend (not an exact match throughout).

## Time table
|  n  | itterations | log2(n) |
| :--: | :---------: | :--: |
| 0 | 1 | Undefined |
| 1 | 1 | 0 |
| 2 | 3 | 1 |
| 3 | 3 | 2 |
| 4 | 2 | 2 |
| 5 | 3 | 3 |
| 6 | 4 | 3 |
| 7 | 4 | 3 |
| 8 | 4 | 3 |
| 9 | 2 | 4 |
| 10 | 5 | 4 |
| 11 | 5 | 4 |
| 12 | 5 | 4 |
| 13 | 5 | 4 |
| 14 | 5 | 4 |
| 15 | 5 | 4 |
| 16 | 4 | 4 |
| 17 | 5 | 5 |
| 18 | 5 | 5 |
| 19 | 5 | 5 |
| 20 | 6 | 5 |
| 21 | 6 | 5 |
| 22 | 6 | 5 |
| 23 | 6 | 5 |
| 24 | 6 | 5 |
| 25 | 5 | 5 |
| 26 | 6 | 5 |
| 27 | 6 | 5 |
| 28 | 6 | 5 |
| 29 | 6 | 5 |
| 30 | 6 | 5 |
| 31 | 6 | 5 |
| 32 | 6 | 5 |
| 33 | 6 | 6 |
| 34 | 6 | 6 |
| 35 | 6 | 6 |
| 36 | 6 | 6 |
| 37 | 7 | 6 |
| 38 | 7 | 6 |
| 39 | 7 | 6 |
| 40 | 7 | 6 |
| 41 | 7 | 6 |
| 42 | 7 | 6 |
| 43 | 7 | 6 |
| 44 | 7 | 6 |
| 45 | 7 | 6 |
| 46 | 7 | 6 |
| 47 | 7 | 6 |
| 48 | 6 | 6 |
| 49 | 3 | 6 |
