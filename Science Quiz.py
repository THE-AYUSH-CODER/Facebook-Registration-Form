score= 0
print("Science Quiz:")
print("______________________________________________")

# Question 1
print("\n")
print("1. Which gas is required for breathing?")
print("A: Nitrogen")
print("B: Oxygen")
print("C: Hydrogen")
print("D: Carbon Dioxide")
answer1= input("Write an option from A-D: ")
print("\n")

if(answer1 == "B" or answer1 == "b"):
    print("Correct!")
    score = score+1
else:
    print("Incorrect")
    
# Question 2
print("______________________________________________")
print("\n")
print("2. Which gas is required for breathing?")
print("A: Nitrogen")
print("B: Oxygen")
print("C: Hydrogen")
print("D: Carbon Dioxide")
answer2= input("Write an option from A-D: ")
print("\n")

if(answer2 == "B" or answer2 == "b"):
    print("Correct!")
    score = score+1
else:
    print("Incorrect")
    
# Question 3
print("______________________________________________")
print("\n")
print("3. Which gas is required for breathing?")
print("A: Nitrogen")
print("B: Oxygen")
print("C: Hydrogen")
print("D: Carbon Dioxide")
answer3= input("Write an option from A-D: ")
print("\n")

if(answer3 == "B" or answer3 == "b"):
    print("Correct!")
    score = score+1
else:
    print("Incorrect")

# Question 4
print("______________________________________________")
print("\n")
print("4. Which gas is required for breathing?")
print("A: Nitrogen")
print("B: Oxygen")
print("C: Hydrogen")
print("D: Carbon Dioxide")
answer4= input("Write an option from A-D: ")
print("\n")

if(answer4 == "B" or answer4 == "b"):
    print("Correct!")
    score = score+1
else:
    print("Incorrect")

# Question 5
print("______________________________________________")
print("\n")
print("5. Which gas is required for breathing?")
print("A: Nitrogen")
print("B: Oxygen")
print("C: Hydrogen")
print("D: Carbon Dioxide")
answer5= input("Write an option from A-D: ")
print("\n")

if(answer5 == "B" or answer5 == "b"):
    print("Correct!")
    score = score+1
else:
    print("Incorrect")

print("______________________________________________")
print("\n")
if score>3 or score==5:
    print("Well Done!")
if score<4:
    print("Better luck next time")
print("Your score is, ",score,"out of 5")
print("______________________________________________")
print("\n")
print("Correct Answers are:")
print("Question1. Your answer:",answer1,"Correct answer:B")  
print("Question2. Your answer:",answer2,"Correct answer:B")
print("Question3. Your answer:",answer3,"Correct answer:B")
print("Question4. Your answer:",answer4,"Correct answer:B")
print("Question5. Your answer:",answer5,"Correct answer:B")
print("\n")
print("______________________________________________")
