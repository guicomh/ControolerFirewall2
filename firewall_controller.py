import os
import sys
import ctypes
from tkinter import *
from tkinter import ttk

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def ativar_firewall():
    if is_admin():
        os.system("netsh advfirewall set allprofiles state on")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def desativar_firewall():
    if is_admin():
        os.system("netsh advfirewall set allprofiles state off")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

janela = Tk()

janela.geometry("500x250")
janela.title("Controlador de Firewall 2")

texto = Label(janela, text="Controlador de Firewall", font=("Arial", 20, "bold")) . pack()


botao_ativar = Button(janela, text="Ativar", command=ativar_firewall) . pack(pady=20)


botao_desativar = Button(janela, text="Desativar", command=desativar_firewall) . pack(pady=20)

entrada = Entry(janela, width=20, font=("Arial", 16)) . pack()

janela.mainloop()
