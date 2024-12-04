#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk


def main():
    # Функция для добавления текста из Entry в Listbox
    def add_to_list(event):
        text = entry.get()
        if text:  # Проверяем, что текст не пустой
            listbox.insert(tk.END, text)
            entry.delete(0, tk.END)  # Очищаем поле ввода

    # Функция для копирования текста из Listbox в Entry
    def copy_to_entry(event):
        selected_item_index = listbox.curselection()
        if selected_item_index:  # Проверяем, что выбран элемент
            selected_item = listbox.get(selected_item_index)
            entry.delete(0, tk.END)  # Очищаем поле ввода
            entry.insert(0, selected_item)  # Вставляем выбранный элемент

    # Создание основного окна
    root = tk.Tk()
    root.title("Список товаров")

    # Создание однострочного текстового поля
    entry = tk.Entry(root)
    entry.pack(pady=10)
    entry.bind("<Return>", add_to_list)  # Привязываем нажатие Enter к функции

    # Создание Listbox для отображения списка
    listbox = tk.Listbox(root)
    listbox.pack(pady=10)
    listbox.bind(
        "<Double-Button-1>", copy_to_entry
    )  # Привязываем двойной клик к функции

    # Запуск основного цикла приложения
    root.mainloop()


if __name__ == "__main__":
    main()
