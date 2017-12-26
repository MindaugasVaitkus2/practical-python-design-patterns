import pygame

window_dimensions = 800, 600
screen = pygame.display.set_mode(window_dimensions)

x = 100
y = 100

player_quits = False

while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 4: y -= 4
        if pressed[pygame.K_DOWN] and y < 576: y += 4
        if pressed[pygame.K_LEFT] and x > 4: x -= 4
        if pressed[pygame.K_RIGHT] and x < 776: x += 4

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 20))

        pygame.display.flip()
