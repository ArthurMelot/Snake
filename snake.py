import pygame
import random

pygame.init()

width = 720
height = 480
nrow = height//10
ncol = width//10
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()

#Colors
black = pygame.Color(0,0,0)
gray = pygame.Color(100,100,100)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)



def write_score(font,size,color,score):
    textbox = pygame.font.SysFont(font, size).render("Score: {0}".format(score), True, color)
    rect = textbox.get_rect()
    rect.center = (40,35)
    window.blit(textbox,rect)

#Loop
def loop():
    #Tiles
    head_pos = [nrow//2,ncol//2]
    snake_body = [[nrow//2, ncol//2],[nrow//2, ncol//2-1],[nrow//2, ncol//2-2],[nrow//2, ncol//2-3]]
    fruit_pos = [random.randrange(0,nrow),random.randrange(0,ncol)]
    direction = "right"

    score = 0
    state = "playing"
    new_dir = "right"
    fruit_exist = True
    while state != "exit":
        
        if state == "playing":
            #Input detection
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        new_dir = "up"
                    if event.key == pygame.K_LEFT:
                        new_dir = "left"
                    if event.key == pygame.K_DOWN:
                        new_dir = "down"
                    if event.key == pygame.K_RIGHT:
                        new_dir = "right"
                elif event.type == pygame.QUIT:
                    state = "exit"

            if new_dir == "up" and direction != "down":
                direction = "up"
            
            if new_dir == "down" and direction != "up":
                direction = "down"

            if new_dir == "left" and direction != "right":
                direction = "left"

            if new_dir == "right" and direction != "left":
                direction = "right"

            if direction == "up":
                head_pos[0] -= 1
            if direction == "down":
                head_pos[0] += 1
            if direction == "left":
                head_pos[1] -= 1
            if direction == "right":
                head_pos[1] += 1

            snake_body.insert(0,list(head_pos))
            if fruit_pos[0] == head_pos[0] and fruit_pos[1] == head_pos[1]:
                score += 1
                fruit_exist = False

            else:
                snake_body.pop()

            if not fruit_exist:
                fruit_pos = [random.randrange(0,nrow),random.randrange(0,ncol)]
            
            fruit_exist = True
            window.fill(gray)

            for pos in snake_body:
                pygame.draw.rect(window,blue,pygame.Rect(pos[1]*10,pos[0]*10,10,10))
            
            pygame.draw.rect(window,red,pygame.Rect(fruit_pos[1]*10,fruit_pos[0]*10,10,10))

        #Win
        if len(snake_body) == nrow*ncol-1 and state != "exit":
            state = "win"

        #Gameover

        if head_pos[0] < 0 or head_pos[0] > nrow-1:
            state = "gameover"
        if head_pos[1] < 0 or head_pos[1] > ncol-1:
            state = "gameover"

        for part in snake_body[1:]:
            if part[0] == head_pos[0] and part[1] == head_pos[1]:
                state = "gameover"
        
        if state == "gameover" and state != "exit":
            textbox = pygame.font.SysFont("Calibri",50,True).render("Game Over!",True,black)
            rect = textbox.get_rect()
            rect.center = (width//2,height//2)
            window.blit(textbox,rect)

            textbox2 = pygame.font.SysFont("Calibri",35,True).render("R to restart",True,black)
            rect2 = textbox2.get_rect()
            rect2.center = (width//2,height//2 + 50)
            window.blit(textbox2,rect2)      

        elif state == "win" and state != "exit":
            textbox = pygame.font.SysFont("Calibri",50,True).render("You Won!",True,black)
            rect = textbox.get_rect()
            rect.center = (width//2,height//2)
            window.blit(textbox,rect)

            textbox2 = pygame.font.SysFont("Calibri",35,True).render("R to restart",True,black)
            rect2 = textbox2.get_rect()
            rect2.center = (width//2,height//2 + 50)
            window.blit(textbox2,rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = "exit"
            
            elif state == "win" or state == "gameover":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        state = "exit"
                        loop()
        
        write_score("Calibri",20,black,score)
        pygame.display.update()
        fps.tick(15)


loop()
pygame.display.quit()
pygame.quit()
quit()    