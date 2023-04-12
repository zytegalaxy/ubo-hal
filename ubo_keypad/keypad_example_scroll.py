import time
import os
import sys

SDK_HOME_PATH = os.path.dirname(os.path.abspath(__file__)) + '/../'
sys.path.append(SDK_HOME_PATH)

from display.lcd import LCD as LCD
from ubo_keypad import * # Might have to revisit this form of import

#initialize LCD and Keypad
lcd = LCD()

class mykeypad(KEYPAD):
    listIndex = 0
    def __init__(self, *args, **kwargs):
        super(mykeypad, self).__init__(*args, **kwargs)
        self.test_result  = False

    def button_event(self):        
        self.logger.debug(self.buttonPressed)
        
        if self.buttonPressed == "0":
            items[self.listIndex][1]()
        if self.buttonPressed == "1":
            items[self.listIndex + 1][1]()
        if self.buttonPressed == "2":
            items[self.listIndex + 2][1]()
        if self.buttonPressed == "up":
            if self.listIndex > 0:
                self.listIndex -= 1
        if self.buttonPressed == "down":        
            if self.listIndex < 5:
                self.listIndex += 1
            
        displayItems(self.listIndex)


def action1():
    item = "Item1"
    print(item + " was pressed")

def action2():
    item = "Item2"
    print(item + " was pressed")

def action3():
    item = "Item3"
    print(item + " was pressed")

def action4():
    item = "Item4"
    print(item + " was pressed")

def action5():
    item = "Item5"
    print(item + " was pressed")

def action6():
    item = "Item6"
    print(item + " was pressed")

def action7():
    item = "Item7"
    print(item + " was pressed")

def action8():
    item = "Item8"
    print(item + " was pressed")


items = (("Item 1", action1), 
         ("Item 2", action2), 
         ("Item 3", action3), 
         ("Item 4", action4), 
         ("Item 5", action5),
         ("Item 6", action6), 
         ("Item 7", action7), 
         ("Item 8", action8)) 

def displayItems(i):
        lcd.show_menu(title="scroll", menu_items=[items[i][0],
                                                  items[i+1][0],
                                                  items[i+2][0]])

def main():

    try:
        keypad = mykeypad()
    except:
        # did not detect keypad on i2c bus
        print("failed to initialize keypad")

    index = 0
    displayItems(index)
    while (1): 
        time.sleep(1)
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(0)


