#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def main():
    def update_text_area():
        try:
            rows = int(rows_entry.get())
            cols = int(cols_entry.get())
            text_area.config(height=rows, width=cols)
        except ValueError:
            pass  # Игнорируем ошибки преобразования

    def on_focus_in(event):
        text_area.config(bg="white")

    def on_focus_out(event):
        text_area.config(bg="lightgrey")

    # Создаем главное окно
    root = tk.Tk()
    root.title("Изменение размера текстового поля")

    # Создаем однострочные текстовые поля для ввода размеров
    rows_entry = tk.Entry(root)
    rows_entry.pack(pady=5)
    rows_entry.insert(0, "Введите количество строк")

    cols_entry = tk.Entry(root)
    cols_entry.pack(pady=5)
    cols_entry.insert(0, "Введите количество столбцов")

    # Создаем кнопку для изменения размера
    resize_button = tk.Button(root, text="Изменить размер", command=update_text_area)
    resize_button.pack(pady=5)

    # Создаем многострочное текстовое поле
    text_area = tk.Text(root, bg="lightgrey", height=5, width=30)
    text_area.pack(pady=5)

    # Привязываем события фокуса
    text_area.bind("<FocusIn>", on_focus_in)
    text_area.bind("<FocusOut>", on_focus_out)

    # Обработка нажатия клавиши Enter
    def on_enter(event):
        update_text_area()

    text_area.bind("<Return>", on_enter)

    # Запускаем главный цикл
    root.mainloop()


if __name__ == "__main__":
    main()
