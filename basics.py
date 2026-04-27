# this is your first code
print("helloooo")

# variables
# = "Chloe"
#sample_int = -23
#sample_float = 1.64
#sample_boolean = False
#print(f"this is my name: {sample_string}")
#print(f"this is my float {sample_float}")
#print(f"this is my int {sample_int}")
#print(f"this is my boolean {sample_boolean}")

#type casting
#sample_float =sample_float + 12
#sample_float = str(sample_float) # this changes the float variable into  a string
#print (type(sample_float)) #this tells which type the  value is

#print(sample_string)

#user inputs

#Name = input("What is your name?: ")
#Age = input("what is your  age?: ")
#school = input("what is your school?: ")

#print(f"hello {Name}! ")
#print(f"you are {Age} years old")
#print(f"and you go to {school} school")
#print(f"are the answers you wrote correct?")

#calculator test rectangle
#length= int(input("what is your length?: "))
#area = length*width

#print(f"the area of a rectangle  is {area}")

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