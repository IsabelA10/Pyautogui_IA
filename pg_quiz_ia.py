import pyautogui as pg
import time
import webbrowser 

points = 0

# Question
answer = pg.prompt(
"""
What would you rather do?

a)Go out all night and party with your friends.
b)Stay home and binge watch your favorite show and eat a lot of food.
c)Have a tranquil meal with your parents.
d)Adopt a chair.

"""
    ) 


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question
answer = pg.prompt(
"""
What would you rather do during summer?

a)Hang out with your friends in town.
b)Travel to a very cool place.
c)Go to math camp.
d)Play with furniture.

"""
    ) 


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4


# Question
answer = pg.prompt(
"""
What day of the week is your favorite?

a)Saturday
b)Friday
c)Monday
d)What's a week?

"""
    ) 


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question
answer = pg.prompt(
"""
What is your favorite subject?

a)Study hall
b)English
c)Love all of them
d)I don't go to school

"""
    ) 


# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4




# End of Survey

pg.alert("You are...")

#Too social
if points < 7:
    pg.alert("Too social, be with ur family a little")
    webbrowser.open("https://i.imgur.com/6sjgqQB.gif")

#Pretty normal
elif points >=7 and points < 10:
    pg.alert("Congrats! ur normal")
    webbrowser.open("https://kathleensallen.files.wordpress.com/2015/08/dean-says-youre-awesome.gif")

#Get out of your house
elif points >= 10 and points < 13:
    pg.alert("Get out of ur house and get some friends")
    webbrowser.open("https://assets-auto.rbl.ms/fdb6763855d5495d4ea7c7acbcd9a915d9ae8f0409d0c9312f625b117d28dd18")

#ur wierd 
elif points >= 13:
    pg.alert("ur the wierdest person i know")
    webbrowser.open("https://media.giphy.com/media/N3oLgfdoU4nPG/giphy.gif")
    

    
    
