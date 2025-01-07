import pygame

running = True
if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            pos = pygame.mouse.get_pos()
            screen.blit(pygame.image.load("./data/arrow.png"), (pos[0], pos[1]))
        pygame.display.flip()
    pygame.quit()
