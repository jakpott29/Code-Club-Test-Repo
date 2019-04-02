import pygame, time, random

pygame.init()
width, height = 800, 600
dvdLogoSpeed = [1, 1]

backgroundColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
screen = pygame.display.set_mode((width, height))

dvdLogo = pygame.image.load("dvd-logo-white.png")
dvdLogoRect = dvdLogo.get_rect()

while True:
    screen.fill(backgroundColor)

    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

    if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
        dvdLogoSpeed[0] = -dvdLogoSpeed[0]
        backgroundColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
        dvdLogoSpeed[1] = -dvdLogoSpeed[1]
        backgroundColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    pygame.display.flip()
    time.sleep(0.1)
