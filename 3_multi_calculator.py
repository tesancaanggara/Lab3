#
# Calculator
# Tesanca Anggara 

sum = 0

# 1. Input
X1 = input ("Enter X1:")
X2 = input ("Enter X2:")
op = input ("Enter Operator:")

# 2. Process
if op == "+":
    sum = int(X1) + int(X2)
elif op == "-":
    sum = int(X1) - int(X2)
elif op == "*":
    sum = int(X1) * int (X2)
elif op == "/":
    sum = int(X1) / int(X2)

# 3. Output 
print(f"Sum:{sum}")