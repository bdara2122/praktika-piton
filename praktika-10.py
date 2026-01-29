# ПРАКТИЧЕСКАЯ 10

import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class App(tk.Tk):
    def __init__(self, author_name):
        super().__init__()
        
        # 1. Название приложения (ФИО автора)
        self.title(Бондаренко Дарья Сергеевна)
        self.geometry("600x400")
        self.resizable(True, True)
        
        # Создание вкладок
        self.tab_control = ttk.Notebook(self)
        
        # Вкладка 1: Калькулятор
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='Калькулятор')
        
        # Вкладка 2: Чекбоксы
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Чекбоксы')
        
        # Вкладка 3: Работа с текстом
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text='Текст')
        
        self.tab_control.pack(expand=1, fill='both', padx=10, pady=10)
        
        self.create_tab1()
        self.create_tab2()
        self.create_tab3()

    def create_tab1(self):
        """Создаёт интерфейс калькулятора."""
        tk.Label(self.tab1, text="Число 1:").grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.entry1 = tk.Entry(self.tab1, width=15)
        self.entry1.grid(row=0, column=1, padx=5, pady=10)

        tk.Label(self.tab1, text="Число 2:").grid(row=1, column=0, padx=5, pady=10, sticky='w')
        self.entry2 = tk.Entry(self.tab1, width=15)
        self.entry2.grid(row=1, column=1, padx=5, pady=10)


        tk.Label(self.tab1, text="Операция:").grid(row=2, column=0, padx=5, pady=10, sticky='w')
        self.operation = ttk.Combobox(self.tab1, values=['+', '-', '*', '/'], state='readonly', width=12)
        self.operation.current(0)  # по умолчанию '+'
        self.operation.grid(row=2, column=1, padx=5, pady=10)


        self.result_label = tk.Label(self.tab1, text="Результат: —", fg="blue")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)


        calc_btn = tk.Button(self.tab1, text="Вычислить", command=self.calculate)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate(self):
        """Выполняет вычисление по выбранным числам и операции."""
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            op = self.operation.get()

            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                if b == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль!")
                    return
                res = a / b

            self.result_label.config(text=f"Результат: {res}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")

    def create_tab2(self):
        """Создаёт интерфейс с чекбоксами и кнопкой."""
        self.check1_var = tk.BooleanVar()
        self.check2_var = tk.BooleanVar()
        self.check3_var = tk.BooleanVar()

        tk.Checkbutton(self.tab2, text="Первый", variable=self.check1_var).pack(anchor='w', pady=5)
        tk.Checkbutton(self.tab2, text="Второй", variable=self.check2_var).pack(anchor='w', pady=5)
        tk.Checkbutton(self.tab2, text="Третий", variable=self.check3_var).pack(anchor='w', pady=5)

        btn = tk.Button(self.tab2, text="Проверить выбор", command=self.show_checkbox_result)
        btn.pack(pady=20)

    def show_checkbox_result(self):
        """Показывает всплывающее окно с выбранным вариантом."""
        selected = []
        if self.check1_var.get():
            selected.append("Первый")
        if self.check2_var.get():
            selected.append("Второй")
        if self.check3_var.get():
            selected.append("Третий")

        if selected:
            msg = "Вы выбрали: " + ", ".join(selected)
        else:
            msg = "Ничего не выбрано."

        messagebox.showinfo("Результат", msg)

    def create_tab3(self):
        """Создаёт интерфейс для работы с текстом и меню загрузки файла."""
        # Текстовая область
        self.text_area = tk.Text(self.tab3, wrap='word', height=15)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)

        # Меню (в верхней части окна)
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Открыть файл...", command=self.load_file)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.quit)
        menubar.add_cascade(label="Файл", menu=filemenu)
        self.config(menu=menubar)

    def load_file(self):
        """Загружает текст из файла в текстовую область."""
        filepath = filedialog.askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if filepath:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")



# Запуск приложения
if __name__ == "__main__":
    # Замените на свои ФИО
    author = "Бондаренко Дарья Сергеевна"
    app = App(author)
    app.mainloop()
