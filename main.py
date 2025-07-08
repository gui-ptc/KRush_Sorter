import tkinter as tk
from tower_logic import tower_sorter

root = tk.Tk()
root.title("Kingdom Rush Tower Sorter")

def sort_display():
    list_result.delete(0, tk.END)

    num_slots = slots_var.get()

    tower_upgrade_prior, upgrade = tower_sorter(num_slots)

    list_result.insert(tk.END, "===Colocação===")
    for idx, torre in enumerate(tower_upgrade_prior, start=1):
        list_result.insert(tk.END, f"{idx}º: {torre}")

    list_result.insert(tk.END, "-" * 25)

    list_result.insert(tk.END, "=== Upgrade ===")
    for torre in upgrade:
        list_result.insert(tk.END, torre)

frame_input = tk.Frame(root, pady=30, padx=90)
frame_input.pack()

frame_output = tk.Frame(root, pady=10)
frame_output.pack()

list_result = tk.Listbox(frame_output, width=30, height=35)
list_result.pack()

# Label e Spinbox para escolher número de slots
tk.Label(frame_input, text="Slots:").pack(side="left")
slots_var = tk.IntVar(value=15)
spin_slots = tk.Spinbox(frame_input, from_=1, to=30, textvariable=slots_var, width=5)
spin_slots.pack(side="left", padx=5)

# Botão que, mais tarde, chamará a função de sorteio
btn_sort = tk.Button(frame_input, text="Sort", command=sort_display)
btn_sort.pack(side="left", padx=5)

root.mainloop()