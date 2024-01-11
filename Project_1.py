print("Welcome to my quiz game !")
print("-------------------------")
name = input("Enter Your Name: ")
print("-------------------------")
print("Choose difficulty:")
print("Easy          Hard")
difficulty = input("E/H           ")

if difficulty.lower()[:1] != "e" and difficulty.lower()[:1] != "h":
    print("Please Spell Correctly ")
    while difficulty != "e" and difficulty != "h":
        difficulty = input("E/H           ")

if difficulty.lower()[:1] == "e":
    question = open('Easy',"r")
    answer = open("Easy_ans","r")
    correct = open("Easy_Correct_ans")
elif difficulty.lower()[:1] == "h":
    question = open("Hard","r")
    answer = open("Hard_ans","r")
    correct = open("Hard_Correct_ans")

print("-------------------------")
print("Let's start the game")
print("-------------------------")
score = 0
for i in range(1,5):
    print("Question number " + str(i))
    print("")
    print(question.readline())
    print(answer.readline())
    print("-------------------------")
    user_ans = input("Your answer is:")
    if correct.readline().strip().lower().replace(" ","") == user_ans.lower().strip().replace(" ",""):
        score += 10
    elif score > 0 and correct.readline().strip().lower().replace(" ","") != user_ans.lower().strip().replace(" ",""):
        score -= 5

    print("-------------------------")
print("Game Finished !")
print(name +" Your score is: " + str(score))




