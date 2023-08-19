import tkinter as tk

class ClassiFileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ClassiFile")
        self.root.configure(bg="#f0f0f0")

        # Logo Label
        self.logo_label = tk.Label(root, text="ClassiFile - Classing your Files", font=("Helvetica", 24, "bold"), fg="#007BFF")
        self.logo_label.pack(pady=20)

        # Buttons
        self.upload_btn = tk.Button(root, text="Upload Files", command=self.increment_files, bg="#ADD8E6", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.upload_btn.pack(pady=10)

        self.create_account_btn = tk.Button(root, text="Create Account", command=self.dummy_function, bg="#ADD8E6", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.create_account_btn.pack(pady=10)

        self.organize_files_btn = tk.Button(root, text="Organize Files", command=self.dummy_function, bg="#ADD8E6", fg="white", font=("Helvetica", 12), padx=20, pady=10)
        self.organize_files_btn.pack(pady=10)

        # Sustainability Widget
        self.num_files = 0  # Files counter

        # Sustainability Label
        self.sustainability_label = tk.Label(root, text="Sustainability Widget", font=("Helvetica", 16))
        self.sustainability_label.pack(pady=20)

        # Sustainability Info Label
        self.sustainability_info_label = tk.Label(root, text="You haven't uploaded any files yet.", font=("Helvetica", 12))
        self.sustainability_info_label.pack(pady=10)

    def increment_files(self):
        # Increment the files counter when the "Upload Files" button is clicked
        self.num_files += 1
        self.update_sustainability_widget()

    def update_sustainability_widget(self):
        # Calculate trees saved based on the number of files (Assume 10 files = 1/10 of a tree)
        num_trees_saved = self.num_files // 10
        self.sustainability_info_label.config(text=f"You saved {num_trees_saved} trees by uploading {self.num_files} files.")

    def dummy_function(self):
        # Placeholder function for button commands
        print("Button clicked!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ClassiFileApp(root)
    root.mainloop()
