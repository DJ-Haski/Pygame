import pygame, time

pygame.init()
window=pygame.display.set_mode((600,300))
myfont= pygame.font.SysFont("Roboto", 60)
label = myfont.render("hello, pygame!",1,(255,255,0))
window.blit(label,(100,100))
pygame.display.update()
time.sleep(5)
pygame.quit()


