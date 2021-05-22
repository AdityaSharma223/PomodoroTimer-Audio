import time
import pygame
import math
import random 
import os
import sys
#---------------------------

#-----VARS--------------------
swidth, sheight = 300, 200 
run = True
s, m = 0, 0 
hours, minutes = map(int,input("""
Hi and welcome to PyTimer
Please type (in minutes) how long u want the time to be
here: """).split())
timel = hours*60 + minutes
#-----------------------------
#------PYGAME INIT------------
pygame.init()
window = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("STOPWATCH")
#-----------------------------

#------MAIN LOOP--------------
while run: 
	pygame.time.delay(60)

	time.sleep(1)
	if m!=(timel): 
		s+=1
		if s>59: 
			s=0
			m+=1

	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			run = False 
 
	if len(str(m))!=2 and len(str(s))!= 2: 
		t = "0" + str(m) + ":" + "0" + str(s)
	elif len(str(m))!=2: 
		t = "0" + str(m) + ":" + str(s)
	elif len(str(s))!=2: 
		t = str(m) + ":" + "0" + str(s)
	else: 
		t = str(m) + ":" + str(s)
	myfont = pygame.font.SysFont('Lucida Console', 60)
	timee = myfont.render(t, False, (255, 255, 255))
	window.fill((0,0,0))
	window.blit(timee,(70, 65))
	pygame.display.update()
#-------------------------------
pygame.quit()
