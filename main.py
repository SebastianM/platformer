import pygame, sys, time, random
pygame.init()

win = pygame.display.set_mode((500,500))

green = (0,255,0)
white = (255,255,255)
red = (255,0,0)
purple = (121, 25, 122)

run = True

speed = 3
jump = 100

cubeX = 250
cubeY = 250
cubeSize = 25

gravity = 3

while run:
  pygame.time.delay(10)
  cubeY += gravity

  
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

  

  pCube = pygame.Rect(490, 320, 50, 50)
    
  player = pygame.Rect(cubeX, cubeY, cubeSize, cubeSize)

  platform = pygame.Rect(0,350,500,30)
  
  if(keys[pygame.K_UP] & player.colliderect(platform)):
    cubeY-=jump
    
  if player.colliderect(platform):
    cubeY -= gravity
  if player.colliderect(pCube):
    cubeX = 0
    cubeY = 315


  pygame.draw.rect(win, green, pCube)
  pygame.draw.rect(win, purple, platform)
  pygame.draw.rect(win, red, player)
  pygame.display.update()