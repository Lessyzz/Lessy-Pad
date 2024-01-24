from tkinter import *
import tkinter as tk
from tkinter import scrolledtext, filedialog

class LessyPad():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lessy Pad")
        self.root.config(background = "white")
        self.root.overrideredirect(True)
        self.root.geometry(f"300x160+{int(self.root.winfo_screenwidth() / 2 - 80)}+{int(self.root.winfo_screenheight() / 2 - 80)}")

        title_bar_F = Frame(self.root, background = "#F8D7FF", relief = "raised", bd = 0)
        title_bar_F.pack(fill = X)
        title_bar_F.bind("<B1-Motion>", self.move_app)

        title_bar_File = Menubutton(title_bar_F, text = "File", background = "#F8D7FF", foreground = "black", font = "Courier 8 bold")
        title_bar_File.pack(side = "left", padx = 5, pady = 3)

        file_menu = Menu(title_bar_File, tearoff = False)
        title_bar_File.config(menu = file_menu)

        file_menu.add_command(label = "New", command = self.new)
        file_menu.add_command(label = "Open", command = self.open)
        file_menu.add_command(label = "Save", command = self.save)
        file_menu.add_separator()
        file_menu.add_command(label = "Exit", command = self.exit)

        x_B = Button(title_bar_F, background = "#F8D7FF", foreground = "black", text = "X", font = "Courier 8 bold", bd = 0, command = self.root.destroy)
        x_B.pack(side = "right", padx = 10, pady = 3)

        title_bar_L = Label(title_bar_F, background = "#F8D7FF", foreground = "black", text = "LessyPad", font = "Courier 8 bold")
        title_bar_L.pack(side = "right", padx = 5, pady = 3)

        self.text = scrolledtext.ScrolledText(self.root, wrap = tk.WORD, width = 40, height = 10, background = "white", foreground = "black")
        self.text.pack(expand = True, fill = "both")

        self.root.mainloop()

    def move_app(self, e):
        self.root.geometry(f"+{e.x_root}+{e.y_root}")

    def new(self):
        self.text.delete(1.0, tk.END)

    def open(self):
        file = tk.filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("Text Files", "*.txt"), ("All Dosyalar", "*.*")])
        if file:
            with open(file, "r") as read_file:
                icerik = read_file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, icerik)

    def save(self):
        file = tk.filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as write_file:
                write_file.write(self.text.get(1.0, tk.END))

    def exit(self):
        self.root.destroy()

LessyPadRun = LessyPad()
