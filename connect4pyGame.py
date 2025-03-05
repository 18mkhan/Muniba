from pygame import *
# needed to set up pygame
grid=[["B","B","B","B","B","B","B"],
      ["B","B","B","B","B","B","B"],
      ["B","B","B","B","B","B","B"],
      ["B","B","B","B","B","B","B"],
      ["B","B","B","B","B","B","B"]]
init()
width = 800
height = 600
screen = display.set_mode((width, height))
endProgram = False
Playerturn="R"
colchosen=-1
while endProgram == False:
	for e in event.get():
		if e.type == QUIT: 
			endProgram = True
		if e.type==KEYDOWN:
			if e.key==K_1:
				print("1 was pressed")
				colchosen=0
			elif e.key==K_2:
				print("2 was pressed")
				colchosen=1
			elif e.key==K_3:
				print("3 was pressed")
				colchosen=2
			elif e.key==K_4:
				print("4 was pressed")
				colchosen=3
			elif e.key==K_5:
				print("5 was pressed")
				colchosen=4
			elif e.key==K_6:
				print("6 was pressed")
				colchosen=5
			elif e.key==K_7:
				print("7 was pressed")
				colchosen=6
	
		if colchosen!=-1:
			row=4
			placed=False
			while row>=0 and placed==False:
				if grid[row][colchosen]=="B":
					grid[row][colchosen]=Playerturn
					placed=True
				row=row-1
			colchosen=-1
			if placed ==False:
				print("error,that column is full")
			else:
				if Playerturn=="R":
					Playerturn="Y"
				else:
					Playerturn="R"
					
				
			
			
	
	screen.fill((0,0,0))
	# screen - is where we will be drawing to
	# (31,182,255) is the colour of the rectangle.
	# (50,50,700,500) is the co-ordinates of the rectangle 
	# x,y ,width, height
	draw.rect(screen, (31,182,255),(50,50,700,500))
	
	row=0
	while row<5:
		col=0
		y=(100*row)+100
		while col<7:
			x=(100*col)+100
			if grid[row][col]=="B":
				draw.circle(screen, (255,255,255), (x,y),40)
			elif grid[row][col]=="R":
				draw.circle(screen, (255,0,0), (x,y),40)
			else: 
				draw.circle(screen, (225,255,0), (x,y),40)
			col=col+1
		row=row+1
		

		
		
	# show the newly drawn screen.
	display.flip()
	# short delay to slow down animation.
	time.delay(5)
