# Naive Exact String Matching

### The Naive String Matching Algorithm is the simplest methiod for finding all occurrences of a pattern `P` in a text `T`.


### So the basic idea the algo aligns the pattern with the text at every possible position and compares characters one by one.

possible string position are:<br>
0,1,2 ... n-m

At each position 
- compare `P[0]` with `T[i]`,<br>
- compare `P[1]` with `T[i+1]` <br>

continue until - a mismatch occurs, or all m characters match.

## Psudocode

```
NAIVE-STRING-MATCH(T, P)
    n = length(T)
    m = length(P)

    for i = 0 to n (minus) m
        j = 0
        while j < m and T[i + j] = P[j]
            j = j + 1
        if j = m
            output i    
```

## Time Complexity
Worst Case <br>
At each of the `n - m + 1` positions, up to `m` comparisons may be performed. <br>
`N((n-m+1)m) = O(nm)`

### Example of worst case
```
T = AAAAAAAA
P = AAAAB
```

### Best case <br>
`O(n)`

### Example of best case
```
T = AAA
P = AA
```
Matches at postion: `0, 1, 2`



## Summary
- Tries every possible alignment of the pattern in the text.
- Compare characters left to right.
- Reports all maching postions
- Requires no preprocessing
- Runs in O(nm) time in the worst case.