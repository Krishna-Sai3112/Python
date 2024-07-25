import tkinter as tk
class Rect:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
def draw_rectangle(canvas,rect):
    canvas.create_rectangle(rect.x,rect.y,rect.x+rect.width,rect.y+rect.height,outline='blue',fill='red')
root=tk.Tk()
root.title("Draw rectangle")
canvas=tk.Canvas(root,width=500,height=100)
canvas.pack()
recta=Rect(50,50,300,50)
draw_rectangle(canvas,recta)
root.mainloop()