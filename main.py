import pygame

# Initialize pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((600, 600))

# Paddle positions
paddle_1X = 255
paddle_2Y = 250
paddle_3X = 255
paddle_4Y = 250

# Draw paddles
def draw_paddles():
    paddle_1 = pygame.Rect(paddle_1X, 20, 90, 15)
    paddle_2 = pygame.Rect(20, paddle_2Y, 15, 90)
    paddle_3 = pygame.Rect(paddle_3X, 560, 90, 15)
    paddle_4 = pygame.Rect(560, paddle_4Y, 15, 90)
    pygame.draw.rect(screen, (255, 0, 0), paddle_1)
    pygame.draw.rect(screen, (255, 0, 0), paddle_2)
    pygame.draw.rect(screen, (255, 0, 0), paddle_3)
    pygame.draw.rect(screen, (255, 0, 0), paddle_4)

# Game loop
running = True
while running:
    # Background Color
    screen.fill((0, 0, 0))
    draw_paddles()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            paddle_1X -= 5
        if event.key == pygame.K_d:
            paddle_1X += 5
        if event.key == pygame.K_ESCAPE:
            paddle_2Y -= 5
        if event.key == pygame.K_BACKQUOTE:
            paddle_2Y += 5
        if event.key == pygame.K_LEFT:
            paddle_3X -= 5
        if event.key == pygame.K_RIGHT:
            paddle_3X += 5
        if event.key == pygame.K_p:
            paddle_4Y -= 5
        if event.key == pygame.K_l:
            paddle_4Y += 5

    # update screen
    pygame.display.update()