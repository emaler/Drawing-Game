import pygame

screenX = 500; screenY = 500
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Draw Game")

running = True
clock = pygame.time.Clock()
timer = 0

mouseX, mouseY = pygame.mouse.get_pos()

playerHeight = 50; playerWidth = 50
playerX = 10; playerY = 10
playerSpeed = 150

backgroundColor = (55,55,55)

playerIcon = pygame.image.load("player.png").convert_alpha()
playerIcon = pygame.transform.scale(playerIcon, (playerHeight,playerWidth))

bullets=[]
bulletSize = 10

def drawBullet(x, y):
    bullets.append({'x':playerX + playerHeight, 'y':playerY+playerHeight})

while running:
    
    # --- Time ---
    delta_time = clock.tick(60) / 1000
    timer += delta_time
    
    # --- Draw ---
    screen.fill(backgroundColor)
    pygame.draw.rect(screen, (100, 100, 100), (playerX + playerHeight, playerY + playerWidth, bulletSize, bulletSize))
    for bullet in bullets:pygame.draw.rect(screen, (255,255,255), (int(bullet['x']), int(bullet['y']), bulletSize, bulletSize))
    screen.blit(playerIcon, (playerX, playerY))
    
    keysPressed = pygame.key.get_pressed()
    
    # --- Movement ---
    moveX = 0; moveY = 0
    if keysPressed[pygame.K_UP] or keysPressed[pygame.K_w]:
        moveY -= playerSpeed * delta_time
    if keysPressed[pygame.K_DOWN] or keysPressed[pygame.K_s]:
        moveY += playerSpeed * delta_time
    if keysPressed[pygame.K_LEFT] or keysPressed[pygame.K_a]:
        moveX -= playerSpeed * delta_time
    if keysPressed[pygame.K_RIGHT] or keysPressed[pygame.K_d]:
        moveX += playerSpeed * delta_time    
    playerX += moveX; playerY += moveY
    
    # --- Keybinds ---
    if keysPressed[pygame.K_SPACE]:
        drawBullet(playerX + playerHeight, playerY+playerHeight)
    if keysPressed[pygame.K_ESCAPE]:
        bullets = []
    if keysPressed[pygame.K_i]: 
        bulletSize += 1
    if keysPressed[pygame.K_o]: 
        if bulletSize != 1: bulletSize -= 1
    
    # Update Screen
    pygame.display.flip()
    
    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
pygame.quit()