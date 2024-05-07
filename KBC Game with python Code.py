import random

# Questions, options, and Answers
questions = {
    "Who is the creator of Python?": {
        "options": ["Guido van Rossum", "Larry Page", "Mark Zuckerberg", "Jeff Bezos"],
        "answer": "Guido van Rossum",
        "amount": "₹1000"
    },
    "What is the capital of France?": {
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris",
        "amount": "₹2000"
    },
    "What is the largest mammal in the world?": {
        "options": ["Blue Whale", "Elephant", "Giraffe", "Hippopotamus"],
        "answer": "Blue Whale",
        "amount": "₹5000"
    },
    "What is the chemical symbol for water?": {
        "options": ["H2O", "CO2", "NaCl", "CH4"],
        "answer": "H2O",
        "amount": "₹10000"
    },
    "What year did the Titanic sink?": {
        "options": ["1912", "1905", "1920", "1899"],
        "answer": "1912",
        "amount": "₹20000"
    },
    "What is the color of Sky?": {
        "options": ["Red", "Blue", "Yellow", "Green"],
        "answer": "Blue",
        "amount": "₹50000"
    },
    "Where the Taj Mahal?": {
        "options": ["Haryana", "Uttar Pardesh", "Goa", "Bihar"],
        "answer": "Uttar Pardesh",
        "amount": "₹80000"
    },
    "Who is the First Prime Minister Of India?": {
        "options": ["Mahatma Gandhi ", "Sardar Ballab Bhai Patel", "Dr. Bheem Rao Ambedar", "Pt Jawhar lal Nehru"],
        "answer": "Pt Jawhar lal Nehru",
        "amount": "₹120000"
    },
    "What is the Old name of India?": {
        "options": ["Bharat", "India", "Hindu", "Samaj"],
        "answer": "Bharat",
        "amount": "₹180000"
    },
    "What is the total Capital of India ?": {
        "options": ["28", "22", "19", "25"],
        "answer": "28",
        "amount": "₹250000"
    }
}

def get_random_question():
    return random.choice(list(questions.keys()))

def play_kbc():
    print("Welcome to Kaun Banega Crorepati!")
    score = 0
    won_rupees = 0
    for i, (question, data) in enumerate(questions.items(), start=1):
        print("\nQuestion {}: {} (Amount: {})".format(i, question, data["amount"]))
        options = data["options"]
        random.shuffle(options)
        for j, option in enumerate(options, start=1):
            print(f"{j}. {option}")
        print("Enter 'q' to quit the game.")
        answer_input = input("Enter your answer (1-4): ")
        if answer_input.lower() == 'q':
            print("\nYou chose to exit the game.")
            print("\n Okk bye ....")
            break
        else:
            answer_index = int(answer_input) - 1
            user_answer = options[answer_index]
            correct_answer = data["answer"]
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
                won_rupees = data["amount"]
            else:
                print("Incorrect! The correct answer is:", correct_answer)
    print("\nGame Over!")
    print("You scored {} out of 10.".format(score))
    print("You won {}.".format(won_rupees))

play_kbc()
