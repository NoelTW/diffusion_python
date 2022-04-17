import turtle


class HelloWold:

    def are_you_ready(self):
        """
        A method to say hello to who want to learn python
        """
        your_ans = input('are you ready? ')
        if 'ye' in your_ans.lower():
            self.hello_world()
        else:
            print('ok, anytime when you are ready')

    @staticmethod
    def hello_world():
        win = turtle.Screen()
        win.title("Hello World")
        win.bgcolor("black")
        turtle_instance = turtle.Turtle()
        turtle_instance.color("white")
        turtle_instance.pensize(4)
        turtle_instance.speed(20)

        # Print the letter H
        turtle_instance.penup()
        turtle_instance.goto(-320, 0)
        turtle_instance.pendown()
        turtle_instance.left(90)
        turtle_instance.forward(70)
        turtle_instance.penup()
        turtle_instance.goto(-320, 35)
        turtle_instance.down()
        turtle_instance.right(90)
        turtle_instance.forward(50)
        turtle_instance.penup()
        turtle_instance.goto(-270, 70)
        turtle_instance.pendown()
        turtle_instance.right(90)
        turtle_instance.forward(70)

        # printing letter E
        turtle_instance.penup()
        turtle_instance.goto(-260, 0)
        turtle_instance.pendown()
        turtle_instance.right(180)
        turtle_instance.forward(70)
        turtle_instance.right(90)
        turtle_instance.forward(35)
        turtle_instance.penup()
        turtle_instance.goto(-260, 35)
        turtle_instance.pendown()
        turtle_instance.forward(35)
        turtle_instance.penup()
        turtle_instance.goto(-260, 0)
        turtle_instance.pendown()
        turtle_instance.forward(35)

        # printing letter L
        turtle_instance.penup()
        turtle_instance.goto(-210, 70)
        turtle_instance.pendown()
        turtle_instance.right(90)
        turtle_instance.forward(70)
        turtle_instance.left(90)
        turtle_instance.forward(35)

        # printing letter L
        turtle_instance.penup()
        turtle_instance.goto(-165, 70)
        turtle_instance.pendown()
        turtle_instance.right(90)
        turtle_instance.forward(70)
        turtle_instance.left(90)
        turtle_instance.forward(35)

        # printing letter O
        turtle_instance.penup()
        turtle_instance.goto(-90, 70)
        turtle_instance.pendown()

        for i in range(25):
            turtle_instance.right(15)
            turtle_instance.forward(10)

        # printing  letter w
        turtle_instance.penup()
        turtle_instance.goto(-10, 70)
        turtle_instance.pendown()
        turtle_instance.right(55)
        turtle_instance.forward(70)
        turtle_instance.left(150)
        turtle_instance.forward(70)
        turtle_instance.right(155)
        turtle_instance.forward(70)
        turtle_instance.left(150)
        turtle_instance.forward(70)

        # printing letter O
        turtle_instance.penup()
        turtle_instance.goto(70, 55)
        turtle_instance.pendown()

        for i in range(25):
            turtle_instance.right(15)
            turtle_instance.forward(10)

        # printing letter R
        turtle_instance.penup()
        turtle_instance.goto(160, 70)
        turtle_instance.pendown()
        turtle_instance.right(150)
        turtle_instance.forward(70)
        turtle_instance.goto(160, 70)
        turtle_instance.right(200)
        for i in range(20):
            turtle_instance.right(15)
            turtle_instance.forward(6)
        turtle_instance.left(180)
        turtle_instance.forward(60)

        # printing letter L
        turtle_instance.penup()
        turtle_instance.goto(220, 70)
        turtle_instance.pendown()
        turtle_instance.right(40)
        turtle_instance.forward(70)
        turtle_instance.left(90)
        turtle_instance.forward(35)

        # printing letter L
        turtle_instance.penup()
        turtle_instance.goto(290, 70)
        turtle_instance.pendown()
        turtle_instance.right(90)
        turtle_instance.forward(70)
        turtle_instance.penup()
        turtle_instance.goto(270, 70)
        turtle_instance.pendown()
        turtle_instance.left(120)
        for i in range(15):
            turtle_instance.right(15)
            turtle_instance.forward(10)
        turtle.done()


if __name__ == '__main__':
    HelloWold().are_you_ready()