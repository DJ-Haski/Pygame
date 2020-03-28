import pygame, time

pygame.init()
window=pygame.display.set_mode((600,300))
myfont= pygame.font.SysFont("Roboto", 60)
label = myfont.render("Hello, pygame!",1,(255,255,0))
background = pygame.Surface(window.get_size())
background.fill((55,60,255))
background = background.convert()
window.blit(background, (0, 0))

window.blit(label,(100,100))
pygame.display.update()
time.sleep(5)
pygame.quit()


