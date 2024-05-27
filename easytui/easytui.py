from key_getter import KeyGetter
import os
import time


class Size:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class KeyBind:
    def __init__(self, key: str, command=None):
        self._key = key
        self._command = command

    def setKey(self, key: str):
        self._key = key

    def setCommand(self, command: callable):
        self._command = command

    def runCommand(self):
        #self._command
        print(type(self._command))


class EasyTUI:
    def __init__(self):
        temp = os.get_terminal_size()
        self.screen_size = Size(temp.columns, temp.lines - 2)
        self.key_getter = KeyGetter()

        self.fps = 10  # default value

        self.panes = []
        self.pixels = []
        self.keybinds = {
            'q': lambda: exit(0),
            'p': self.pause,
        }

        for y in range(0, self.screen_size.y):
            row = []
            for x in range(0, self.screen_size.x):
                row.append(" ")
                #self.pixels[(y * self.screen_size.y) + x] = ' '
                #print((y * self.screen_size.y) + x)
            self.pixels.append(row)
        print(self.screen_size.y * self.screen_size.x)
        print(f"{self.screen_size.x}, {self.screen_size.y}")
            #self.pixels[self.screen_size.y * x - 1] = "X"

        self.horz = 45
        self.count = 0
        #self.mainloop()

    def updatePanes(self):
        for pane in self.panes:

            pane.renderPane()

    def render(self):
        self.updatePanes()
        screen = ""
        for y in self.pixels:
            for x in y:
                screen += x
            screen += "\n"
        #for y in range(0, self.screen_size.y):
        #    for x in range(0, self.screen_size.x):
        #        screen += self.pixels[(y * self.screen_size.y) + x]
        #    screen += "\n"
        print(screen)

    def mainloop(self):
        while True:
            if self.key_getter.kbhit():
                input = self.key_getter.getch(False)
                print(input)
                if input in self.keybinds:
                    (self.keybinds[input])()
                    exit()
            self.render()
            self.count += 1
            time.sleep(1 / self.fps)

    def pause(self):
        print("paused, enter to resume")
        input()
        self.mainloop()


class Pane(EasyTUI):
    def __init__(self, master: EasyTUI, x = None, y = None, width = None, height = None):
        # defaults to filling entire master TUI screen
        if x is None or type(x) != int:
            self.posx = 0
        else:
            self.posx = x
        if y is None or type(y) != int:
            self.posy = 0
        else:
            self.posy = y
        if width is None or type(width) != int:
            self.width = master.screen_size.x
        else:
            self.width = width
        if height is None or type(height) != int:
            self.height = master.screen_size.y
        else:
            self.height = height
        self.pixels = master.pixels

    def renderPane(self):
        for y in range(self.posy, self.posy + self.height):
            for x in range(self.posx, self.posx + self.width):
                self.pixels[y][x] = 'X'
        #print(self.pixels)


#    def render(self):
#        count = 0
#        screen = "\n"
#        for y in range(0, self.screen_size.y):
#            t = 0
#            for x in range(0, self.screen_size.x):
#                #screen += str(t)
#                if y == self.horz:
#                    screen += "X"
#                else:
#                    screen += str(" ")
#                #if t == 0:
#                #    t = 1
#                #else:
#                #    t = 0
#            screen += "\n"
#            count += 1
#        print(screen)


# TESTING
if __name__ == "__main__":
    tui = EasyTUI()
    pane = Pane(tui, x=5, y=5, width=10, height=10)
    #pane = Pane(tui)
    tui.panes.append(pane)
    tui.mainloop()
