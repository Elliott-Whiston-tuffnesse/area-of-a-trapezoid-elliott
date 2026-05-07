game.splash("Lets calculate the area of a trapezoid!")
let Base1 = game.askForNumber("What is the length of base1? (cm)")
let Base2 = game.askForNumber("What is the length of base2? (cm)")
let Height = game.askForNumber("What is the height of the trapezoid? (cm)")
let Step1 = Base1 + Base2
let Step2 = Step1 / 2
let Step3 = Step2 * Height
game.splash("The area of the trapezoid with base1 length " + Base1 + "(cm), base2 length " + Base2 + "(cm) and a height of " + Height + " (cm), is:" + Step3 + " (cm^2)")
