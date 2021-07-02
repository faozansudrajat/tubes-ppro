import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.scrolledtext import ScrolledText
from time import strftime

todos = {}

def detailTodo(cb=None):
    win = tk.Toplevel()
    win.wm_title("Detail todo")
    win['background']='#212121'
    selectedItem = treev.focus()
    selectedIndex = treev.item(selectedItem)['text']
    selectedTodo = todos[tanggal][selectedIndex]
    Title = tk.StringVar(value=selectedTodo['Title'])
    tk.Label(win, text="Date:", font='Times 12', bg='#212121', fg='#fcca03').grid(row=0, column=0, sticky='W')
    tk.Label(win, text="{} | {}".format(tanggal, selectedTodo['Time']), bg='#3d3d3d', fg='white').grid(row=0, column=1, sticky="W")
    tk.Label(win, text="Title:", font='Times 12', bg='#212121', fg='#fcca03').grid(row=1, column=0, sticky='W')
    tk.Entry(win, textvariable=Title, bg='#3d3d3d', fg='white').grid(row=1, column=1, sticky="W")
    tk.Label(win, text="Information:", font='Times 12', bg='#212121', fg='#fcca03').grid(row=2, column=0, sticky='W')
    keterangan = ScrolledText(win, width=24, height=5)
    keterangan.grid(row=2, column=1, sticky='W')
    keterangan.insert(tk.INSERT, selectedTodo['keterangan'])
    keterangan.configure(bg='#3d3d3d', fg='white')

def LoadTodos():
    global todos
    f = open('mytodo.dat', 'r')
    data = f.read()
    f.close()
    todos = eval(data)
    ListTodo()

def SaveTodos():
    f = open('mytodo.dat','w')
    f.write(str(todos))
    f.close()

def delTodo():
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus()
    todos[tanggal].pop(treev.item(selectedItem)['text'])
    ListTodo()

def ListTodo(cb=None):
    for i in treev.get_children():
        treev.delete(i)
    tanggal = str(cal.selection_get())
    if tanggal in todos:
        for i in range(len(todos[tanggal])):
            treev.insert("", "end", text=i, values=(todos[tanggal][i]['Time'], todos[tanggal][i]['Title']))

def addTodo(win, key, Time, menit, Title, keterangan):
    newTodo = {
        'Time':'{}:{}'.format(Time.get(), menit.get()),
        'Title': Title.get(),
        'keterangan': keterangan.get('1.0', tk.END)
    }
    if key in todos:
        todos[key].append(newTodo)
    else:
        todos[key] = [newTodo]
    win.destroy()
    ListTodo()

def AddForm():
    win = tk.Toplevel()
    win.wm_title("+++")
    win['background']='#212121'

    Time = tk.IntVar(value=10)
    menit = tk.IntVar(value=30)
    Title = tk.StringVar(value="")
    tk.Label(win, text="Time:", fg='#fcca03', font='Times 12', bg='#212121').grid(row=0, column=0, sticky='W')
    tk.Spinbox(win, from_=0, to=23, textvariable=Time, width=3, bg='#3d3d3d', fg='white').grid(row=1, column=0, sticky='W')
    tk.Spinbox(win, from_=0, to=59, textvariable=menit, width=3, bg='#3d3d3d', fg='white').grid(row=1, column=1, sticky='W')
    tk.Label(win, text="Title:", fg='#fcca03', font='Times 12', bg='#212121').grid(row=2, column=0, sticky='W')
    tk.Entry(win, textvariable=Title, bg='#3d3d3d', fg='white').grid(row=3, column=0, columnspan=3, sticky='W')
    tk.Label(win, text="Information:", fg='#fcca03', font='Times 12', bg='#212121').grid(row=4, column=0, sticky='W')
    keterangan = ScrolledText(win, width=12, height=5, bg='#3d3d3d', fg='white')
    keterangan.grid(row=5, column=0, sticky='W', columnspan=2, rowspan=4)
    tanggal = str(cal.selection_get())
    tk.Button(win, text="Add", command=lambda: addTodo(win, tanggal, Time, menit, Title, keterangan), fg='#212121', bg='#fcca03', font='Times 12').grid(row=9, column=0, sticky='W')

def title():
    Time = strftime('%H:%M')
    tanggal = str(cal.selection_get())
    root.title(tanggal + " | " + Time + " | Calendar")
    root.after(1000, title)

def size():
    root.geometry('300x610')

root = tk.Tk()
size()
root['background']='#212121'
s = ttk.Style()
s.configure('Treeview', rowheight=16)
root.title("Calendar")
cal = Calendar(root, font='Times 12',
    selectmode='day',
    cursor='man',
    
    foreground='black',
    background="#212121",
    normalforeground='white',
    normalbackground="#212121",
    weekendforeground='white',
    weekendbackground='#212121',

    headersforeground='white',
    disabledbackground="#212121",
    bordercolor="#212121",
    headersbackground="#181818",
    
    othermonthforeground='white',
    othermonthbackground='#3d3d3d',
    othermonthweforeground='white',
    othermonthwebackground='#3d3d3d',
)
cal.grid(row=4, column=0)
cal.bind("<<CalendarSelected>>", ListTodo)
cal['background']='#fcca03'

tk.Label(text='Calendar', font='Times 25 bold', fg='#212121',bg='#fcca03').grid(row=1,column=0)
tk.Label(text='\"Make your best future plans.\"', font='Times 12 italic', fg='white', bg='#212121').grid(row=2,column=0)
tk.Label(text='h',font='Arial 2', width=2, bg='red', fg='red').grid(row=1,column=0, sticky='N')

#kotak spasi
tk.Label(height=2, bg='#212121').grid(row=0,column=0, sticky='W')
tk.Label(height=2, bg='#212121').grid(row=3,column=0,sticky='W')
tk.Label(height=2, bg='#212121').grid(row=20,column=0,sticky='W')
tk.Label(height=2, bg='#212121').grid(row=30,column=0,sticky='W')

#garis-garis
tk.Label(text='h',font='Arial 2', width=5, bg='red', fg='red').grid(row=0,column=0, sticky='W S')
tk.Label(text='h',font='Arial 2', width=10, bg='#fcca03', fg='#212121').grid(row=1,column=0, sticky='W')
tk.Label(text='h',font='Arial 2', width=15, bg='white', fg='#fcca03').grid(row=2,column=0, sticky='W N')


tanggal = str(cal.selection_get())
treev = ttk.Treeview(root)
treev.grid(row=40, column=0)
scrollBar = tk.Scrollbar(root, orient='vertical', command=treev.yview)
scrollBar.grid(row=40, column=3, sticky="WNS", rowspan=8)
treev.configure(yscrollcommand=scrollBar.set)
treev.bind("<Double-1>", detailTodo)
treev['columns'] = ("1", "2")
treev['show'] = "headings"
treev.column("1", width=100)
treev.column("2", width=180)
treev.heading("1", text="Time")
treev.heading("2", text="Title")

btnAdd = tk.Button(root, text="Add", width=16, command=AddForm, bg='#fcca03', fg='#212121')
btnAdd.grid(row=20, column=0, sticky='W')

btnDel = tk.Button(root, text="Delete", width=16, command=delTodo, bg='#fcca03',fg='#212121')
btnDel.grid(row=20, column=0,sticky='E')

btnLoad= tk.Button(root, text="Load", width=16, command=LoadTodos, bg='#fcca03',fg='#212121')
btnLoad.grid(row=30, column=0, sticky='W')

btnSave = tk.Button(root, text="Save", width=16, command=SaveTodos, bg='#fcca03',fg='#212121')
btnSave.grid(row=30, column=0,sticky='E')
title()
root.mainloop()