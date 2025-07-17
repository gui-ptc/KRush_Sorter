import tkinter as tk
from tower_logic import tower_sorter
import os
import json
from tkinter import ttk
import random

BASE_DIR = os.path.dirname(__file__)
CK_PATH = os.path.join(BASE_DIR, "checkpoint.json")
json_path = os.path.join(BASE_DIR, "stages.json")

with open(json_path, encoding="utf-8") as f:
    STAGES = json.load(f)

with open(os.path.join(BASE_DIR, "heroes.json"), encoding="utf-8") as f:
    HEROES = json.load(f)

def sort_display():
    list_result.delete(0, tk.END)

    fase = combo_stage.get()
    modo = combo_mode.get()
    nivel = combo_difficulty.get()
    num_slots = STAGES.get(fase, 0)

    chosen_hero = random.choice(HEROES)
    tower_placement, upgrade = tower_sorter(num_slots)

    checkpoint = {"stage": fase, "mode": modo, "difficulty": nivel}
    with open(CK_PATH, "w", encoding="utf-8") as ck:
        json.dump(checkpoint, ck, ensure_ascii=False, indent=2)

    last_var.set(f"Última Fase: {fase} ({modo}|{nivel})")

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

last_var = tk.StringVar(value="Última Fase: —")
checkpoint_label = tk.Label(
    frame_output,
    textvariable=last_var,
    anchor="nw",
    justify="left",
    font=("Arial", 10, "bold")
)
checkpoint_label.pack(side="left", fill="x", padx=(20,0))

tk.Label(frame_input, text="Fase:").pack(side="left", padx=(0,4))

combo_stage = ttk.Combobox(
    frame_input,
    values=list(STAGES.keys()),
    state="readonly",
    width=35
)

combo_stage.current(0)
combo_stage.pack(side="left", padx=5)

tk.Label(frame_input, text="Modo:").pack(side='left', padx=(20,4))
combo_mode = ttk.Combobox(
    frame_input,
    values=["Heroico", "Ferrenho"],
    state="readonly",
    width=12
)
combo_mode.current(0)
combo_mode.pack(side="left", padx=(5))


tk.Label(frame_input, text="Nível:").pack(side='left', padx=(20,4))
combo_difficulty = ttk.Combobox(
    frame_input,
    values=["Casual", "Normal", "Veterano"],
    state="readonly",
    width=12
)
combo_difficulty.current(0)
combo_difficulty.pack(side="left", padx=(5))

btn_sort = tk.Button(frame_input, text="Sort", command=sort_display)
btn_sort.pack(side="left", padx=5)

if os.path.exists(CK_PATH):
    with open(CK_PATH, encoding="utf-8") as ck:
        last = json.load(ck)
    last_var.set(f"Última Fase: {last['stage']} ({last['mode']}|{last['difficulty']})")

root.mainloop()