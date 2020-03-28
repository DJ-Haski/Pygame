import pygame
pygame.init()
swidth=600
sheight=600
window=pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption("First Game in Python")
myfont= pygame.font.SysFont("Roboto", 40)
label = myfont.render("Arrows and Space to move!",10,(255,255,0))
window.blit(label,(100,100))
pygame.display.update()
pygame.time.delay(1500)

x = 280
y = 280
width = 40
height = 40
speed = 5

isJump=False
jumpCount=10

run = True
while run is True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # тут ошибка, которую я не могу пофиксить :(
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
            negative=1
            if jumpCount< 0:
                negative =- 1

            y -= (jumpCount**2)/2 * negative
            jumpCount -= 1
        else:
            isJump=False
            jumpCount=10


    window.fill((0,0,0))
    pygame.draw.circle(window,(238,130,238),(300,300),40)
    #pygame.draw.polygon(window, (255, 255, 255), ((250, 0),(125,125),(0,250)))
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
pygame.time.delay(1000)
pygame.quit()



