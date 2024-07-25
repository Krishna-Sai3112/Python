import tkinter as tk
class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
def draw_circle(canvas,circle):
    canvas.create_oval(circle.x,circle.y,circle.x+circle.radius,circle.y+circle.radius,outline='black',fill='Blue')
root=tk.Tk()
root.title("Draw circle")
canvas=tk.Canvas(root,width=500,height=200)
canvas.pack()
circ1=Circle(50,50,25)
circ2=Circle(100,80,30)
circ3=Circle(115,80,30)
draw_circle(canvas,circ1)
draw_circle(canvas,circ2)
draw_circle(canvas,circ3)
root.mainloop()