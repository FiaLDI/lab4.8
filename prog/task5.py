#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def main():
    def move_to_click(event):
        """Запускаем движение шара к месту клика."""
        global target_x, target_y
        target_x, target_y = event.x, event.y
        move_ball()

    def move_ball():
        """Перемещаем шар к указанным координатам."""
        global target_x, target_y
        current_coords = c.coords(ball)
        current_x, current_y = (current_coords[0] + current_coords[2]) / 2, (
            current_coords[1] + current_coords[3]
        ) / 2

        # Вычисляем шаги движения
        dx = target_x - current_x
        dy = target_y - current_y
        step_x = 1 if dx > 0 else -1 if dx < 0 else 0
        step_y = 1 if dy > 0 else -1 if dy < 0 else 0

        # Если шар не достиг цели, двигаем его
        if abs(dx) > 1 or abs(dy) > 1:
            c.move(ball, step_x, step_y)
            root.after(10, move_ball)

    # Создаем окно и холст
    root = Tk()
    c = Canvas(root, width=300, height=200, bg="white")
    c.pack()

    # Создаем круг
    ball = c.create_oval(0, 100, 40, 140, fill="green")

    # Обрабатываем клик мыши
    c.bind("<Button-1>", move_to_click)

    # Инициализация
    target_x, target_y = 0, 0

    # Запускаем приложение
    root.mainloop()


if __name__ == "__main__":
    main()
