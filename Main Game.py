from pygame import * 

#Pygame Initialization
init()
size = width, height = 800, 600
screen = display.set_mode(size)

#Color Initialization
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Fonts Initialization
fontHello = font.SysFont("HACKED", 30) 

#These image loading functions are here before the others because it is used to fill out time while other images loads
loading1 = image.load("loading1.png")
loading2 = image.load("loading2.png")
loading3 = image.load("loading3.png")
loading4 = image.load("loading4.png")
loading5 = image.load("loading5.png")

#This define function is in front of every other one because it is used to fill out loading time while other images get imported
def loading():
    screen.blit(loading1, (0, 0, 800, 600))
    time.wait(50)
    display.flip()
    screen.blit(loading2, (0, 0, 800, 600))
    time.wait(50)
    display.flip()
    screen.blit(loading3, (0, 0, 800, 600))
    time.wait(50)
    display.flip()
    screen.blit(loading4, (0, 0, 800, 600))
    time.wait(50)
    display.flip()
    screen.blit(loading5, (0, 0, 800, 600))
    time.wait(50)
    display.flip()    

#Loading in nessessary files such as images and sounds for mario moving right.
marioForward1 = image.load("FORWARD (1).png")
marioForward2 = image.load("FORWARD (2).png")
marioForward3 = image.load("FORWARD (3).png")
marioForward4 = image.load("FORWARD (4).png")
marioForward5 = image.load("FORWARD (5).png")
marioForward6 = image.load("FORWARD (6).png")
marioForward7 = image.load("FORWARD (7).png")
marioForward8 = image.load("FORWARD (8).png")
marioForward9 = image.load("FORWARD (9).png")
marioForward9 = image.load("FORWARD (9).png")
marioForwardList = [marioForward1, marioForward2, marioForward3, marioForward4, marioForward5, marioForward6, marioForward7, marioForward8, marioForward9]

#Loading in nessessary files such as images and sounds for mario moving left.
marioBackward1 = image.load("BACKWARD (1).png")
marioBackward2 = image.load("BACKWARD (2).png")
marioBackward3 = image.load("BACKWARD (3).png")
marioBackward4 = image.load("BACKWARD (4).png")
marioBackward5 = image.load("BACKWARD (5).png")
marioBackward6 = image.load("BACKWARD (6).png")
marioBackward7 = image.load("BACKWARD (7).png")
marioBackward8 = image.load("BACKWARD (8).png")
marioBackward9 = image.load("BACKWARD (9).png")
marioBackward9 = image.load("BACKWARD (9).png")
marioBackwardList = [marioBackward1, marioBackward2, marioBackward3, marioBackward4, marioBackward5, marioBackward6, marioBackward7, marioBackward8, marioBackward9]
loading()

#Loading in nessessary files such as images and sounds for eyes background for home screen.
menuBackground1 = image.load("eyesFrame (1).png")
menuBackground2 = image.load("eyesFrame (2).png")
menuBackground3 = image.load("eyesFrame (3).png")
menuBackground4 = image.load("eyesFrame (4).png")
menuBackground5 = image.load("eyesFrame (5).png")
menuBackground6 = image.load("eyesFrame (6).png")
menuBackground7 = image.load("eyesFrame (7).png")
menuBackground8 = image.load("eyesFrame (8).png")
menuBackground9 = image.load("eyesFrame (9).png")
menuBackground10 = image.load("eyesFrame (10).png")
menuBackground11 = image.load("eyesFrame (11).png")
menuBackground12 = image.load("eyesFrame (12).png")
menuBackground13 = image.load("eyesFrame (13).png")
menuBackground14 = image.load("eyesFrame (14).png")
menuBackground15 = image.load("eyesFrame (15).png")
menuBackground16 = image.load("eyesFrame (16).png")
menuBackground17 = image.load("eyesFrame (17).png")
menuBackgroundList = [menuBackground1, menuBackground2, menuBackground3, menuBackground4, menuBackground5, menuBackground6, menuBackground7, menuBackground8,
                      menuBackground9, menuBackground10, menuBackground11, menuBackground12, menuBackground13, menuBackground14, menuBackground15, menuBackground16, menuBackground17]
hackerFrame = image.load("hackerFrame.png")

#Loading in nessessary files such as images and sounds for home screen options and graphics.
compVirus = image.load("compVirus.png")
compVirusRed = image.load("compVirusRed.png")
compCrime = image.load("compCrime.png") 
compCrimeRed = image.load("compCrimeRed.png")
compQuit = image.load("compQuit.png")
compQuitRed = image.load("compQuitRed.png")
watchDogs2 = image.load("watchDogs2.png")
copyRight = image.load("copyRightText.png")

#Loading in nessessary files such as images and sounds for saving screen.
saveMain = image.load("saveMain.png")
saveYes = image.load("saveYes.png")
saveNo = image.load("saveNo.png")
saveCancel = image.load("saveCancel.png")
saveYesMouse = image.load("saveYesMouse.png")
saveNoMouse = image.load("saveNoMouse.png")
saveCancelMouse = image.load("saveCancelMouse.png")
loading()

#Loading in nessessary files such as images and sounds for ending scene.
crimeFrame1 = image.load("crimeFrame1.png")
crimeFrame2 = image.load("crimeFrame2.png")
crimeFrame3 = image.load("crimeFrame3.png")
crimeFrame4 = image.load("crimeFrame4.png")
crimeFrame5 = image.load("crimeFrame5.png")
crimeFrame6 = image.load("crimeFrame6.png")
crimeFrame7 = image.load("crimeFrame7.png")
crimeFrame8 = image.load("crimeFrame8.png")
crimeFrame9 = image.load("crimeFrame9.png")
crimeFrame10 = image.load("crimeFrame10.png")
crimeFrame11 = image.load("crimeFrame11.png")
crimeFrame12 = image.load("crimeFrame12.png")
crimeFrame13 = image.load("crimeFrame13.png")
crimeFrame14 = image.load("crimeFrame14.png")
crimeFrame15 = image.load("crimeFrame15.png")
crimeFrame16 = image.load("crimeFrame16.png")
crimeFrame17 = image.load("crimeFrame17.png")
crimeFrame18 = image.load("crimeFrame18.png")
crimeFrame19 = image.load("crimeFrame19.png")
crimeFrame20 = image.load("crimeFrame20.png")
crimeFrame21 = image.load("crimeFrame21.png")
crimeFrame22 = image.load("crimeFrame22.png")
crimeFrame23 = image.load("crimeFrame23.png")
crimeFrame24 = image.load("crimeFrame24.png")
crimeFrame25 = image.load("crimeFrame25.png")
crimeFrame26 = image.load("crimeFrame26.png")
crimeFrame27 = image.load("crimeFrame27.png")
crimeFrame28 = image.load("crimeFrame28.png")
crimeFrame29 = image.load("crimeFrame29.png")
crimeFrame30 = image.load("crimeFrame30.png")
crimeFrame31 = image.load("crimeFrame31.png")
crimeFrame32 = image.load("crimeFrame32.png")
crimeFrame33 = image.load("crimeFrame33.png")
crimeFrame34 = image.load("crimeFrame34.png")
crimeFrame35 = image.load("crimeFrame35.png")
crimeFrame36 = image.load("crimeFrame36.png")
crimeFrame37 = image.load("crimeFrame37.png")
crimeFrame38 = image.load("crimeFrame38.png")
crimeFrame39 = image.load("crimeFrame39.png")
crimeFrame40 = image.load("crimeFrame40.png")
crimeFrame41 = image.load("crimeFrame41.png")
crimeFrame42 = image.load("crimeFrame42.png")
crimeFrame43 = image.load("crimeFrame43.png")
crimeFrame44 = image.load("crimeFrame44.png")
crimeFrame45 = image.load("crimeFrame45.png")
crimeFrame46 = image.load("crimeFrame46.png")
crimeFrameList = [crimeFrame1, crimeFrame2, crimeFrame3, crimeFrame4, crimeFrame5, crimeFrame6, crimeFrame7, crimeFrame8, crimeFrame9,
                  crimeFrame10, crimeFrame11, crimeFrame12, crimeFrame13, crimeFrame14, crimeFrame15, crimeFrame16, crimeFrame17, crimeFrame18, crimeFrame19,
                  crimeFrame20, crimeFrame21, crimeFrame22, crimeFrame23, crimeFrame24, crimeFrame25, crimeFrame26, crimeFrame27, crimeFrame28, crimeFrame29,
                  crimeFrame30, crimeFrame31, crimeFrame32, crimeFrame33, crimeFrame34, crimeFrame35, crimeFrame36, crimeFrame37, crimeFrame38, crimeFrame39,
                  crimeFrame40, crimeFrame41, crimeFrame42, crimeFrame43, crimeFrame44, crimeFrame45, crimeFrame46]

#Loading in nessessary files such as images and sounds for crime screen background.
crimeBackground1 = image.load("crimeBackground (1).gif")
crimeBackground2 = image.load("crimeBackground (2).gif")
crimeBackground3 = image.load("crimeBackground (3).gif")
crimeBackground4 = image.load("crimeBackground (4).gif")
crimeBackground5 = image.load("crimeBackground (5).gif")
crimeBackground6 = image.load("crimeBackground (6).gif")
crimeBackground7 = image.load("crimeBackground (7).gif")
crimeBackground8 = image.load("crimeBackground (8).gif")
crimeBackground9 = image.load("crimeBackground (9).gif")
crimeBackground10 = image.load("crimeBackground (10).gif")
crimeBackground11 = image.load("crimeBackground (11).gif")
crimeBackground12 = image.load("crimeBackground (12).gif")
crimeBackground13 = image.load("crimeBackground (13).gif")
crimeBackground14 = image.load("crimeBackground (14).gif")
crimeBackground15 = image.load("crimeBackground (15).gif")
crimeBackground16 = image.load("crimeBackground (16).gif")
crimeBackground17 = image.load("crimeBackground (17).gif")
crimeBackground18 = image.load("crimeBackground (18).gif")
crimeBackground19 = image.load("crimeBackground (19).gif")
crimeBackground20 = image.load("crimeBackground (20).gif")
crimeBackground21 = image.load("crimeBackground (21).gif")
crimeBackground22 = image.load("crimeBackground (22).gif")
crimeBackground23 = image.load("crimeBackground (23).gif")
crimeBackground24 = image.load("crimeBackground (24).gif")
crimeBackground25 = image.load("crimeBackground (25).gif")
crimeBackground26 = image.load("crimeBackground (26).gif")
crimeBackground27 = image.load("crimeBackground (27).gif")
crimeBackground28 = image.load("crimeBackground (28).gif")
crimeBackground29 = image.load("crimeBackground (29).gif")
crimeBackground30 = image.load("crimeBackground (30).gif")
crimeBackground31 = image.load("crimeBackground (31).gif")
crimeBackground32 = image.load("crimeBackground (32).gif")
crimeBackgroundList = [crimeBackground1, crimeBackground2, crimeBackground3, crimeBackground4, crimeBackground5, crimeBackground6, crimeBackground7, crimeBackground8, crimeBackground9,
                  crimeBackground10, crimeBackground11, crimeBackground12, crimeBackground13, crimeBackground14, crimeBackground15, crimeBackground16, crimeBackground17, crimeBackground18, crimeBackground19,
                  crimeBackground20, crimeBackground21, crimeBackground22, crimeBackground23, crimeBackground24, crimeBackground25, crimeBackground26, crimeBackground27, crimeBackground28, crimeBackground29,
                  crimeBackground30, crimeBackground31, crimeBackground32]
loading()

def saveScreen():
    global home, virus, crime, running, menuCounter, menuSecondaryCounter, save
    screen.blit(saveMain, (0, 0, 800, 600))
    mx, my = (mouse.get_pos())
    if 250 < mx < 345 and 315 < my < 350:
        screen.blit(saveYesMouse, (0, 0, 800, 600))
    else:
        screen.blit(saveYes, (0, 0, 800, 600))
    if 355 < mx < 450 and 315 < my < 350:
        screen.blit(saveNoMouse, (0, 0, 800, 600))
    else:
        screen.blit(saveNo, (0, 0, 800, 600))
    if 457 < mx < 550 and 315 < my < 350:
        screen.blit(saveCancelMouse, (0, 0, 800, 600))
    else:
        screen.blit(saveCancel, (0, 0, 800, 600))
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            if 250 < mx < 345 and 315 < my < 350:
                running = False
            if 355 < mx < 450 and 315 < my < 350:
                running = False
            if 457 < mx < 550 and 315 < my < 350:
                save = False
            print("(%i, %i)" %(mx, my))    
#Defining function of homeScreen, which will print and edit the home screen when called
def homeScreen():
    global home, virus, crime, running, menuCounter, menuSecondaryCounter, save
    screen.blit(menuBackgroundList[menuCounter%16], (0, 0, 800, 600))
    screen.blit(hackerFrame, (0, 0, 800, 600))
    screen.blit(watchDogs2, (0, 0, watchDogs2.get_width(), watchDogs2.get_height()))
    screen.blit(copyRight, (0, 565, copyRight.get_width(), copyRight.get_height()))
    if menuSecondaryCounter == 3:
        menuCounter += 1
        menuSecondaryCounter = 0
    else:
        menuSecondaryCounter += 1
    mx, my = (mouse.get_pos())
    if 10 < mx < 385 and 140 < my < 205:
        text = fontHello.render ("COMPUTER VIRUS", 3, RED)
        screen.blit(compVirusRed, (0, 140, compVirusRed.get_width(), compVirusRed.get_height()))
    else:
        text = fontHello.render ("COMPUTER VIRUS", 3, BLACK)
        screen.blit(compVirus, (0, 140, compVirus.get_width(), compVirus.get_height()))
    if 10 < mx < 395 and 210 < my < 260:
        screen.blit(compCrimeRed, (0, 200, compCrimeRed.get_width(), compCrimeRed.get_height()))
    else:
        screen.blit(compCrime, (0, 200, compCrime.get_width(), compCrime.get_height()))
    if 10 < mx < 150 and 270 < my < 305:
        screen.blit(compQuitRed, (0, 260, compQuitRed.get_width(), compQuitRed.get_height()))
    else:
        screen.blit(compQuit, (0, 260, compQuit.get_width(), compQuit.get_height()))
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            if 10 < mx < 385 and 140 < my < 205:
                virus = True
                home = False
            if 10 < mx < 395 and 210 < my < 260:
                crime = True
                home = False
            if 10 < mx < 150 and 270 < my < 305:
                save = True
            print("(%i, %i)" %(mx, my))

#Defining function of Virus Screen, displaying information about virus
def virusScreen():
    global home, virus, crime, running
    draw.rect(screen, RED, (0, 0, 800, 600), 0)
    mx, my = (mouse.get_pos())
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            if 600 < mx < 800 and 0 < my < 200:
                print("COMPUTER VIRUS DETECTED")
                virus = False
                home = True
            print("(%i, %i)" %(mx, my))   

#Defining function of Crime Screen, displaying information about computer crimes.
def crimeScreen():
    global home, virus, crime, running, menuCounter, crimeCounter, crimeSecondaryCounter
    screen.blit(crimeBackgroundList[crimeCounter%32], (0, 0, 800, 600))
    if crimeSecondaryCounter == 10:
        crimeCounter += 1
        crimeSecondaryCounter = 0
    else:
        crimeSecondaryCounter += 1
    mx, my = (mouse.get_pos())
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            if 600 < mx < 800 and 0 < my < 200:
                print("COMPUTER VIRUS DETECTED")
                crime = False
                home = True
            print("(%i, %i)" %(mx, my)) 
    menuCounter += 1

#Defining function for moving mario, allowing it to move everytime the loop cycles.
def objectAnimation():
    global marioCounter, marioSecondaryCounter, marioClimb, marioPosX, lastDirection, running, save
    mx, my = (mouse.get_pos())
    if marioPosX < mx:
        lastDirection = "FORWARD"
        marioPosX += 1
        screen.blit(marioForwardList[marioCounter%9], (marioPosX - 100, 400 + marioCounter*2, marioForwardList[marioCounter%9].get_width(), marioForwardList[marioCounter%9].get_height()))
    elif marioPosX > mx:
        lastDirection = "BACKWARD"
        marioPosX -= 1
        screen.blit(marioBackwardList[marioCounter%9], (marioPosX - 100, 400 + marioCounter*2, marioBackwardList[marioCounter%9].get_width(), marioBackwardList[marioCounter%9].get_height()))
    else:
        if lastDirection == "FORWARD":
            screen.blit(marioForwardList[marioCounter%9], (marioPosX - 100, 400 + marioCounter*2, marioForwardList[marioCounter%9].get_width(), marioForwardList[marioCounter%9].get_height()))
        else:
            screen.blit(marioBackwardList[marioCounter%9], (marioPosX - 100, 400 + marioCounter*2, marioBackwardList[marioCounter%9].get_width(), marioBackwardList[marioCounter%9].get_height()))
    if marioSecondaryCounter == 5:
        marioCounter += marioClimb
        marioSecondaryCounter = 0
    else:
        marioSecondaryCounter += 1
    if marioCounter == 9:
        marioClimb = -1
    elif marioCounter == 0:
        marioClimb = 1

#Creation of variables for each stage of the while running loop
virus = False
crime = False
home = True
running = True
save = False

#Menu variables
menuCounter = 0
menuSecondaryCounter = 0
endCounter = 0

#Variables used in mario moving
lastDirection = "FORWARD"
marioSecondaryCounter = 0
marioCounter = 0
marioClimb = 1
marioPosX = 400
myClock = time.Clock()

#Variables used in crime screen
crimeCounter = 0
crimeSecondaryCounter = 0

# Game Loop
while running:
    if home == True and save == False:
        homeScreen()
        objectAnimation()
    elif virus == True:
        virusScreen()
    elif crime == True:
        crimeScreen()
    if save == True:
        saveScreen()
    for evnt in event.get():
        if evnt.type == KEYDOWN:
            print("HERE")
            key = pygame.event.poll()
            print(key)
    display.flip()
    myClock.tick(60)
    
while endCounter < 45:
    screen.blit(crimeFrameList[endCounter], (0, 0, 800, 600))
    endCounter += 1  
    display.flip()
    time.wait(30)
    myClock.tick(60)
quit()
