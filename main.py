import pygame, sys, time, random
pygame.init()

win = pygame.display.set_mode((500,500))

green = (0,255,0)
white = (255,255,255)
red = (255,0,0)
purple = (121, 25, 122)

run = True

speed = 3
jump = 155

cubeX = 250
cubeY = 250
cubeSize = 25

plat1X = 0
plat1Y = 390

plat2X = 275
plat2Y = 290

plat3X = 0
plat3Y = 225

plat4X = 300
plat4Y = 120

plat5X = 150
plat5Y = 40


playerGrav= 3
gravity = 0.5

while run:
  pygame.time.delay(5)
  cubeY += playerGrav
  plat1Y += gravity
  plat2Y += gravity
  plat3Y += gravity
  plat4Y += gravity
  plat5Y += gravity
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

  keys = pygame.key.get_pressed()
  win.fill(white)
  if(keys[pygame.K_RIGHT]):
    cubeX+=speed

  if(keys[pygame.K_LEFT]):
    cubeX-=speed
    
  
  if(keys[pygame.K_DOWN]):
    cubeY+=speed

  
  platform1 = pygame.Rect(plat1X,plat1Y,240,30)
  platform2 = pygame.Rect(plat2X,plat2Y,250,30)
  platform3 = pygame.Rect(plat3X,plat3Y,240,30)
  platform4 = pygame.Rect(plat4X,plat4Y,250,30)
  platform5 = pygame.Rect(plat5X,plat5Y,160,30)
  
    
  player = pygame.Rect(cubeX, cubeY, cubeSize, cubeSize)

  platform = pygame.Rect(0,475,500,30)
  
  if player.colliderect(platform):
    break
  if(keys[pygame.K_UP] & player.colliderect(platform1)):
    cubeY-=jump
    
  if player.colliderect(platform1):
    cubeY -= playerGrav
    
  if(keys[pygame.K_UP] & player.colliderect(platform2)):
    cubeY-=jump
    
  if player.colliderect(platform2):
   cubeY -= playerGrav

  if(keys[pygame.K_UP] & player.colliderect(platform3)):
    cubeY-=jump
    
  if player.colliderect(platform3):
   cubeY -= playerGrav
    
  if(keys[pygame.K_UP] & player.colliderect(platform4)):
    cubeY-=jump
    
  if player.colliderect(platform4):
   cubeY -= playerGrav
    
  if(keys[pygame.K_UP] & player.colliderect(platform5)):
    cubeY-=jump
    
  if player.colliderect(platform5):
   cubeY -= playerGrav


  
  if platform1.colliderect(platform):
    plat1Y = 0

  if platform2.colliderect(platform):
    plat2Y = 0
    
  if platform3.colliderect(platform):
    plat3Y = 0
    
  if platform4.colliderect(platform):
    plat4Y = 0
    
  if platform5.colliderect(platform):
    plat5Y = 0


  pygame.draw.rect(win, red, platform)
  pygame.draw.rect(win, purple, platform1)
  pygame.draw.rect(win, purple, platform2)
  pygame.draw.rect(win, purple, platform3)
  pygame.draw.rect(win, purple, platform4)
  pygame.draw.rect(win, purple, platform5)
  
  pygame.draw.rect(win, green, player)
  pygame.display.update()