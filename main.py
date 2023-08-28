import tkinter as tk

def press(button_name):
    print(f"Button '{button_name}' pressed!")

def arrange_files_alphabetically(file_list):
    sorted_files = sorted(file_list)
    print("Files arranged alphabetically:", sorted_files)

def increment_files():
    global num_files
    num_files += 1
    update_sustainability_widget()

def update_sustainability_widget():
    num_trees_saved = num_files // 10
    sustainability_info_label.config(text=f"You saved {num_trees_saved} trees by uploading {num_files} files.")

def create_account():
    print("Create Account button clicked!")

def organize_files():
    print("Organize Files button clicked!")

root = tk.Tk(className='ClassiFile')
root.configure(bg="#f0f0f0")

# Page Title
page_title = tk.Label(root, text="ClassiFile - Classing your Files", font=("Helvetica", 24, "bold"), fg="#007BFF")
page_title.pack(pady=20)

# Sustainability Widget
sustainability_label = tk.Label(root, text="Sustainability Widget", font=("Helvetica", 16))
sustainability_label.pack(pady=20)

# Dummy files
dummy_files = ["file3.txt", "file1.doc", "file4.pdf", "file2.png", "file5.xlsx"]
num_files = len(dummy_files)
num_trees_saved = num_files // 10

sustainability_info_label = tk.Label(root, text=f"You saved {num_trees_saved} trees by uploading {num_files} files.", font=("Helvetica", 12))
sustainability_info_label.pack(pady=10)

# Arrange Files Buttons
arrange_alphabetically_btn = tk.Button(root, text="Arrange Alphabetically", command=lambda: arrange_files_alphabetically(dummy_files), bg="#9C27B0", fg="white", font=("Helvetica", 12), padx=20, pady=10)
arrange_alphabetically_btn.pack(pady=10)

# Buttons
upload_btn = tk.Button(root, text="Upload Files", command=lambda: press("Upload Files"), bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=20, pady=10)
upload_btn.pack(pady=10)

create_account_btn = tk.Button(root, text="Create Account", command=lambda: press("Create Account"), bg="#007BFF", fg="white", font=("Helvetica", 12), padx=20, pady=10)
create_account_btn.pack(pady=10)

organize_files_btn = tk.Button(root, text="Organize Files", command=lambda: press("Organize Files"), bg="#FFC107", fg="white", font=("Helvetica", 12), padx=20, pady=10)
organize_files_btn.pack(pady=10)

root.mainloop()
