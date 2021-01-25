#! python3
# randomQuizGenerator.py - This makes quizzes with questions, answers
# in a randomized order. It will also have the answer key.

import random

# Below is the quiz data. This version is just U.S. states w/ capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah':
'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Next, we generate 35 quiz files of randomized questions:
for quizNum in range(35):
    # TODO: Create quiz and answer key files.

    # TODO: Write out the quiz header.

    # TODO: Shuffle the order of the states.