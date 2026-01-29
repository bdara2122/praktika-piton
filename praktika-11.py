# ПРАКТИЧЕСКАЯ 11 ВАРИАНТ 7

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import json
import os

class RepoInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repo Info")
        self.root.geometry("500x300")

        # Интерфейс
        tk.Label(root, text="Имя репозитория (owner/repo):").pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        self.btn = tk.Button(root, text="Получить информацию", command=self.fetch_repo_info)
        self.btn.pack(pady=10)
        
        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=5)

    def fetch_repo_info(self):
        repo_name = self.entry.get().strip()
        if not repo_name:
            messagebox.showwarning("Внимание", "Введите имя репозитория (например, kubernetes/kubernetes)")
            return

        url = f"https://api.github.com/repos/{repo_name}"
        
        try:
            response = requests.get(url)
            if response.status_code == 404:
                messagebox.showerror("Ошибка", "Репозиторий не найден.")
                return
            elif response.status_code != 200:
                messagebox.showerror("Ошибка", f"HTTP {response.status_code}: {response.text}")
                return

            data = response.json()

            # Формируем нужный словарь
            result = {
                'company': None,
                'created_at': data.get('created_at', None),
                'email': None,
                'id': data.get('id', None),
                'name': data.get('name', None),
                'url': data.get('owner', {}).get('url', None) or data.get('url', None)
            }

            # Сохраняем в файл
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("Text files", "*.txt"), ("All files", "*.*")],
                title="Сохранить как"
            )
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(result, f, indent=4, ensure_ascii=False)
                self.status_label.config(text=f"Сохранено в: {os.path.basename(filename)}", fg="green")
            else:
                self.status_label.config(text="Файл не сохранён.", fg="red")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка сети", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))



# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = RepoInfoApp(root)
    root.mainloop()
