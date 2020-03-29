import pygame
pygame.init()
swidth=901
sheight=901
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
R=0
G=0
B=0

isJump=False
jumpCount=10

run = True
while run is True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # тут ошибка, которую я не могу пофиксить :( // уже пофиксил
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


    window.fill((R,G,B))

    for point in range(0, 900, 64):  # range(start, stop, step)
        pygame.draw.line(window, (255, 0, 255), (0, 0), (450, point), 2)
        pygame.draw.line(window, (0, 255, 255), (900, 0), (450, point), 2)
    for point in range(0, 900, 64):  # range(start, stop, step)
        pygame.draw.line(window, (255, 0, 0), (0, 900), (450, point), 2)
        pygame.draw.line(window, (0, 255, 0), (900, 900), (450, point), 2)
    #pygame.draw.circle(window, (238, 130, 238), (300, 300), 40)
    #pygame.draw.arc(window, (0, 255, 0), (0, -900, 1800, 1800), 3.14, (0.75 * 6.28))
    #pygame.draw.polygon(window, (255, 0, 0), ((500, 175), (600, 500), (350, 300), (650, 300), (400, 500)), 10)
    pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
pygame.time.delay(1000)
pygame.quit()



