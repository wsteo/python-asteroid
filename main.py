import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    MAX_FPS = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
        screen.fill(COLOR_BLACK)
        
        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        # limit frame rate
        dt = clock.tick(MAX_FPS) / 1000

if __name__ == "__main__":
    main()