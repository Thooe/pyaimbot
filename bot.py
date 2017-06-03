import pyautogui
import time
import win32api
#for i in pyautogui.getWindows():
#	print(i)
print("Starting in 3 seconds...")
time.sleep(3)
found = 0
notfound = 0
while(True):

	stuff = pyautogui.locateOnScreen('pixels/FF0013.png', region=(620, 320, 150, 170))
	if stuff == None:
		stuff = pyautogui.locateOnScreen('pixels/FF0012.png', region=(620, 320, 150, 170))
		if stuff == None:
			stuff = pyautogui.locateOnScreen('pixels/FF0014.png', region=(620, 320, 150, 170))
			if stuff != None:
				x, y = pyautogui.center(stuff)
				found = found + 1
				print(str(x)+" "+str(y))
				win32api.SetCursorPos((x,y))
				time.sleep(1)
			else: notfound = notfound + 1
	print("Found: "+str(found)+" Not Found:"+str(notfound))
#def coolStart(howLong, text):
#	while howLong>0:
#		print("Starting in {howLong} seconds...".format(int(howLong))
#		howLong = howLong-1
