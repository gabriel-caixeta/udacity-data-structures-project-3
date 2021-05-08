# Algorithm
- Use a Trie to implement an autocomplete algorithm

# Time and Space Complexity Analysis
# Insertion
- Time: `O(n)` where n is the number of characters in the word to be added
- Space: `O(n)`
## Analysis
- Itterate through the `n` characters in the word and add the necessary TrieNodes
  - Time: `O(n)`
  - Space: `O(n)`

# Search
- Time: `O(n)`
- Space: `O(1)`
## Analysis
- Itterate through the existing nodes the match the characters in the prefix
  - Time: `O(n)`
  - Space: `O(1)`

# Get suffixes
- Time: `O(n)` where n is the number of child nodes
- Space: `O(1)`
## Analysis
- Itterate through all children of a prefix node, and return all the possible words.
  - Time: `O(n)`
  - Space: `O(1)`
