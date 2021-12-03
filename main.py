from turtle import Turtle, Screen,time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Nokia 1100")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



#screen.update()
game_is_on=True
while game_is_on:
  screen.update() # update the screen with 0.1 sec delay
  time.sleep(0.1)

  snake.move()


  # collison of snake and food detection
  if snake.head.distance(food)<15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
    


  # detect collison with wall
  if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()>-280:
    game_is_on=False
    scoreboard.game_over()


  # detect collison with tail(if head collide with any part of segment)



  for segment in snake.segments[1:]: # by slicing  we can avoid the first case of head hitting head
    if snake.head.distance(segment)<10:
      game_is_on=False
      scoreboard.game_over()

    


    


screen.exitonclick()  