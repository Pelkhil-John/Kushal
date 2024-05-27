import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1300, 680

window = pygame.display.set_mode((WIDTH, HEIGHT))
pslayer1 = pygame.rect.Rect(WIDTH//2, HEIGHT//2, 20,20)
pslayer2 = pygame.rect.Rect(random.random()*WIDTH, random.random()*HEIGHT, 20,20)
walls = []
clock = pygame.time.Clock()
projeciles = [[],[]]
p1_score = 0
p2_score = 0
p1_fire_count = 0


def draw():
    window.fill("black")
    pygame.draw.rect(window, "blue", pslayer2)
    pygame.draw.rect(window, "red", pslayer1)
    for proj_list in projeciles:
        for proj in proj_list:
            pygame.draw.rect(window, "grey", proj)
    for wall in walls:
        pygame.draw.rect(window, "brown", wall)
    pygame.display.update()

def fire(obj, left):
    if left:
        projeciles[0].append(pygame.rect.Rect(obj.left - 10, obj.centery, 10,10))
    else:
        projeciles[1].append(pygame.rect.Rect(obj.right + 10, obj.centery, 10,10))

def collide():
    global p2_score, p1_score
    for proj_list in projeciles:
        for proj in proj_list:
            if pslayer1.colliderect(proj):
                p2_score +=1
                win("blue wins")
            elif pslayer2.colliderect(proj):
                p1_score += 1
                win("red wins")
                


def win(str):
    global projeciles
    window.blit(pygame.font.SysFont("Calibri",50).render(str, False, "white"), (2*WIDTH/5, HEIGHT/3))
    window.blit(pygame.font.SysFont("Calibri",50).render(f"p1: {p1_score}", False, "red"), (WIDTH/5, HEIGHT/5))
    window.blit(pygame.font.SysFont("Calibri",50).render(f"p2: {p2_score}", False, "blue"), (4*WIDTH/5, HEIGHT/5))
    exit_button_rect = pygame.rect.Rect(WIDTH/3, HEIGHT*2/3, WIDTH/3, HEIGHT/4)
    pygame.draw.rect(window, "red", exit_button_rect)
    pygame.display.update()
    while True:
        clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        mouse_list = pygame.mouse.get_pressed()
        if exit_button_rect.collidepoint(mouse_pos) and mouse_list[0]:
            projeciles = [[],[]]
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()

def make_walls():
    global walls
    walls.append(pygame.rect.Rect(0,HEIGHT/4,100,20))         
    walls.append(pygame.rect.Rect(0,3*HEIGHT/4,100,20))
    walls.append(pygame.rect.Rect(WIDTH-100,3*HEIGHT/4,100,20))
    walls.append(pygame.rect.Rect(WIDTH-100,HEIGHT/4,100,20))
    walls.append(pygame.rect.Rect(WIDTH/2-10,3*HEIGHT/4-50,20,100))
    walls.append(pygame.rect.Rect(WIDTH/2-10,HEIGHT/4-50,20,100))

def main():
    global p1_fire_count
    make_walls()
    while True:
        clock.tick(60)
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and pslayer1.x - 5 > 0:
            pslayer1.x -= 5
        if keys[pygame.K_d] and pslayer1.x + 5 < WIDTH - pslayer1.w:
            pslayer1.x += 5
        if keys[pygame.K_s] and pslayer1.y + 5 < HEIGHT - pslayer1.h :
            pslayer1.y += 5
        if keys[pygame.K_w] and pslayer1.y - 5 > 0:
            pslayer1.y -= 5
        if keys[pygame.K_LEFT] and pslayer2.x - 5 > 0:
            pslayer2.x -= 5
        if keys[pygame.K_RIGHT] and pslayer2.x + 5 < WIDTH - pslayer1.w:
            pslayer2.x += 5
        if keys[pygame.K_DOWN]and pslayer2.y + 5 < HEIGHT - pslayer1.h :
            pslayer2.y += 5
        if keys[pygame.K_UP]and pslayer2.y - 5 > 0:
            pslayer2.y -= 5
        
        for proj in projeciles[0]:
            proj.x -= 7
            if proj.x < 0:
                projeciles[0].remove(proj)
        for proj in projeciles[1]:
            proj.x += 7
            if proj.x > WIDTH:
                projeciles[1].remove(proj)
        draw()
        collide()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if p1_fire_count == 10 * p1_score:
                        fire(pslayer1, pslayer1.x > pslayer2.x)
                    p1_fire_count = 0
                if event.key == pygame.K_RCTRL:
                    fire(pslayer2, pslayer2.x > pslayer1.x)
        if p1_fire_count < p1_score * 10:
            p1_fire_count +=1 

if __name__ == "__main__":
    main()
    
     
