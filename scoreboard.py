from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.highscore}', align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.updatescoreboard()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write('Game Over', align='center', font=('Arial', 24, 'normal'))

    def increasescore(self):
        self.score += 1
        self.clear()
        self.updatescoreboard()
