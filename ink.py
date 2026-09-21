import tkinter as tk
from tkinter import ttk, messagebox
import pyfiglet

def generate_clean_art():
    user_text = entry_text.get().strip()
    if not user_text:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "\n   [!] Type a word above to see clean symbol text.")
        return
    
    selected_font = font_var.get()
    symbol_mode = symbol_var.get()
    
    try:
        # Generate the base ASCII font layout
        art = pyfiglet.figlet_format(user_text, font=selected_font)
        
        # Replace messy internal characters with high-legibility solid symbols
        if symbol_mode != "Original Figlet":
            # Pick symbol character based on user selection
            char_map = {
                "Solid Block (█)": "█",
                "Clean Hash (#)": "#",
                "Bold At (@)": "@",
                "Star Grid (*)": "*",
                "Dot Matrix (•)": "•"
            }
            fill_char = char_map.get(symbol_mode, "█")
            
            clean_lines = []
            for line in art.splitlines():
                # Swap any character that isn't a space for our crisp symbol
                new_line = "".join([fill_char if c != " " else " " for c in line])
                clean_lines.append(new_line)
            art = "\n".join(clean_lines)
            
        # Output clean text
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, art)
        
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error rendering font: {e}")

def copy_art():
    art_text = output_box.get("1.0", tk.END).strip()
    if art_text and not art_text.startswith("[!]"):
        window.clipboard_clear()
        window.clipboard_append(art_text)
        messagebox.showinfo("Copied!", "Clean ASCII art copied to clipboard!")

# --- GUI Setup ---
window = tk.Tk()
window.title("Clean & Readable Symbol Text Generator")
window.geometry("950x650")
window.configure(bg="#121212")

# Header
title_label = tk.Label(
    window, 
    text="CLEAR SYMBOL TEXT GENERATOR", 
    font=("Consolas", 20, "bold"), 
    bg="#121212", 
    fg="#00E5FF"
)
title_label.pack(pady=(15, 5))

sub_label = tk.Label(
    window, 
    text="Transforms plain text into high-definition block & symbol letters", 
    font=("Segoe UI", 10), 
    bg="#121212", 
    fg="#888888"
)
sub_label.pack(pady=(0, 15))

# Controls Frame
controls = tk.Frame(window, bg="#1e1e1e", padx=15, pady=15, highlightbackground="#333333", highlightthickness=1)
controls.pack(fill="x", padx=20, pady=5)

# Row 1: Text Input
r1 = tk.Frame(controls, bg="#1e1e1e")
r1.pack(fill="x", pady=5)

tk.Label(r1, text="Your Text:", font=("Consolas", 11, "bold"), bg="#1e1e1e", fg="white").pack(side="left", padx=5)
entry_text = tk.Entry(r1, font=("Consolas", 13), bg="#2a2a2a", fg="white", insertbackground="white", width=25)
entry_text.insert(0, "HELLO")
entry_text.pack(side="left", padx=5)

# Row 2: Font & Symbol Style Dropdowns
r2 = tk.Frame(controls, bg="#1e1e1e")
r2.pack(fill="x", pady=10)

# High-legibility fonts only
tk.Label(r2, text="Readable Font:", font=("Consolas", 11, "bold"), bg="#1e1e1e", fg="white").pack(side="left", padx=5)
font_var = tk.StringVar(value="block")
clean_fonts = ["block", "standard", "big", "slant", "small", "rectangles", "banner"]
font_dropdown = ttk.Combobox(r2, textvariable=font_var, values=clean_fonts, state="readonly", width=12)
font_dropdown.pack(side="left", padx=5)

# High-contrast fill symbols
tk.Label(r2, text="Fill Symbol:", font=("Consolas", 11, "bold"), bg="#1e1e1e", fg="white").pack(side="left", padx=(15, 5))
symbol_var = tk.StringVar(value="Solid Block (█)")
symbols = ["Solid Block (█)", "Clean Hash (#)", "Bold At (@)", "Star Grid (*)", "Dot Matrix (•)", "Original Figlet"]
symbol_dropdown = ttk.Combobox(r2, textvariable=symbol_var, values=symbols, state="readonly", width=16)
symbol_dropdown.pack(side="left", padx=5)

# Buttons
btn_frame = tk.Frame(controls, bg="#1e1e1e")
btn_frame.pack(fill="x", pady=(10, 0))

generate_btn = tk.Button(
    btn_frame, 
    text="Generate Clear Output", 
    font=("Consolas", 11, "bold"), 
    bg="#00E5FF", 
    fg="black", 
    activebackground="#00B0FF", 
    relief="flat", 
    command=generate_clean_art, 
    padx=15
)
generate_btn.pack(side="left", padx=5)

copy_btn = tk.Button(
    btn_frame, 
    text="Copy Text", 
    font=("Consolas", 11), 
    bg="#333333", 
    fg="white", 
    activebackground="#444444", 
    relief="flat", 
    command=copy_art, 
    padx=15
)
copy_btn.pack(side="left", padx=5)

# Monospaced Display Box
output_frame = tk.Frame(window, bg="#121212")
output_frame.pack(expand=True, fill="both", padx=20, pady=15)

x_scroll = tk.Scrollbar(output_frame, orient="horizontal")
x_scroll.pack(side="bottom", fill="x")

y_scroll = tk.Scrollbar(output_frame, orient="vertical")
y_scroll.pack(side="right", fill="y")

# Strict Courier monospaced font guarantees lines line up 100% correctly
output_box = tk.Text(
    output_frame, 
    font=("Courier", 10, "bold"), 
    bg="#080808", 
    fg="#00FF66", 
    wrap="none",
    xscrollcommand=x_scroll.set,
    yscrollcommand=y_scroll.set,
    padx=15, 
    pady=15
)
output_box.pack(expand=True, fill="both")

x_scroll.config(command=output_box.xview)
y_scroll.config(command=output_box.yview)

# Run default generation
generate_clean_art()

window.mainloop()