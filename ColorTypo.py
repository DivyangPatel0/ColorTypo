
import tkinter
import random

def main():
  # list of possible colour.
  global colours, timeleft, score
  
  colours = ['Red','Blue','Green','Pink','Black',
                  'Yellow','Orange','White','Purple','Brown']
  score = 0

  # the game time left, initially 30 seconds.
  timeleft = 30

  # function that will start the game.
  def startGame(event):
          
          if timeleft == 30:
                  # start the countdown timer.
                  countdown()
                  
          # run the function to
          # choose the next colour.
          nextColour()

  # Function to choose and
  # display the next colour.
  def nextColour():

          # use the globally declared 'score'
          # and 'play' variables above.
          global score
          global timeleft

          # if a game is currently in play
          if timeleft > 0:

                  # make the text entry box active.
                  e.focus_set()

                  # if the colour typed is equal
                  # to the colour of the text

                  #give score+10 if correct and -5 is incoorect answer
                  if e.get().lower() == colours[1].lower():
                          
                          score += 1
                          timeleft += 10
                  else :
                          if(timeleft <= 5):
                                timeleft = 0
                          else :
                                timeleft -= 5
 
                  # clear the text entry box.
                  e.delete(0, tkinter.END)
                  
                  random.shuffle(colours)
                  
                  # change the colour to type, by changing the
                  # text _and_ the colour to a random colour value44
                  instructions.destroy()
                  label.config(fg = str(colours[1]), text = str(colours[0]),font = ('Helvetica', 60), borderwidth=2, relief="sunken", bg = "#F7F9F9")
                  
                  # update the score.
                  scoreLabel.config(text = " Score: " + str(score)+" ")


  # Countdown timer function
  def countdown():

          global timeleft

          # if a game is in play
          if timeleft > 0:

                  # decrement the timer.
                  timeleft -= 1
                  
                  # update the time left label
                  timeLabel.config(text = "Time left: "+ str(timeleft))
                                                                  
                  # run the function again after 1 second.
                  timeLabel.after(1000, countdown)
          else :
                  
                  timeLabel.config(text = "Game Over!", bg = "#E74C3C")
                  e.destroy()

                  #Creating Restart button to play the game again calling func resetButton
                  B = tkinter.Button(root, text ="Restart?", bg="#A569BD", command = resetButton)
                  B.pack()


  def resetButton():
            #Clearing the current window and restarting the game
            root.quit()
            root.destroy()
            main()
          

  # Driver Code
  # create a GUI window
  global e, scoreLabel ,timeLabel ,label, instructions
  root = tkinter.Tk()

  # set the title
  root.title("ColorTypo")

  root.configure(background="#FF5733")
  #root.configure(background='grey')

  # set the size
  root.geometry("375x300")

  # add an instructions label
  instructions = tkinter.Label(root, text = "Type in the Color of the Text, \nand not the text!",font = ('Helvetica', 12),bg = "#FF5733",fg="black")
  instructions.pack()

  # add a score label
  scoreLabel = tkinter.Label(root, text = " Press Enter To Start! ",font = ('Helvetica', 12), borderwidth=2, relief="groove",bg="#2ECC71",fg ="white")
  scoreLabel.pack(pady = 10)

  # add a time left label
  timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft), font = ('Helvetica', 12), borderwidth=2, relief="sunken",bg="black",fg ="white")
                          
  timeLabel.pack(pady = 10)

  # add a label for displaying the colours
  label = tkinter.Label(root, text = "Ready?\n^.^" ,font = ('Helvetica', 20),bg = "#FF5733", fg ="white")
  label.pack(pady = 10)

  # add a text entry box for
  # typing in colours
  e = tkinter.Entry(root)

  # run the 'startGame' function
  # when the enter key is pressed
  root.bind('<Return>', startGame)
  e.pack()

  # set focus on the entry box
  e.focus_set()

  # start the GUI
  root.mainloop()

#starting the game
main()
