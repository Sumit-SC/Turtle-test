import streamlit as st
from turtle import Turtle, Screen
from scorebord import Scorebord
from cars import  Car_Manager
from player import Player
import time


st.title("Turtle Crossing Road game ")

def run_game():
    screen = Screen()
    screen.title("Turtle Crossing Game")
    screen.setup(600,600)
    screen.bgcolor("white")
    screen.tracer(0)


    player = Player((0,-280))
    car_manager = Car_Manager()
    scorebord = Scorebord()

    screen.listen()
    screen.onkey(player.go_up , "Up")



    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.cars()
        car_manager.move_cars()

        for car in car_manager.all_cars:
            if car.distance(player)<20:
                scorebord.game_over()
                game_is_on = False

    #     decting a successfully crossing
        if player.is_at_finish():
            player.go_to_start()
            car_manager.level_up()
            scorebord.increse_level()



if st.button("start Game"):
    run_game()

