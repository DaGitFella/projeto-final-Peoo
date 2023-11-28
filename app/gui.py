import customtkinter as Ct

Ct.set_default_color_theme("dark-blue")
Ct.set_appearance_mode("dark")

window = Ct.CTk()
window.geometry("500x300")
window.title("calculator")

text = Ct.CTkLabel(window, 
                   text="fazer login")

text.pack(padx=10, pady=10)

button = Ct.CTkButton(window, 
                      text="login", 
                      command=lambda: print('clicked'))

button.pack(padx=10, pady=10)

window.mainloop()