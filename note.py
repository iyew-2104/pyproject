import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog


class AppCommand:

    def new_file(self):

        self.text_editor.delete(1.0,tk.END)


    def open_file(self):

        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),("All Files","*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")


    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text_editor.get(1.0, tk.END)
            with open(file_path, "w") as file:
                file.write(content)


    def undo(self):
        self.text_editor.edit_undo()


    def redo(self):
        self.text_editor.edit_redo()


    def cut(self):
        self.text_editor.event_generate("<<Cut>>")


    def copy(self):
        self.text_editor.event_generate("<<Copy>>")


    def paste(self):
        self.text_editor.event_generate("<<Paste>>")


    def find(self):
        search_term = simpledialog.askstring("Find", "Enter text to find:")
        if search_term:
            start_pos = self.text_editor.search(search_term, "1.0", tk.END)
            if start_pos:
                end_pos = f"{start_pos}+{len(search_term)}c"
                self.text_editor.tag_remove("found", "1.0", tk.END)
                self.text_editor.tag_add("found", start_pos, end_pos)
                self.text_editor.mark_set("insert", start_pos)
                self.text_editor.see("insert")
                self.text_editor.tag_config("found", background="yellow")


    def replace(self):
        search_term = simpledialog.askstring("Replace", "Enter text to replace:")
        if search_term:
            replace_text = simpledialog.askstring("Replace", f"Replace with '{search_term}' by:")
            if replace_text:
                start_pos = self.text_editor.search(search_term, "1.0", tk.END)
                if start_pos:
                    end_pos = f"{start_pos}+{len(search_term)}c"
                    self.text_editor.delete(start_pos, end_pos)
                    self.text_editor.insert(start_pos, replace_text)


    def about_menu(self):

            messagebox.showinfo("Note","""
                Note
                Version: 1.0.0
                Coder: Yew
                ----
                Github: https://github.com/iyew-2104
                Facebook: https://facebook.com/yew210.4
            """)

class PyYew(AppCommand):
    
    def __init__(self, root):

        self.root = root
        self.root.title("Note")
        self.root.geometry("720x540")
        self.menu_bar()
        self.text_editor()


    def menu_bar(self):
        
        self.menu_bar = tk.Menu(self.root)
        
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New File",command=self.new_file)
        self.file_menu.add_command(label="Open File",command=self.open_file)
        self.file_menu.add_command(label="Save",command=self.save_file)
        self.file_menu.add_command(label="Exit",command=root.destroy)
                    
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo",command=self.undo)
        self.edit_menu.add_command(label="Redo",command=self.redo)
        self.edit_menu.add_command(label="Cut",command=self.cut)
        self.edit_menu.add_command(label="Copy",command=self.copy)
        self.edit_menu.add_command(label="Paste",command=self.paste)
        self.edit_menu.add_command(label="Find",command=self.find)
        self.edit_menu.add_command(label="Replace",command=self.replace)


        self.menu_bar.add_cascade(label="File",menu=self.file_menu)
        self.menu_bar.add_cascade(label="Edit",menu=self.edit_menu)
        self.menu_bar.add_cascade(label="About",command=self.about_menu)

    def text_editor(self):
        
        custom_font = ("Consolas",11)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.text_editor = tk.Text(self.canvas, wrap="none", font=custom_font,width=80, height=10,undo=True)
        self.text_editor.pack(side="right", fill="both", expand=True)

if __name__ == "__main__":

    root = tk.Tk()
    app = PyYew(root)
    root.mainloop()

