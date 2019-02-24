#this tool loads a list of three columns and tests them, depending on their level. Success increases the level by 1, not succssful reduces it to 1. All is stored in a CSV file.
#v2 added request from 6 to 1, wheareas values that drop to 1 will be repeated again
#v2 proper distance by using 2**(n-1) for calculating the distance
#v2 


import random, time, os

def importing(filename): #this function takes a file of the given name, located in the same folder as the script and splits its three columns into three groups called "clue", "target" and "level"
    #loads the vocabulary file
    vocFile = open(".\\" + filename + ".csv")
    vocText = vocFile.read()
    vocFile.close()
   #teilt den Text von vocText (split) in einzelne Zeilen (lines()) und löscht die erste Zeile(Titel) sowie die letzte Zeile falls sie leer ist
    lines = vocText.split("\n")
    del lines[0]
    if lines[-1]== "":
        del lines[-1]
    #jede Zeile wird entlang des ";" aufgeteilt und der Wert der Liste german und french zugeschrieben
    a = 0
    for x in range(len(lines)):
        x = lines[a]
        z = x.split(";")
        clu = z[0]
        tar = z[1]
        lev = z[2]
        clue.append(clu)
        target.append(tar)
        level.append(lev)
        a = a + 1

def daytest(levelnr): #this function takes the level(1-6) and calculates the appropriate distance for testing. If the current day is properly divisible by this distance, it executes a test-all-for-x-search
    dist = 2**(int(levelnr) - 1) #calculates on what day the level should be tested (1, 2, 4, 8, 16, 32)
    if dist > 31: #falls die Distanz ein Monat überschreitet (mehr als 31, setzte es auf 29)
        dist = 29
    if (int((time.strftime("%d"))) % dist) == 0: #tests if day is evenly divisible by the distance value
        print("Today is the " + str(time.strftime("%d")) + ". Time for testing level " + str(levelnr) + "!")
        testallforx(levelnr)
    else:
        print("Not a testday for level " + str(levelnr) + " today\n")

def testallforx(lev): #this function tests all the values if they have level x and executes testing if found
    print("Now searching for level " + str(lev) + "...\n")
    a = 0
    for x in range (len(level)):
        x = level[a]
        if int(x) == int(lev):
            testing(a)
        a = a + 1

def testing(indexnr): # this function takes an index value (integer) and tests the user on it. If correct: level +1, if not back to level 1
    print("The clue is »" + str(clue[indexnr]) + "«")
    check = input()
    if check == str(target[indexnr]): # compare input to index
        print("Correct! Level up!\n")
        level[indexnr] = int(level[indexnr]) + 1
    else:
        while True: # gives correct solution until it is repeted correctly
            print("Not correct! Back to level 1\nThe target was »" + str(target[indexnr]) + "«\n Repeat!")
            level[indexnr] = 1
            check2 = input()
            if check2 == str(target[indexnr]):
                print("Yes, that's correct!\n")
                break

def exporting(col1, col2, col3): #exports the three groups as three columns in a csv file
    """if os.path.exists(".\\update.csv") == False: #checks if updatee file exists, else creates one
        listFile = open(".\\update.csv", "w")
        listFile.write("clue;target;level\n")
        listFile.close()"""

    listFile2 = open(".\\shoebox.csv", "w") # records result in update file
    listFile2.write("clue;target;level\n")
    b = 0
    for x in range (len(level)):
        x = str(col1[b]) + ";" + str(col2[b]) + ";" + str(col3[b])
        listFile2.write(x+"\n")
        b = b + 1
    listFile2.close()

def adding(): #ugly! function is here for requesting and adding does to much without parameters
    while True:
        print("What is the Clue? (enter »exit« to quit)")
        clueimp = input()
        if clueimp == "exit":
            break
        print("What is the Target?")
        targetimp = input()
        listFile = open(".\\shoebox.csv", "a") # adds entry to the shoebox.csv
        x = str(clueimp) + ";" + str(targetimp) + ";1"
        listFile.write(x+"\n")
        listFile.close()    

#set up list of clue, target and level
clue = []
target = []
level = []
print("Choose ADD or GO")
choice = input()
if choice == "GO":
    importing("shoebox")
    for x in range (6, 0, -1):
        daytest(x)
    exporting(clue, target, level)
elif choice == "ADD":
    adding()
