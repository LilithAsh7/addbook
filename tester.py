import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
button2 = tk.Button(r, text='Stop 2', width=25, command=r.destroy)
button2.pack()
button.pack_forget()
button2.pack_forget()
r.mainloop()