from tkinter import *
import tkinter as tk
from tkinter import ttk
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
        self.geometry('1000x400')
        self.c = Canvas(self, height=400, width=1000, bg='#d1d1d1')
        self.c.pack()

        # WINDOW ELEMENTS

        self.processes = []

        self.lbl_proc_number = tk.Label(self.c, text='Numero de procesos: ', bg='#d1d1d1')
        self.inputBox_proc_number = tk.Entry(self.c)

        self.btnSaveProc = tk.Button(self.c, text="Agregar", command=lambda: self.ComboBox())


        self.comboBox_processes = ttk.Combobox(self.c, values=self.processes, width=18)

        self.lbl_arrive_time = tk.Label(self.c, text='Numero de procesos: ', bg='#d1d1d1')
        self.inputBox_arrive_time = tk.Entry(self.c)
        self.lbl_exe_time = tk.Label(self.c, text='Numero de procesos: ', bg='#d1d1d1')
        self.inputBox_exe_time = tk.Entry(self.c)

        self.btnGenSim = tk.Button(self.c, text="Generar Gráfica", width=25, command= lambda: self.ShowData())

        self.c.create_window(100, 100, window=self.lbl_proc_number)
        self.c.create_window(300, 100, window=self.inputBox_proc_number)
        self.c.create_window(300, 150, window=self.comboBox_processes)
        self.c.create_window(300, 200, window=self.inputBox_arrive_time)
        self.c.create_window(300, 250, window=self.inputBox_exe_time)
        self.c.create_window(450, 100, window=self.btnSaveProc)
        self.c.create_window(300, 300, window=self.btnGenSim)

        # VARIABLES

    def DataTreatment(self):
        x = 0

        # DATA WINDOW

    def ShowData(self):

        root = tk.Tk()
        root.configure(background="#d1d1d1")
        root.title('CPU Process Graphic Representation')

        canvasData = tk.Canvas(root,height=0, width=1100)
        canvasData.pack()

        # PLOT

        xs = np.linspace(1, 21, 200)

        plot = plt.figure(figsize=(12, 6))
        a = plot.add_subplot(111)
        a.hlines(y=35, xmin=100, xmax=175, colors='green', linestyles='-', lw=14, label='Single Short Line')
        a.hlines(y=[39, 40, 41], xmin=[0, 25, 50], xmax=[len(xs)], colors='purple', linestyles='--', lw=2,
                   label='Multiple Lines')
        a.legend(bbox_to_anchor=(0.5, 1.3), loc="upper center", borderaxespad=5)
        canvas = FigureCanvasTkAgg(plot, master=root)
        canvas.get_tk_widget().pack()
        canvas.draw()

        # TABLE

        data = {
            '1': {'Source': 'OB', 'Campaign': 'X7765LKBTYYU-TAB-US', 'Impr.': 9457123, 'CTR': '0.12%', 'Spent': 45.78},
            '2': {'Source': 'OB', 'Campaign': 'X6159TNFYTHY-PHONE-US-A', 'Impr.': 5456953, 'CTR': '0.27%',
                  'Spent': 12.52},
            '3': {'Source': 'OB', 'Campaign': 'X7765LGKJHYRT-TAB-US', 'Impr.': 9457123, 'CTR': '0.12%', 'Spent': 45.78},
            '4': {'Source': 'OB', 'Campaign': 'X6159FTJKYUKKX-PHONE-US-A', 'Impr.': 5456953, 'CTR': '0.27%',
                  'Spent': 12.52}
        }

        tbl_frame = tk.Frame(root, width=1000, height=550, bg="lightcoral")
        tbl_frame.pack(side=tk.BOTTOM)
        model = TableModel()
        table = TableCanvas(tbl_frame, model=model, data=data, editable=False, width=800, height=300)

        table.show()


        # TABLE




if __name__ == "__main__":
    testObj = Win()
    testObj.mainloop()