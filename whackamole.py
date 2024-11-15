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
        mole_position = (0, 0)
        running = True
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    x = position[0] // 32
                    y = position[1] // 32
                    position = (x, y)
                    if position == mole_position:
                        x = random.randrange(0, 640)
                        y = random.randrange(0, 512)
                        row = x // 32
                        col = y // 32
                        mole_position = (row, col)
                        pygame.display.flip()
            screen.fill("light green")
            for i in range(16):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
            for j in range(20):
                pygame.draw.line(screen, "black", (j * 32, 0), (j * 32, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position[0] * 32, mole_position[1] * 32)))
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
