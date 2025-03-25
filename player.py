import turtle

turtle.colormode(255)

# Constants
WIN_Y_POSITION = 200
PLAYER_START_POSITION = (0, -230)
PLAYER_MOVE_DISTANCE = 20


class Player(turtle.Turtle):
    """Represents the player character, which moves up and down to avoid cars and reach the goal."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.setheading(90)
        self.goto(PLAYER_START_POSITION)

    def move_up(self):
        """Moves the player upwards."""
        self.setheading(90)
        self.forward(PLAYER_MOVE_DISTANCE)

    def move_down(self):
        """Moves the player downwards."""
        self.setheading(270)
        self.forward(PLAYER_MOVE_DISTANCE)

    def win_condition(self):
        """Checks if the player has reached the winning position."""
        return self.ycor() > WIN_Y_POSITION