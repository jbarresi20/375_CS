def main():
    repeat = "y"
    print("This is your ebay fee calculator")
    x = 1
    for i in range (10000000):
        x = x + 1
    while repeat == "y":
        selling_price = eval(input("What did your item sell for?"))
        total_value = selling_price - (selling_price * .10)
        print("Congrats your total Value for that item is", total_value)
        repeat = input("Press y to do another. If you do not want to press anything else.")
    print("Thank you for using our software! Have a good day now.")
main()
