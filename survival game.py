from pygame import *

class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.sprite = image.load("sonic.png")
		self.sprite = transform.scale(self.sprite, (50, 70))

	def draw(self, screen):
		screen.blit(self.sprite, (self.x, self.y))

	def update(self):
		self.x += self.dx
		self.y += self.dy
		

	def moveLeft(self):
		self.dx = -1
		self.dy = 0

	def moveRight(self):
		self.dx = 1
		self.dy = 0

	def moveUp(self):
		self.dy = -1
		self.dx = 0

	def moveDown(self):
		self.dy = 1
		self.dx = 0

	def stop(self):
		self.dx = 0
		self.dy = 0


clock = time.Clock()
init()
screen = display.set_mode((600, 600))
display.set_caption("suv")
endGame = False
mainPlayer = Player(200, 200)

while not endGame:
	for e in event.get():
		if e.type == QUIT:
			endGame = True
		elif e.type == KEYDOWN:
			if e.key == K_LEFT:
				mainPlayer.moveLeft()
			elif e.key == K_RIGHT:
				mainPlayer.moveRight()
			elif e.key == K_UP:
				mainPlayer.moveUp()
			elif e.key == K_DOWN:
				 mainPlayer.moveDown()
		elif e.type == KEYUP:
			if e.key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]:
				mainPlayer.stop()

	screen.fill((123, 50, 168))
	mainPlayer.update()
	mainPlayer.draw(screen)
	clock.tick(60)
	display.update()

class enemy:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.speed = 1
		self.sprite = image.load("eggman.png")
		self.sprite = transform.scale(self.sprite, (50, 70))

	def draw(self, screen):
		screen.blit(self.sprite, (self.x, self.y))

	def update(self):
		px,py = mainPlayer.getpos
		self.x += self.dx
		self.y += self.dy


	def follow(self,mainPlayer):
		self.x = mainPlayer.x - self.x
		self.y = mainPlayer.y - self.y
		screen.blit(self.sprite, (self.x, self.y))

	def stop(self):
		self.dx = 0
		self.dy = 0

clock = time.Clock()
init()
screen = display.set_mode((600, 600))
display.set_caption("suv")
endGame = False
mainPlayer = Player(200, 200)
mainEnemy = enemy(100,100)

while not endGame:
	for e in event.get():
		if e.type == QUIT:
			endGame = True
		elif e.type == KEYDOWN:
			if e.key == K_LEFT:
				mainPlayer.moveLeft()
			elif e.key == K_RIGHT:
				mainPlayer.moveRight()
			elif e.key == K_UP:
				mainPlayer.moveUp()
			elif e.key == K_DOWN:
				 mainPlayer.moveDown()
		elif e.type == KEYUP:
			if e.key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]:
				mainPlayer.stop()

	screen.fill((123, 50, 168))
	mainPlayer.update()
	mainPlayer.draw(screen)
	mainEnemy.update()
	mainEnemy.draw(screen)
	mainEnemy.follow(mainPlayer)
	clock.tick(60)
	display.update()

class Player(Rect):
	def __init__(self,x,y):
		self.dx = 0
		self.dy = 0
		self.sprite = image.load("sonic.png")
		self.sprite = transform.scale(self.sprite, (50, 70))
		self.w = 50 
		self.h = 70
		self.x = x
		self.y = y
	def getPos(self):
		return (self.x,self.y)
	
		




