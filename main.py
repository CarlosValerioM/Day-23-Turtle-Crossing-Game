#!/usr/bin/env python3
"""
turtle_game.py - A simple game using the Turtle module.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/23
License: MIT
Dependencies: None (built-in functions only)

Description:
This script implements a basic game where a player avoids moving cars.
It includes:
1. A game window with a black background.
2. A player-controlled character that moves up and down.
3. Multiple cars that move horizontally across the screen.
4. Collision detection between the player and cars.
5. A win condition when the player reaches the top of the screen.

Controls:
- Player:
    - Move Up: "Up" arrow key
    - Move Down: "Down" arrow key

Usage:
Run the script:
    python turtle_game.py

Example Gameplay:
- The player starts at the bottom of the screen.
- Cars appear and move from one side of the screen to the other.
- The player must navigate through the cars without getting hit.
- Reaching the top of the screen results in a win.
"""

from turtle import Screen
from player import Player
from car import Car

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = "black"
CAR_COUNT = 10
UP_KEY = "Up"
DOWN_KEY = "Down"


def main():
    """Initializes the game, sets up the screen, creates the player and cars, and starts the game loop."""
    screen = Screen()
    screen.bgcolor(BACKGROUND_COLOR)  # Set background color
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)  # Set window size
    screen.listen()  # Enable key event detection

    # Create player
    player = Player()

    # Create cars
    cars = []
    for _ in range(CAR_COUNT):
        new_car = Car()
        new_car.set_position()
        cars.append(new_car)

    # Assign key controls for the player
    screen.onkey(player.move_up, UP_KEY)
    screen.onkey(player.move_down, DOWN_KEY)

    # Start game loop
    game_active = True
    while game_active:
        for car in cars:
            car.move()

            # Check for collision with the player
            if car.collision(player):
                game_active = False
                break

            car.end_of_screen()

        # Check if the player reaches the goal
        if player.win_condition():
            game_active = False

    screen.exitonclick()


if __name__ == '__main__':
    main()