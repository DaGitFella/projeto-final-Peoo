import customtkinter as Ct

window = Ct.CTk()
window.geometry("500x300")

text = Ct.CTkLabel(window, 
                   text="fazer login")

text.pack(padx=10, pady=10)

button = Ct.CTkButton(window, 
                      text="login", 
                      command=lambda: print('clicked'))

button.pack(padx=10, pady=10)

window.mainloop()