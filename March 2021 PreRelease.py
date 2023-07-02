import random

def multiplication_quiz_testing():
    name = input("Enter your name: ")
    table = get_table_input()

    score = 0

    for question_number in range(1, 6):
        multiplier = random.randint(1, 12)
        answer = get_user_answer(table, multiplier)

        if answer == table * multiplier:
            score += 1

    print(f"{name}, your score is {score}/5")
    if score == 5:
        print("Well done! Full marks!")
    else:
        print("Have another practice!")


def multiplication_quiz_learning():
    name = input("Enter your name: ")
    table = get_table_input()

    for question_number in range(1, 6):
        multiplier = random.randint(1, 12)
        answer_attempts = 0

        while answer_attempts < 3:
            answer = get_user_answer(table, multiplier)

            if answer == table * multiplier:
                print(f"{name}, your answer is correct!")
                break
            else:
                answer_attempts += 1
                if answer > table * multiplier:
                    print(f"{name}, your answer is too large.")
                else:
                    print(f"{name}, your answer is too small.")

        if answer_attempts == 3:
            print(f"{name}, you have reached the maximum number of attempts.")
            print(f"The correct answer is: {table * multiplier}")


def multiplication_quiz_varying():
    name = input("Enter your name: ")
    table = get_table_input()
    num_questions = int(input("Enter the number of questions you want in the test: "))
    mixed_questions = input("Do you want mixed questions? (yes/no): ").lower() == "yes"

    score = 0

    for question_number in range(1, num_questions + 1):
        if mixed_questions:
            table = random.randint(2, 12)
        multiplier = random.randint(1, 12)
        answer = get_user_answer(table, multiplier)

        if answer == table * multiplier:
            score += 1

    print(f"{name}, your score is {score}/{num_questions}")
    if score == num_questions:
        print("Well done! Full marks!")
    else:
        print("Have another practice!")


def get_table_input():
    while True:
        try:
            table = int(input("Enter the multiplication table you want to use (2-12): "))
            if 2 <= table <= 12:
                return table
            else:
                print("Invalid input. Please enter a number between 2 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_user_answer(table, multiplier):
    while True:
        try:
            answer = int(input(f"Question: {table} X {multiplier} = "))
            return answer
        except ValueError:
            print("Invalid input. Please enter a valid number.")


multiplication_quiz_testing()
multiplication_quiz_learning()
multiplication_quiz_varying()
