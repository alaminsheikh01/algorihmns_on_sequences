"""
Compute the LPS (Longest Proper Prefix which is also Suffix) array.

lps[i] = length of the longest proper prefix of pattern[0:i+1]
which is also a suffix of pattern[0:i+1]
""" 

def compute_lps(pattern):
   m = len(pattern)
   lps = [0] * m

   length = 0

   i = 1

   while i < m:
        if pattern[i] == pattern[length]:
           # Characters match, extend current prefix-suffix
           length += 1
           lps[i] = length
           i += 1
        else:
           lps[i] = 0
           i += 1   
   return lps;
                  


"""
Find all occurances of pattern in text using KMP algorithm.
Return: List of starting indices where pattern occurs.
"""

def kmp_search(text, pattern):
    if not text or not pattern:
        return []
    
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)
    result = []

    # i - index for text
    # j - index for pattern

    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        # full pattern matched
        if j == m:
            result.append(i - j)
            
            # continue searching for next match
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                # jump using lps
                j = lps[j - 1]
            else:
                # No partial match, move text pointer
                i += 1

    return result;                







#Example usage
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print("Text:    ", text)
    print("Pattern: ", pattern)

    lps = compute_lps(pattern)
    print("LPS:     ", lps)

    matches = kmp_search(text, pattern)
    print("Matches at indices:", matches)

    # Overlapping example
    text2 = "AAAA"
    pattern2 = "AA"

    print("\nText:    ", text2)
    print("Pattern: ", pattern2)
    print("LPS:     ", compute_lps(pattern2))
    print("Matches at indices:", kmp_search(text2, pattern2))