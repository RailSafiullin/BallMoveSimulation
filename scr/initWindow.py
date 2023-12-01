import tkinter as tk
from tkinter import messagebox
from BallMoveSimulation import BallMoveSimulation


class InitWindow:
    def __init__(self, help='', version=''):
        self.__init_window = tk.Tk()
        self.__init_window.title("Начальное окно")
        self.__init_window.geometry("520x380")

        self.__version_text = version
        self.__help_text = help

        self.variables = {
            "WINDOW_WIDTH": {"value": 900, "label": "Ширина экрана"},
            "WINDOW_HEIGHT": {"value": 600, "label": "Высота экрана"},
            "BALL_RADIUS": {"value": 20, "label": "Радиус мяча"},
            "BALL_COLOR": {"value": (25, 25, 105), "label": "Цвет мяча"},
            "ball_vx": {"value": 0.0, "label": "Горизонтальная скорость мяча"},
            "ball_vy": {"value": 1.0, "label": "Вертикальная скорость мяча"},
            "ball_ax": {"value": 0.0, "label": "Горизонтальное ускорение мяча"},
            "ball_ay": {"value": 9.85, "label": "Вертикальное ускорение мяча"},
            "k": {"value": 0.8, "label": "Коэффициент упругости"},
            "clock_tick": {"value": 120, "label": "Количество кадров в секунду"},
            "escape_height": {"value": 10.0, "label": "Высота поднятия после которой программа завершается"},
        }

        self.__create_widgets()

    def __create_widgets(self):
        row = 0
        for var_name, var_info in self.variables.items():
            label_text = var_info["label"]
            default_value = var_info["value"]

            label = tk.Label(self.__init_window, text=label_text)
            label.grid(row=row, column=0, padx=4, pady=4)

            entry = tk.Entry(self.__init_window)
            entry.insert(0, str(default_value))
            entry.grid(row=row, column=1, columnspan=2,  padx=4, pady=4)
            self.variables[var_name]["entry"] = entry

            row += 1

        button_start = tk.Button(self.__init_window, text="Старт", command=self.__start_simulation)
        button_start.grid(row=row, column=0, ipadx=6, ipady=6, padx=4, pady=4)

        button_help = tk.Button(self.__init_window, text="Справка", command=self.__show_help)
        button_help.grid(row=row, column=1, ipadx=6, ipady=6, padx=4, pady=4)

        label_version = tk.Label(self.__init_window, text=self.__version_text)
        label_version.grid(row=row, column=2, ipadx=6, ipady=6, padx=4, pady=4)

    def __start_simulation(self):
        WINDOW_WIDTH = int(self.variables["WINDOW_WIDTH"]["entry"].get())
        WINDOW_HEIGHT = int(self.variables["WINDOW_HEIGHT"]["entry"].get())
        BALL_RADIUS = float(self.variables["BALL_RADIUS"]["entry"].get())
        BALL_COLOR = eval(self.variables["BALL_COLOR"]["entry"].get())
        ball_ax = float(self.variables["ball_ax"]["entry"].get())
        ball_ay = float(self.variables["ball_ay"]["entry"].get())
        ball_vx = float(self.variables["ball_vx"]["entry"].get())
        ball_vy = float(self.variables["ball_vy"]["entry"].get())
        k = float(self.variables["k"]["entry"].get())
        clock_tick = int(self.variables["clock_tick"]["entry"].get())
        escape_height = float(self.variables["escape_height"]["entry"].get())

        self.__init_window.destroy()

        simulation = BallMoveSimulation(
                WINDOW_WIDTH=WINDOW_WIDTH,
                WINDOW_HEIGHT=WINDOW_HEIGHT,
                ball_ax=ball_ax,
                ball_ay=ball_ay,
                ball_vx=ball_vx,
                ball_vy=ball_vy,
                BALL_RADIUS=BALL_RADIUS,
                BALL_COLOR=BALL_COLOR,
                k=k,
                clock_tick=clock_tick,
                escape_height=escape_height
        )
        simulation.start_simulation()

    def __show_help(self):
        messagebox.showinfo("Справка", self.__help_text)

    def run(self):
        self.__init_window.mainloop()