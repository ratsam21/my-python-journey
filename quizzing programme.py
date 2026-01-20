



def run_quiz(questions):
    score = 0

    for german, english in questions.items():
        answer = input(f"{german}: what is this in English? ")

        if answer.lower() == english.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    return score

def save_score(result):
    f = open("happy.txt","r+")
    print("Your previous scores were",f.read())

    f.write("\n"+str(result))




questions = {
    "Tag": "day",
    "Kalt": "cold",
    "Deutsch": "German",
    "empfehlen": "to recommend",
    "und": "and"
}

print("This is a quiz")
print("Find the English word for these German words")

result = run_quiz(questions)
print(f"You got {result} out of {len(questions)}")
save_score(result)



