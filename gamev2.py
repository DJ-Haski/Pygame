import pygame
pygame.init()
swidth=600
sheight=600
window=pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("First Game in Python")

x = 50
y = 50
width = 40
height = 60
speed = 5

isJump=False
jumpCount=10

run = True
while run is True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT(): # тут ошибка, которую я не могу пофиксить :(
            run = False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x<swidth-width-speed:
        x += speed
    if not(isJump):
        if keys[pygame.K_UP] and y>speed:
            y -= speed
        if keys[pygame.K_DOWN] and y<sheight-height-speed:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount**2)/2
            jumpCount -= 1
        else:
            isJump=False
            jumpCount=10


    window.fill((0,0,0))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()

#pygame.quit()



