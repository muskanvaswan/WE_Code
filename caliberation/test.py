def lengthOfLongestSubstring(s : str) -> int :
    visited = {}
    max_sub_len = 0
    start = 0
    for i in range(0, len(s)):

        if s[i] in visited:
            print(max_sub_len)
            max_sub_len = max(max_sub_len, i - start)
            print(s[start:i])
            start = visited[s[i]] + 1
            print(start)

        visited[s[i]] = i
        print(visited)
    max_sub_len = max(max_sub_len, len(s) - start)
    return max_sub_len

#print(lengthOfLongestSubstring("abcabcabc"))
print(lengthOfLongestSubstring("nchsndhul"))
