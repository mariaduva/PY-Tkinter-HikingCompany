import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk 

class WindowGUI:
	def __init__(self, window):
		self.window = window
		self.window.title("Agencia de Viajes")
		self.window.geometry("800x700+300+10")
		self.window['background']='#F8FFF7'
		self.create_widgets()

		
	def create_widgets(self):
		#Title
		self.frame = Frame(self.window, bg="black",  height=1)
		self.frame.pack(fill = X, expand = False, side = TOP)
		self.frame.columnconfigure(0, weight=1)
		self.frame.columnconfigure(2, weight=1)
		self.frame.rowconfigure(0, weight=1)

		self.label1 = Label(self.frame,
						text="VIAJES DE SENDERISMO",
						bg="black",
						fg="#EE5C23",
						font="Helvetica 16 bold italic")
		self.label1.grid(row=0, column=1,pady=10, sticky="nsew")

		#Image and text
		self.frame2 = Frame(self.window, bg="#F8FFF7",  height=1)
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

		#Form > Datos del excursionista
		self.labelframe = LabelFrame(self.window, text='Datos del excursionista', bg="#F8FFF7", fg="#EE5C23", font="Helvetica 13 bold italic")
		self.labelframe.pack(fill=X, expand=False, side=TOP, padx=10, pady=(20,0))

		def create_entry_frame(frame, text, pos, values=None):
			if values is not None:
				combo = ttk.Combobox(frame, width=27)
				combo['values'] = values
				combo.current(0)
				combo.grid(row=0, column=pos, padx=10, pady=(20, 10), sticky="nw")
				return combo
			entry = Entry(frame, width=30 if values is None else 27)
			entry.grid(row=0, column=pos, padx=10, pady=(20, 10), sticky="nw")
			entry.insert(0, text)
			entry.bind("<FocusIn>", lambda event: click(entry))
			return entry

		self.frame3 = Frame(self.labelframe, bg="#F8FFF7")
		self.frame3.pack(fill=X, expand=False, side=TOP)
  
		self.entryName = create_entry_frame(self.frame3, "Nombre", 0)
		self.entrySurname = create_entry_frame(self.frame3, "Apellidos", 1)
		self.combo = create_entry_frame(self.frame3, "Ciudad", 2, ("Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón"))

		self.frame4 = Frame(self.labelframe, bg="#F8FFF7")
		self.frame4.pack(fill=X, expand=False, side=TOP)

		self.entryTlf = create_entry_frame(self.frame4, "Teléfono", 0)
		self.entryEmail = create_entry_frame(self.frame4, "Email", 1)

		#Form > Ruta y accesorios
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

		OPTIONS = [("Monte Abantos", 1),("La Pedriza", 2),("Las dehesas de Cercedilla", 3),("La Cabrera-Pico de la Miel", 4)]

		self._rbtns_selected = tkinter.StringVar(value=OPTIONS[0][0])

		for option_text, option_value in OPTIONS:
			Radiobutton(
			self.frame5, text=option_text, variable=self._rbtns_selected, 
			value=option_text, bg="#F8FFF7", font="Helvetica 10 italic"
			).grid(row=option_value, column=0, padx=10, pady=(0,10), sticky="nw")

		self.frame6 = Frame(self.labelframe2, bg="#F8FFF7")
		self.frame6.grid(row=0, column=1, sticky="nsew")

		self.label5 = Label(self.frame6,
			text="Accesorios",
			bg="#F8FFF7",
			fg="#EE5C23",
			font="Helvetica 10 bold italic")
		self.label5.grid(row=0, column=0, padx=10, sticky="nw")

		self.items = ["Mochila", "Linterna", "GPS", "Mapa", "Prismáticos", "Cantimplora", "Botiquín", "Crema Solar"]

		self.accessories_vars = []

		# create the Checkbutton widgets and add them to the list
		for i, item in enumerate(self.items):
			var = BooleanVar()  # create a BooleanVar for each Checkbutton
			check = Checkbutton(self.frame6, text=item, bg="#F8FFF7", font="Helvetica 10 italic", variable=var)
			check.grid(row=i % 4 + 1, column=i // 4, padx=10, pady=(0,10), sticky="nw")
			self.accessories_vars.append(var)  # add the variable to the list

		#Listbox and button
		self.frame7 = Frame(self.window, bg="#F8FFF7")
		self.frame7.pack(fill = X, expand = False, side = TOP, padx=10, pady=(20,0))

		self.button1 = Button(self.frame7, text="Reservar", bg="#EE5C23", fg="#F8FFF7", font="Helvetica 10 bold italic", command=self.add_item_to_listbox)
		self.button1.pack(fill = X, expand = False, side = TOP, padx=10, pady=(0,10))
  
		self.scrollbar = Scrollbar(self.frame7)
		self.scrollbar.pack(side=RIGHT, fill=Y)
  
		self.listbox = Listbox(self.frame7, yscrollcommand=self.scrollbar.set, bg="#F8FFF7", font="Helvetica 10 italic")
		self.listbox.pack(fill = X, expand = False, side = TOP, padx=10, pady=(20,10))
		self.scrollbar.config(command=self.listbox.yview)
  
		self.window.mainloop()

	def add_item_to_listbox(self):
		boolean = validate_enrtries(self)
		if boolean:
			name = self.entryName.get()
			surname = self.entrySurname.get()
			email = self.entryEmail.get()
			tlf = self.entryTlf.get()
			city = self.combo.get()
			route = self._rbtns_selected.get()
			accessories = getChekboxes(self)
			self.listbox.insert(END, f"{name} {surname} - {tlf} - {email} - {city} - {route} - {accessories}")
			reset(self)


def reset(self):
		#reset entries
		ENTRIES = [(self.entryName, "Nombre"), (self.entrySurname, "Apellidos"), (self.entryTlf, "Teléfono"), (self.entryEmail, "Email")]
		for entry, hint in ENTRIES:
			entry.delete(0, END)
			entry.insert(0, hint)

		#reset combo
		self.combo.current(0)
		
		#reset radio buttons
		self._rbtns_selected.set("Monte Abantos")

		#reset checkboxes
		for widget in self.frame6.winfo_children():
			if isinstance(widget, Checkbutton):
				widget.deselect()	


def click(entry):
	entry.delete(0, END)
	entry.config(fg="black")

def leave(entry, hint):
	if not entry.get():
		entry.insert(0, hint)
		entry.config(fg="gray")

#Create function to validate entries
def validate_enrtries(self):
	if not self.entryName.get() or not self.entrySurname.get() or not self.entryTlf.get() or not self.entryEmail.get() or self.entryName.get() == "Nombre" or self.entrySurname.get() == "Apellidos" or self.entryTlf.get() == "Teléfono" or self.entryEmail.get() == "Email":
		messagebox.showerror("Error", "No se han rellenado todos los campos")
		return False
	return True

def getChekboxes(self):
	accessories = []
	for var, item in zip(self.accessories_vars, self.items):
		if var.get():
			accessories.append(item)
	return accessories

if __name__ == "__main__":
	root = tkinter.Tk()
	window = WindowGUI(root)