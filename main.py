# import modules
from turtle import Turtle, Screen
import random
from list_of_turtles import turtles_list

racer_list = []


class Racer(Turtle):

    def __init__(self, name, col, start_pos_x, start_pos_y):
        Turtle.__init__(self)
        self.name = name
        self.col = col
        self.start_pos_x = start_pos_x
        self.start_pos_y = start_pos_y

    def __str__(self):
        return f"name: {self.name}, col: {self.col}, start_x: {self.start_pos_x}, start_y: {self.start_pos_y}"


# create screen object
scr = Screen()
# change screen size
scr.setup(width=500, height=400)

n_turtles = 6
count = 0
racer_prompt = ''

# select racers and ON YOUR MARKS!
while count < n_turtles:
    # randomly select racer from turtles list
    turtle_selected = random.choice(turtles_list)
    # remove randomly selected racer from turtles list for future iterations
    turtles_list.pop(turtles_list.index(turtle_selected))
    print(turtle_selected)

    # calculate starting pos
    x = -230
    y = -150+(350/n_turtles*count)

    racer = Racer(turtle_selected[0], turtle_selected[1], x, y)
    racer.shape("turtle")
    racer.color(racer.col)
    racer_list.append(racer)
    print(racer)
    if count != n_turtles - 1:
        racer_prompt += racer.name + ', '
    else:
        racer_prompt += racer.name
    count += 1


user_bet = scr.textinput(title="BID ON WINNER", prompt=f"Who do you pick to win? ({racer_prompt})")
if user_bet is None:
    exit()


for racer in racer_list:
    racer.penup()
    racer.goto(racer.start_pos_x, racer.start_pos_y)


finished_race = False
winner = ''
# RACE GO!!!
while not finished_race:
    for competitor in racer_list:
        competitor.forward(random.randint(0,5))
        random.shuffle(racer_list)
        if competitor.pos()[0] >= scr.window_width()/2 - 30:
            winner = competitor.name
            finished_race = True

scr.bye()
if user_bet != winner:
    print(f"You lost. The winner was {winner}")
else:
    print(f"You won. The winner was {winner}")


# keep screen alive
scr.exitonclick()