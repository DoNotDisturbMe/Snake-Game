from turtle import Turtle

STARTIN_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
Distance_move = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for position in STARTIN_POSITIONS:
            self.add_segement(position)

    def add_segement(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segement(self.segments[-1].position())

    def move(self):
       for seg_num in range(len(self.segments) - 1, 0, -1):
           new_x = self.segments[seg_num - 1].xcor()
           new_y = self.segments[seg_num - 1].ycor()
           self.segments[seg_num].goto(new_x, new_y)
       self.segments[0].forward(Distance_move)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
