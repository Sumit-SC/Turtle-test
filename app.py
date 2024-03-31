import streamlit as st
from scorebord import Scorebord
from cars import Car_Manager
from player import Player
import time

st.title("Turtle Crossing Road game ")

def run_game():
    canvas = st.canvas(width=600, height=600)
    canvas.background("white")

    player = Player((0, -280))
    car_manager = Car_Manager()
    scorebord = Scorebord()

    while True:
        time.sleep(0.1)
        canvas.clear()

        player.go_up_if_key_pressed()

        car_manager.cars()
        car_manager.move_cars()

        if player.is_at_finish():
            player.go_to_start()
            car_manager.level_up()
            scorebord.increase_level()

        player.draw(canvas)
        for car in car_manager.all_cars:
            car.draw(canvas)

        if car_manager.check_collision(player):
            scorebord.game_over()
            break

if st.button("Start Game"):
    run_game()
