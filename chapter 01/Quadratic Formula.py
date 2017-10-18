import math

def main():
    print("Had enough of your math class?, Luckily The Quadriatic Equation Solver 5000 is here!")
    a = eval(input("What is the A value?"))
    b = eval(input("What is the B Value?"))
    c = eval(input("Now tell me the C Value?"))
    discriminate = (b * b - 4 * a * c)
    if discriminate > 0:
        print("Root 1 is", (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
        print("Root 2 is", (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a))
    if discriminate < 0:
        print("there is no solution my man")

main()
