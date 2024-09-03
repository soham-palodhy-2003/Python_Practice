#Python Quiz game

questions = ("How many elements are in the periodic table? :",
              "Which animal lays the largest legs? :",
              "What is the most abdundant gas in the Earth's atmosphere? :",
              "How many bones are there in the human body? :",
              "Which planet in the solar system is the hottest? :")

options = (("A. 116", "B. 117 ", "C. 118 ", "D. 119"),
            ("A. Whale", "B. Ostrich", "C. Elephants", "D. Crocodile "),
            ("A. Nitrogen", "B. Oxygen", "C. Hydrogen", "D. Carbon-Dioxide"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercury", "B. Venus", "C. Saturn", "D. Mars"))   

answers = ("C", "B", "A", "A", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("You're Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")    
    question_num += 1    

print("--------------------")
print("  RESULTS  ")
print("--------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end =" ")
print()

for guess in guesses:
    print(guess, end =" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is : {score}%")
