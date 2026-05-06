import tkinter as tk
from tkinter import filedialog, messagebox

# function to open file------------

def open_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to replace text-----------------------------------------------------------------

def replace_text():
    try:
        old_word = entry_old.get()
        new_word = entry_new.get()
        
        content = text_area.get("1.0", tk.END)
        if old_word == "":
            messagebox.showwarning("Warning", "Enter word to replace")
            return
        updated_content = content.replace(old_word, new_word)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, updated_content)
        
        messagebox.showinfo("Success", "Text replaced successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

        # Function to save a file------------------------------------------------------------------

def save_file():
    try:
        if not current_file:
            messagebox.showwarning("Warning", "No file selected")
            return
        
        content = text_area.get("1.0", tk.END)

        # ✅ CONFIRMATION HERE (before overwrite)
        confirm = messagebox.askyesno("Confirm", "Overwrite existing file?")
        if not confirm:
            return
        
        with open(current_file, "w") as file:
            file.write(content)
        
        messagebox.showinfo("Success", "File saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        
# Function to save as a file------------------------------------------------------------------

def save_as_file():
    try:
        # Ask user where to save
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if not file_path:
            return  # user cancelled

        content = text_area.get("1.0", tk.END)

        with open(file_path, "w") as file:
            file.write(content)

        messagebox.showinfo("Success", "File saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    try:
        if not current_file:
            messagebox.showwarning("Warning", "No file selected")
            return
        
        content = text_area.get("1.0", tk.END)
        with open(current_file, "w") as file:
            file.write(content)
        messagebox.showinfo("Success", "File saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window----------------------------------------------------------------

root = tk.Tk()
root.title("Text File Editor")
root.configure(bg="Lightgreen")
root.geometry("700x500")
current_file = None

# Create text area----------------------------------------------------------------

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Frame for inputs----------------------------------------------------------------

frame = tk.Frame(root)
frame.pack(pady=5)

# Old word-----------------------------------------------------------------------

tk.Label(frame, text="Find:").grid(row=0, column=0)
entry_old = tk.Entry(frame)
entry_old.grid(row=0, column=1, padx=5)

# New word---

tk.Label(frame, text="Replace:").grid(row=0, column=2)
entry_new = tk.Entry(frame)
entry_new.grid(row=0, column=3, padx=5)

# Buttons------------------------------------------------------------------------

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Open File", command=open_file).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Replace", command=replace_text).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Save File", command=save_file).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Save as File",command=save_as_file).grid(row=0, column=3, padx=5)

# Run app------------------------------------------------------------------------
root.mainloop()