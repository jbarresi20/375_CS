#This Program is designed by Joe Barresi. This program is designed to calculate a students test averages

def main():
    print("This program is going to calculate your average from your exam scores!")
    score = input("What's your Test Score (Enter to calculate)")
    number_of_scores = 0
    total = 0
    while score != "":
        total = eval(score) + total
        score = input("What's the next score (Enter to Calculate)")
        number_of_scores = number_of_scores + 1 #Since average is sum/number of scores we need a way to find both. We solve this by adding one to the total everytime a loop is completed.
    test_average = total / number_of_scores
    if test_average >= 90:
        comment = "Good Work, You're at an A!"
    elif test_average >= 80:
        comment = "Keep it up, You're on your way to an A"
    elif test_average >= 70:
        comment = "You're right at a C. Keep grinding for a B"
    else:
        comment = "Pick it up, you can do better!"
    print("Your Test Average is,", test_average, comment) #This section of the program makes your average a variable. It then uses If/Else to figure out your grade and gives a customized comment to it.

main()
