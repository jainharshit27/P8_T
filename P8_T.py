import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

b1 = pygame.Rect(100,100,50,50)
b1_y_change = 1
b1_x_change = 1

movement_state = "horizontal"

# define movement function

while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    movement()
    
    if movement_state == "horizontal":
        b1.x = b1.x + b1_x_change
        if b1.x >= 250:
            b1.x = 250
            movement_state = "vertical"
        if b1.x <= 100:
            b1.x = 100
            movement_state = "vertical"
    if movement_state == "vertical":
        b1.y = b1.y + b1_y_change
        if b1.y >= 250:
            b1.y = 250
            movement_state = "horizontal"
        if b1.y <= 100:
            b1.y = 100
            movement_state = "horizontal"
            
    pygame.draw.rect(screen,(0,0,0),b1)
    pygame.display.update()
    pygame.time.delay(5)