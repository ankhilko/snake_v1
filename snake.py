from turtle import Turtle
from gameconst import SEGMENT_SIZE, UP, DOWN, LEFT, RIGHT, SNAKE_SIZE


class Snake:
    def __init__(self):
        self.snake_start_size = SNAKE_SIZE
        self.snake_segments = []
        self.starting_positions = self.set_starting_positions()
        self.start = 0
        self.make_new_snake()
        self.head = self.snake_segments[0]
        pass

    def set_starting_positions(self):
        positions = []
        start = 0
        for i in range(self.snake_start_size):
            positions.append((start, 0))
            start -= SEGMENT_SIZE
        return positions

    def make_new_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)
        pass

    def add_segment(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)  # setup()
        self.snake_segments.append(new_snake_part)
        pass

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
        pass

    def move(self):
        for seg_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_number - 1].xcor()
            new_y = self.snake_segments[seg_number - 1].ycor()
            self.snake_segments[seg_number].goto(new_x, new_y)
        self.snake_segments[0].forward(SEGMENT_SIZE)
        pass

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        pass

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        pass

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        pass

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        pass

    def update_snake(self):
        for segment in self.snake_segments:
            segment.hideturtle()
        self.snake_segments.clear()
        self.make_new_snake()
        self.head = self.snake_segments[0]
        pass
