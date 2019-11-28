from tkinter import *


class Application(Frame):

	def __init__(self, master):
		super().__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self, text="BMSCE CANTEEN").grid(row=0, column= 2, columnspan=10)
		Label(self, text="Item-Price").grid(row=1, column= 0, columnspan=5, sticky =W)
		Label(self, text="Quantity").grid(row=1, column= 2, columnspan=5, sticky =W)
		Label(self, text="Order").grid(row=1, column= 4, columnspan=5, sticky =W)
		Button(self, text="Place Order", command= self.price).grid(row = 7, column = 0, sticky =W)
		
		Label(self, text="Idli Rs10/-").grid(row=2, column= 0, columnspan=5, sticky =W)
		self.q_idli = Entry(self)
		self.q_idli.grid(row = 2, column = 2, columnspan=5, sticky = W)
		self.idli = BooleanVar()
		Checkbutton(self, variable = self.idli).grid(row = 2, column= 4, columnspan=5)

		Label(self, text="Vada Rs15/-").grid(row=3, column= 0, columnspan=5, sticky =W)
		self.q_vada = Entry(self)
		self.q_vada.grid(row = 3, column = 2, columnspan= 5, sticky = W)
		self.vada = BooleanVar()
		Checkbutton(self, variable = self.vada).grid(row = 3, column = 4, columnspan=5, stick = W)

		Label(self, text="Dosa Rs25/-").grid(row=4, column= 0, columnspan=5, sticky =W)
		self.q_dosa = Entry(self)
		self.q_dosa.grid(row = 4, column = 2, columnspan= 5, sticky = W)
		self.dosa = BooleanVar()
		
		Checkbutton(self, variable = self.dosa).grid(row = 4, column = 4, columnspan=5, stick = W)
		
		self.txt = Text(self, width = 30, height = 7, wrap =WORD)
		self.txt.grid(row= 5, column = 0, columnspan= 10)

	def price(self):
		bill_amount = 0
		msg =""
		if self.idli.get():
			pidli = 10*int(self.q_idli.get())
			bill_amount= bill_amount+pidli
		if self.vada.get():
			pvada = 15*int(self.q_vada.get())
			bill_amount = bill_amount+pvada
		if self.dosa.get():
			pdosa = 15*int(self.dosa.get())
			bill_amount = bill_amount+pdosa

		msg = "Your total bill is Rs"+str(bill_amount)+". Thank You. Visit Again"
		self.txt.delete(0.0,END)
		self.txt.insert(0.0,msg)


root = Tk()
root.title("BMSCE CANTEEN")
app = Application(root)
root.mainloop()
