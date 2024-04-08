# Tesanca Anggara
# BMI

sum = 0 

while True : 
    # 1. Input
    x1 = input ("Enter your weight in kilograms  : ")
    x2 = input ("Enter your height in meters     : ")

    # 2. Process
    sum =  float (x1) / (float (x2)**2)

    # 3. Output
    print (f"Your BMI is : {sum} ")
    res = input ("Continue? (yes/no) : ")
    if res == "no" :  
        break;

