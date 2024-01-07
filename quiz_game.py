print("************************")
print("Welcome to My Quiz Game!!!")

question_bank = [
    {"text": "In Python, what is the process of creating a new class based on an existing class known as?", "answer": "A"},
    {"text": "Which of the following is used to represent the 'self' parameter in a class method in Python?", "answer": "B"},
    {"text": "What is the purpose of the 'if __name__ == '__main__': statement in a Python script?", "answer": "B"},
    {"text": "Which of the following is the correct way to open a file named 'example.txt' in Python for reading?", "answer": "B"},
    {"text": "What is the purpose of the 'super()' function in Python?", "answer": "A"}
]

options = [
    ["A. Inheritance", "B. Encapsulation", "C. Polymorphism", "D. Abstraction"],
    ["A. this", "B. self", "C. object", "D. instance"],
    ["A. To define the main function", "B. To check if the script is being run as the main program", "C. To include external libraries", "D. To handle exceptions"],
    ["A. file = open('example.txt', 'w')", "B. file = open('example.txt', 'r')", "C. file = open('example.txt', 'a')", "D. file = open('example.txt', 'D. x')"],
    ["A. To call the superclass constructor", "B. To create an instance of the superclass", "C. To access the superclass's attributes", "D. To override a method in the superclass"]
]

score = 0

# Checking the answers if it is correct or not
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
    

for question_num in range(len(question_bank)):
    print("*********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)
    
    guess = input("Enter your answer (A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])   #Calling the check_answer function to check the answer
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")

print("Your final score is", score)