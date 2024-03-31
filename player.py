from turtle import Turtle

starting_position = (0,-280)
finish_line = 280
class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.shapesize(1)
        self.penup()
        self.go_to_start()

    def go_up(self):
        new_y = self.ycor() + 10
        self.sety(new_y)


    def go_to_start(self):
        self.goto(starting_position)

    def is_at_finish(self):
        if self.ycor() > finish_line:
            return True
        else :
            return False

