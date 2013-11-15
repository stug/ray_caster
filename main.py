import Tkinter


class Game(object):
    def __init__(self):
        self.top = Tkinter.Tk()
        self.canvas = Tkinter.Canvas(self.top, height=500, width=500, background='black')
        # self.thing = self.canvas.create_rectangle(50, 50, 100, 100, outline='blue')
        self.canvas.pack()

        self.counter = 0
        self.top.after(10, self.animate)
        self.top.mainloop()

    def animate(self):
        pass
        # self.canvas.move(self.thing, 1, 1)
        # self.canvas.update()
        # self.counter += 1
        # if self.counter < 400:
        #    self.top.after(10, self.animate())


if __name__ == '__main__':
    game = Game()
