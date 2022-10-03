from random import randint
from turtle import Turtle
from gameconst import SCREEN_WIDTH, SCREEN_HEIGHT, SEGMENT_SIZE

food_plate_x = int((SCREEN_WIDTH / 2) - SEGMENT_SIZE)
food_plate_y = int((SCREEN_HEIGHT / 2) - SEGMENT_SIZE)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x_rand = randint(-food_plate_x, food_plate_x)
        y_rand = randint(-food_plate_y, food_plate_y)
        self.goto(x_rand, y_rand)
        pass

    def refresh(self):
        x_rand = randint(-food_plate_x, food_plate_x)
        y_rand = randint(-food_plate_y, food_plate_y)
        self.goto(x_rand, y_rand)
        pass
   
   pass
