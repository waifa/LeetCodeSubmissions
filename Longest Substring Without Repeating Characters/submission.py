# link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        longest = 1
        for i in range(len(s)-1):
            for j in range(i+1+longest, len(s)+1):
                lencurr = len(s[i:j])
                if len(set(s[i:j]))<lencurr:
                    break
                if lencurr>longest:
                    longest = lencurr
        return longest
                