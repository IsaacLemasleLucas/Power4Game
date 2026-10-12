from Grille import Grille
import pygame

game_gril = Grille()
game_gril.init_grille()
game_gril.play(3)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")
    for i in range(game_gril.get_nb_lines()):
        for j in range(game_gril.get_nb_column()):
            circle_pos = pygame.Vector2(screen.get_width()/8*(i+1), screen.get_height()/8*(j+1))
            pygame.draw.circle(screen, "black",circle_pos,40)

    # RENDER YOUR GAME HERE
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()



if __name__ == '__main__':
    print ("Bienvenue dans le jeu du puissance 4 !")
    game_gril.print_grille()