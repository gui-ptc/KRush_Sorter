import tkinter as tk
from tower_logic import tower_sorter
import os
import json
from tkinter import ttk
import random

BASE_DIR = os.path.dirname(__file__)
json_path = os.path.join(BASE_DIR, "stages.json")

with open(json_path, encoding="utf-8") as f:
    STAGES = json.load(f)

with open(os.path.join(BASE_DIR, "heroes.json"), encoding="utf-8") as f:
    HEROES = json.load(f)

def sort_display():
    list_result.delete(0, tk.END)

    fase = combo_stage.get()
    num_slots = STAGES.get(fase, 0)

    chosen_hero = random.choice(HEROES)
    tower_placement, upgrade = tower_sorter(num_slots)

    list_result.insert(tk.END, "===Colocação===")
    for idx, (slot, torre) in enumerate(tower_placement, start=1):
        list_result.insert(
            tk.END,
            f"{idx}ª: {torre} ==|== slot {slot}"
        )

    list_result.insert(tk.END, "-" * 30)
    list_result.insert(tk.END, "=== Upgrade ===")
    for torre in upgrade:
        list_result.insert(tk.END, torre)

    list_result.insert(tk.END, "-" * 30)
    list_result.insert(tk.END, f"===Herói: {chosen_hero}===")

    combo_stage.selection_clear()
    list_result.focus_set()

root = tk.Tk()
root.title("Kingdom Rush Tower Sorter")

frame_input = tk.Frame(root, pady=30, padx=90)
frame_input.pack()

frame_output = tk.Frame(root, pady=10)
frame_output.pack()

list_result = tk.Listbox(frame_output, width=30, height=35)
list_result.pack()

# Label e Combobox para escolher a fase
tk.Label(frame_input, text="Fase:").pack(side="left")

combo_stage = ttk.Combobox(
    frame_input,
    values=list(STAGES.keys()),   # carrega as chaves do JSON
    state="readonly",
    width=35
)
combo_stage.current(0)   # opcional: pré-seleciona o primeiro item
combo_stage.pack(side="left", padx=5)

# Botão que, mais tarde, chamará a função de sorteio
btn_sort = tk.Button(frame_input, text="Sort", command=sort_display)
btn_sort.pack(side="left", padx=5)

root.mainloop()