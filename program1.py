class Solution(object):
    def isValid(self, s):
        if len(s)%2:
            return False
        left, right = 0, len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
        return True

if __name__ == "__main__":
    print(Solution.isValid())