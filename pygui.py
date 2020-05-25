import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    
    #for cactus
    for i in range(490,525):   #x axis
        for j in range(198,230): #yaxis
            if data[i, j] < 100:
                hit("up")
                return
    # Draw the rectangle for birds
    for i in range(490,525):   #x axis
        for j in range(170,205): #yaxis
            if data[i, j] == 171:
                hit("down")
                return
    
    return

if __name__ == "__main__":
    print("start after 5 secs")
    time.sleep(5)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
        
        # # Draw the rectangle for cactus
        # for i in range(490,525):   #x axis
        #     for j in range(198,230): #yaxis
        #         data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(490,525):   #x axis
        #     for j in range(170,190): #yaxis
        #         data[i, j] = 171

        # image.show()
        # break
      