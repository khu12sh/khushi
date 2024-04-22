import tkinter as tk
from tkinter import messagebox

class EmployeeManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Management System")

        self.label_name = tk.Label(master, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="e")
        self.entry_name = tk.Entry(master)
        self.entry_name.grid(row=0, column=1)

        self.label_id = tk.Label(master, text="ID:")
        self.label_id.grid(row=1, column=0, sticky="e")
        self.entry_id = tk.Entry(master)
        self.entry_id.grid(row=1, column=1)

        self.label_position = tk.Label(master, text="Position:")
        self.label_position.grid(row=2, column=0, sticky="e")
        self.entry_position = tk.Entry(master)
        self.entry_position.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.list_button = tk.Button(master, text="List Employees", command=self.list_employees)
        self.list_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.employees = []

    def add_employee(self):
        name = self.entry_name.get()
        employee_id = self.entry_id.get()
        position = self.entry_position.get()

        if name and employee_id and position:
            self.employees.append({"name": name, "id": employee_id, "position": position})
            messagebox.showinfo("Success", "Employee added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def list_employees(self):
        if self.employees:
            employee_list = "\n".join([f"Name: {emp['name']}, ID: {emp['id']}, Position: {emp['position']}" for emp in self.employees])
            messagebox.showinfo("Employee List", employee_list)
        else:
            messagebox.showinfo("Employee List", "No employees added yet.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
        self.entry_position.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
