import tkinter as tk
import openpyxl as pxl
import os
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import date
from tkinter import messagebox

window=tk.Tk()
window.title('Formulário')

frame=tk.Frame(window)
frame.pack()

#user info
user_info=tk.LabelFrame(frame,text='Informações da Unidade')
user_info.grid(row=0, column=0, padx=20, pady=10)

user_info=tk.LabelFrame(frame,text='Informações da Unidade')
user_info.grid(row=0, column=0, padx=20, pady=10)

name=tk.Label(user_info, text='Responsável pelo preenchimento')
name.grid(row=0, column=0)
name_entry=tk.Entry(user_info)
name_entry.grid(row=1,column=0)

un=tk.Label(user_info, text='Unidade responsável')
un.grid(row=2,column=0)
un_combo=ttk.Combobox(user_info, values=['SESTAT','COPEG','SEPLANE'])
un_combo.grid(row=3,column=0)

for widget in user_info.winfo_children():
	widget.grid_configure(padx=5, pady=5)

proj_info=tk.LabelFrame(frame,text='Informações sobre o projeto')
proj_info.grid(row=4, column=0, padx=20, pady=10)

proj_name=tk.Label(proj_info, text='Nome do Projeto')
proj_name.grid(row=5, column=0)
proj_name_entry=tk.Entry(proj_info)
proj_name_entry.grid(row=5, column=1)

#calendar
#date 1
date1=tk.Label(proj_info, text='Data de início')
date1.grid(row=6, column=0)

def upd(*args):
	#a1.config(text=cal.get_date())
  #a1.config(text=cal.get())
  dt=cal.get_date()
  str1=dt.strftime('%d-%m-%y')
  a1.config(text=str1)

sel=tk.StringVar()
cal=DateEntry(proj_info, selecmode='day', textvariable=sel)
cal.grid(row=6, column=1)
a1=tk.Label(proj_info)
a1.grid(row=6, column=3)

b1=tk.Button(proj_info, text='Confirmar data', command=lambda:upd())
b1.grid(row=6, column=2)

#date 2
date2=tk.Label(proj_info, text='Data final')
date2.grid(row=7, column=0)

def ups(*args):
	#a2.config(text=cal.get_date())
  #a2.config(text=cal.get())
  dt1=cal1.get_date()
  str2=dt1.strftime('%d-%m-%y')
  a2.config(text=str2)

sel1=tk.StringVar()
cal1=DateEntry(proj_info, selecmode='day', textvariable=sel1)
cal1.grid(row=7, column=1)

a2=tk.Label(proj_info)
a2.grid(row=7, column=3)

b2=tk.Button(proj_info, text='Confirmar data', command=lambda:ups())
b2.grid(row=7, column=2)

for widget in proj_info.winfo_children():
	widget.grid_configure(padx=5, pady=5)

status=tk.Label(proj_info, text='Status do projeto')
status.grid(row=8, column=0)

status_entry=ttk.Combobox(proj_info, values=['Em andamento', 'Finalizado'])
status_entry.grid(row=8, column=1)

def enter_data():
    responsavel=name_entry.get()
    unidade=un_combo.get()
    projeto=proj_name_entry.get()
    data1=cal.get()
    data2=cal1.get()
    stat=status_entry.get()

    if responsavel and unidade and projeto and data1 and data2 and stat:
      print('Responsável pelo preenchimento', responsavel, 'Unidade responsável', unidade,                 'Nome do projeto', projeto, 'Data de início', data1, 'Data final', data2, 'Status             do projeto',stat)
    else:
      tk.messagebox.showwarning(title='Erro', message='Preencha todos os campos')

final=tk.Button(frame, text='Enviar respostas', command=enter_data)
final.grid(row=9, column=0, padx=10, pady=10)

window.mainloop()