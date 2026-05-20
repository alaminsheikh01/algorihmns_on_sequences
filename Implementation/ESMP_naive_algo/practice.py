def naive_string_matching(text, pattern):

    n = len(text)
    m = len(pattern)
    result = []

    if m == 0 or m > n:
        return result
    

    # try every possible starting postion 
    for i in range(n - m + 1):
        j = 0

        while j < m and text[i + j] == pattern[j]:
            j +=1

        if j == m:
            result.append(i)

    return result            



text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

output = naive_string_matching(text, pattern)

print(output)