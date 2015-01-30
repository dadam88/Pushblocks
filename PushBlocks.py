import pygame

pygame.init()

size = (630,630)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PushBlocks")

clock = pygame.time.Clock()


#2d Graphics
# Define some colors
BLACK    = (   0,   0,   0)
TRANS    = ( 90, 225, 90)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
# This sets the width and height of each grid location
drawwidth  = 120
drawheight = 120

drawmargin = 5

# Play "O Fortuna" by MIT Choir
# Available from: 
# http://freemusicarchive.org/music/MIT_Concert_Choir/Carmina_Burana_Carl_Orff/01_1355
pygame.mixer.music.load('JazzTip.wav')

pygame.mixer.music.play(-1)


block_sound = pygame.mixer.Sound("move_block.wav")
hole_sound = pygame.mixer.Sound("fall_in_hole.wav")

wall_image = pygame.image.load("wall.png").convert()
block_image = pygame.image.load("block.png").convert()
player_image = pygame.image.load("player.png").convert()
hole_image = pygame.image.load("hole.png").convert()
floor_image = pygame.image.load("floor.png").convert()

hole_image.set_colorkey(TRANS)
player_image.set_colorkey(WHITE)
block_image.set_colorkey(TRANS)


GRID = []
ROWS = 5
COLS = 5

for row in range(ROWS):
    GRID.append([])
    for column in range(COLS):
        GRID[row].append('0')
        
def print_grid():
    for row in range(ROWS):
        print(GRID[row])
class Wall:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = "'"
        self.set_grid()
    def set_grid(self):
        GRID[self.row][self.col] = self.value    
       
class Hole:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = "O"
        self.set_grid()
    def set_grid(self):
        GRID[self.row][self.col] = self.value    
         
class Player:    
    def __init__(self):
        self.row = 0
        self.col = 0
        self.value = 'X'
        self.x_speed = 10
        self.y_speed = 10
       
        self.x_coord = self.col
        self.y_coord = self.row    
    
        

    def set_grid(self):
        GRID[self.row][self.col] = self.value
        
    def move(self, row, col):
          
            
        if GRID[row][col] == '0':
            GRID[self.row][self.col] = '0' #set old to empty
            self.row = row
            self.col = col
            self.set_grid()
        else:
            pass
    
    
                
        
class Block:
    def __init__(self, row=None, col=None):
        
        if not row:
            row = 0
        if not col:
            col = 0
            
        self.row = row
        self.col = col
        self.value = '#'
        
        self.check_if_able_to_place()
    def set_grid(self):
        GRID[self.row][self.col] = self.value  
        
    def check_if_able_to_place(self):
        if GRID[self.row][self.col] == '0':
            GRID[self.row][self.col] = self.value
        else:
            self.row, self.col = self.get_empty_coordinates()
            GRID[self.row][self.col] = self.value
            
    def get_empty_coordinates(self):
        for row in range(ROWS):
            for col in range(COLS):
                if GRID[row][col] == '0':
                    return row, col
                
    def move(self,row,col):
        
        if GRID[row][col] == '0':
            GRID[self.row][self.col] = '0' #set old to empty
            self.row = row
            self.col = col
            self.set_grid()
        elif GRID[row][col] == 'O':
            GRID[self.row][self.col] = '0' #set old to empty
            self.row = row
            self.col = col
            pygame.time.delay(250)
            hole_sound.play()
       
    
    def is_hit(self, pusher, ROWS, COLS):
    
        if self.row+1 < ROWS and self.row-1 >= 0: 
            block_sound.play()
            if self.row+1 == pusher.row and self.col == pusher.col:
                block_sound.play()
                self.move(self.row-1, self.col)
                
            if self.row-1 == pusher.row and self.col == pusher.col:
                block_sound.play()
                self.move(self.row+1, self.col) 
                
        if self.col+1 < COLS and self.col-1 >= 0:
            block_sound.play()
            if self.row == pusher.row and self.col+1 == pusher.col:
                block_sound.play()
                self.move(self.row, self.col-1)
                
               
            if self.row == pusher.row and self.col-1 == pusher.col:
                block_sound.play()
                self.move(self.row, self.col+1) 
        
blocklist = []   
     
unit = Player()

block = Block(3,1)
block2 = Block(1,2)
block3 = Block(2,2)
block4 = Block(0,2)

wall = Wall(3,3)
wall2 = Wall(3,2)

hole = Hole(0,4)

blocklist.append(block)
blocklist.append(block2)
blocklist.append(block3)
blocklist.append(block4)


unit.set_grid()
block.set_grid()
block2.set_grid()
block3.set_grid()
block4.set_grid()
hole.set_grid()

print_grid()

'''  
x = int(input('Enter row'))
y = int(input('Enter col'))
unit.move(x,y)
#if block is clicked on....
block.is_hit(unit)
block2.is_hit(unit)

print_grid()
'''

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        '''
        pos = pygame.mouse.get_pos()
        print('X: {}, Y {}'.format(pos[0],pos[1]))
        col = pos[0] // (drawwidth+drawmargin)
        row = pos[1] // (drawheight+drawmargin)
        print('ROW {0}, COL {1}'.format(row,col))
        '''
        
        col = unit.col
        row = unit.row
        # User pressed down on a key
        
        if event.type == pygame.KEYDOWN:
             # Figure out if it was an arrow key. If so
             # adjust speed.
             if event.key == pygame.K_ESCAPE:
                 done = True
             if event.key == pygame.K_p:
                 pass
                 
                 
             if event.key == pygame.K_LEFT:
                if unit.col-1 >= 0 and unit.col-1 < COLS:
                    col = unit.col-1
                    row = unit.row
                    try:
                        unit.move(row,col)
                    except IndexError:
                        pass
                         
             if event.key == pygame.K_RIGHT:
                col = unit.col+1
                row = unit.row
                try:
                    unit.move(row,col)
                except IndexError:
                    pass
                                 
             if event.key == pygame.K_UP:	
                 if unit.row-1 >= 0 and unit.row-1 < ROWS:
                     col = unit.col
                     row = unit.row-1
                     try:
                         unit.move(row,col)
                     except IndexError:
                         pass
                 
             if event.key == pygame.K_DOWN:
                 col = unit.col
                 row = unit.row+1
                 try:
                     unit.move(row,col)
                 except IndexError:
                     pass

        try:
            if GRID[row][col] == '#':
                for block in blocklist:
                    if block.row == row and block.col == col:
                        
                        block.is_hit(unit, ROWS, COLS)
                            
                      
        except IndexError:
            pass
                    
                    
                    
        
           
            
            
                
                
    
    
    #Draw
    screen.fill(BLACK)

    
    color = WHITE
    
    x= drawmargin
    y= drawmargin
    for row in range(ROWS):
        for col in range(COLS):
            
                
            pygame.draw.rect(screen,color,[x,y,drawwidth,drawheight])
            screen.blit(floor_image, [x,y])
            if GRID[row][col] == "O":
                screen.blit(hole_image,[x,y])
            if GRID[row][col] == "X":
                screen.blit(player_image,[x,y])
            if GRID[row][col] == '#':
                screen.blit(block_image,[x,y])
            if GRID[row][col] == "'":
                screen.blit(wall_image,[x,y])
            #if GRID[row][col] == "0":
                #screen.blit(floor_image,[x,y])
            x += drawwidth
            x += drawmargin
            
            
        x = drawmargin
        y += drawheight
        y += drawmargin

   
    # limit FPS
    clock.tick(30)

    print_grid()
    
    #flip/update screen
    pygame.display.flip()
pygame.quit()
                  