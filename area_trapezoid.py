#Created by Elliott Whiston
#Created on 06/08/2026
# This program calculates the area of a trapezoid using the formula: Area = (Base1 + Base2) / 2 * Height
print("Lets calculate the area of a trapezoid!")
#asks for the measurments of the trapezoid from the user
Base1 = float(input("What is the length of base1? (cm)"))
Base2 = float(input("What is the length of base2? (cm)"))
Height = float(input("What is the height of the trapezoid? (cm)"))
#Initializes step1, step2, and area variables to calculate the area of the trapezoid
Step1 = Base1 + Base2
Step2 = Step1 / 2
Area = Step2 * Height

# displays the area of the trapezoid to the user
print("The area of the trapezoid with base1 length " + str(Base1) + 
    " (cm), base2 length " + str(Base2) + 
    " (cm) and a height of " + str(Height) + 
    " (cm), is: " + str(Area) + " (cm^2)")