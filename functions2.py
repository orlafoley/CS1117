'''
To celebrate the start of the Rugby World cup,
I want to you to read the following pseudocode and write the code into a file called rugby_world_cup.py
Outline:
Write a program that asks the user for the names of the teams in the opening match,
the tries and points scored and prints out the results (my input here is only an example,
find the actual scores from last Saturdays match online).

Output of Program
Enter the name of team1: Japan
Enter the name of team2: Russia
Enter the number of tries for Japan: 0
Enter the number of tries for Russia: 2
Enter the number of converted/penalty points for Japan: 12
Enter the number of converted/penalty points for Russia: 9
'''

def rugby_teams():
    try:
        team1 = input("Please name a team playing in the 2019 Rugby World Cup: ").capitalize()
        team2 = input("Please name a second team playing in the 2019 Rugby World Cup: ").capitalize()

        tries1 = int(input("Enter the number of tries for " + team1 + ": "))
        tries2 = int(input("Enter the number of tries for " + team2 + ": "))

        points1 = int(input("Enter the number of converted/penalty points for " + team1 + ": "))
        points2 = int(input("Enter the number of converted/penalty points for " + team2 + ": "))

        #Print the results headings
        print("Team\tGoals\tPoints")
        print(team1, str(tries1),'', str(points1), sep='\t')
        print(team2, str(tries2),'', str(points2), sep='\t')
    except:
        print('Sad integer noises.')

#rugby_teams()







'''
Add a second function to your rugby_world_cup.py file, 
this function will request the name of an Irish rugby 
player and their age in days (check online for their ages). 
The program should tell them their ages in years and days.
'''

def rugby_players_age():
    try:
        players_name = input("Rugby Players Name: ").capitalize()
        days_old = int(input("How old is " + players_name + " in days? "))
        no_of_years = (days_old//365)
        #There are 365 days in a year
        remaining_days = (days_old - (no_of_years*365))
        print(players_name, "is", no_of_years, "years and", remaining_days, "days old.")
    except:
        print('That\'s not an age...')

#rugby_players_age()





'''
Work out how many seconds there is in 42 minutes and 42s?

How many miles are there in 10km? Hint there are 1.61km in 1 miles

If you run a 10km race in 42m 42s, what is your average pace i.e. time per mile in
minutes and seconds?

What is your average speed in miles per hour?
'''

a = ((42*60) + 42)
#print(a, "seconds")

b = (10*1.61)
#print(b, "miles")

c = (b/(a*60))
#print("Your average pace is", c, "time per mile.")

#There are 3600 seconds in an hour
d = b/(a*3600)
#print("Your average speed is", d, "miles per hour.")