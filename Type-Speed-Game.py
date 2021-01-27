# importing the modules 
from tkinter import *
import random
 
# list of 8 colours
colours = ['Red','Blue','Green','Pink','Black',
           'White','Orange','Purple']

#intialising score 
score = 0
 
# timer starts at 40 
secondsleft = 40
 
# function to start 
def startGame(event):
     
    if secondsleft == 40:
         
        # countdown timer starts
        countdown()
         
    
    # going for next colour function
    nextColour()
 

# function to select next colour
def nextColour():
 
    # declare score and secondsleft globally
    global score
    global secondsleft
 
    # if a game is currently in play
    if secondsleft > 0:
 
        # make the text entry box active.
        entry.focus_set()
 
        
        # if the colour typed is equal to colour of the text
        if entry.get().lower() == colours[1].lower():
             
            score=score+1
 
        # clear the text entry box.
        entry.delete(0,END)
         
        random.shuffle(colours)
         
        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))
         
        # update the score.
        scoreLabel.config(text = "Score: " + str(score))
 
 
# Countdown timer function 
def countdown():
 
    global secondsleft
 
    # if a game is in play
    if secondsleft > 0:
 
        # decrement the timer.
        secondsleft=secondsleft-1
         
        # update the time left label
        timeLabel.config(text = "Seconds left: "
                               + str(secondsleft))
                                
        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
 
 
    

    
# Driver Code
 
# GUI window
root = Tk()
 
# title
root.title("TYPE SPEED TEST")
 
# size and background
root.geometry("900x600")
root.configure(background='Yellow')
 
# add an instructions label
instructions = Label(root, text = "Type in the colour "
                        "of the words and not the word text!",
                                      font = ('Times', 28),background="White", foreground="Black")
instructions.pack() 
 
# add a score label
scoreLabel = Label(root, text = "Press ENTER KEY to start",
                                      font = ('Times', 24),background="Orange", foreground="Brown")
scoreLabel.pack()
 
# add a luck label
luckLabel = Label(root, text = "GOOD LUCK!",
                                      font = ('Times', 24),background="Orange", foreground="Purple")
luckLabel.pack()
# add a time left label
timeLabel = Label(root, text = "Seconds left: " +
              str(secondsleft), font = ('Times', 24),background="Orange", foreground="Brown")
               
timeLabel.pack()
 
# add a label for displaying the colours
label = Label(root, font = ('Times', 100))
label.pack()
 
# add a text entry box for
# typing in colours
entry = Entry(root)
 
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
entry.pack()
 
# set focus on the entry box
entry.focus_set()
 
#quit command 

Button(root,text="quit",command=root.destroy).pack()

# start the GUI
root.mainloop()
