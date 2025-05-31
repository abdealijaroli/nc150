class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {')':'(', ']':'[', '}':'{'}
        
        for c in s:
            if c in charMap:
                if stack and stack[-1] == charMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
                
            