######################
#
#   Import Libraries
#
######################
import pgzrun
from random import randint
from math import sqrt


######################
#
#   Intitalize Actors and Variables
#
######################
pineapple = Actor("pineapple")
apple = Actor("apple")
user_score = 0
message = ""
game_over = False

######################
#
#   Main Drawing Function
#
######################
def draw():
    screen.clear()

    if game_over:
        #Show Game Over Screen
        screen.draw.text("Game Over!", center=(400,300), fontsize=80, color='red')
        screen.draw.text(f"Final Score: {user_score}", center=(400, 370), fontsize=50,color='white')
        screen.draw.text("Click anywhere to play again", center =(400, 440), fontsize=40, color='yellow')
    else:
        #Show game state
        pineapple.draw()
        apple.draw()
        screen.draw.text(f"Score: {user_score}", topleft = (10,10), fontsize = 40, color = 'white')
        screen.draw.text(message, midtop = (400,10), fontsize = 40, color = 'yellow')

######################
#
#   Game Functions
#
######################
#Helper function to measure distance between fruits
def distance(a1, a2):
    return sqrt((a1.x - a2.x) ** 2 + (a1.y - a2.y) ** 2)

#Randomly place pineapple without overlapping the apple    
def place_pineapple():
    while True:
        pineapple.x = randint(10, 800)
        pineapple.y = randint(10, 600)
        if distance(pineapple, apple) > 100:
            break

#Randomly place apple without overlapping pineapple
def place_apple():
    while True:
        apple.x = randint(10, 800)
        apple.y = randint(10, 600)
        if distance(apple, pineapple) > 100:
          break

#Move both fruits if the game is not over
def move_fruits():
    if not game_over:
        place_pineapple()
        place_apple()

#Check if the game should end
def check_game_over():
    global game_over
    if user_score < 0:
        game_over = True
    elif user_score > 10:
        game_over = True

#Reset game to inital state
def restart_game():
    global user_score, message, game_over
    user_score = 0
    message = ""
    game_over = False
    place_pineapple()
    place_apple()

#Handle mouse clicks
def on_mouse_down(pos):
    global user_score, message

    if game_over:
        restart_game()
        return
    
    if pineapple.collidepoint(pos):
        user_score += 1
        message = "Good Shot, Pineapple Murderer!"

    elif apple.collidepoint(pos):
        user_score -=1
        message = "That Poor Apple!"

    else:
        message = "You Missed!"

    check_game_over()

#Initial Fruit Placement        
place_pineapple()
place_apple()

#Move fruits every 0.8 seconds
clock.schedule_interval(move_fruits, 0.8)

#Start the game
pgzrun.go()
