"""
Generates an array `lps_arr` such that each element
`lps_arr[i]` corresponds to the length of the longest 
proper prefix that is also a proper suffix in pat[:i].
"""
def calculate_lps_array(pat):
    lps_arr = [0] * len(pat)

    i = 1
    pref_ptr = 0 # ptr to check end of prefix

    while i < len(pat):
        if pat[pref_ptr] == pat[i]: # if 2 characters are equal
            pref_ptr += 1           # prefix suffix length here = pref_ptr + 1
            lps_arr[i] = pref_ptr 
            i += 1
        elif pref_ptr == 0: # if pref_ptr at 0 and 2 characters are not equal
            lps_arr[i] = 0  # prefix suffix length here is 0
            i += 1
        else: # look through prefix to see if there are any matches
            pref_ptr = lps_arr[pref_ptr - 1]

    return lps_arr

"""
Implementation of kmp that returns first index in array of a
given pattern.
"""
def kmp(pat, text):
    lps_arr = calculate_lps_array(pat)

    pt = 0 # ptr for text
    pp = 0 # ptr for pattern

    while (pt < len(text)):
        if text[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = lps_arr[pp - 1]

        if pp == len(pat): # if pattern is found
            return pt - len(pat)

    return -1

print(kmp("aaaa", "aaacaaaa"))

"""
# Why is kmp O(m + n)?
At first glance, its not obvious that both loops run in linear
time. This is mainly due to the decrements (of both pref_ptr
and pp). However, if you notice that the number of decrements
is always less than the number of increments, it should be
obvious that both loops run in linear times.
"""