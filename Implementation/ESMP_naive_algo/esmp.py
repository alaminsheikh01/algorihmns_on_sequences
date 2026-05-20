def esmp_naive(text, pattern):
    """
    Naive exact string matching algorithm.
    Finds all occurrences of pattern in text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to find
    
    Returns:
        list: Indices where pattern is found in text
    """
    if not pattern or not text:
        return []
    
    occurrences = []
    n = len(text)
    m = len(pattern)
    
    # Check each position in text
    for i in range(n - m + 1):
        # Check if pattern matches at position i
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        if match:
            occurrences.append(i)
    
    return occurrences


if __name__ == "__main__":
    # Test cases
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    result = esmp_naive(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Occurrences at indices: {result}")
    print()
    
    # Test with overlapping patterns
    text2 = "AAAA"
    pattern2 = "AA"
    result2 = esmp_naive(text2, pattern2)
    print(f"Text: {text2}")
    print(f"Pattern: {pattern2}")
    print(f"Occurrences at indices: {result2}")
    print()
    
    # Test with no match
    text3 = "HELLO"
    pattern3 = "XYZ"
    result3 = esmp_naive(text3, pattern3)
    print(f"Text: {text3}")
    print(f"Pattern: {pattern3}")
    print(f"Occurrences at indices: {result3}")
