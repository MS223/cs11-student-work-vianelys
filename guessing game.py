name = raw_input("What's your name?")
# This line asks the user's name
upper_bound = input("Alright" + name + ", what's the highest number you can think of?")
#this line asks the user for the highest number they can think of and inserts their name into a statement
user_guess = input ("Between 1 and your number, what number am I thinking of?") #this line makes it clear that this is a guessing game between 1 and the number they chose in the line above
import random #this line is the beginning of randomness
number = random.randint(1,upper_bound)
#this line chooses a random number between 1 and the user's number in line 3
while number != user_guess:
# this while loop tells the computer what to do if they are wrong
    if number < user_guess:
        print ("A little lower!")
        user_guess = input ("Between 1 and your number, what number am I thinking of?")
    elif number > user_guess:
        print ("Woah! Too high!")
        user_guess = input ("Between 1 and your number, what number am I thinking of?")
print ("You got it!")
# hey monday me. I can't think right now, so you finish it.
 #It took 4 periods but I finally got it!
