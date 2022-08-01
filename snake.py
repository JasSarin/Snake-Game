from turtle import Turtle
startingpos=[(0, 0), (-20, 0), (-40, 0)]
movedis = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in startingpos:
            self.addseg(position)

    def addseg(self, position):
        newseg = Turtle('square')
        newseg.color('white')
        newseg.penup()
        newseg.goto(position)
        self.segments.append(newseg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]

    def extend(self):
        self.addseg(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segnum - 1].xcor()
            newy = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newx, newy)
        self.head.forward(movedis)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


