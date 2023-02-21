###COPYRIGHT NYKOLAÏ 2023###
#TODO:
# x Add image-button
# x Add sounds
#Additional content: 
# x bgm? 
# other sounds?
# Get nutella
############################

import os #Necessary to avoid issues later on; define main file as root directory.
def root_path():
    return os.path.abspath(os.sep)

import sys,pygame,random
from pygame import mixer
from pathlib import Path
pygame.init()
mixer.init()

font = pygame.font.SysFont(None, 24)
black =(0,0,0)
pygame.display.set_caption('Le funny catgorl')
size = width, height = 500, 500 #Size of window
center=(width/2,height/2)
IconSize=(250,250) #Size of each icon
bgcolor = 240, 180, 238 #Background color
screen = pygame.display.set_mode(size)

buttonNeutralColor=(100,20,200)
buttonHoverColor=(150,100,200)
buttonPressedColor=(50,15,75)

GloomyYay=pygame.image.load("Yay.png")
Yayimg=pygame.transform.scale(GloomyYay, IconSize)
button1rect=pygame.Rect(center[0]-(IconSize[0]/2)-10,center[1]-(IconSize[1]/2)-10,IconSize[0]+10,IconSize[0]+10)
button1Color=buttonNeutralColor

mixer.music.load('meowsome.mp3') #Owner of the music: The Living Tombstone
mixer.music.set_volume(0.5)
mixer.music.play(-1)

mouseCoord=pygame.mouse.get_pos() #Coordinate of cursor (x,y)
textCoord = font.render(str(mouseCoord),True,black)
textRect = textCoord.get_rect()
textRect.center = (100 // 2, 100 // 2)

bgm=font.render(str("BGM"),True,black,(255,0,0)) #bgm button
bgmRect=bgm.get_rect()
bgmRect.center=(50,450)
bgmRunning=True

soundList=os.listdir('Yay')
randSoundNumber=random.randint(0,len(soundList)-1)

pygame.display.set_icon(GloomyYay)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        if mouseCoord[0]>(center[0]-IconSize[0]/2) and mouseCoord[0]<center[0]+IconSize[0]/2 and mouseCoord[1]>(center[1]-IconSize[1]/2) and mouseCoord[1]<center[1]+IconSize[1]/2:
            button1Color=buttonHoverColor
        else:button1Color=buttonNeutralColor
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseCoord[0]>(center[0]-IconSize[0]/2) and mouseCoord[0]<center[0]+IconSize[0]/2 and mouseCoord[1]>(center[1]-IconSize[1]/2) and mouseCoord[1]<center[1]+IconSize[1]/2:
                if event.button == 1:
                    randSoundNumber=random.randint(0,len(soundList)-1)
                    soundFilePath=str("Yay/")+str(soundList[randSoundNumber])
                    YaySound=pygame.mixer.Sound(soundFilePath)
                    YaySound.set_volume(0.5)
                    YaySound.play()
                    button1Color=buttonPressedColor
                    print("YAY "+str(soundList[randSoundNumber]))
            if mouseCoord[0]>bgmRect[0] and mouseCoord[0]<bgmRect[0]+bgmRect[2] and mouseCoord[1]>bgmRect[1] and mouseCoord[1]<bgmRect[1]+bgmRect[3]:
                if event.button == 1:
                    if bgmRunning==True:
                        mixer.music.pause()
                        bgmRunning=False
                        print("Mute")
                    else:
                        mixer.music.unpause()
                        bgmRunning=True
                        print("Unmute")
    mouseCoord=pygame.mouse.get_pos()
    textCoord = font.render(str(mouseCoord),True,black)
    screen.fill(bgcolor)
    pygame.draw.rect(screen,button1Color,button1rect,10)
    screen.blit(Yayimg,(center[0]-IconSize[0]/2,center[1]-IconSize[1]/2))
    #screen.blit(textCoord, textRect)
    screen.blit(bgm, bgmRect)
    pygame.display.flip()