import tkinter as tk

def reset_clock(event=None):
    timer_count.set(5)

def update_clock():
    if timer_count.get() == 0:
        TextBox.delete(1.0, tk.END)
        reset_clock()
    timer_count.set(timer_count.get() - 1)
    root.after(1000, update_clock)


root = tk.Tk()
root.geometry("600x400")
root.columnconfigure(0, weight=1)

timer_count = tk.IntVar()
timer_count.set(5)

tk.Label(root, text="Dont Stop").grid(row=0, column=0)
Timer = tk.Label(root, textvariable=timer_count)
Timer.grid(row=1, column=0)
TextBox = tk.Text(root)
TextBox.bind("<Key>", reset_clock)
TextBox.grid(row=2, column=0, padx=20, pady=20)

update_clock()
root.mainloop()

