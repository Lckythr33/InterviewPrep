#### Prompt

Say: "Tell me about the last project you worked on."

- *Identify*: Does the interviewee discuss their competencies based on what you have asked them? Competencies include:
   - Technical Skills (libraries, languages, etc.)
   - Interpersonal Skills  


- *Prove*: Does the interviewee provide a _specific_ example (past experience or hypothetical scenario)  to showcase competencies and/or fit? Is it presented in the form of a story (punchline, beginning, middle, positive end)?


- *Close*: Does the interviewee showcase why the company should hire them and how their skills/experience/values will add value to and align with the team/company? Does the interviewee showcase what they have learned in "Prove" and how they will apply it to the new role?

# 201 - Longest Substring Without Repeating Characters

Given a string `s`, find the longest substring without repeating characters.

```
Input: String
Output: String
```

# Example
```
Input: abcabcbb      =>	Output: abc
Input: bbbbb	 	=>	Output: b
Input: pwwkew		=>	Output: wke
```

# Constraints
```
N ~ Length of input string
K ~ Number of unique characters in input string

Time Complexity: O(N)
Auxiliary Space Complexity: O(K)
```

`s` consists of English letters, digits, symbols and spaces.

# Solution:

Use a sliding window approach, expanding as long as there are 0 repeated characters, and contracting as long as you have more than 0 repeated characters. Use a dictionary and an additional `repeated_chars` variable to keep track of repeated characters. Keep track of the indexes of the longest string you encounter along the way, and use them to return the best substring.


# Code

Solution in Python:

```py
def longest(s):
  l, r = 0, 0
  best_l, best_r = 0, 0
  chars = {}
  repeated_chars = 0

  while r < len(s):
    # expand
    if repeated_chars == 0:
      if r - l > best_r - best_l:
        best_l, best_r = l, r
      chars[s[r]] = chars.get(s[r], 0) + 1
      if chars[s[r]] > 1:
        repeated_chars += 1
      r += 1

    # contract
    while repeated_chars > 0:
      chars[s[l]] = chars.get(s[l], 0) - 1
      if chars[s[l]] == 1:
        repeated_chars -= 1
      l += 1

  return s[best_l:best_r]

```
