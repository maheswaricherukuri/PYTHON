class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_map={} #dict
        for i in range(len(s)):
            if s[i] not in letter_map:
                if t[i] in letter_map.values():
                    return False
                letter_map[s[i]]=t[i]
            else:
                if letter_map[s[i]] != t[i]:
                    return False
        return True
        
        
 class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
