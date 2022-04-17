class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        stack = []
        d = {"(": ")", "[": "]", "{": "}"}
        
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            elif s[i] != d[stack[-1]]:
                return False
            else:
                stack.pop()
        
        return not stack

mySolution = Solution()
print(Solution.isValid(mySolution, "()[]")) 
