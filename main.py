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

title_font = pygame.font.Font('freesansbold.ttf', 64)
button_font = pygame.font.Font('freesansbold.ttf', 14)




def intro():
    run = True
    while run:
        screen.fill((128, 128, 128))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



        title = title_font.render("Welcome to 4 Player Pong", True, (0, 0, 0))
        screen.blit(title, (40, 250))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

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
        else:
            button_2_normal = pygame.Rect(550, 400, 110, 60)
            pygame.draw.rect(screen, (200, 0, 0), button_2_normal)

        button1_text = button_font.render("Play", True, (0, 0, 0))
        screen.blit(button1_text, (((225+(110/2))-15), (400+(60/2))-5))
        button2_text = button_font.render("How to play", True, (0, 0, 0))
        screen.blit(button2_text, (((550+(110/2))-40), (400+(60/2))-5))

        pygame.display.update()





# Game loop
def main():

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    paddle_1X -= 10
                if event.key == pygame.K_d:
                    paddle_1X += 10
                if event.key == pygame.K_ESCAPE:
                    paddle_2Y -= 10
                if event.key == pygame.K_BACKQUOTE:
                    paddle_2Y += 10
                if event.key == pygame.K_LEFT:
                    paddle_3X -= 10
                if event.key == pygame.K_RIGHT:
                    paddle_3X += 10
                if event.key == pygame.K_o:
                    paddle_4Y -= 10
                if event.key == pygame.K_l:
                    paddle_4Y += 10
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_b:
                    intro()





    running = True
    while running:
        # Background Color
        screen.fill((128, 128, 128))
        draw_game_background()
        draw_paddles()

        # Move paddles


        # update screen
        pygame.display.update()

intro()
main()



