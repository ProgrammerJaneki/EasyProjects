#from datetime import datetime
#from playsound import playsound

from datetime import datetime
from playsound import playsound
import random
import os 
import time
from time import sleep
from progress.spinner import PieSpinner
from progress.bar import Bar, FillingCirclesBar


#Create Acronyms using Python

#user_input = str(input("Enter a Phrase: ")) # press ctrl + alt + b -- to input an answer
user_input = "Artificial Intelligence"
text = user_input.split() # splits every words into a list

holder = " "
for x in text:
	holder = holder + str(x[0].upper())

print("Acronym of ", user_input, " is: " ,holder)

#Alarm Clock with Python using datetime and playsound library


#-The program will ask for time of the alarm in a format of 
#-Hour:Minute:Seconds:Period
#-Input will be read as a string not a integer. 
#-In order to get the values, we need to use string slicing 
#-for the for alarm_ variables
"""
alarm_time = input("Enter the time of alarm to be set: HH:MM:SS:PM/AM\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")

#-strftime() is a function used to convert date and time objects 
#-to their string representation
#-To set up the current time, we declared the "now = datetime.now()"
#-We are getting the current time by using the strftime() function
#-and storing the values on the current_ variables
#-If the current time is equal to the alarm set, the playsound
#-function will play the ringtone set and break off the loop


while True:
	now = datetime.now()
	current_hour = now.strftime("%I")
	curret_minute = now.strftime("%M")
	current_seconds = now.strftime("%S")
	current_period = now.strftime("%p")
	if alarm_period == current_period:
		if alarm_hour == current_hour:
			if alarm_minute == curret_minute:
				if alarm_seconds == current_seconds:
					print("Wake up!!")
					playsound('my_alarm.wav')
					break """
###################################
# Email Slicer with Python
# 
# the email will be separated into 'username' and 'domain_name'
# the '@' will be the point of separation when using string slicing
# +1 on the starting index for domain_name get the value after '@'
email = "revillazjannelz@gmail.com".strip()
username = email[:email.index("@")] 
domain_name = email[email.index("@")+1:]
#
# An improve way to format strings in Python
# You can use either f or F result will be the same
format_ = (f"Username: {username} || Domain Name: {domain_name} ")
#
# The second one is hardly readable when you are dealing with multipler parameters
last_format = ("Your username: {} || Your Domain Name: {}".format(username,domain_name)) 
#
print(format_)
#
###################################

# Python Program to Generate Password
# We will import the random module to
# generate random password

# We will get the desired password length
# of the user
#password_length = int(input("Enter the length of the password: "))
password_length = 7
rans = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# We will use the method random and sample
# to return a given sample of the sequence
# in a specific length that the user input
password = "".join(random.sample(rans, password_length))
print(f"Password: {password}")

#################
# Random Password Generator Counter
#
# The program will ask the user how 
# many times the program will generate 
# a password
# We will count how many times the
# same element will occur while
# getting the percentage
# 
"""
counting = 0
percentage = 0
same_element = 0
password = []
repeated_elements = []

run_program = int(input("Enter how many times the program will run: "))
password_length = int(input("Enter the password length: "))
#pass_choices = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass_choices = "123456789"

# We will run loop n times and check
# if the same password will occur more
# than one times
# All outputs will be stored in the
# password variable
while counting < run_program:
	# random.choice is used because it can draw the same elements 
	# that were already drawn while random.sample will not pick 
	# elements in the same position more than once because they're
	# remove from the sample population

	password_string = "".join([random.choice(pass_choices) for i in range(password_length)])
	# It will check wheter the current value 
	# on the password_string is already present
	# in the password list

	if password_string in password:
		same_element += 1
		repeated_elements.append(password_string)
	# Here we will add the strings into the password list
	password.append(password_string)
	counting += 1

# formula to get the percentage of repeated elements
actual_percentage = float((len(repeated_elements) / run_program) * 100)

print(f"Password lists: {password} ")
print()
print(f"No. of elements: {run_program} ")
print(f"Same elements: {same_element} ")
print(f"Repeated elements: {repeated_elements} ")
print(f"Percentage: {actual_percentage} % ") """
print()
#
#################
# Rock, Paper and Scissors Game with Python
#
# User will continuously input their bets against a random
# choice by the computer using random module
#
class Games:
	def RPS(self):
		
		# We will set up the list of choices and make the Program
		# choose randomly before the player inputs their choice
		rps_choices = ["Rock", "Paper", "Scissor"]
		random_choice = random.choice(rps_choices)

		# This will help us break the nested loop
		loop_breaker = False

		# We will use while loop and let the user decide when the
		# program will stop
		while True:
			print("(Rock || Paper || Scissor) ")
			user_choice = input("Pick: ")
			print()

			# We will use conditional statements based on the user
			# choice and the random choice
			comp_choice = str(random_choice.upper())
			player_choice = str(user_choice.upper())
			if player_choice== "ROCK":
				time.sleep(0.1)
				print(f"Player: {player_choice} ")
				print(f"Computer: {comp_choice} ")
				if comp_choice == "PAPER":
					print("You lose!")
				elif comp_choice == "SCISSOR":
					print("You won!")
				else:
					print("Tie!")
			elif player_choice == "PAPER":
				time.sleep(0.1)
				print(f"Player: {player_choice} ")
				print(f"Computer: {comp_choice} ")
				if comp_choice == "SCISSOR":
					print("You lose!")
				elif comp_choice == "ROCK":
					print("You won!")
				else:
					print("Tie!")
			elif player_choice == "SCISSOR":
				time.sleep(0.1)
				print(f"Player: {player_choice} ")
				print(f"Computer: {comp_choice} ")
				if comp_choice == "ROCK":
					print("You lost!")
				elif comp_choice == "PAPER":
					print("You won!")
				else:
					print("Tie!")
			else:
				os.system('cls')
				continue
			
			# We will ask the user if he wants to continue or not
			while True:		
				another_loop = input("Do you want to continue? Y/N: ")
				if another_loop.upper() == "Y":
					break
				elif another_loop.upper() == "N":
					loop_breaker = True
					break

			if loop_breaker == True:
				time.sleep(0.2)
				os.system('cls')
				print("BYE!")
				break
			os.system('cls')
			#time.sleep(1)
# 	
game = Games()
#game.RPS() 

############################
# Progress Bar
#
def load_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '|'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filled_length = int(length * iteration // total)
	bar = fill * filled_length + '_' * (length - filled_length)
	print(f'\r{prefix} < {bar} > {percent}% {suffix}', end = '\r')
	if iteration == total:
		print()

item = list(range(0, 50))
l = len(item)
'''
load_bar(0, l, prefix = "Progress:", suffix = "Complete", length =l)
for i, item in enumerate(item):
	sleep(0.01)
	load_bar(i + 1, l, prefix = "Progress:", suffix = "Complete", length =l)
'''

############################
# Incrementing list of numbers in one Line
#
# We will make a program that continuously 
# add periods in a single line only
increment_this = []

for i in range(1,21):
	increment_this.append(i)
	if i == 20:
		print(f"\rList: {increment_this}", end="\r")
		break
	else:
		print(f"\rList: {increment_this} == Next no: {i + 1} ", end="\r")
		sleep(0.02)
print()

###########################
# Different Progress Bar
#
# 
print(10*"#", "Progress Bar", 10*"#")
class ProgressBar:
	def Bar(self):		
		bar = Bar("Processing", fill="=",suffix="%(percent)d%%",max = 20)
		for i in range(20):
			sleep(0.1)
			bar.next()
		bar.finish()
	def FillingBar(self):
		with FillingCirclesBar("Processing", max = 20) as filling_square_bar:
			for x in range(20):
				sleep(0.1)
				filling_square_bar.next()

	def Spinner(self):
		from progress.spinner import Spinner
		# state 
		spinner = PieSpinner("Loading ")
		spinner_counter = 0
		while spinner != "FINISHED":
			sleep(0.1)
			print(f"  Counter: {spinner_counter} ", end="")
			spinner.next() 
			spinner_counter += 1
			if spinner_counter == 21:
				spinner.finish()
				break

	def BubbleBar(self):
		from alive_progress import alive_bar
		from time import sleep

		with alive_bar(200, bar = 'bubbles', spinner = 'notes2') as bar:
			for x in range(200):
				sleep(0.03)
				bar()
       			                    # call after consuming one item		

# This is where different progress bars are
"""
progress_bar = ProgressBar()
progress_bar.Bar()
#progress_bar.Spinner()
progress_bar.FillingBar()
progress_bar.BubbleBar()
print()
"""
print()
thisNumber = 12
thisThis = f"My age is {12}"
print(thisThis)

