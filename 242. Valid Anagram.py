'''Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if self.dic(s)==self.dic(t): 
            return True
        else:
            return False  
            
    def dic(self, word):
        dic={}
        for i in word:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic.get(i)+1
        return dic
