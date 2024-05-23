# import modules
from turtle import Turtle, Screen
import random
from list_of_turtles import turtles_list
from racer import Racer

# create screen object
scr = Screen()
# change screen size
scr.setup(width=500, height=400)

# declare variables
n_turtles = 6
racer_list = []
racer_prompt = ''

# select racers
for turtle_index in range(0, n_turtles):
    # randomly select racer from turtles list
    turtle_selected = random.choice(turtles_list)
    # remove randomly selected racer from turtles list for future iterations
    turtles_list.pop(turtles_list.index(turtle_selected))
    # calculate starting pos
    x = -230
    y = -150+(350/n_turtles*turtle_index)
    # create new Racer instance
    racer = Racer(shape="turtle", name=turtle_selected[0], col=turtle_selected[1], start_pos_x=x, start_pos_y=y)
    racer.color(racer.col)
    # add racer instance to racer_list
    racer_list.append(racer)
    # update racer prompt for the user input later on
    if turtle_index != n_turtles - 1:
        racer_prompt += racer.name + ', '
    else:
        racer_prompt += racer.name

# prompt user to select who they think will win
user_bet = scr.textinput(title="BID ON WINNER", prompt=f"Who do you pick to win? ({racer_prompt})")
# if no bet (user cancels the prompt) exit the game
if user_bet is None:
    exit()

# ON YOUR MARKS, GET SET...
for racer in racer_list:
    # hide the drawing line
    racer.penup()
    # send the racer selected from the list to their respective starting positions
    racer.goto(racer.start_pos_x, racer.start_pos_y)

# initialise finished race variable
finished_race = False
# RACE GO!!!
while not finished_race:
    for competitor in racer_list:
        # move the turtle forward by a random position between 1 & 10
        competitor.forward(random.randint(0,10))
        random.shuffle(racer_list)
        # check to see if a turtle has reached the finished line
        if competitor.xcor() >= scr.window_width()/2 - 30:
            if user_bet != competitor.name:
                print(f"You lost. The winner was {competitor.name}")
            else:
                print(f"You won. The winner was {competitor.name}")
            finished_race = True

# close screen instance
scr.bye()

# keep screen alive
scr.exitonclick()