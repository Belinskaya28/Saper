import pygame
white=(255,255,255)
black=(0,0,0)
size=[500,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("pole")
done=False
clock=pygame.time.Clock()
i=0
while done==False:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            done=True
    screen.fill(white)
    pygame.draw.line(screen,black,[i,0],[size[0]+i,size[1]],3)
    if (i>size[0]):
        i=0
    i=i+1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
