import tkinter as tk
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
def draw_point(canvas,point):
    rad=1
    canvas.create_oval(point.x,point.y,point.x+rad,point.y+rad,outline='black',fill='white')
root=tk.Tk()
root.title("Draw point")
canvas=tk.Canvas(root,width=500,height=100)
canvas.pack()
poin=Point(50,50)
draw_point(canvas,poin)
root.mainloop()