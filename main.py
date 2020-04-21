import pygame

# Initialize pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((900, 600))

# Paddle positions
paddle_1X = 555
paddle_2Y = 250
paddle_3X = 555
paddle_4Y = 250

# Fonts
title_font = pygame.font.Font('freesansbold.ttf', 64)
button_font = pygame.font.Font('freesansbold.ttf', 14)

# Main menu
def intro():
    runnning = True
    while runnning:
        screen.fill((128, 128, 128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        title = title_font.render("Welcome to 4 Player Pong", True, (0, 0, 0))
        screen.blit(title, (40, 250))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button1_border = pygame.Rect(210, 385, 140, 90)
        pygame.draw.rect(screen, (0, 0, 255), button1_border)

        button2_border = pygame.Rect(535, 385, 140, 90)
        pygame.draw.rect(screen, (0, 0, 255), button2_border)


        if 335 > mouse[0] > 225 and 460 > mouse[1] > 400:
            button_1_light = pygame.Rect(225, 400, 110, 60)
            pygame.draw.rect(screen, (0, 255, 0), button_1_light)
            if click[0] == 1:
                main()
        else:
            button_1_normal = pygame.Rect(225, 400, 110, 60)
            pygame.draw.rect(screen, (0, 200, 0), button_1_normal)
        if 660 > mouse[0] > 550 and 460 > mouse[1] > 400:
            button_2_light = pygame.Rect(550, 400, 110, 60)
            pygame.draw.rect(screen, (255, 0, 0), button_2_light)
            if click[0] == 1:
                how_to_play_screen()
        else:
            button_2_normal = pygame.Rect(550, 400, 110, 60)
            pygame.draw.rect(screen, (200, 0, 0), button_2_normal)

        button1_text = button_font.render("Play", True, (0, 0, 0))
        screen.blit(button1_text, (((225+(110/2))-15), (400+(60/2))-5))
        button2_text = button_font.render("How to play", True, (0, 0, 0))
        screen.blit(button2_text, (((550+(110/2))-40), (400+(60/2))-5))

        pygame.display.update()


def draw_game_background():
    game_background = pygame.Rect(300, 0, 600, 600)
    pygame.draw.rect((screen), (0, 0, 0), game_background)

def draw_paddles():
    global paddle_1X, paddle_2Y, paddle_3X, paddle_4Y
    paddle_1 = pygame.Rect(paddle_1X, 20, 90, 15)
    paddle_2 = pygame.Rect(320, paddle_2Y, 15, 90)
    paddle_3 = pygame.Rect(paddle_3X, 560, 90, 15)
    paddle_4 = pygame.Rect(860, paddle_4Y, 15, 90)
    pygame.draw.rect(screen, (255, 0, 0), paddle_1)
    pygame.draw.rect(screen, (0, 255, 0), paddle_2)
    pygame.draw.rect(screen, (0, 0, 255), paddle_3)
    pygame.draw.rect(screen, (255, 255, 0), paddle_4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                paddle_1X -= 20
            if event.key == pygame.K_d:
                paddle_1X += 20
            if event.key == pygame.K_ESCAPE:
                paddle_2Y -= 20
            if event.key == pygame.K_BACKQUOTE:
                paddle_2Y += 20
            if event.key == pygame.K_LEFT:
                paddle_3X -= 20
            if event.key == pygame.K_RIGHT:
                paddle_3X += 20
            if event.key == pygame.K_o:
                paddle_4Y -= 20
            if event.key == pygame.K_l:
                paddle_4Y += 20
            if event.key == pygame.K_b:
                intro()

        if paddle_1X + 90 > 900:
            paddle_1X = 810
        if paddle_1X < 300:
            paddle_1X = 300
        if paddle_2Y + 90 > 600:
            paddle_2Y = 510
        if paddle_2Y < 0:
            paddle_2Y = 0
        if paddle_3X + 90 > 900:
            paddle_3X = 810
        if paddle_3X < 300:
            paddle_3X = 300
        if paddle_4Y + 90 > 600:
            paddle_4Y = 510
        if paddle_4Y < 0:
            paddle_4Y = 0

def text(font_size, x, y, text, color):
    text_font = pygame.font.Font('freesansbold.ttf', font_size)
    text = text_font.render(text, True, color)
    screen.blit(text, (x, y))

def how_to_play_screen():
    running = True
    while running:
        screen.fill((128,128,128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        text(32, 50, 80, "Objective:", (255,255,255))
        text(16, 50, 120, "This game is like normal pong,", (255,255,255))
        text(16, 50, 140, "except that there are four players.", (255, 255, 255))
        text(16, 50, 160, "Each player starts out with 10 points.", (255, 255, 255))
        text(16, 50, 180, "If the ball goes out, the player's who's", (255, 255, 255))
        text(16, 50, 200, "side it went out on loses a point", (255, 255, 255))
        text(16, 50, 220, "Then the round ends and the ball will ", (255, 255, 255))
        text(16, 50, 240, "reapper on the center of the screen.", (255, 255, 255))
        text(16, 50, 260, "At the end of 10 rounds whoever as the most points wins", (255, 255, 255))
        

        pygame.display.update()

# def scoring():
    # paddle_1_score = 10
    # paddle_1_score = 10
    # paddle_1_score = 10
    # paddle_1_score = 10

ball_x = 600
ball_y = 500
ball_dx = 10
ball_dy = 10




# Game loop
def main():
    paddle_1_score = 10
    paddle_2_score = 10
    paddle_3_score = 10
    paddle_4_score = 10
    global ball_dx, ball_dy, paddle_1X, ball_x, ball_y
    running = True
    while running:
        # Background Color
        screen.fill((128, 128, 128))
        draw_game_background()
        draw_paddles()

        pygame.draw.rect(screen, (255, 0, 0), (50, 400, 90, 15))
        pygame.draw.rect(screen, (0, 255, 0), (50, 450, 90, 15))
        pygame.draw.rect(screen, (0, 0, 255), (50, 500, 90, 15))
        pygame.draw.rect(screen, (255, 255, 0), (50, 550, 90, 15))

        pygame.draw.circle(screen, (255, 255, 255), [ball_x, ball_y], 10)
        ball_x = ball_x + ball_dx
        ball_y = ball_y - ball_dy

        if paddle_1X < ball_x < paddle_1X + 100 and ball_y == 30:
            ball_y = ball_y + 20
            ball_dy *= -1

        if paddle_2Y < ball_y < paddle_2Y + 100 and ball_x == 330:
            ball_x = ball_x + 20
            ball_dx *= -1

        if paddle_3X < ball_x < paddle_3X + 100 and ball_y == 560:
            ball_y = ball_y - 20
            ball_dy *= -1

        if paddle_4Y < ball_y < paddle_4Y + 100 and ball_x == 860:
            ball_x = ball_x - 20
            ball_dx *= -1

        if ball_x > 900:
            ball_x = 600
            ball_y = 300
            paddle_4_score -= 1
            print(paddle_4_score)
        if ball_x < 300:
            ball_x = 600
            ball_y = 300
            paddle_2_score -= 1
            print(paddle_2_score)
        if ball_y < 0:
            ball_x = 600
            ball_y = 300
            paddle_1_score -= 1
            print(paddle_1_score)
        if ball_y > 600:
            ball_x = 600
            ball_y = 300
            paddle_3_score -= 1
            print(paddle_3_score)







        # Back button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 205 > mouse[0] > 90 and 110 > mouse[1] > 50:
            back_button_light = pygame.Rect(95, 50, 110, 60)
            pygame.draw.rect(screen, (0, 0, 255), back_button_light)
            if click[0] == 1:
                ball_x = 600
                ball_y = 500
                intro()
        else:
            back_button_normal = pygame.Rect(95, 50, 110, 60)
            pygame.draw.rect(screen, (0, 0, 200), back_button_normal)

        back_button_font = pygame.font.Font('freesansbold.ttf', 20)
        back_button_text = back_button_font.render("Back", True, (0, 0, 0))
        screen.blit(back_button_text, (123, 73))

        # update screen
        pygame.display.update()

intro()




