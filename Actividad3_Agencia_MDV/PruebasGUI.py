import tkinter
from tkinter import *
from tkinter import ttk 

class WindowGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Agencia de Viajes")
        self.window.geometry("800x500")

        # Add scrollbar
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Create canvas for scrolling
        self.canvas = Canvas(self.window, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Configure scrollbar to work with canvas
        self.scrollbar.config(command=self.canvas.yview)

        # Create a frame inside the canvas to hold all widgets
        self.frame = Frame(self.canvas, bg="#F8FFF7")
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        # Add widgets to the frame
        self.create_widgets()

    def create_widgets(self):
        #Title
        self.frame1 = Frame(self.frame, bg="black",  height=1)
        self.frame1.pack(fill = X, expand = False, side = TOP)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(0, weight=1)

        self.label1 = Label(self.frame1,
                      text="VIAJES DE SENDERISMO",
                      bg="black",
                      fg="#EE5C23",
                      font="Helvetica 16 bold italic")
        self.label1.grid(row=0, column=1,pady=10, sticky="nsew")

        #Image and text
        self.frame2 = Frame(self.frame, bg="#F8FFF7",  height=1)
        self.frame2.pack(fill = X, expand = False, side = TOP)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(2, weight=1)
        self.frame2.rowconfigure(0, weight=1)

        self.img1 = PhotoImage(file="hiking2.png") 

        self.label2 = Label(self.frame2,
                      image=self.img1, 
                      bg="#F8FFF7")
        self.label2.grid(row=0, column=1, pady=(20,0), sticky="nsew")

        self.label3 = Label(self.frame2,
            text="¡Explora la naturaleza con nosotros!",
            bg="#F8FFF7",
            fg="#EE5C23",
            font="Helvetica 13 bold italic")
        self.label3.grid(row=1, column=1, pady=5, sticky="nsew")

        #Form
        self.labelframe = LabelFrame(self.frame, text='Datos del excursionista', bg="#F8FFF7", fg="#EE5C23", font="Helvetica 13 bold italic")
        self.labelframe.pack(fill = X, expand = False, side = TOP, padx=10, pady=(20,0))

        self.frame3 = Frame(self.labelframe, bg="#F8FFF7")
        self.frame3.pack(fill = X, expand = False, side = TOP)

        self.entry1 = Entry(self.frame3, width=30)
        self.entry1.grid(row=0, column=0,padx=10, pady=(20,10), sticky="nw")
        leave(self.entry1, "Nombre")
        self.entry1.bind("<Button-1>", lambda event: click(self.entry1))
        self.entry1.bind("<Leave>", lambda event: leave(self.entry1, "Nombre"))
        
        self.entry2 = Entry(self.frame3, width=45)
        self.entry2.grid(row=0, column=1,padx=10, pady=(20,10), sticky="nw")
        leave(self.entry2, "Apellidos")
        self.entry2.bind("<Button-1>", lambda event: click(self.entry2))
        self.entry2.bind("<Leave>", lambda event: leave(self.entry2, "Apellidos"))

        self.combo = ttk.Combobox(self.frame3, width=27)
        self.combo['values'] = ("Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón")
        self.combo.current(0)
        self.combo.grid(row=0, column=2, padx=10, pady=(20,10), sticky="nw")

        self.frame4 = Frame(self.labelframe, bg="#F8FFF7")
        self.frame4.pack(fill = X, expand = False, side = TOP)

        self.entry3 = Entry(self.frame4, width=30)
        self.entry3.grid(row=0, column=0,padx=10, pady=(0,10), sticky="nw")
        leave(self.entry3, "Teléfono")
        self.entry3.bind("<Button-1>", lambda event: click(self.entry3))
        self.entry3.bind("<Leave>", lambda event: leave(self.entry3, "Teléfono"))
        
        self.entry4 = Entry(self.frame4, width=45)
        self.entry4.grid(row=0, column=1,padx=10, pady=(0,10), sticky="nw")
        leave(self.entry4, "Email")
        self.entry4.bind("<Button-1>", lambda event: click(self.entry4))
        self.entry4.bind("<Leave>", lambda event: leave(self.entry4, "Email"))
        
        self.labelframe2 = LabelFrame(self.window, text='Excursión', bg="#F8FFF7", fg="#EE5C23", font="Helvetica 13 bold italic")
        self.labelframe2.pack(fill = X, expand = False, side = TOP, padx=10, pady=(20,0))
        self.labelframe2.columnconfigure(0, weight=1)
        self.labelframe2.columnconfigure(1, weight=1)
        self.labelframe2.rowconfigure(0, weight=1)
        self.frame5 = Frame(self.labelframe2, bg="#F8FFF7")
        self.frame5.grid(row=0, column=0, sticky="nsew")
        
        self.label4 = Label(self.frame5,
                            text="Rutas",
                            bg="#F8FFF7",
                            fg="#EE5C23",
                            font="Helvetica 10 bold italic")
        self.label4.grid(row=0, column=0, padx=10, pady=(0, 10),  sticky="nw")
        
        self._rbtns_selected = tkinter.StringVar(value="Monte Abantos")
        self.radio1 = Radiobutton(self.frame5, text="Monte Abantos", variable= self._rbtns_selected, value=1, bg="#F8FFF7", font="Helvetica 10 italic")
        self.radio1.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.radio2 = Radiobutton(self.frame5, text="La Pedriza", variable= self._rbtns_selected, value=2, bg="#F8FFF7", font="Helvetica 10 italic")
        self.radio2.grid(row=2, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.radio3 = Radiobutton(self.frame5, text="Las dehesas de Cercedilla", variable= self._rbtns_selected, value=3, bg="#F8FFF7", font="Helvetica 10 italic")
        self.radio3.grid(row=3, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.radio4 = Radiobutton(self.frame5, text="La Cabrera-Pico de la Miel", variable= self._rbtns_selected, value=4, bg="#F8FFF7", font="Helvetica 10 italic")
        self.radio4.grid(row=4, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.frame6 = Frame(self.labelframe2, bg="#F8FFF7")
        self.frame6.grid(row=0, column=1, sticky="nsew")
        
        self.label5 = Label(self.frame6,
                            text="Accesorios",
                            bg="#F8FFF7",
                            fg="#EE5C23",
                            font="Helvetica 10 bold italic")
        self.label5.grid(row=0, column=0, padx=10, sticky="nw")
        
        self.check1 = Checkbutton(self.frame6, text="Mochila", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check1.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.check2 = Checkbutton(self.frame6, text="Linterna", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check2.grid(row=2, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.check3 = Checkbutton(self.frame6, text="GPS", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check3.grid(row=3, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.check4 = Checkbutton(self.frame6, text="Mapa", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check4.grid(row=4, column=0, padx=10, pady=(0,10), sticky="nw")
        
        self.check5 = Checkbutton(self.frame6, text="Prismáticos", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check5.grid(row=1, column=1, padx=10, pady=(0,10), sticky="nw")
        
        self.check6 = Checkbutton(self.frame6, text="Cantimplora", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check6.grid(row=2, column=1, padx=10, pady=(0,10), sticky="nw")
        
        self.check7 = Checkbutton(self.frame6, text="Botiquín", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check7.grid(row=3, column=1, padx=10, pady=(0,10), sticky="nw")
        
        self.check8 = Checkbutton(self.frame6, text="Crema Solar", bg="#F8FFF7", font="Helvetica 10 italic")
        self.check8.grid(row=4, column=1, padx=10, pady=(0,10), sticky="nw")
        
        self.window.mainloop()

def click(entry):
    entry.delete(0, END)
    entry.config(fg="black")

def leave(entry, hint):
    if not entry.get():
        entry.insert(0, hint)
        entry.config(fg="gray")

if __name__ == "__main__":
	root = tkinter.Tk()
	window = WindowGUI(root)