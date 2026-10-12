from Grille import Grille
import pygame


game_gril = Grille()
game_gril.init_grille()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# fill the screen with a color to wipe away anything from last frame
screen.fill("blue")
for i in range(game_gril.get_nb_lines()):
    for j in range(game_gril.get_nb_column()):
        circle_pos = pygame.Vector2(screen.get_width()/8*(i+1), screen.get_height()/8*(j+1))
        pygame.draw.circle(screen, "black",circle_pos,40)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # RENDER YOUR GAME HERE
    key_value = 0
    play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        play = True
        key_value = 0
    elif keys[pygame.K_2]:
        play = True
        key_value = 1
    elif keys[pygame.K_3]:
        play = True
        key_value = 2
    elif keys[pygame.K_4]:
        play = True
        key_value = 3
    elif keys[pygame.K_5]:
        play = True
        key_value = 4
    elif keys[pygame.K_6]:
        play = True
        key_value = 5
    elif keys[pygame.K_7]:
        play = True
        key_value = 6

    if play :
        statut = game_gril.gril_status(key_value)
        game_gril.play(key_value)
        print(f"key = {statut}")
        circle_pos = pygame.Vector2(screen.get_width()/8*(key_value+1), screen.get_height()/8*(8-statut+1))
        pygame.draw.circle(screen, "red",circle_pos,40)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    


pygame.quit()



if __name__ == '__main__':
    print ("Bienvenue dans le jeu du puissance 4 !")
    game_gril.print_grille()