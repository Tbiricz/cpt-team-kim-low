class collider():
    def __init__(self,pos ,direction):
        self.position = pos
        self.direction = direction
        
class Player():
    
    def __init__(self,x,y):
        
        self.position = PVector(x, y)
        self.acceleration = PVector(0,0)
        self.velocity = PVector(0,0)
        self.friction = .8
        self.maxSpeed = 2
        self.maxJump = 12
        self.playerDimensions = 20
        self.gravity = -1
        
    def display(self):
        screenPos = worldPoint_to_screenPoint(self.position)
        
        fill(0)
        rect(int(screenPos.x - self.playerDimensions/2), int(screenPos.y - self.playerDimensions/2), self.playerDimensions, self.playerDimensions)
        
    def direction(self, pos):
        
        if pos.x > grapplingLocation.x:
            rise
            
    def grappling(self):
        distance = PVector.sub(self.position, mouseX, mouseY)
        a = PVector.fromAngle(distance.heading())
        a = distance.mag()
        
    def applyForce(self,x ,y):
        
        self.acceleration.x += x
        self.acceleration.y += y
        
    def makeColliders(self, velocity, position):

        self.colorColliders = []
        
        r1 = PVector(position.x + self.playerDimensions/2 + velocity.x, position.y + self.playerDimensions/2)
        r2 = PVector(position.x + self.playerDimensions/2 + velocity.x, position.y - self.playerDimensions/2)
        u1 = PVector(position.x + self.playerDimensions/2, position.y + self.playerDimensions/2 + velocity.y)
        u2 = PVector(position.x - self.playerDimensions/2, position.y + self.playerDimensions/2 + velocity.y)
        l1 = PVector(position.x - self.playerDimensions/2 + velocity.x, position.y + self.playerDimensions/2)
        l2 = PVector(position.x - self.playerDimensions/2 + velocity.x, position.y - self.playerDimensions/2)
        d1 = PVector(position.x + self.playerDimensions/2, position.y - self.playerDimensions/2 + velocity.y)
        d2 = PVector(position.x - self.playerDimensions/2, position.y - self.playerDimensions/2 + velocity.y)
        
        self.colorColliders.append(collider(r1, 'right'))
        self.colorColliders.append(collider(r2, 'right'))
        self.colorColliders.append(collider(u1, 'up'))
        self.colorColliders.append(collider(u2, 'up'))
        self.colorColliders.append(collider(l1, 'left'))
        self.colorColliders.append(collider(l2, 'left'))
        self.colorColliders.append(collider(d1, 'down'))
        self.colorColliders.append(collider(d2, 'down'))
        
    def colorCollide(self, position, colorColliders):
        
        screenPos = worldPoint_to_screenPoint(position)

        for collider in self.colorColliders:
                        
            colliderScreenPos = worldPoint_to_screenPoint(collider.position)
            
            c = blockMap.get(int(colliderScreenPos.x),int(colliderScreenPos.y))
            
            right = False
            left = False
            up = False
            self.grounded = False
            if c == color(104,255,147) and collider.direction == 'right' :
                right = True
                self.velocity.x = 0
                self.position.x -= self.velocity.x *2
                print('Right')
                
            elif c == color(104,255,147) and collider.direction == 'left':
                left = True
                self.velocity.x = 0 
                self.position.x += self.velocity.x *2 
                print('Left')
                
            elif c == color(104,255,147) and collider.direction == 'up':
                up = True
                self.velocity.y = 0
                self.position.y += self.velocity.y *2
                print('Roof')
                
            elif c == color(104,255,147) and collider.direction == 'down':
                self.grounded = True
                self.velocity.y = 0
                self.position.y -= self.velocity.y *2
                print('Ground')   
                
            else:
                self.grounded = False
            
    #         if grounded == True or up == True and right == True or left == True:
    # )

    def update(self):
        
        self.applyForce(0,self.gravity)
        
        if keyArrays[0] == True:
            self.applyForce(-self.maxSpeed, 0)
        if keyArrays[1] == True:
            self.applyForce(self.maxSpeed,0)
        if keyArrays[2] == True and self.grounded == True:
            self.applyForce(0,self.maxJump)
        # if keyArrays[3] == True:
        #     self.applyForce(0,-self.maxJump)
                                    
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        
        self.velocity.x *= self.friction
        
        self.makeColliders(self.velocity, self.position)

        self.colorCollide(self.position, self.colorColliders)

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
                    
        self.acceleration = PVector(0,0)
        
    
        print('-----------------')
        self.display()
         
def worldPoint_to_screenPoint(worldPoints):
    return PVector((width/2 + worldPoints.x),(height/2 - worldPoints.y))

def setup():
    size(400,400)
    
    global blockMap
    blockMap = loadImage("cs_allmine.png")
      
    global playerObj
    playerObj = Player(0,200)
    
    global keyArrays
    keyArrays = [False, False, False, False]     # up down left right
    
    global grapplingLocation
    grapplingLocation = PVector(None, None)
def draw():
    background(blockMap)
    
    playerObj.update()
    
def mouseClicked():
    grapplingLocation = PVector(mouseX, mouseY)
    
def keyPressed():
    
    if keyCode == LEFT or key == "a" :
        keyArrays[0] = True
    if keyCode == RIGHT or key == "d":
        keyArrays[1] = True
    if keyCode == UP or key == "w":
        keyArrays[2] = True 
    if keyCode == DOWN or key == "s":
        keyArrays[3] = True
def keyReleased():
    
    if keyCode == LEFT or key == "a":
        keyArrays[0] = False
    if keyCode == RIGHT or key == "d":
        keyArrays[1] = False
    if keyCode == UP or key == "w":
        keyArrays[2] = False 
    if keyCode == DOWN or key == "s":
        keyArrays[3] = False
