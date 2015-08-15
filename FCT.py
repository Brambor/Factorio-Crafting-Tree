import os
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("FCT")#název okna
bg_color = (255, 255, 255)



files = os.listdir("pic")

savefile = open("save.txt", "r")

save = savefile.read().split("\n")
saves = {name:(int(x), int(y)) for name, x, y in [line.split(",") for line in save]}
#print(saves)

pics = pygame.sprite.Group()
for i in files:
	name, format = i.split(".")
	if format == "png":
		x, y = 0, 0
		if name in saves:
			#print(name)
			x, y = saves[name]
		pic = pygame.sprite.Sprite()
		pic.name = name
		pic.image = pygame.image.load("pic/" + i).convert_alpha()
		pic.rect = pic.image.get_rect()
		pic.rect.topleft = (x, y)
		pics.add(pic)
	elif name != "Thumbs":
		#print(name)
		print("WRONG FORMAT OF PICTURE, ACCEPTING ONLY PNG")
savefile.close()
#pic = pygame.sprite.Sprite()


craftfile = open("crafting.txt", "r").read().split("\n")
#crafting = []
#for i in craftfile.read().split("\n"):
#	crafting.append([i.split(": ")])
#print(crafting)
crafting = {}
for craftit in craftfile:
	name, recipe = craftit.split(": ")
	crafting[name] = recipe.split(" + ")
#print(crafting)
#for i in range(len(files)):
#	files[i], x = files[i].split(".")
#	files[i] += ": "
#crafting = open("crafting.txt", "w")
#crafting.write("\n".join(files))
#crafting.close()
name = "Copper plate"
speedx, speedy = 0, 0
while True:
	pygame.time.Clock().tick(60)
	for pic in pics:
		if pic.name == name:
			x, y = pic.rect.topleft
	for event in pygame.event.get():
		if pygame.mouse.get_pressed()[0]:
			pos = pygame.mouse.get_pos()
			for pic in pics:
				if pic.rect.left < pos[0] and pic.rect.right > pos[0] and pic.rect.top < pos[1] and pic.rect.bottom > pos[1]:
					name = pic.name
					x, y = pic.rect.topleft
					print(name)
					break
		
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			saveit = []
			for pic in pics:
				saveit.append(",".join([pic.name, str(pic.rect.left), str(pic.rect.top)]))
			save = open("save.txt", "w")
			save.write("\n".join(saveit))
			save.close()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
#			print("Got DOWN")
			if event.key == pygame.K_LEFT:
				speedx -= 1
			if event.key == pygame.K_RIGHT:
				speedx += 1
			if event.key == pygame.K_UP:
				speedy -= 1
			if event.key == pygame.K_DOWN:
				speedy += 1
			if event.key == 110: #n
				nextone = False
				for pic in pics:
					if nextone:
						name = pic.name
						x, y = pic.rect.topleft
						nextone = False
						break
					if pic.name == name:
						nextone = True
				if nextone:
					for pic in pics:
						name = pic.name
						x, y = pic.rect.topleft
						break
				print(name)
			if event.key == 115: #s
				fname = input("set name to: ")
				for pic in pics:
					if fname == pic.name:
						print("found")
						name = fname
						x, y = pic.rect.topleft


		elif event.type == pygame.KEYUP:
#			print("Got UP")
			if event.key == pygame.K_LEFT:
				speedx += 1
			if event.key == pygame.K_RIGHT:
				speedx -= 1
			if event.key == pygame.K_UP:
				speedy += 1
			if event.key == pygame.K_DOWN:
				speedy -= 1
	x, y =  x + speedx, y + speedy
	for pic in pics:
		if pic.name == name:
			pic.rect.topleft = (x, y)

	screen.fill(bg_color)
	for pic in pics:
		if pic.name in crafting:
			points = crafting[pic.name]
			start = pic.rect.center
			for morepic in pics:
				if morepic.name in points:
					pygame.draw.line(screen, (0, 0, 0), start, morepic.rect.center, 2)

#					Surface, color,		start_pos, end_pos, width=1
#	pygame.draw.line(screen, (0, 0, 0), (0, 0), (50, 50), 2) # myline
#	pygame.draw.lines(screen, (0, 0, 0), False, [(100,100), (150,200), (200,100)], 1) #V
	pics.draw(screen)

	pygame.display.update()

input()
