import csv
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


def add_expense(self):
    expense = self.expense_entry.get()
    item = self.item_entry.get()
    category = self.category_var.get()
    date = self.date_entry.get()
    if expense and date:
        self.expenses.append((expense, item, category, date))
        self.expense_listbox.insert(
            tk.END, f"{expense} - {item} - {category} ({date})"
        )
        self.expense_entry.delete(0, tk.END)
        self.item_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Expense and Date cannot be empty.")
    self.update_total_label()


def edit_expense(self):
    selected_index = self.expense_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        selected_expense = self.expenses[selected_index]
        new_expense = simpledialog.askstring(
            "Edit Expense", "Enter new expense:", initialvalue=selected_expense[0]
        )
        if new_expense:
            self.expenses[selected_index] = (
                new_expense,
                selected_expense[1],
                selected_expense[2],
                selected_expense[3],
            )
            self.refresh_list()
            self.update_total_label()


def delete_expense(self):
    selected_index = self.expense_listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        del self.expenses[selected_index]
        self.expense_listbox.delete( selected_index )
        self.update_total_label()


def save_expenses(self):
    with open("expenses.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        column_headers = ["Expense Amount", "Item Description", "Category", "Date"]
        writer.writerow(column_headers)
        for expense in self.expenses:
            writer.writerow(expense)