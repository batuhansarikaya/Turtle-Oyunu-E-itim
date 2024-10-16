import turtle
import random

# Ekranı ayarla
screen = turtle.Screen()
screen.bgcolor("Green")
screen.title("Catch The Turtle")

# Puan göstergesi
score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.color("dark blue")
FONT = ('Arial', 30, 'normal')
score = 0

def setup_score_turtle():
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

# Otomatik hareket eden turtle
def make_turtle():
    t = turtle.Turtle()
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("yellow")
    return t


def move_turtle(t):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    screen.ontimer(lambda: move_turtle(t), 400)


def increase_score(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)


turtle_instance = make_turtle()
setup_score_turtle()


turtle_instance.onclick(increase_score)


move_turtle(turtle_instance)


turtle.mainloop()
