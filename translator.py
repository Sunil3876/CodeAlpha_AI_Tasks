import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    text_to_translate = text_input.get("1.0", tk.END).strip()
    selected_language = lang_var.get()

    if not text_to_translate:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    try:
        # Full name se uska respective language code nikalna
        target_lang_code = languages_dict[selected_language]
        
        # Text ko API ke through translate karna
        translated = GoogleTranslator(source='auto', target=target_lang_code).translate(text_to_translate)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# UI Setup
root = tk.Tk()
root.title("Advanced Language Translation Tool")
root.geometry("600x550") # Window size ko bada kiya hai taaki bade boxes fit ho sakein

# Input Label aur Box
tk.Label(root, text="Enter Text:", font=("Arial", 10, "bold")).pack(pady=5)
text_input = tk.Text(root, height=8, width=65) # Height 5 se 8 aur Width 50 se 65 ki gayi hai
text_input.pack(pady=5)

# Language Selection
tk.Label(root, text="Select Target Language:", font=("Arial", 10, "bold")).pack(pady=5)

# Languages Dictionary jisme full names aur unke codes map hain
languages_dict = {
    'Hindi': 'hi',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Arabic': 'ar',
    'Japanese': 'ja',
    'Russian': 'ru',
    'Italian': 'it',
    'Chinese (Simplified)': 'zh-CN',
    'Portuguese': 'pt',
    'Korean': 'ko',
    'Dutch': 'nl'
}

lang_var = tk.StringVar(value='Hindi')
# Combobox mein ab short codes ki jagah Full Names dikhenge
lang_dropdown = ttk.Combobox(root, textvariable=lang_var, values=list(languages_dict.keys()), state="readonly", width=25)
lang_dropdown.pack(pady=5)

# Translate Button
tk.Button(root, text="Translate", command=translate_text, bg="blue", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=15)

# Output Label aur Box
tk.Label(root, text="Translated Text:", font=("Arial", 10, "bold")).pack(pady=5)
text_output = tk.Text(root, height=8, width=65) # Output box ko bhi bada kiya hai
text_output.pack(pady=5)

root.mainloop()