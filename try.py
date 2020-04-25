import pygame
import random
import operator

# Initialize pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((900, 600))

# Load crown

crown = pygame.image.load('crown.png')

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

        if paddle_1X + 90 > 835:
            paddle_1X = 745
        if paddle_1X < 365:
            paddle_1X = 365
        if paddle_2Y + 90 > 535:
            paddle_2Y = 445
        if paddle_2Y < 65:
            paddle_2Y = 65
        if paddle_3X + 90 > 835:
            paddle_3X = 745
        if paddle_3X < 365:
            paddle_3X = 365
        if paddle_4Y + 90 > 535:
            paddle_4Y = 445
        if paddle_4Y < 65:
            paddle_4Y = 65

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
        text(16, 50, 260, "At the end of 10 rounds whoever has", (255, 255, 255))
        text(16, 50, 280, "the most points wins. The game can also", (255, 255, 255))
        text(16, 50, 300, "when the time limit is reached,", (255, 255, 255))
        text(16, 50, 320, "so don't be shocked if the game ends", (255, 255, 255))
        text(16, 50, 340, "in the middle of the round. It is also", (255, 255, 255))
        text(16, 50, 360, "important to know that the physics", (255, 255, 255))
        text(16, 50, 380, "of this game is really wacky to make", (255, 255, 255))
        text(16, 50, 400, "the game more fun.", (255, 255, 255))
        text(32, 450, 80, "Controls:", (255,255,255))
        text(16, 550, 140, "Left - a  Right - d",(255,255,255))
        text(16, 550, 190, "Up - esc  Down - `", (255, 255, 255))
        text(16, 550, 240, "Left - left arrow  Right - right arrow", (255, 255, 255))
        text(16, 550, 290, "Up - o  Down - l", (255, 255, 255))



        pygame.draw.rect(screen, (255, 0, 0), (450, 140, 90, 15))
        pygame.draw.rect(screen, (0, 255, 0), (450, 190, 90, 15))
        pygame.draw.rect(screen, (0, 0, 255), (450, 240, 90, 15))
        pygame.draw.rect(screen, (255, 255, 0), (450, 290, 90, 15))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 840 > mouse[0] > 780 and 590 > mouse[1] > 530:
            button_2_light = pygame.Rect(780, 530, 110, 60)
            pygame.draw.rect(screen, (255, 0, 0), button_2_light)
            if click[0] == 1:
                intro()
        else:
            button_2_normal = pygame.Rect(780, 530, 110, 60)
            pygame.draw.rect(screen, (200, 0, 0), button_2_normal)

        text(14, 815, 555, "Back", (0, 0, 0))

        pygame.display.update()

# def scoring():
    # paddle_1_score = 10
    # paddle_1_score = 10
    # paddle_1_score = 10
    # paddle_1_score = 10

ball_x = 600
ball_y = 150
ball_dx = 10
ball_dy = 10


def end_screen(red_score, blue_score, green_score, yellow_score):
    running = True
    while running:
        screen.fill((128, 128, 128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        text(50, 300, 50, "Rankings:", (255, 255, 0))
        text(32, 320, 150, "1.", (0,0,0))
        text(32, 320, 250, "2.", (0, 0, 0))
        text(32, 320, 350, "3.", (0, 0, 0))
        text(32, 320, 450, "4.", (0, 0, 0))

        ranking(red_score, green_score, blue_score, yellow_score)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 840 > mouse[0] > 780 and 590 > mouse[1] > 530:
            button_2_light = pygame.Rect(780, 530, 110, 60)
            pygame.draw.rect(screen, (255, 0, 0), button_2_light)
            if click[0] == 1:
                intro()
        else:
            button_2_normal = pygame.Rect(780, 530, 110, 60)
            pygame.draw.rect(screen, (200, 0, 0), button_2_normal)

        text(14, 815, 555, "Back", (0, 0, 0))

        screen.blit(crown, (395, 120))

        pygame.display.update()

def ranking(red_score, blue_score, green_score, yellow_score):
    scores = {
        "red": red_score,
        "blue": blue_score,
        "green": green_score,
        "yellow": yellow_score
    }

    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
    # print(sorted_scores)
    def Convert(tup, di):
        for a, b in tup:
            di.setdefault(a, []).append(b)
        # print(di)
        def getList(dict):
            return dict.keys()

        keys = getList(di)
        k = list(keys)
        # print(keys)

        # print(k[0])
        draw_rankings(k[3], k[2], k[1], k[0])
        return di


    dictionary = {}
    Convert(sorted_scores, dictionary)

def draw_rankings(first, second, third, fourth):

    if first == "red":
        first_color = (255, 0, 0)
    if first == "green":
        first_color = (0, 255, 0)
    if first == "blue":
        first_color = (0, 0, 255)
    if first == "yellow":
        first_color = (255, 255, 0)
    if second == "red":
        second_color = (255, 0, 0)
    if second == "green":
        second_color = (0, 255, 0)
    if second == "blue":
        second_color = (0, 0, 255)
    if second == "yellow":
        second_color = (255, 255, 0)
    if third == "red":
        third_color = (255, 0, 0)
    if third == "green":
        third_color = (0, 255, 0)
    if third == "blue":
        third_color = (0, 0, 255)
    if third == "yellow":
        third_color = (255, 255, 0)
    if fourth == "red":
        fourth_color = (255, 0, 0)
    if fourth == "green":
        fourth_color = (0, 255, 0)
    if fourth == "blue":
        fourth_color = (0, 0, 255)
    if fourth == "yellow":
        fourth_color = (255, 255, 0)

    pygame.draw.rect(screen, first_color, (360, 160, 90, 15))
    pygame.draw.rect(screen, second_color, (360, 260, 90, 15))
    pygame.draw.rect(screen, third_color, (360, 360, 90, 15))
    pygame.draw.rect(screen, fourth_color, (360, 460, 90, 15))


# Game loop
def main():
    timer = 0
    timer += 1
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
        ball_x = round(ball_x + ball_dx)
        ball_y = round(ball_y - ball_dy)


        if ball_dx > 0 and ball_dy > 0:
            if paddle_1X < ball_x < paddle_1X + 50 and ball_y == 30:
                ball_y += 20
                ball_x -= 20
                ball_dx *= -1
                ball_dy *= -1
            elif paddle_1X + 50 <= ball_x <= paddle_1X + 100 and ball_y == 30:
                ball_y += 20
                ball_x += 20
                ball_dx *= 1
                ball_dy *= -1
            if paddle_4Y < ball_y < paddle_4Y + 50 and ball_x == 860:
                ball_x -= 20
                ball_dx *= -1
                ball_dy *= 1
            elif paddle_4Y + 50 < ball_y < paddle_4Y + 100 and ball_x == 860:
                ball_x -= 20
                ball_y += 20
                ball_dx *= -1
                ball_dy *= -1

        elif ball_dx > 0 and ball_dy < 0:
            if paddle_3X < ball_x < paddle_3X + 50 and ball_y == 560:
                ball_x -= 20
                ball_y -= 20
                ball_dx *= -1
                ball_dy *= -1
            elif paddle_3X + 50 <= ball_x < paddle_3X + 100 and ball_y == 560:
                ball_x += 20
                ball_y -= 20
                ball_dx *= 1
                ball_dy *= -1
            if paddle_4Y < ball_y < paddle_4Y + 50 and ball_x == 860:
                ball_x -= 20
                ball_y -= 20
                ball_dx *= -1
                ball_dy *= -1
            elif paddle_4Y + 50 <= ball_y < paddle_4Y + 100 and ball_x == 860:
                ball_x -= 20
                ball_y += 20
                ball_dx *= -1
                ball_dy *= 1

        elif ball_dx < 0 and ball_dy > 0:
            if paddle_1X - 10 < ball_x < paddle_1X + 50 and ball_y == 30:
                ball_x -= 20
                ball_y += 20
                ball_dx *= 1
                ball_dy *= -1
            elif paddle_1X + 50 <= ball_x <= paddle_1X + 100 and ball_y == 30:
                ball_x += 20
                ball_y += 60
                ball_dx *= -1
                ball_dy *= -1
            if paddle_2Y < ball_y < paddle_2Y + 50 and ball_x == 330:
                ball_x += 20
                ball_y -= 20
                ball_dx *= -1
                ball_dy *= 1
            elif paddle_2Y + 50 <= ball_y < paddle_2Y + 100 and ball_x == 330:
                ball_x += 20
                ball_y += 20
                ball_dx *= -1
                ball_dy *= -1

        elif ball_dx < 0 and ball_dy < 0:
            if paddle_2Y < ball_y < paddle_2Y + 50 and ball_x == 330:
                ball_x += 20
                ball_y -= 20
                ball_dx *= -1
                ball_dy *= -1
            elif paddle_2Y + 50 <= ball_y < paddle_2Y + 100 and ball_x == 330:
                ball_x += 20
                ball_y += 20
                ball_dx *= -1
                ball_dy *= 1
            if paddle_3X < ball_x < paddle_3X + 50 and ball_y == 560:
                ball_x += 20
                ball_y -= 20
                ball_dx *= 1
                ball_dy *= -1
            elif paddle_3X + 50 <= ball_x < paddle_3X + 100 and ball_y == 560:
                ball_x -= 20
                ball_y -= 20
                ball_dx *= -1
                ball_dy *= -1

        if ball_x > 900:
            ball_x = 600
            ball_y = 150
            ball_dx = 10
            ball_dy = 10
            paddle_4_score -= 1
            # print("paddle 4")
            # print(ball_x)
            # print(ball_y)
            # print(paddle_4_score)
        if ball_x < 300:
            ball_x = 600
            ball_y = 150
            ball_dx = 10
            ball_dy = 10
            paddle_2_score -= 1
            # print("paddle 2")
            # print(ball_x)
            # print(ball_y)
            # print(paddle_2_score)
        if ball_y < 0:
            ball_x = 600
            ball_y = 150
            ball_dx = 10
            ball_dy = 10
            paddle_1_score -= 1
            # print("paddle 1")
            # print(ball_x)
            # print(ball_y)
            # print(paddle_1_score)
        # if 430 >= ball_x >= 410 and ball_y == 600:
        #     paddle_3_score += 1
        #     print(paddle_3_score)
        if ball_y > 605:
            # print("paddle 3")
            # print(ball_x)
            # print(ball_y)
            ball_x = 600
            ball_y = 150
            ball_dx = 10
            ball_dy = 10
            paddle_3_score -= 1

            # print(paddle_3_score)

        if paddle_1_score + paddle_2_score + paddle_3_score + paddle_4_score == 30 or timer > 10000:
            end_screen(paddle_1_score, paddle_2_score, paddle_3_score, paddle_4_score)

        # elif ball_dx <= 0:
        #
        #     if paddle_1X < ball_x < paddle_1X + 50 and ball_y == 40:
        #         ball_y = ball_y + 20
        #         ball_dy *= -1
        #
        #     if paddle_1X + 50 < ball_x < paddle_1X + 100 and ball_y == 40:
        #         if ball_dy > 0:
        #             ball_x += 20
        #             ball_y += 20
        #             ball_dy *= -1
        #             ball_dx *= -1
        #         else:
        #             ball_x -= 20
        #             ball_y += 20
        #             ball_dy *= -1
        #             ball_dx *= -1
        #
        #     if paddle_2Y + 10 < ball_y < paddle_2Y + 100 and ball_x == 330:
        #         ball_x = ball_x + 20
        #         ball_dx *= -1
        #
        #     if paddle_3X < ball_x < paddle_3X + 50 and ball_y == 560:
        #         ball_y = ball_y - 20
        #         ball_dy *= -1
        #
        #     if paddle_3X + 50 < ball_x < paddle_3X + 100 and ball_y == 560:
        #         if ball_dy > 0:
        #             ball_x -= 20
        #             ball_y -= 20
        #             ball_dy *= -1
        #             ball_dx *= -1
        #
        #         else:
        #             ball_x += 20
        #             ball_y -= 20
        #             ball_dy *= -1
        #             ball_dx *= -1
        #
        #     if paddle_4Y < ball_y < paddle_4Y + 100 and ball_x == 860:
        #         ball_x = ball_x - 20
        #         ball_dx *= -1

        text(25, 175, 395, str(paddle_1_score) + "  -  a d", (255, 255, 255))
        text(25, 175, 445, str(paddle_2_score) + "  - esc `", (255, 255, 255))
        text(25, 175, 495, str(paddle_3_score) + "- arrows", (255, 255, 255))
        text(25, 175, 545, str(paddle_4_score) + "  -  o l", (255, 255, 255))








        # Back button
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 205 > mouse[0] > 90 and 110 > mouse[1] > 50:
            back_button_light = pygame.Rect(95, 50, 110, 60)
            pygame.draw.rect(screen, (0, 0, 255), back_button_light)
            if click[0] == 1:
                ball_x = 600
                ball_y = 150
                ball_dx = 10
                ball_dy = 10
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




