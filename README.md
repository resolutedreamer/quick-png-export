# Quick Export PNG (Layer Name) for GIMP 3

A lightweight Python 3 plug-in for **GIMP 3.0+** that immediately exports your visible layers as a `.png` file named after your **currently selected layer**—with **zero confirmation dialogs or format pop-ups**.

---

## Features

* **One-Click / One-Key Export:** Bypasses both the file-save dialog and the PNG compression/metadata confirmation window.
* **Automatic Layer Naming:** Uses the active layer's name for the output file (automatically sanitizing invalid filename characters like `\ / : * ? " < > |`).
* **Smart Output Location:** Saves directly into the same directory as your current `.xcf` or source image (falls back to your `Desktop` folder for brand-new, unsaved canvases).
* **Full Composite Export:** Merges all currently visible layers on a temporary duplicate image so transparency and layer effects export cleanly without altering your open project.
* **Overwrite Compatible:** Updates GIMP's internal exported file path so `Ctrl+E` continues to work seamlessly.

---

## Requirements

* **GIMP 3.0** or newer (uses the GIMP 3.0 GObject Introspection Python API; not compatible with GIMP 2.10).

---

## Installation

GIMP 3 requires every Python plug-in to live inside a **subfolder with the exact same name** as the `.py` file.

1. Open GIMP 3 and go to **Edit > Preferences > Folders > Plug-ins** to locate your user plug-ins directory.
   * **Windows:** `C:\Users\<YourUsername>\AppData\Roaming\GIMP\3.0\plug-ins\`
   * **macOS:** `~/Library/Application Support/GIMP/3.0/plug-ins/`
   * **Linux:** `~/.config/GIMP/3.0/plug-ins/`
2. Inside that `plug-ins` directory, create a new folder named:
   ```text
   quick-png-export
   ```
3. Place **`quick-png-export.py`** inside that folder so the final path looks like:
   ```text
   .../plug-ins/quick-png-export/quick-png-export.py
   ```
   *(Linux/macOS users: ensure the script has executable permissions via `chmod +x quick-png-export.py`.)*
4. **Restart GIMP 3** completely to register the plug-in.

---

## Usage

1. Select the layer whose name you want to use as the filename.
2. Click **File > Quick Export PNG (Layer Name)** in the top menu bar.
3. GIMP immediately saves `<Layer Name>.png` and displays the output path in the status bar at the bottom of the window.

### Optional: Bind a Keyboard Shortcut

1. Go to **Edit > Keyboard Shortcuts**.
2. Search for **`Quick Export PNG`**.
3. Click **Quick Export PNG (Layer Name)**, click **Disabled**, and press your preferred key combination (e.g., `Ctrl+Shift+S` or `F5`).
4. Click **Save**.

### Optional: Customize Default PNG Compression

Because the plug-in exports non-interactively, it uses your saved default PNG export settings:
1. Export any image once via **File > Export As...** as a `.png`.
2. Adjust your desired compression level and metadata checkboxes in the PNG dialog.
3. Click **Save Defaults** at the bottom of the dialog. All future Quick Exports will use those settings automatically.

---

## License

Free to use, modify, and distribute.
