def longestPalindrome(s):

    if s == "":
        return ""

    longest = s[0]   
    for i in range(len(s)):
        for j in range(i, len(s)):
            
            subchaine = s[i:j+1]

            if subchaine == subchaine[::-1]:
                
                if len(subchaine) > len(longest):
                    longest = subchaine

    return longest

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("dada"))
print(longestPalindrome("kayak"))
print(longestPalindrome("nana"))

