#This program is by Joe Barrei and converts MPH and M/s

def main():
    print("So you wanna know how fast your going? You really couldn't be like every other country and use metric")
    print("Nonetheless here is the MPH converter 1600")
    y = eval(input("Please type the velocity in m/s? You best don't put no commas."))
    if y < 0:
        print("Invalid Input!")
    else:
        #2.23694 is derived from Google which is derived from m/s multiplied by 3600 to get meters/mile. From there dividing by 1609.34 to get meters to Miles. This simplified is 2.23694
        print(y, "m/s =" , 2.23694 * y, "MPH")

main()
