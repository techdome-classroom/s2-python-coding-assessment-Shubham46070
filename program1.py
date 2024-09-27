class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)

if __name__ == "__main__":
    print(Solution.isValid())