#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Listbox, Button, END, MULTIPLE


def main():
    # Функция для перемещения выбранных товаров из одного списка в другой
    def move_items(source_listbox, target_listbox):
        selected_items = source_listbox.curselection()
        for index in selected_items[
            ::-1
        ]:  # Перемещение с конца, чтобы не нарушить индексы
            item = source_listbox.get(index)
            target_listbox.insert(END, item)
            source_listbox.delete(index)

    # Создание основного окна
    root = tk.Tk()
    root.title("Перемещение товаров")

    # Список товаров
    products = ["Яблоки", "Бананы", "Молоко", "Хлеб", "Яйца", "Сыр"]

    # Создание Listbox для товаров
    product_listbox = Listbox(root, selectmode=MULTIPLE)
    for product in products:
        product_listbox.insert(END, product)
    product_listbox.pack(side=tk.LEFT, padx=10, pady=10)

    # Создание пустого Listbox для покупок
    shopping_listbox = Listbox(root, selectmode=MULTIPLE)
    shopping_listbox.pack(side=tk.RIGHT, padx=10, pady=10)

    # Кнопки для перемещения товаров
    add_button = Button(
        root,
        text="Добавить в покупки",
        command=lambda: move_items(product_listbox, shopping_listbox),
    )
    add_button.pack(pady=5)

    remove_button = Button(
        root,
        text="Вернуть в товары",
        command=lambda: move_items(shopping_listbox, product_listbox),
    )
    remove_button.pack(pady=5)

    # Запуск основного цикла приложения
    root.mainloop()


if __name__ == "__main__":
    main()
