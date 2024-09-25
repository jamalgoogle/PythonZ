
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
paddle_width, paddle_height = 15, 90
paddle_speed = 5

# Ball settings
ball_size = 15
ball_speed_x, ball_speed_y = 5, 5

# Create paddles and ball
player = pygame.Rect(50, height//2 - paddle_height//2, paddle_width, paddle_height)
opponent = pygame.Rect(width - 50 - paddle_width, height//2 - paddle_height//2, paddle_width, paddle_height)
ball = pygame.Rect(width//2 - ball_size//2, height//2 - ball_size//2, ball_size, ball_size)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= paddle_speed
    if keys[pygame.K_DOWN] and player.bottom < height:
        player.y += paddle_speed

    # Move the opponent's paddle (simple AI)
    if opponent.centery < ball.centery and opponent.bottom < height:
        opponent.y += paddle_speed
    elif opponent.centery > ball.centery and opponent.top > 0:
        opponent.y -= paddle_speed

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= width:
        ball.center = (width//2, height//2)
        ball_speed_x *= -1

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the center line
    pygame.draw.aaline(screen, WHITE, (width//2, 0), (width//2, height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
