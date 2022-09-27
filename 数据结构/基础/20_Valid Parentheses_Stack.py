# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        
        
        for i in s:
            if i in open_par:
                stack.append(i)
            # elif stack" condition will work only when stack is NOT empty. It's a equivalent to "elif len(stack) != 0
            elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return stack == []
