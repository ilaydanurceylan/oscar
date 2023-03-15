import tkinter
class oscar():
    def __init__(self):
        self.pencerem=tkinter.Tk()
        self.label_türler=tkinter.Label(self.pencerem,text="türler:")
        self.label_türler.grid(row=0,column=0,columnspan=2,sticky="w",padx=5,pady=5)
        self.label_filmler=tkinter.Label(self.pencerem,text="filmler:")
        self.label_filmler.grid(row=0,column=3,columnspan=2,sticky="w",padx=5,pady=5)
        self.türler=tkinter.StringVar()
        self.scroll=tkinter.Scrollbar(self.pencerem,orient=tkinter.VERTICAL)
        self.scroll.grid(row=1,column=1,sticky="ns")
        self.listbox_türler=tkinter.Listbox(self.pencerem,listvariable=self.türler,yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listbox_türler.yview)
        self.listbox_türler.grid(row=1,column=0,sticky="n")
        
        self.myset=set()
        self.dosyam=open("Oscars.txt","r")
        for line in self.dosyam:
            line=line.rstrip()
            line=line.split(",")
            self.myset.add(line[1])
        self.listem=list(self.myset)
        self.türler.set(tuple(self.listem))
        self.dosyam.close()
        self.filmler=tkinter.StringVar()
        self.listbox_filmler=tkinter.Listbox(self.pencerem,listvariable=self.filmler)
        self.listbox_türler.bind("<<ListboxSelect>>",self.filmlerigöster)
        self.listbox_filmler.grid(row=1,column=3)
        tkinter.mainloop()

    def filmlerigöster(self,event):
        self.tür=self.listbox_türler.get(self.listbox_türler.curselection())
        self.listem2=[]
        self.dosya=open("Oscars.txt","r")
        for satir in self.dosya:
            satir=satir.rstrip()
            satir=satir.split(",")
            if satir[1]==self.tür:
                self.listem2.append(satir[0])
        self.filmler.set(tuple(self.listem2))        

oscar()