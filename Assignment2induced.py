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
        # induced the lower limit of normal weight by 0.1.
    elif 18.6 <= formatbmi < 25:
        print('normal weight')
    elif 25 <= formatbmi < 30:
        print("overweight")
    elif formatbmi > 30:
        print("Obese")
    else:
        print("not on scale")

    input()


getmeasure()
