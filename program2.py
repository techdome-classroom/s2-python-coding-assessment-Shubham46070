class Solution(object):
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum((-1 if d[s[i]] < d[s[i + 1]] else 1) * d[s[i]] for i in range(len(s) - 1)) + d[s[-1]]