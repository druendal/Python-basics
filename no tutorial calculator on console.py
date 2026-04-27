#Simple Calculator program
Question = input("What would you like to calculate?:")
if Question == "Subtraction" or Question == "S":
    Subtrahend = float(input("What is your First Value?:"))
    Minuend = float(input("What is your Second Value?:"))
    difference = (Subtrahend - Minuend)
    print(f"this is your answer: {difference}")
elif Question == "Addition" or Question == "A" :
    Addends1 = float(input("What is  your first Value?:"))
    Addends2 = float(input("What is  your second Value?:"))
    ssum = Addends1 + Addends2
    print(f"this is your answer: {sum}")
elif Question == "Multiplication" or Question == "M":
    multiplicand = float(input("what is your first value?:"))
    multiplier = float(input("what is your second value?:"))
    product = multiplicand * multiplier
    print(f"this is your answer: {product}")

elif Question == "Division" or Question == "D":
    dividend = float(input("What is your first Value?:"))
    divisor = float(input("What is your second Value?:"))
    if dividend == 0 or divisor == 0:
        print("You cannot Divide with 0!")
    else:
       quotient = dividend / divisor
       print(f"this is your answer: {quotient}")

else:
    print(f"{Question} is not a valid arithmethic expression")
#end
