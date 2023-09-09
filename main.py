import tkinter as tk

root = tk.Tk()
root.title('ClassiFile')
root.configure(bg="#f0f0f0")


def create():
    create_account()


create_account_btn = tk.Button(root, text="Create Account", command=create, bg="#007BFF", fg="white",
                               font=("Helvetica", 12), padx=20, pady=10)
create_account_btn.pack(pady=10)


def create_account():
    print("Your Account has been successfully created!")


def upload():
    press("Upload Files")


upload_btn = tk.Button(root, text="Upload Files", command=upload, bg="#4CAF50", fg="white", font=("Helvetica", 12),
                       padx=20, pady=10)
upload_btn.pack(pady=10)


def organize_files():
    print("Files being classed...")


def press(button_name):
    if button_name == "Upload Files":
        print("Your files will be uploaded soon!")
    else:
        print(f"Button '{button_name}' pressed!")


def arrange_files_alphabetically(file_list):
    sorted_files = sorted(file_list)
    print("Files arranged alphabetically:", sorted_files)


def arrange_files_by_length(file_list):
    sorted_files = sorted(file_list, key=lambda x: len(x))
    print("Files arranged by length (shortest to longest):", sorted_files)


# Page Title
page_title = tk.Label(root, text="ClassiFile - Classing your Files", font=("Helvetica", 24, "bold"), fg="#007BFF")
page_title.pack(pady=20)

# Sustainability Widget
sustainability_label = tk.Label(root, text="Sustainability Widget", font=("Helvetica", 16))
sustainability_label.pack(pady=20)


def update_sustainability_widget():
    sustainability_info_label.config(text=f"You saved {num_trees_saved} trees by uploading {num_files} files.")


def increment_files():
    global num_files
    num_files += 1
    update_sustainability_widget()


# Dummy files
dummy_files = [
    "TechBasics1.pdf",
    "Bachelor_Thesis.docx",
    "Minor_VWL.docx",
    "ToDoList.pdf",
    "Autumn_Plans.ppt",
    "TechBasics1_Hany.py",
    "Literature_Reading_List.txt",
    "Economics_Research_Paper.docx",
    "DigitalMedia_Bachelor.zip",
    "Student_Transcript.pdf"
]

num_files = len(dummy_files)
num_trees_saved = num_files // 5

sustainability_info_label = tk.Label(root, text=f"You saved {num_trees_saved} trees by uploading {num_files} files.",
                                     font=("Helvetica", 12))
sustainability_info_label.pack(pady=10)


# Organize Files

def organize():
    organize_files()


organize_files_btn = tk.Button(root, text="Organize Files", command=organize, bg="#FFC107", fg="white",
                               font=("Helvetica", 12), padx=20, pady=10)
organize_files_btn.pack(pady=10)


def arrange_alphabetically():
    arrange_files_alphabetically(dummy_files)


arrange_alphabetically_btn = tk.Button(root, text="Organize files alphabetically", command=arrange_alphabetically,
                                       bg="#9C27B0", fg="white", font=("Helvetica", 12), padx=20, pady=10)
arrange_alphabetically_btn.pack(pady=10)


def arrange_by_length():
    arrange_files_by_length(dummy_files)


arrange_by_length_btn = tk.Button(root, text="Organize files by Length", command=arrange_by_length, bg="#2196F3",
                                  fg="white",
                                  font=("Helvetica", 12), padx=20, pady=10)
arrange_by_length_btn.pack(pady=10)

root.mainloop()
