import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 1000
HEIGHT = 600
SPEED = 10
BLOCK_SIZE = 20

# Set up some colors
BLACK = (0, 0, 0)
GREEN = (57, 255, 20)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the snake and the food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
direction = 'RIGHT'

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Move the snake
    head = snake[0]
    if direction == 'UP':
        new_head = (head[0], (head[1] - BLOCK_SIZE) % HEIGHT)
    elif direction == 'DOWN':
        new_head = (head[0], (head[1] + BLOCK_SIZE) % HEIGHT)
    elif direction == 'LEFT':
        new_head = ((head[0] - BLOCK_SIZE) % WIDTH, head[1])
    elif direction == 'RIGHT':
        new_head = ((head[0] + BLOCK_SIZE) % WIDTH, head[1])

    snake.insert(0, new_head)

    # Check if the snake has eaten the food
    if snake[0] == food:
        food = (random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE))
        SPEED += 1
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the speed
    pygame.time.delay(1000 // SPEED)
