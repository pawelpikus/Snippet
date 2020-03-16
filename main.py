from file_manager import FileManager
from tkinter import *


class Snippet(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.search_var = StringVar()
        self.initUI()

    ##################################### MODEL #######################################################################
    def on_click_lbox(self, *args):
        """Append and display selected list item to label, copy text from label to system clipboard"""
        root.clipboard_clear()  # clear the system clipboard contents
        selection = self.lbox.curselection()
        seltext = self.lbox.get(selection).capitalize() + ". "  # get value by dict item ["text"] or .cget("text")
        seltext = self.lbl["text"] + seltext  # append selection to already displayed text
        self.lbl.configure(text=seltext)  # display text in label
        root.clipboard_append(seltext)  # add the label text to system clipboard

    def update_list(self, *args):
        search_term = self.search_var.get()
        self.lbox.delete(0, END)
        # reading file from snippet.txt
        snippets = FileManager.read_file()
        for item in snippets:
            if search_term.lower() in item.lower():
                self.lbox.insert(END, item)

    ######################################## VIEW ######################################################################
    def initUI(self):
        self.master.title('Snippet')
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(3, weight=1)
        # trace the changes in entry
        self.search_var.trace('w', self.update_list)

        entry = Entry(self, textvariable=self.search_var, width=15)
        entry.grid(sticky='W', pady=4, padx=5)

        self.lbox = Listbox(self)
        self.lbox.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky='E' + 'W' + 'S' + 'N')

        # binding to label
        self.lbox.bind('<ButtonRelease-1>', self.on_click_lbox)

        self.lbl = Label(self, height=15, width=60, justify="left", anchor='nw', wraplength=400)
        self.lbl.grid(row=5, column=0, columnspan=2, rowspan=4, padx=10, pady=10)

        # Buttons
        self.clear_btn = Button(self, text='CLEAR')
        self.clear_btn.grid(row=5, column=3, padx=10)

        # populate the Listbox
        self.update_list()


# main
root = Tk()
root.geometry("550x500+500+500")
app = Snippet(root)
app.mainloop()
