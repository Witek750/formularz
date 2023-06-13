import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def submit_form():
    
    name = name_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    age = age_scale.get()
    experience = experience_entry.get()

    
    if not name or not address or not email or not experience:
        messagebox.showerror("Błąd", "Wypełnij wszystkie pola formularza!")
        return

    
    print("Imię i nazwisko:", name)
    print("Adres:", address)
    print("Email:", email)
    print("Płeć:", gender)
    print("Wiek:", age)
    print("Staż pracy:", experience)


    
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender_var.set("Wybierz płci")
    age_scale.set(18)
    experience_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Formularz CV")
root.geometry("400x450")


name_label = tk.Label(root, text="Imię i nazwisko:", font='Tahoma 15', fg='blue')
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

address_label = tk.Label(root, text="Adres:", font='Tahoma 15', fg='blue')
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

email_label = tk.Label(root, text="Email:", font='Tahoma 15', fg='blue')
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

gender_label = tk.Label(root, text="Płeć:", font='Tahoma 15', fg='blue')
gender_label.pack()
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Wybierz płci", "Mężczyzna", "Kobieta"])
gender_combobox.current(0)
gender_combobox.pack()

age_label = tk.Label(root, text="Wiek:", font='Tahoma 15', fg='blue')
age_label.pack()
age_scale = tk.Scale(root, from_=18, to=65, orient=tk.HORIZONTAL)
age_scale.set(18)
age_scale.pack()

experience_label = tk.Label(root, text="Staż pracy (w latach):", font='Tahoma 15', fg='blue')
experience_label.pack()
experience_entry = tk.Entry(root)
experience_entry.pack()

rad = tk.Label(root, text='Studia', font='Tahoma 15', fg='blue')

rad.pack()
gender_var = tk.StringVar()
gender_var.set("Tak")
r1 = tk.Radiobutton(root, text="Tak", variable=gender_var, value="Tak")
r1.pack()
r2 = tk.Radiobutton(root, text='Nie', variable=gender_var, value='Nie')
r2.pack()

submit_button = tk.Button(root, text="Wyślij", command=submit_form)
submit_button.pack()


root.mainloop()
