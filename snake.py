from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        body = Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.segments.append(body)

    def extend_body(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)

        self.segments[0].forward(MOVE_DISTANCE)

    def turn_upward(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def turn_downward(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def turn_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def turn_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
