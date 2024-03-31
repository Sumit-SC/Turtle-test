from turtle import Turtle

font = ("Courier", 15 ,"normal")

class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_scoreborde()

    def update_scoreborde(self):
        self.clear()
        self.write(f"Lavel : {self.level}", align="left", font=font)


    def increse_level(self):
        self.level +=1
        self.update_scoreborde()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.. ", align= "center", font = font)
