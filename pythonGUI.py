import tkinter as tk

window = tk.Tk()
#window.iconphoto(False, "C:\Users\HP\source\repos\App2\assets\sky3.jpg")
window.title = "My first python GUI application"
label = tk.Label(window, text="You are welcome", fg="black", height=1).grid(rowspan=1, column=0)
nameLbl = tk.Label(window, text="Name:", height=1, pady=10, width=8).grid(row=1, column=0)
nameTxt = tk.Text(window, height=1, width=8).grid(row=1, column=1)

emailLbl = tk.Label(window, text="Email:", height=1, pady=10, width=8).grid(row=2, column=0)
emailTxt = tk.Text(window, height=1, width=8).grid(row=2, column=1)

passLbl = tk.Label(window, text="Password:", height=1, pady=10, width=8).grid(row=3, column=0)
passTxt = tk.Text(window, height=1, width=8).grid(row=3, column=1)

submitBtn = tk.Button(window, text="Submit", fg="white", bg="blue", height=1, width=8).grid(row=4, column=1)

window.mainloop()


#top = tkinter.Tk()
#top.mainloop()