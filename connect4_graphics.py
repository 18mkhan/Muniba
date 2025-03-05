from pygame import *
#needed to set up pygame
init()
width = 800
height = 600
# creat a graphics window to draw to
screen = display.set_mode((width, height))
# variable use to end the program
endProgram = False

while endProgram == False:
	for e in event.get():
	    if e.type == QUIT:
		    endProgram = True
	screen.fill((0,0,0))
	# screen- is where we will be drawing to 
	# (31,182,255) is the colour of the rectangle
	# (50,50,700,500) is the co-ordinate of the rectangle
	# x,y,width,height
	
	draw.rect(screen, (31,182,255),(50,50,700,500))
	for x in range(16):
		
	draw.circle(screen, (255,255,255),(100,100),40)
	#show the newly drawn screen
	display.flip()
	#short delay to slow down the animation
	time.delay(5)
	
	
    
