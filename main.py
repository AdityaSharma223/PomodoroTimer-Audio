import time
import pygame
from playsound import playsound
#---------------------------

#-----VARS--------------------
swidth, sheight = 300, 200
run = True
s, m = 0, 0
rest = False
work, breaka = map(int,input("""
Please type work time and break time(in minutes) separated by a space
here: """).split())
#-----------------------------

#------PYGAME INIT------------
pygame.init()
window = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("POMO TIMER")
#-----------------------------

#------MAIN LOOP--------------
while run:
	pygame.time.delay(60)

	time.sleep(1)
	if rest == False:
		if m!=(work):
			s+=1
			if s>59:
				s=0
				m+=1
		else:
			rest = True
			playsound(r"alarm.wav")
			m, s = 0, 0
	else:
		if m!=(breaka):
			s+=1
			if s>59:
				s=0
				m+=1
		else:
			rest = False
			playsound(r"alarm.wav")
			m, s = 0, 0

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
