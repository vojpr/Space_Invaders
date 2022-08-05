from turtle import Turtle, Screen

# Set up screen
screen = Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.listen()
screen.tracer(0)

# Draw border
border_pen = Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.pensize(3)
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
for each in range(4):
    border_pen.forward(600)
    border_pen.left(90)

# Create scoreboard
score = 0
score_pen = Turtle()
score_pen.hideturtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
score_pen.write(f"Score: {score}", False, align="left", font=("Courier", 24, "normal"))

# Create message at the end of the game
end_pen = Turtle()
end_pen.hideturtle()
end_pen.penup()
end_pen.speed(0)
end_pen.color("white")
end_pen.setposition(0, 0)

# Create player
player = Turtle()
player.color("blue")
screen.register_shape("images/player.gif")
player.shape("images/player.gif")
player.penup()
player.speed(0)
player.setposition(x=0, y=-250)
player.setheading(90)

# Create player moves
PLAYER_SPEED = 7

def move_left():
    if player.xcor() > -285:
        player.setx(player.xcor() - PLAYER_SPEED)

screen.onkeypress(move_left, "Left")

def move_right():
    if player.xcor() < 285:
        player.setx(player.xcor() + PLAYER_SPEED)

screen.onkeypress(move_right, "Right")

# Create player bullet
bullet = Turtle()
bullet.shapesize(0.5, 0.5)
bullet.penup()
bullet.speed(0)
bullet.color("yellow")
bullet.shape("triangle")
bullet.setheading(90)
bullet.hideturtle()

# Bullet movement
BULLET_SPEED = 6
bullet_moving = False

def shoot():
    global bullet_moving
    if not bullet_moving:
        bullet_moving = True
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

screen.onkeypress(shoot, "space")

# Create enemies
enemies = []

ENEMY_HORIZONTAL_SPEED = 0.2
ENEMY_VERTICAL_SPEED = 40
NUMBER_OF_ENEMIES = 30

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

screen.register_shape("images/invader.gif")

for each in range(NUMBER_OF_ENEMIES):
    enemy = Turtle()
    enemy.color("red")
    enemy.shape("images/invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_number = 0
        enemy_start_y -= 50

    enemies.append(enemy)


# Check if bullet hit the enemy function
def is_collision(a):
    if a.distance(enemy) < 15:
        return True
    else:
        return False

GAME_RUNNING = True

while GAME_RUNNING:
    screen.update()
    # Moving the enemies
    # Move horizontally
    for enemy in enemies:
        enemy.setx(enemy.xcor() + ENEMY_HORIZONTAL_SPEED)
        if enemy.xcor() < -280 or enemy.xcor() > 280:
            ENEMY_HORIZONTAL_SPEED *= -1
            # Move vertically
            for each in enemies:
                each.sety(each.ycor() - ENEMY_VERTICAL_SPEED)
        # Check if bullet hit the enemy
        if is_collision(bullet):
            # Reset the bullet
            bullet_moving = False
            bullet.hideturtle()
            bullet.setposition(0, -500)
            # Hide hit enemy
            enemy.setposition(0, 1000)
            # Update score
            score_pen.clear()
            score += 1
            score_pen.write(f"Score: {score}", False, align="left", font=("Courier", 24, "normal"))
        # Check if enemies won
        if enemy.ycor() <= -255:
            end_pen.write("GAME OVER", False, align="center", font=("Courier", 34, "normal"))
            GAME_RUNNING = False
    # Moving the bullet
    if bullet_moving:
        bullet.sety(bullet.ycor() + BULLET_SPEED)
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_moving = False
    # Winning the game
    if score == NUMBER_OF_ENEMIES:
        end_pen.write("YOU WIN!", False, align="center", font=("Courier", 34, "normal"))
        GAME_RUNNING = False

screen.exitonclick()
