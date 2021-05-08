# Algorithm
- Using a Trie to implement a HTTP router

# Time and Space Complexity Analysis
## Insertion
- Time: linear `O(n)`
- Space: linear `O(n)`
### Analysis
- Split the string path into an array of strings
  - Time: linear `O(n)`
  - Space: constant `O(1)`
- Add the path to the Trie by itterating through the array and adding the necessary nodes.
  - Time: linear `O(n)`
  - Space: worst case is linear when no item of the path already exists `O(n)`

## Search
- Time: linear `O(n)`
- Space: constant `O(1)`
### Analysis
- Split the string path into an array of strings
  - Time: linear `O(n)`
  - Space: constant `O(1)`
- Loop through nodes in the path, and get the handler
  - Time: linear `O(n)`
  - Space: constant `O(1)`