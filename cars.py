from turtle import Turtle
import random


colors = ["red","green","orange","blue","yellow","black","skyblue"]
starting_poisition = 5
speed = 2

class Car_Manager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = starting_poisition


    def cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 :
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1 ,  stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-240,260)
            new_car.goto(360, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += speed