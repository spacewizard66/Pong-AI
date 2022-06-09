# Fun AI version of playable Pong game
from inspect import BoundArguments
import pygame, sys, random



# General Setup
pygame.init()
clock = pygame.time.Clock()
FPS = 1200.0

# Setting up the Main Window
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong AI')

# Game Rectangles
ball = pygame.Rect(screen_width/2-10, screen_height/2-10, 20, 20)
player = pygame.Rect(screen_width-20, screen_height/2-50, 10, 100)
opponent = pygame.Rect(10, screen_height/2-50, 10, 100)
divider_rect = pygame.Rect(screen_width/2-5, 0, 10, screen_height)
count_rect = pygame.Rect(screen_width/2-75, 20, 150, 100)

# Colors
ball_color = (0, 0, 0)
background = (70,160,126)
light_grey = (200,200,200)
pink = (255,192,203)
red = (255,0,0)
black = (0,0,0)

# Animations
ball_speed_x = 1 * random.choice((1, -1))
ball_speed_y = 1 * random.choice((1, -1))
player_speed = 2
opponent_speed = 2

count_value = 0

font_size = 90
font = pygame.font.Font(None, font_size)



def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    #player.y += player_speed
    # Player Borders
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    # AI logic
    if player.top < ball.y+5:
        player.top += player_speed
    if player.bottom > ball.y+5:
        player.bottom -= player_speed

def opponent_ai():
    # Opponent screen borders
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    # AI logic follows ball
    if opponent.top < ball.y+5:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y+5:
        opponent.bottom -= opponent_speed

def ball_restart():
    """Ball restarts at beginning position if missed"""
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def bounce_count():
    """Counts every ball bounce and displays the result"""
    global count_value
    # Logic to count bounces when ball collides
    if ball.colliderect(opponent) or ball.colliderect(player):
        count_value += 1
    else:
        pass
    count = font.render(str(count_value), True, red)
    return count



############################ Loop runs the game ################################
while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if count_value == 10000:
        font_size = 65
        font = pygame.font.Font(None, font_size)

    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(background)
    pygame.draw.rect(screen, light_grey, divider_rect)
    pygame.draw.rect(screen, black, count_rect)    
    pygame.draw.rect(screen, black, player)
    pygame.draw.rect(screen, black, opponent)
    pygame.draw.ellipse(screen, red, ball)
    screen.blit(bounce_count(), (430, 45))

    # Updating the Window
    pygame.display.flip()
    clock.tick(FPS)
