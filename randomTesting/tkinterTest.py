import tkinter
import random

playing = False

tk = tkinter
counter = 0
def counter_label(label):
  def count():
    global counter
    if playing:
        counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
def togglePause(lbl):
    global playing
    if playing:
        playing = False
        lbl.config(text='Play')
    else:
        lbl.config(text='Pause')
        playing = True




root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
pauseBut = tk.Button(root, text='Pause', width=25)
pauseBut.config(command=togglePause(pauseBut))
button.pack()
pauseBut.pack()
root.mainloop()
