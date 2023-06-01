import customtkinter
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import control
from tkinter import *
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def obter_dados():
    num_str   = entry_num.get()
    den_str   = entry_den.get()
    time_str  = time_user.get()
    kp_str    = kp_user.get()
    ki_str    = ki_user.get()
    kd_str    = kd_user.get()
    input_str = input_user.get()

    processar_dados(num_str, den_str, time_str, kp_str, ki_str, kd_str, input_str)


def processar_dados(num_str, den_str, time_str, kp_str, ki_str, kd_str, input_str):
    num_list  = [float(n_one) for n_one in num_str.split(',')]
    den_list  = [float(n_two) for n_two in den_str.split(',')]
    time_list = float(time_str)
    Kp_list   = float(kp_str)
    Ki_list   = float(ki_str)
    Kd_list   = float(kd_str)

    t = np.linspace(0, time_list, 1000)

    if input_str == 'Unit Step':
        entrada = np.where(t >= 1, 1, 0)
        title1 = 'Unit Step'
    elif input_str == 'Square Wave':
        entrada = np.sign(np.sin(t))
        title1 = 'Square Wave'
    else:
        entrada = t
        title1 = 'Ramp'

    sys = control.TransferFunction(num_list, den_list)
    controlador = control.TransferFunction([Kd_list, Kp_list, Ki_list], [1, 0])
    sistema_controlado = control.series(controlador, sys)
    t_out, y_out = control.forced_response(sistema_controlado, t, entrada)

    ax.clear()
    ax.plot(t_out, y_out,   label='$y(t)$')
    ax.plot(t_out, entrada, label='$setpoint$')
    ax.legend(loc='best')
    ax.set_xlabel('Time')
    ax.set_ylabel('Output')
    ax.set_title("{} Response".format(title1))
    ax.grid(True)
    ax.set_xlim(min(t_out), max(t_out))
    ax.set_ylim(min(y_out))

    canvas.draw()


def clear_data():
    entry_num.delete(0, tk.END)
    entry_den.delete(0, tk.END)
    time_user.delete(0, tk.END)
    kp_user.delete(0, tk.END)
    ki_user.delete(0, tk.END)
    kd_user.delete(0, tk.END)
    ax.clear()
    canvas.draw()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.title("PID Controller v1.0 | Kiabim")

frame = customtkinter.CTkFrame(master=janela)
frame.pack(pady=15, padx=15, fill="both", expand=True)

entry_num = customtkinter.CTkEntry(master=frame, placeholder_text="Numerator")
entry_num.grid(row=0, column=0, padx=10, pady=5)

entry_den = customtkinter.CTkEntry(master=frame, placeholder_text="Denominator")
entry_den.grid(row=1, column=0, padx=10, pady=5)

time_user = customtkinter.CTkEntry(master=frame, placeholder_text="Simulation Time")
time_user.grid(row=2, column=0, padx=10, pady=5)

kp_user = customtkinter.CTkEntry(master=frame, placeholder_text="Kp")
kp_user.grid(row=3, column=0, padx=10, pady=5)

ki_user = customtkinter.CTkEntry(master=frame, placeholder_text="Ki")
ki_user.grid(row=4, column=0, padx=10, pady=5)

kd_user = customtkinter.CTkEntry(master=frame, placeholder_text="Kd")
kd_user.grid(row=5, column=0, padx=10, pady=5)

input_user = customtkinter.CTkComboBox(master=frame, values=["Unit Step", "Square Wave", "Ramp"])
input_user.grid(row=6, column=0, padx=10, pady=5)
input_user.configure(justify="center")

btn_obter = customtkinter.CTkButton(master=frame, text="Simulation", command=obter_dados)
btn_obter.grid(row=7, column=0, padx=10, pady=5)

btn_limpar = tk.Button(master=frame, text="Clean", command=clear_data, bg="white")
btn_limpar.grid(row=8, column=0, padx=10, pady=5)


fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=0, rowspan=9, column=1)



janela.mainloop()
