import tkinter
canvaSize = 900, 800
canvas = tkinter.Canvas(width=canvaSize[0], height=canvaSize[1])
canvas.pack()
canvas.create_oval(145, 50, 260, 200, fill="#148818")
canvas.create_rectangle(165, 175, 230, 300, fill="#432B07")
 
def stromky(x,y):
    canvas.create_oval(x,50,260,y)
    canvas.create_rectangle(x+20,175,230,y+100)

x1 = int(input("Zadej souřadnici x1: "))
y1 = int(input("Zadej souřadnici y1: "))

canvas.create_rectangle (x1 + 115 // 2 + 30, y1 + 125, x1 + 30, y1 + 250, fill="#432B07")
canvas.create_oval (x1, y1, x1 + 115, y1 + 150, fill="#148818")

canvas.mainloop()