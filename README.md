# Ink — Clear Symbol Text Generator

> Transform plain text into high-definition block and symbol letters. Clean, readable, copy-ready ASCII art.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-2CA121)
![PyFiglet](https://img.shields.io/badge/Figlet-PyFiglet_1.0.4-orange)
![Platform](https://img.shields.io/badge/Platform-Windows_%7C_Linux_%7C_macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-1.0.0-cyan)
![Creator](https://img.shields.io/badge/Creator-zakariaelqannaa--dv-purple)

---

## What is Ink?

**Ink** is a lightweight Python desktop app that converts any word into large, crisp symbol text using Figlet fonts rebuilt with solid fill characters.

Type `HELLO`, pick a font and a fill symbol, hit Generate, and copy the result for Discord, GitHub READMEs, banners, terminals, and social bios.

```text
██    ██  ████████  ██        ██          ████    
██    ██  ██        ██        ██        ██    ██  
████████  ██████    ██        ██        ██    ██  
██    ██  ██        ██        ██        ██    ██  
██    ██  ████████  ████████  ████████    ████    
                                                       
██          ██    ████    ██████    ██        ██████    
██          ██  ██    ██  ██    ██  ██        ██    ██  
██    ██    ██  ██    ██  ██████    ██        ██    ██  
  ██  ██  ██    ██    ██  ██    ██  ██        ██    ██  
    ██  ██        ████    ██    ██  ████████  ██████
```

No web dependencies. No mess. Just clear output.

---

## Features

* **7 readable fonts:** `block`, `standard`, `big`, `slant`, `small`, `rectangles`, `banner`
* **6 fill modes:**
  * `Solid Block (█)`
  * `Clean Hash (#)`
  * `Bold At (@)`
  * `Star Grid (*)`
  * `Dot Matrix (•)`
  * `Original Figlet`
* **One-click copy** to clipboard with confirmation dialog
* **Dark HD UI:** `#121212` background, `#00E5FF` accents, `#00FF66` terminal output
* **Monospaced rendering:** Courier Bold with horizontal + vertical scroll for perfect alignment
* **Instant preview:** default `HELLO` rendered on launch
* **Error handling:** empty input and render errors show inline messages

---

## Tech Stack

| Technology | Purpose | Version |
|---|---|---|
| **Python** | Core language | 3.8+ (tested on 3.14.4) |
| **Tkinter + ttk** | Desktop GUI, Combobox, layout | Built-in |
| **PyFiglet** | ASCII font rendering engine | 1.0.4 |
| **Clipboard API** | `clipboard_clear` / `clipboard_append` copy | Built-in |

**Badges:**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-2CA121)
![PyFiglet](https://img.shields.io/badge/PyFiglet-Fonts-orange)

---

## Quickstart

### 1. Clone
```bash
git clone https://github.com/zakariaelqannaa-dv/ink.git
cd ink
```

### 2. Install dependency
```bash
pip install pyfiglet
# or
pip install -r requirements.txt
```

`requirements.txt`:
```text
pyfiglet==1.0.4
```

### 3. Run
```bash
python ink.py
```

No build step. Works on Windows, Linux, and macOS (Tkinter included with standard Python).

---

## Usage

1. Enter your text in **Your Text** field (default: `HELLO`)
2. Select **Readable Font** — try `block` for maximum clarity
3. Select **Fill Symbol** — try `Solid Block (█)` for HD look
4. Click **Generate Clear Output**
5. Click **Copy Text** to copy to clipboard

Tip: Use `Courier` or `Consolas` monospaced font when pasting elsewhere to keep alignment.

---

## Project Structure

```text
ink/
├── ink.py        # Main app - GUI + Figlet + symbol replacement logic
├── README.md     # This file
└── requirements.txt  # (recommended) pyfiglet==1.0.4
```

Core logic in `ink.py:5-44`:
* `generate_clean_art()` renders with `pyfiglet.figlet_format()` then replaces every non-space char with the selected fill symbol
* `copy_art()` in `ink.py:46-51` handles clipboard copy

---

## Customization

Add a new font in `ink.py:98`:
```python
clean_fonts = ["block", "standard", "big", "slant", "small", "rectangles", "banner"]
```

Add a new fill symbol in `ink.py:23-29`:
```python
char_map = {
    "Solid Block (█)": "█",
    "Clean Hash (#)": "#",
    # Add yours: "Wave (~)": "~"
}
```

Change theme in `ink.py:54-57` and `ink.py:150-160` (`bg`, `fg`, `font`).

---

## Roadmap

* [ ] Export to `.txt` file
* [ ] Live preview on typing
* [ ] More fonts list + preview
* [ ] Custom color themes
* [ ] Screenshot / demo GIF in `assets/demo.png`

Contributions welcome. Fork, branch, PR.

---

### Creator

**Created by [zakariaelqannaa-dv](https://github.com/zakariaelqannaa-dv)**

[![GitHub](https://img.shields.io/badge/GitHub-zakariaelqannaa--dv-181717?logo=github)](https://github.com/zakariaelqannaa-dv)

If you like Ink, star the repo and follow for more Python GUI tools.

---

## License

MIT License — free to use, modify, and distribute.

See `LICENSE` for details.
