def evalRPN(tokens):
        stack = []  
        operators = ['+', '-', '*', '/']
        for ele in tokens:
            if ele not in operators:
                stack.append(int(ele))
            else:
                
                num2 = stack.pop()
                num1 = stack.pop()
                if ele == '+':
                    result = num1 + num2 
                elif ele == '-':
                    result = num1 - num2 
                elif ele == '*':
                    result = num1 * num2 
                else:
                    result = float(num1) / (num2)
                    result = int(result) 
                stack.append(result)

        return stack[0]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))