#
# Tesanca Anggara
# Calculator with function
#

# Define Function
def cal(x1, x2, op):
    x1 = float(x1)
    x2 = float(x2)

    if op == '+':
        return int(x1) + (x2)
    elif op == '-':
        return int(x1) - (x2)
    elif op == '*':
        return int(x1) * (x2)
    elif op == '/':
        return int(x1) / (x2)

# 1. Input
x1 = input('Type x1: ')
x2 = input('Type x2: ')
op = input('Type operator: ')

# 2. Process
sum = cal(x1,x2,op)

# 3. Output
print(f'Sum: {sum}')