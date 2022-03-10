# This function will be used to get the calculations for height and weight
def getmeasure():
    height = float(input("Enter your height in inches "))
    mheight = height * 0.025
    sheight = mheight * mheight

    weight = int(input("Enter your weight in pounds "))
    mweight = weight * .45
    # We will use the formula to get that bmi and format it
    bmi = mweight / sheight
    formatbmi = float(format(bmi, '0.1f'))
    getbmi(formatbmi)


# This function will use the bmi to determine which group the bmi rating belongs to
def getbmi(formatbmi):
    print(formatbmi)

    if formatbmi < 18.5:
        print('underweight')
    elif formatbmi >= 18.5 and formatbmi < 25:
        print('normal weight')
    elif formatbmi >= 25 and formatbmi < 30:
        print("overweight")
    else:
        print("Obese")


getmeasure()
