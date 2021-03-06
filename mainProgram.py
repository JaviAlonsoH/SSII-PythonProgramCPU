import _tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot
from tkintertable import TableCanvas, TableModel
import array as arr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import plotly.graph_objects as go


class Win(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # WINDOW CONFIGURATION

        self.title('Parameters')
        self.geometry('1000x500')
        self.c = Canvas(self, height=600, width=1000, bg='#d1d1d1')
        self.c.pack()

        # WINDOW ELEMENTS

        self.processes = []

        self.lbl_proc_number = tk.Label(self.c, text='Numero de procesos: ', bg='#d1d1d1')
        self.inputBox_proc_number = tk.Entry(self.c)

        self.btnSaveProc = tk.Button(self.c, text="Agregar", command=lambda: self.onSelect())

        self.lbl_select_process = tk.Label(self.c, text='Selecciona el proceso: ', bg='#d1d1d1')
        self.comboBox_processes = ttk.Combobox(self.c, values=self.processes, width=18)
        self.comboBox_processes.bind(self.onSelect)

        self.lbl_arrive_time = tk.Label(self.c, text='Tiempo de llegada: ', bg='#d1d1d1')
        self.inputBox_arrive_time = tk.Entry(self.c)

        self.lbl_exe_time = tk.Label(self.c, text='Tiempo de ejecución: ', bg='#d1d1d1')
        self.inputBox_exe_time = tk.Entry(self.c)

        self.btnSaveData = tk.Button(self.c, text="Guardar Proceso", width=20, command=self.SaveData)

        self.btnGenSim = tk.Button(self.c, text="Generar Gráfica", width=25, height=2, command=self.ShowData)

        # ALGORITMOS

        self.opt = IntVar()

        self.fifo = tk.Radiobutton(self.c, text="FIFO", value=1, bg='#d1d1d1', variable=self.opt)

        self.opt.set(None)

        # SHOW ELEMENTS

        self.c.create_window(100, 70, window=self.lbl_proc_number)
        self.c.create_window(300, 70, window=self.inputBox_proc_number)
        self.c.create_window(450, 70, window=self.btnSaveProc)

        self.c.create_window(100, 125, window=self.lbl_select_process)
        self.c.create_window(300, 125, window=self.comboBox_processes)

        self.c.create_window(100, 180, window=self.lbl_arrive_time)
        self.c.create_window(300, 180, window=self.inputBox_arrive_time)

        self.c.create_window(100, 230, window=self.lbl_exe_time)
        self.c.create_window(300, 230, window=self.inputBox_exe_time)

        self.c.create_window(700, 100, window=self.fifo)

        self.c.create_window(300, 280, window=self.btnSaveData)

        self.c.create_window(500, 450, window=self.btnGenSim)

        # VARIABLES

        self.num_processes = 0
        self.exe_time = 0
        self.response_time = 0
        self.wait_time = 0
        self.arrive_time = 0
        self.ini = 0
        self.end = 0
        self.P = 0
        self.R = 0
        self.Quantum = 0

        # DATOS TABLA

        self.data_table = {
        }

        self.key = ""
        self.counter = 1

    def onSelect(self):
        self.processes = []
        self.num_processes = int(self.inputBox_proc_number.get())
        cont = 1
        while len(self.processes) < self.num_processes:
            self.key = 'Proceso ' + str(cont)
            self.processes.append(self.key)
            cont += 1
        self.inputBox_proc_number.clipboard_clear()
        self.comboBox_processes['values'] = self.processes

        ## PONER LA KEY CONTADOR EN LA ADICION DE REGISTROS EN EL DICCIONARIO

    def SaveData(self):
        self.arrive_time = self.inputBox_arrive_time.get()
        self.exe_time = self.inputBox_exe_time.get()
        self.inputBox_exe_time.delete(0, 'end')
        self.inputBox_arrive_time.delete(0, 'end')

        self.response_time = int(self.wait_time) + int(self.exe_time)
        self.ini = int(self.response_time) - int(self.exe_time)
        self.end = int(self.response_time)
        self.wait_time = int(self.response_time) - int(self.exe_time)
        self.P = int(self.response_time) / int(self.exe_time)
        self.R = int(self.exe_time) / int(self.response_time)

        # ALGORITMO FIFO #
        res = not self.data_table
        proceso = 'Proceso '
        if res:
            row = {'Llegada': self.arrive_time, 'T. Ejecución': self.exe_time, 'Inicio': int(self.arrive_time) - int(self.wait_time),
                   'Fin': int(self.arrive_time) + int(self.wait_time) + int(self.exe_time),
                   'T. Respuesta': self.response_time, 'T. Espera': self.wait_time, 'Penalización': self.P}
            self.data_table[self.comboBox_processes.get()] = row
        else:
            row = {'Llegada': self.arrive_time, 'T. Ejecución': self.exe_time, 'Inicio': self.data_table[proceso +
                str(self.counter - 1)]['Fin'], 'Fin': int(self.data_table[proceso + str(self.counter - 1)]['Fin']) +
                int(self.wait_time) + int(self.exe_time),
                'T. Respuesta': int(self.data_table[proceso + str(self.counter - 1)]['Fin']) - int(
                self.arrive_time) + int(self.exe_time),
                'T. Espera': int(self.data_table[proceso + str(self.counter - 1)]['Fin']) - int(
                self.arrive_time), 'Penalización': int(self.response_time) / int(self.exe_time)}
            self.data_table[self.comboBox_processes.get()] = row
        self.counter += 1



        # DATA WINDOW

    def ShowData(self):

        root = tk.Tk()
        root.configure(background="#d1d1d1")
        root.geometry('1200x1000')
        root.title('CPU Process Graphic Representation')

        canvasData = tk.Canvas(root, height=0, width=1100)
        canvasData.pack()

        # PLOT FIFO
        xs = np.linspace(1, 21, 200)
        plot = plt.figure(figsize=(12, 6))
        a = plot.add_subplot(111)
        axes = plt.gca()
        for i, ax in enumerate(self.processes):
            axes.set_ylabel(str(i))
        startList = []
        endList = []
        waitList = []
        for i in self.data_table.keys():
            start = int(self.data_table[i]['Inicio'])
            end = int(self.data_table[i]['Fin'])
            wait = int(self.data_table[i]['Llegada'])
            waitList.append(wait)
            startList.append(start)
            endList.append(end)
        print(startList, endList, waitList)
        a.hlines(y=self.processes, xmin=waitList, xmax=startList,
                 colors='purple',
                 linestyles='--', lw=20, label='Tiempo de espera')
        a.hlines(y=self.processes, xmin=startList, xmax=endList,
                 colors='green',
                 linestyles='-', lw=20, label='Proceso en ejecución')
        a.legend(bbox_to_anchor=(0.5, 1.3), loc="upper center", borderaxespad=5)
        a.grid()
        plot.gca().invert_yaxis()
        canvas = FigureCanvasTkAgg(plot, master=root)
        canvas.get_tk_widget().pack()
        canvas.draw()
        # TABLE FIFO
        tbl_frame = tk.Frame(root, width=1000, height=550, bg="lightcoral")
        tbl_frame.pack(side=tk.BOTTOM)
        model = TableModel()
        table = TableCanvas(tbl_frame, model=model, data=self.data_table, editable=False, width=1000, height=300)
        table.show()

        # TABLE


if __name__ == "__main__":
    testObj = Win()
    testObj.mainloop()