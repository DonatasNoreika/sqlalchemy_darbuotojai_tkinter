from tkinter import Tk, Frame, Label, Entry, Button, Listbox, SINGLE, END
from sqlalchemy.orm import sessionmaker
from modules.darbuotojas import engine, Darbuotojas
from datetime import datetime

Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

asmuo_edit = None

def update_fields():
    boksas.delete(0, END)
    boksas.insert(END, *session.query(Darbuotojas).all())
    laukas1.delete(0, 'end')
    laukas2.delete(0, 'end')
    laukas3.delete(0, 'end')
    laukas4.delete(0, 'end')
    laukas1.focus()

def ui_add(event):
    global asmuo_edit
    if asmuo_edit:
        dirba_nuo = datetime.strptime(laukas3.get(), "%Y-%m-%d")
        asmuo_edit.vardas = laukas1.get()
        asmuo_edit.pavarde = laukas2.get()
        asmuo_edit.gimimo_data = dirba_nuo
        asmuo_edit.atlyginimas = laukas4.get()
        session.commit()
        asmuo_edit = None
    else:
        dirba_nuo = datetime.strptime(laukas3.get(), "%Y-%m-%d")
        darbuotojas = Darbuotojas(laukas1.get(), laukas2.get(), dirba_nuo, laukas4.get())
        session.add(darbuotojas)
        session.commit()
    update_fields()

def ui_delete():
    record = session.query(Darbuotojas).all()[boksas.curselection()[0]]
    session.delete(record)
    session.commit()
    update_fields()

def ui_edit():
    global asmuo_edit
    asmuo_edit = session.query(Darbuotojas).all()[boksas.curselection()[0]]
    update_fields()
    laukas1.insert(0, asmuo_edit.vardas)
    laukas2.insert(0, asmuo_edit.pavarde)
    laukas3.insert(0, asmuo_edit.gimimo_data)
    laukas4.insert(0, asmuo_edit.atlyginimas)

# Graphic Objects initialization
main_window = Tk()
main_window.title("Darbuotojų katalogas")
# main_window.iconbitmap(r'asmenys.ico')
top_frame = Frame(main_window)
button_frame = Frame(main_window)
boksas = Listbox(button_frame, selectmode=SINGLE)
boksas.insert(END, *session.query(Darbuotojas).all())
uzrasas1 = Label(top_frame, text="Įveskite asmenį", width=40)
laukas1 = Entry(top_frame)
laukas1_uzr = Label(top_frame, text="Vardas")
laukas2 = Entry(top_frame)
laukas2_uzr = Label(top_frame, text="Pavardė")
laukas3 = Entry(top_frame)
laukas3_uzr = Label(top_frame, text="Amžius")
laukas4 = Entry(top_frame)
laukas4_uzr = Label(top_frame, text="Atlyginimas")
mygtukas1 = Button(top_frame, text="Įvesti")
mygtukas1.bind("<Button-1>", ui_add)
laukas1.bind("<Return>", ui_add)
laukas2.bind("<Return>", ui_add)
laukas3.bind("<Return>", ui_add)
mygtukas2 = Button(top_frame, text="Redaguoti", command=ui_edit)
mygtukas3 = Button(top_frame, text="Ištrinti", command=ui_delete)

# Graphic Objects visualization
uzrasas1.grid(row=0, columnspan=2)
laukas1_uzr.grid(row=1, column=0)
laukas1.grid(row=1, column=1)
laukas2_uzr.grid(row=2, column=0)
laukas2.grid(row=2, column=1)
laukas3_uzr.grid(row=3, column=0)
laukas3.grid(row=3, column=1)
laukas4_uzr.grid(row=4, column=0)
laukas4.grid(row=4, column=1)
mygtukas1.grid(row=5, columnspan=2, sticky="E")
mygtukas2.grid(row=5, columnspan=2)
mygtukas3.grid(row=5, columnspan=2, sticky="W")
boksas.pack()
top_frame.pack()
button_frame.pack()
main_window.mainloop()