import pygame
import sys

pygame.init()

#Score
score = 0
score2 = 0

#Colors
white = (255, 255, 255)
yellow = (255, 255, 0)

#Base
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football")
clock = pygame.time.Clock()

#Img
background = pygame.image.load("img/BackGround.jpg")
player_img = pygame.image.load("img/foot_player.png")
player2_img = pygame.image.load("img/foot_player2.png")
ball_img = pygame.image.load("img/ball.png")


#place
player_x = 30
player_y = 100
player_speed = 4.5

player2_x = 300
player2_y = 100
player2_speed = 4.5

ball_x = 200
ball_y = 100
ball_speed_x = 3
ball_speed_y = 3

goal_x = 0
goal_y = 220

goal2_x = 750
goal2_y = 220

#size
ball_img = pygame.transform.scale(ball_img, (70, 70))
player_img = pygame.transform.scale(player_img, (200, 200))
player2_img = pygame.transform.scale(player2_img, (200, 200))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
    #Draw
    screen.blit(background, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(player2_img, (player2_x, player2_y))
    screen.blit(ball_img, (ball_x, ball_y))


#Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player2_y -= player2_speed
    if keys[pygame.K_DOWN]:
        player2_y += player2_speed
    if keys[pygame.K_LEFT]:
        player2_x -= player2_speed
    if keys[pygame.K_RIGHT]:
        player2_x += player2_speed


    #Hit box
    ball_rect = pygame.Rect(ball_x, ball_y, 70, 70)
    player_rect = pygame.Rect(player_x, player_y, 100, 100)
    player2_rect = pygame.Rect(player2_x, player2_y, 100, 100)
    goal_rect = pygame.Rect(goal_x, goal_y, 50, 200)
    goal_rect2 = pygame.Rect(goal2_x, goal2_y, 50, 200)

    #Collision player 1
    if ball_rect.colliderect(player_rect):
        ball_speed_y = -ball_speed_y
        ball_speed_x = -ball_speed_x


    # Collision player 2
    if ball_rect.colliderect(player2_rect):
        ball_speed_y = -ball_speed_y
        ball_speed_x = -ball_speed_x

    # Goal 1
    if ball_rect.colliderect(goal_rect):
        score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = -3
        ball_speed_y = 3

    # Goal 2
    if ball_rect.colliderect(goal_rect2):
        score2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = 3
        ball_speed_y = 3

    #Text1
    font = pygame.font.Font(None, 36)
    text = font.render(f"Player Up/Down score: {score2}", True, yellow)

    #Text2
    font = pygame.font.Font(None, 36)
    text2 = font.render(f"Player w/s score: {score}", True, yellow)

    #Borders
    if player_y < 0: player_y = 0
    if player_y > 450: player_y = 450
    if player_x < 0: player_x = 0
    if player_x > 650: player_x = 650

    if player2_y < 0: player2_y = 0
    if player2_y > 450: player2_y = 450
    if player2_x < 0: player2_x = 0
    if player2_x > 650: player2_x = 650

    #Ball move
    ball_x += ball_speed_x
    ball_y += ball_speed_y


    #Bounce of up/down
    if ball_y <= 0 or ball_y >= 550:
        ball_speed_y =- ball_speed_y

    #Bounce of left/right
    if ball_x <= 0 or ball_x >= 750:
        ball_speed_x =- ball_speed_x

    pygame.draw.rect(screen, white, (goal_x, goal_y, 50, 200))
    pygame.draw.rect(screen, white, (goal2_x, goal2_y, 50, 200))


    #Draw texts
    screen.blit(text, (100, 25))
    screen.blit(text2, (500, 25))


    pygame.display.flip()
    clock.tick(120)

