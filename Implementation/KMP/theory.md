## KMP (Knuth-Morris-pratt) String Matching Algorithm

This algorithm invented to improves over the naive method by avoiding unnecessary re-comparisons.


### Main idea
when a mismatch occurs, the naive algorithm shifts the pattern by one position and starts comparing from the beginning.

Instead of KMP uses information from the pattern itself to decide how far to shift the pattern.

It actually preprocesses the pattern and builds an array called
- LPS = Longest Proper Prefix which is also a Suffix

### What is LPS
- Prefix = starts at the beginning 
- Suffix = ends at the end
- Proper prefix = not the whole string

### Psudocode

```
KMP(T, P)
    compute lps[]
    i = 0
    j= 0

    while i < n
        if T[i] == P[j]
            i++
            j++

        if j == m
            output i - j
            j = lps[j - 1]

        else if i < n and T[i] != P[j]
            if j != 0
                j = lps[j - 1]
            else 
                i++        
```

### Time complexity

Preprocessing LPS<br>
`O(m)`<br>
Searching<br>
`O(n)`<br>
Total<br>
`O(n + m)`


### Advantages of KMP

- Much faster than naive in worst case.
- Never moves the text pointer backward
- Guranteed linear time.

### Summary

KMP consits of two phases:<br>
- Build the LPS array.
- Use the LPS array to search efficiently