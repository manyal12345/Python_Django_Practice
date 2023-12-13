# The calculation of the GPA is just assumption and Grade is as per nepal

percentage = float(input("Input is your percentage: "))

if percentage >= 90 and percentage <= 100:
    GPA = (percentage/20 -1)
    print('Your Grade is "A+"','GPA is ' + str(GPA))
elif percentage >= 80 and percentage < 90:
    GPA = (percentage/20 -1)
    print('Your Grade is "A"','GPA is ' + str(GPA))
elif percentage >= 70 and percentage < 80:
    GPA = (percentage/20 -1)
    print('Your Grade is "B+"','GPA is ' + str(GPA))
elif percentage >= 60 and percentage < 70:
    GPA = (percentage/20 -1)
    print('Your Grade is "B"','GPA is ' + str(GPA))
elif percentage >= 50 and percentage < 60:
    GPA = (percentage/20 -1)
    print('Your Grade is "C+"','GPA is ' + str(GPA))
elif percentage >= 40 and percentage < 50:
    GPA = (percentage/20 -1)
    print('Your Grade is "C"','GPA is ' + str(GPA))
elif percentage >= 35 and percentage < 40:
    GPA = (percentage/20 -1)
    print('Your Grade is "D"','GPA is ' + str(GPA))
elif percentage < 35:
    GPA = (percentage/20 -1)
    print('Your Grade is "NG"','GPA is ' + str(GPA))
else:
    print('Invalid percentage')