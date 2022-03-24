#Briana DeAndrade
#In order to run the program correctly, please know the name of my "fortunes file" is fortune.txt and will be the first input of the user

#I had to import random seeing as we will be pulling a random fortune from my fortune txt file
import random

#I begin with my main function. Here is where I established the all_fortunes variable, prompt the user of the name of my fortunes file
#I also established the function composition of what is to come: Load_fortunes function and display_fortunes function
def main():

    all_fortunes = open("fortune.txt", 'r')
    file = input("What is the name of your fortunes file?")
    load_fortunes(file)

    print(load_fortunes(file))

    display_fortunes(load_fortunes(file))

#Here is my load_fortunes function where I opened my file as a parameter, a string of my 20 fortunes will be output for the user and I had to return all_lines here as requested
def load_fortunes(file_name):
    file = open(file_name, 'r')
    all_lines = file.readlines()
    return all_lines

#Here is my display_fortunes function where I now use that list of strings as a parameter (as well as the random all_functions variable I established at the top)
def display_fortunes(all_fortunes):
    response = ""
    #Here I establish answers that I am not initially looking for
    no_answers = ["no", "not really", "no thanks"]
    #Here is where I use my no_answers variable and list
    while response not in no_answers:
        response = input("Do you want another fortune")
        #No matter the input, a random choice of all_fortunes will be used and output for the user
        response = response.lower()
        fortune1 = random.choice(all_fortunes)
        print(fortune1)
    #Once the user decides they do not want to receive any more fortunes, they will be shown "Have a good day." instead of more fortunes, thus completeing the project.
    while response in no_answers:
        print("Have a good day.")
main()