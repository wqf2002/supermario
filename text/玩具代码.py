import pygame

pygame.init()
w, h = 500, 500
pygame.display.set_mode((w, h))
screen = pygame.display.get_surface()
maps = pygame.image.load("map.png")
maps = pygame.transform.scale(maps, (w, h))
mario_image = pygame.image.load('超级玛丽.png')
mario = pygame.sprite.Sprite()
mario.image = mario_image
mario.rect = mario.image.get_rect()
mario.rect.x, mario.rect.y = w / 2, h / 2
player_group = pygame.sprite.Group()
player_group.add(mario)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y += 10
            if keys[pygame.K_UP]:
                mario.rect.y -= 10
            if keys[pygame.K_LEFT]:
                mario.rect.x -= 10
            if keys[pygame.K_RIGHT]:
                mario.rect.x += 10
    screen.blit(maps, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
