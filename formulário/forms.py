import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    budget = entry_budget.get()
    genre = entry_genre.get()
    num_episodes = entry_episodes.get()
    num_seasons = entry_seasons.get()
    total_duration = entry_duration.get()
    
    info = f"Nome: {name}\nOrçamento: {budget}\nGênero: {genre}\nQuantidade de Episódios: {num_episodes}\nQuantidade de Temporadas: {num_seasons}\nDuração Total: {total_duration}"
    messagebox.showinfo("Informações da Série", info)

forms = tk.Tk()
forms.title("Formulário de Séries")
forms.geometry("320x270")

fields = [
    "Nome:",
    "Orçamento:",
    "Gênero:",
    "Quantidade de Episódios:",
    "Quantidade de Temporadas:",
    "Duração Total:"
]

for field in fields:
    label = tk.Label(forms, text=field)
    label.pack(anchor="w")
    
    entry = tk.Entry(forms)
    entry.pack(fill=tk.X)

entry_name = forms.winfo_children()[1]
entry_budget = forms.winfo_children()[3]
entry_genre = forms.winfo_children()[5]
entry_episodes = forms.winfo_children()[7]
entry_seasons = forms.winfo_children()[9]
entry_duration = forms.winfo_children()[11]

submit_button = tk.Button(forms, text="Enviar", command=submit_form)
submit_button.pack()

forms.mainloop()
