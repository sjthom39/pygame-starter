import pygame # import library

pygame.init()
#spygame.image.load(samuri).convert()
# Create the window
win = pygame.display.set_mode((1500, 990))
img=pygame.image.load('samuri.png')

# Load the spritesheet
spritesheet = pygame.image.load('assets/gfx/objects.png').convert_alpha()

# Create the first image
chest_closed = pygame.Surface([16, 16]).convert() # Create a surface with size 16 x 16
chest_closed.blit(spritesheet, (0, 0), (0, 0, 16, 16)) # Apply a slice of the spritesheet image (16 x 16) to the surface we made above

# Create the second image

#samuri images
samuri = pygame.image.load('samuri.png')
x=600
y=290



back = pygame.image.load('assets/dark background.png') 

# Create the font
font = pygame.font.SysFont("arial italic", 50)
text = font.render("THE LONE WARRIOR 狼", True, (255, 255, 255))

x=200
y=200
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys=pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    x -=15
   
  if keys[pygame.K_RIGHT]:
    x +=15
  
  if keys[pygame.K_DOWN]:
    y +=15

  if keys[pygame.K_UP]:
    y -=15



# Game code starts here ---------------------
  
  win.fill((0, 0, 0))
  #win.blit(img, (400,300))
  # win.blit(chest_closed,(100,100))
  #win.blit(chest_open,(150,100))
  win.blit(back,(0, 0 ))
  
  win.blit(text,(400,300))

  win.blit(samuri, (x, y))

  #win.blit(spritesheet, (100, 200))

  # Draw a rectangle
  #pygame.draw.rect(win, (0, 204, 102), (50, 50, 100, 200))
  
  #Update the display
  pygame.display.update()

print("Ending game")
pygame.quit()
