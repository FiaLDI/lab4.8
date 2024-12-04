#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def main():
    # Создаем окно
    root = tk.Tk()
    root.title("Рисунок с домом и травой")

    # Создаем холст
    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    # Рисуем дом (основа и крыша)
    canvas.create_rectangle(
        100, 150, 200, 250, fill="lightblue", outline="lightblue"
    )  # Основа дома
    canvas.create_polygon(
        60, 150, 150, 100, 240, 150, fill="lightblue", outline="lightblue"
    )  # Крыша

    # Рисуем солнце
    canvas.create_oval(220, 20, 270, 70, fill="yellow", outline="yellow")  # Солнце

    # Рисуем траву с использованием цикла
    for x in range(0, 300, 10):  # С шагом 10 пикселей
        canvas.create_line(x, 300, x + 10, 260, fill="green", width=2)

    # Запускаем приложение
    root.mainloop()


if __name__ == "__main__":
    main()
