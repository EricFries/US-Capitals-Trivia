# The US Capitals game

#Import random module
import random

#Introduces the game
print("Welcome to the US Capitals Trivia Contest!  Find out if you're smart as your 7 year old niece!\n")
player = input("What's your name? ")

#Create list of states & their Capitals (tuples)
all_states_caps = [('Alabama', 'Montgomery'), ('Alaska', 'Juneau'), ('Arizona', 'Phoenix'), ('Arkansas', 'Little Rock'), ('California', 'Sacramento'), ('Colorado', 'Denver'), ('Connecticut', 'Hartford'), ('Delaware', 'Dover'), ('Florida', 'Tallahassee'), ('Georgia', 'Atlanta'), ('Hawaii', 'Honolulu'), ('Idaho', 'Boise'), ('Illinois', 'Springfield'), ('Indiana', 'Indianapolis'), ('Iowa', 'Des Moines'), ('Kansas', 'Topeka'), ('Kentucky', 'Frankfort'), ('Louisiana', 'Baton Rouge'), ('Maine', 'Augusta'), ('Maryland', 'Annapolis'), ('Massachusetts', 'Boston'), ('Michigan', 'Lansing'), ('Minnesota', 'Saint Paul'), ('Mississippi', 'Jackson'), ('Missouri', 'Jefferson City'), ('Montana', 'Helena'), ('Nebraska', 'Lincoln'), ('Nevada', 'Carson City'), ('New Hampshire', 'Concord'), ('New Jersey', 'Trenton'), ('New Mexico', 'Santa Fe'), ('New York', 'Albany'), ('North Carolina', 'Raleigh'), ('North Dakota', 'Bismark'), ('Ohio','Columbus'), ('Oklahoma', 'Oklahoma City'), ('Oregon', 'Salem'), ('Pennsylvania', 'Harrisburg'), ('Rhode Island', 'Providence'), ('South Carolina', 'Columbia'), ('South Dakota', 'Pierre'), ('Tennessee', 'Nashville'), ('Texas', 'Austin'), ('Utah', 'Salt Lake City'), ('Vermont','Montpelier'), ('Virginia', 'Richmond'), ('Washington', 'Olympia'), ('West Virginia', 'Charleston'), ('Wisconsin', 'Madison'), ('Wyoming', 'Cheyenne')]

#Get random integer in a range to choose a random state/city tuple
X = random.randint(0,49)
selected_state_cap = all_states_caps[X]

#Ask the trivia question integrating the state from the random tuple
print("What is the capital of %s?\n" %(selected_state_cap[0]))

#Create list to store the answer choices
ans_choices = [selected_state_cap[1]]

#Create list for used random numbers to prevent using same state/city twice.
used_numbs = [X]

#Populate the rest of ans_choices with three wrong answer choices
while len(used_numbs) < 4:
    Z = random.randint(0,49)
 
    if Z not in used_numbs:
        used_numbs.append(Z)
        ans_choices.append(all_states_caps[Z][1])
    else:
        pass

#Create list of answer choices and shuffle their order.
display_choices = []
for city in ans_choices:
    display_choices.append(city)

random.shuffle(display_choices)

#Set winning answer to an integer that corresponds to the number choices shown to the user by adding 1.
#Display choices. 
correct_answer = display_choices.index(selected_state_cap[1])+1
print ("1 -", display_choices[0], "\n2 -", display_choices[1], "\n3 -", display_choices[2], "\n4 -", display_choices[3])

#Initialize input and counting variables.  Ask the question, and give the player 3 chances to get it right.
users_guess = None
attempts = 0

while (attempts < 3):
    try:
        users_guess = int(input("\nWhat's your answer? "))
        attempts = attempts + 1
    except:
        print ("\nSorry, that's an invalid choice. Enter 1-4.")
        continue
    
    if users_guess == correct_answer:
        print ("\nThat's right, %s!" % (player))
        break
     
    elif (users_guess != correct_answer) & (attempts == 1):
        print ("\nWrong.  You have 2 guesses left.")

    elif (users_guess != correct_answer) & (attempts == 2):
        print ("\nWrong.  You have 1 guess left.")

    else:
        print ("\nThat's wrong, %s! The correct answer is %s." % (player, selected_state_cap[1]))
