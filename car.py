import random
import turtle

##Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
START_X_LEFT = -380
START_X_RIGHT = 380
START_Y_RANGE = (-150, 150)
MOVE_SPEED_RANGE = (10, 50)
COLLISION_DISTANCE = 20

class Car(turtle.Turtle):
    """Represents a moving car in the game that can collide with the player."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed("fastest")
        self.movement = random.randint(*MOVE_SPEED_RANGE)
        self.xstart = 0
        self.ystart = 0
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)

    def set_position(self):
        """Sets a random starting position and direction for the car."""
        heading = random.choice([0, 180])
        self.setheading(heading)
        x = START_X_LEFT if heading == 0 else START_X_RIGHT
        y = random.randint(*START_Y_RANGE)
        self.goto(x, y)
        self.xstart = x
        self.ystart = y

    def move(self):
        """Moves the car forward."""
        self.forward(self.movement)

    def end_of_screen(self):
        """Resets the car to the starting position if it moves off-screen."""
        if self.xstart == START_X_LEFT and self.xcor() > SCREEN_WIDTH // 2 - 10:
            self.goto(self.xstart, self.ystart)
        elif self.xstart == START_X_RIGHT and self.xcor() < -SCREEN_WIDTH // 2 + 10:
            self.goto(self.xstart, self.ystart)

    def collision(self, player):
        """Checks if the car collides with the player."""
        return self.distance(player) < COLLISION_DISTANCE