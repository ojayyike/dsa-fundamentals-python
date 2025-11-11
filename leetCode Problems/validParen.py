class Solution:
    def __init__(self):
        self.open = {']':'[','}':'{',')':'('}
    
    def validParen(self,parens):
        stack = []
        for char in parens:
            if char in [')','}',']']:
                if not stack or stack[-1] != self.open[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
    
s = Solution()
print(s.validParen("()"))      # True
print(s.validParen("()[]{}"))  # True
print(s.validParen("(]"))      # Should be False - does yours work?
print(s.validParen("([)]"))    # Should be False
print(s.validParen("{[]}"))    # True
