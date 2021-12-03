from turtle import Turtle
import random

class Food(Turtle):  # inheriting Turtle class in Food class

  def __init__(self):
    super().__init__() # super().__init__() calls the init of Turtle class and inherits all the properties
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_len=0.5,stretch_wid=0.5)
    self.color("red")
    self.speed("fastest")
    self.refresh()

  def refresh(self):
    random_x=random.randint(-280,280)
    random_y=random.randint(-280,280)
    self.goto(random_x,random_y)


    

   