#! python3
# randomQuizGenerator.py - This makes quizzes with questions, answers
# in a randomized order. It will also have the answer key.

import random

# Below is the quiz data. This version is just U.S. states w/ capitals.
# Commented-out lines come from Al Sweigart's example source code.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitalsItems = list(capitals.items())

# Next, we generate 35 quiz files of randomized questions:
for quizNum in range(35):
    # Now, we create the quiz and answer key files:
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    #quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
    #answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write the header for the quiz:
    quizFile.write('Name:\n\nDate: \n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    #quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Next, shuffle the order of the states:
    states = list(capitals.keys())  # keys = state names; values = capital names
    random.shuffle(states)

    # Loop through all 50 states and make a question for each:
    for questionNum in range(50):

        # Give right and wrong answers:
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())  # get a complete list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # remove right answer
        wrongAnswers = random.sample(wrongAnswers, 3)   # give 3 random wrong answers
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)   # randomizes the answer order

        # Write question and answer options to the quiz file:
    quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
    for i in range(4):
        quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')
        # Write answer key to a file:
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKeyFile.close()