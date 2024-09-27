class Solution(object):
    def isValid(self, s):
        if len(s)%2:
            return False
        l = len(s)//2
        