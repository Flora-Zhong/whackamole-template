import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        position = (640, 512)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    x = position[0] // 32
                    y = position[1] // 32
                    print(x)
            screen.fill("light green")
            for i in range(16):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
            for j in range(20):
                pygame.draw.line(screen, "black", (j * 32, 0), (j * 32, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            x = 0
            y = 0
            if position == (x, y):
                x = random.randrange(0, 640) // 32 * 32
                y = random.randrange(0, 512) // 32 * 32
                screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
