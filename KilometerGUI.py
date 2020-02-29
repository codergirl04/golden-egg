# Program Header
# CS 21B Intermediate Python Programming
# Maya Itty
# Lab 6
# 2/24/20

import tkinter
from tkinter import messagebox

# Function to create a window that takes the input from the user and pops up a
# dialog box with the equivalent distance in miles

class KilometerConverterGUI:
    def __init__(self):
        # create the root window
        self.main_window = tkinter.Tk()
        # create the label which prompts the user to enter a number
        self.label = tkinter.Label(self.main_window, text='Enter a kilometer '
                                                          'value to be '
                                                          'converted to miles')
        self.label.pack()
        # creates entry for user to enter a number
        self.entry = tkinter.Entry(self.main_window)
        self.entry.pack()
        # creates a button labeled "convert"
        # calls convert function while pressed
        self.convert_button = tkinter.Button(self.main_window, text='Convert',
                                             command=self.convert)
        self.convert_button.pack()
        # creates a button labeled "exit"
        # exits the program when pressed
        self.exit_button = tkinter.Button(self.main_window, text='Quit',
                                          command=exit)
        self.exit_button.pack()
        self.main_window.mainloop()

    # converts kilometers entered in entry to miles
    # converted value displayed in dialogue box
    def convert(self):
        try:
            kilometers = float(self.entry.get())
            if kilometers >= 0:
                miles = kilometers * 0.62137
                tkinter.messagebox.showinfo('Kilometers to Miles Converter',
                                            "%.2f kilometers is %.2f miles"
                                            % (kilometers, miles))
            else:
                tkinter.messagebox.showinfo('Error', "Invalid input")
        except ValueError:
            tkinter.messagebox.showinfo('Error', "Invalid input")


if __name__ == '__main__':
    k = KilometerConverterGUI()