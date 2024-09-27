class Solution(object):
    def isValid(self, s):
        lis = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                lis.append(i)
            else:
                if not lis:
                    return False
                if (i == ")" and lis[-1] != "(") or \
                   (i == "}" and lis[-1] != "{") or \
                   (i == "]" and lis[-1] != "["):
                    return False
                lis.pop()
        return len(lis) == 0