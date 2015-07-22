import os
import pygame
import inspect


pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("2048")#název okna
pygame.display.set_mode
clock = pygame.time.Clock()
bg_color = (50, 50, 50)

files = os.listdir("pic")

pic = []
for i in files:
	print(i)
	x, format = i.split(".")
	if format == "png":
		pic.append(pygame.image.load("pic\Copper cable.png"))
	else:
		print("WRONG FORMAT OF PICTURE, ACCEPTING ONLY PNG")
#pic = pygame.sprite.Sprite()
pic_rect = pic[0].get_rect()

craftfile = open("crafting.txt", "r")
crafting = []
for i in craftfile.read().split("\n"):
	crafting.append([i.split(": ")])
print(crafting)

#for i in range(len(files)):
#	files[i], x = files[i].split(".")
#	files[i] += ": "
#crafting = open("crafting.txt", "w")
#crafting.write("\n".join(files))
#crafting.close()

a = 0
while True:
	clock.tick(60)

	screen.fill(bg_color)
	screen.blit(pic[0], pic_rect)

	pygame.display.update()

input()