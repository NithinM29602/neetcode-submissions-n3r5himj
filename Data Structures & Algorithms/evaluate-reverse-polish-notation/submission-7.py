class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                value2 = stack.pop()
                value1 = stack.pop()

                if token == '+': stack.append(value1+value2)        
                elif token == '-': stack.append(value1-value2) 
                elif token == '*': stack.append(value1*value2) 
                elif token == '/': stack.append(int(value1/value2)) 

        return stack.pop()