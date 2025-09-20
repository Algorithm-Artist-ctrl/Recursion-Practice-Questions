def subsequence(str1):
    if len(str1) == 0:
        return [""]
    small = subsequence(str1[1:])
    result = []
    for item in small:
        result.append(item)
    for item in small:
        result.append(str1[0] + item)
    return result
print(subsequence("abc"))