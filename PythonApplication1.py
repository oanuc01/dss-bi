import tkinter as tk
from tkinter import ttk, messagebox

class FamilyTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Family Tree Application")

        # Tạo danh sách để lưu thành viên gia đình
        self.family_tree = []

        # Combobox chọn Parent Name
        self.parent_name_var = tk.StringVar()
        ttk.Label(root, text="Parent Name:").grid(row=0, column=0, padx=10, pady=10)
        self.parent_combobox = ttk.Combobox(root, textvariable=self.parent_name_var)
        self.parent_combobox.grid(row=0, column=1, padx=10, pady=10)

        # Filter by Gender
        self.gender_filter_var = tk.StringVar()
        ttk.Label(root, text="Filter by Gender:").grid(row=1, column=0, padx=10, pady=10)
        self.gender_combobox = ttk.Combobox(root, textvariable=self.gender_filter_var, values=["All", "Male", "Female"])
        self.gender_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.gender_combobox.set("All")

        # Filter by Generation
        self.generation_filter_var = tk.StringVar()
        ttk.Label(root, text="Filter by Generation:").grid(row=2, column=0, padx=10, pady=10)
        self.generation_combobox = ttk.Combobox(root, textvariable=self.generation_filter_var, values=["All", "1", "2", "3", "4"])
        self.generation_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.generation_combobox.set("All")

        # Frame để chứa danh sách các con
        self.children_frame = ttk.Frame(root)
        self.children_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Nút Add Child Field để thêm trường con
        ttk.Button(root, text="Add Child Field", command=self.add_child_field).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Nút Add Child để thêm vào danh sách cây gia phả
        ttk.Button(root, text="Add Child", command=self.add_child).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Listbox để hiển thị thành viên gia đình
        self.family_listbox = tk.Listbox(root)
        self.family_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Lưu trữ danh sách các trường con
        self.children_fields = []

        # Hiển thị lại dữ liệu
        self.refresh_tree()

    def add_child_field(self):
        """Thêm các trường để nhập thông tin về một đứa trẻ mới."""
        row = len(self.children_fields) + 1

        child_name_var = tk.StringVar()
        child_gender_var = tk.StringVar()
        child_generation_var = tk.IntVar()
        child_note_var = tk.StringVar()
        has_children_var = tk.BooleanVar()

        ttk.Label(self.children_frame, text=f"Child {row} Name:").grid(row=row, column=0, padx=5, pady=5)
        ttk.Entry(self.children_frame, textvariable=child_name_var).grid(row=row, column=1, padx=5, pady=5)

        ttk.Label(self.children_frame, text="Gender:").grid(row=row, column=2, padx=5, pady=5)
        ttk.Combobox(self.children_frame, textvariable=child_gender_var, values=["Male", "Female"]).grid(row=row, column=3, padx=5, pady=5)

        ttk.Label(self.children_frame, text="Generation:").grid(row=row, column=4, padx=5, pady=5)
        ttk.Combobox(self.children_frame, textvariable=child_generation_var, values=[1, 2, 3, 4]).grid(row=row, column=5, padx=5, pady=5)

        ttk.Label(self.children_frame, text="Note:").grid(row=row, column=6, padx=5, pady=5)
        ttk.Entry(self.children_frame, textvariable=child_note_var).grid(row=row, column=7, padx=5, pady=5)

        ttk.Checkbutton(self.children_frame, text="Has Children", variable=has_children_var).grid(row=row, column=8, padx=5, pady=5)

        # Lưu tất cả thông tin trường mới vào danh sách
        self.children_fields.append({
            "name_var": child_name_var,
            "gender_var": child_gender_var,
            "generation_var": child_generation_var,
            "note_var": child_note_var,
            "has_children_var": has_children_var
        })

    def add_child(self):
        """Thêm tất cả các con vào cây gia phả."""
        parent_name = self.parent_name_var.get()

        for child_field in self.children_fields:
            child_name = child_field["name_var"].get()
            gender = child_field["gender_var"].get()
            generation = child_field["generation_var"].get()
            has_children = child_field["has_children_var"].get()
            note = child_field["note_var"].get()

            if child_name and gender and generation:
                child = {
                    "parent": parent_name,
                    "name": child_name,
                    "gender": gender,
                    "generation": generation,
                    "has_children": has_children,
                    "note": note
                }
                self.family_tree.append(child)
            else:
                messagebox.showerror("Error", "Please fill all fields for all children!")

        # Sau khi thêm, làm mới lại danh sách hiển thị
        self.refresh_tree()

    def refresh_tree(self):
        """Cập nhật hiển thị danh sách thành viên gia đình."""
        self.family_listbox.delete(0, tk.END)

        # Lọc theo gender
        gender_filter = self.gender_filter_var.get()
        generation_filter = self.generation_filter_var.get()

        for member in self.family_tree:
            if (gender_filter == "All" or member["gender"] == gender_filter) and (generation_filter == "All" or str(member["generation"]) == generation_filter):
                self.family_listbox.insert(tk.END, f"{member['name']} ({member['gender']}, Gen: {member['generation']})")


# Khởi động ứng dụng
root = tk.Tk()
app = FamilyTreeApp(root)
root.mainloop()
