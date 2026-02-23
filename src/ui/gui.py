import tkinter as tk
from tkinter import ttk, messagebox
import re

from services.exercise_service import exercise_service
from services.user_service import user_service


class GymApplicationGUI:
    """Tkinter GUI for the gym training app."""

    VALID_COLUMNS = [
        "date_of_exercise",
        "exercise_type",
        "set_number",
        "repetitions",
        "weight",
    ]

    def __init__(self):
        self._exercise_service = exercise_service
        self._user_service = user_service

        self._root = tk.Tk()
        self._root.title("Gym Training App")
        self._root.geometry("750x550")
        self._root.resizable(False, False)

        self._container = tk.Frame(self._root)
        self._container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self._show_login()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _clear(self):
        for widget in self._container.winfo_children():
            widget.destroy()

    def _check_date_format(self, date):
        return bool(re.match(r'^\d{2}-\d{2}-\d{2}$', date))

    # ── Login screen ──────────────────────────────────────────────────────────

    def _show_login(self):
        self._clear()

        tk.Label(
            self._container,
            text="Welcome to the Gym Training App",
            font=("Helvetica", 18, "bold"),
        ).pack(pady=(60, 20))

        tk.Label(self._container, text="─" * 50).pack()

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=30)

        tk.Button(
            btn_frame, text="Login", width=22, height=2,
            command=self._show_login_form,
        ).pack(pady=8)
        tk.Button(
            btn_frame, text="Create New User", width=22, height=2,
            command=self._show_new_user_form,
        ).pack(pady=8)
        tk.Button(
            btn_frame, text="Quit", width=22, height=2,
            command=self._root.destroy,
        ).pack(pady=8)

    # ── Login form ────────────────────────────────────────────────────────────

    def _show_login_form(self):
        self._clear()

        tk.Label(
            self._container, text="Login", font=("Helvetica", 16, "bold")
        ).pack(pady=(40, 20))

        form = tk.Frame(self._container)
        form.pack(pady=10)

        tk.Label(form, text="Username:", anchor="e", width=16).grid(
            row=0, column=0, pady=8
        )
        username_var = tk.StringVar()
        tk.Entry(form, textvariable=username_var, width=26).grid(
            row=0, column=1, pady=8, padx=8
        )

        tk.Label(form, text="Password:", anchor="e", width=16).grid(
            row=1, column=0, pady=8
        )
        password_var = tk.StringVar()
        tk.Entry(form, textvariable=password_var, show="*", width=26).grid(
            row=1, column=1, pady=8, padx=8
        )

        def do_login():
            username = username_var.get()
            password = password_var.get()
            if self._user_service.login(username, password):
                self._show_main_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Login", width=15, command=do_login).grid(
            row=0, column=0, padx=8
        )
        tk.Button(
            btn_frame, text="Back", width=15, command=self._show_login
        ).grid(row=0, column=1, padx=8)

    # ── New user form ─────────────────────────────────────────────────────────

    def _show_new_user_form(self):
        self._clear()

        tk.Label(
            self._container, text="Create New User", font=("Helvetica", 16, "bold")
        ).pack(pady=(30, 15))

        form = tk.Frame(self._container)
        form.pack(pady=10)

        tk.Label(form, text="Username (≥4 chars):", anchor="e", width=22).grid(
            row=0, column=0, pady=8
        )
        username_var = tk.StringVar()
        tk.Entry(form, textvariable=username_var, width=26).grid(
            row=0, column=1, pady=8, padx=8
        )

        tk.Label(form, text="Password (≥4 chars):", anchor="e", width=22).grid(
            row=1, column=0, pady=8
        )
        password_var = tk.StringVar()
        tk.Entry(form, textvariable=password_var, show="*", width=26).grid(
            row=1, column=1, pady=8, padx=8
        )

        tk.Label(form, text="Repeat password:", anchor="e", width=22).grid(
            row=2, column=0, pady=8
        )
        password2_var = tk.StringVar()
        tk.Entry(form, textvariable=password2_var, show="*", width=26).grid(
            row=2, column=1, pady=8, padx=8
        )

        def do_create():
            username = username_var.get()
            password = password_var.get()
            password2 = password2_var.get()

            if len(username) < 4:
                messagebox.showerror("Error", "Username must be at least 4 characters.")
                return
            if len(password) < 4:
                messagebox.showerror("Error", "Password must be at least 4 characters.")
                return
            if password != password2:
                messagebox.showerror("Error", "Passwords do not match.")
                return

            created = self._user_service.new_user(username, password)
            if created:
                messagebox.showinfo("Success", "User created! Please log in.")
                self._show_login_form()
            else:
                messagebox.showerror(
                    "Error", "Username already taken. Please choose another."
                )

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=20)
        tk.Button(
            btn_frame, text="Create User", width=15, command=do_create
        ).grid(row=0, column=0, padx=8)
        tk.Button(
            btn_frame, text="Back", width=15, command=self._show_login
        ).grid(row=0, column=1, padx=8)

    # ── Main menu ─────────────────────────────────────────────────────────────

    def _show_main_menu(self):
        self._clear()

        username = self._user_service.user.username
        tk.Label(
            self._container,
            text=f"Welcome, {username}!",
            font=("Helvetica", 18, "bold"),
        ).pack(pady=(50, 8))
        tk.Label(
            self._container, text="MAIN MENU", font=("Helvetica", 12)
        ).pack(pady=(0, 20))

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="Add Exercise", width=28, height=2,
            command=self._show_add_exercise,
        ).pack(pady=8)
        tk.Button(
            btn_frame, text="View and Edit Past Exercises", width=28, height=2,
            command=self._show_view_exercises,
        ).pack(pady=8)
        tk.Button(
            btn_frame, text="Remove Profile", width=28, height=2,
            command=self._show_remove_user,
        ).pack(pady=8)
        tk.Button(
            btn_frame, text="Log Out", width=28, height=2,
            command=self._do_logout,
        ).pack(pady=8)

    def _do_logout(self):
        confirmed = messagebox.askyesno("Logout", "Are you sure you want to log out?")
        if confirmed:
            self._user_service.logout()
            self._show_login()

    # ── Add exercise ──────────────────────────────────────────────────────────

    def _show_add_exercise(self):
        self._clear()

        tk.Label(
            self._container, text="Add Exercise", font=("Helvetica", 16, "bold")
        ).pack(pady=(15, 3))
        tk.Label(
            self._container,
            text="Date format: DD-MM-YY  |  Weight with or without decimals",
            font=("Helvetica", 9),
            fg="gray",
        ).pack(pady=(0, 10))

        form = tk.Frame(self._container)
        form.pack(pady=5)

        fields = [
            ("Exercise name:", "exercise_type"),
            ("Set number (integer):", "set_number"),
            ("Repetitions (integer):", "repetitions"),
            ("Weight in kg:", "weight"),
            ("Date (DD-MM-YY):", "date"),
        ]

        vars_ = {}
        for i, (label, key) in enumerate(fields):
            tk.Label(form, text=label, anchor="e", width=22).grid(
                row=i, column=0, pady=6
            )
            v = tk.StringVar()
            tk.Entry(form, textvariable=v, width=26).grid(
                row=i, column=1, pady=6, padx=8
            )
            vars_[key] = v

        def do_add():
            exercise_type = vars_["exercise_type"].get().strip()
            set_number_str = vars_["set_number"].get().strip()
            repetitions_str = vars_["repetitions"].get().strip()
            weight_str = vars_["weight"].get().strip()
            date = vars_["date"].get().strip()

            if not exercise_type:
                messagebox.showerror("Error", "Exercise name cannot be empty.")
                return
            try:
                set_number = int(set_number_str)
            except ValueError:
                messagebox.showerror("Error", "Set number must be an integer.")
                return
            try:
                repetitions = int(repetitions_str)
            except ValueError:
                messagebox.showerror("Error", "Repetitions must be an integer.")
                return
            try:
                weight = float(weight_str)
            except ValueError:
                messagebox.showerror("Error", "Weight must be a number.")
                return
            if not self._check_date_format(date):
                messagebox.showerror("Error", "Date must be in DD-MM-YY format.")
                return

            added = self._exercise_service.create_exercise(
                exercise_type, set_number, repetitions, weight, date
            )
            if added:
                messagebox.showinfo("Success", "Exercise added successfully.")
                self._show_main_menu()
            else:
                messagebox.showerror("Error", "Failed to add exercise. Please try again.")

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=12)
        tk.Button(
            btn_frame, text="Add Exercise", width=15, command=do_add
        ).grid(row=0, column=0, padx=8)
        tk.Button(
            btn_frame, text="Back", width=15, command=self._show_main_menu
        ).grid(row=0, column=1, padx=8)

    # ── View exercises ────────────────────────────────────────────────────────

    def _show_view_exercises(self):
        self._clear()

        tk.Label(
            self._container, text="Past Exercises", font=("Helvetica", 16, "bold")
        ).pack(pady=(10, 5))

        filter_frame = tk.Frame(self._container)
        filter_frame.pack(pady=5)
        tk.Label(
            filter_frame, text="Filter by date (DD-MM-YY, blank = all):"
        ).pack(side=tk.LEFT)
        date_var = tk.StringVar()
        tk.Entry(filter_frame, textvariable=date_var, width=12).pack(
            side=tk.LEFT, padx=6
        )

        cols = (
            "Date", "Exercise Type", "Set", "Repetitions", "Weight (kg)", "Exercise-ID"
        )
        tree_frame = tk.Frame(self._container)
        tree_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        tree = ttk.Treeview(
            tree_frame, columns=cols, show="headings",
            yscrollcommand=scrollbar.set,
        )
        scrollbar.config(command=tree.yview)

        col_widths = [80, 160, 45, 90, 90, 185]
        for col, w in zip(cols, col_widths):
            tree.heading(col, text=col)
            tree.column(col, width=w, anchor=tk.CENTER)

        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        def load_exercises():
            for row in tree.get_children():
                tree.delete(row)
            date = date_var.get().strip()
            if date:
                if not self._check_date_format(date):
                    messagebox.showerror("Error", "Date must be in DD-MM-YY format.")
                    return
                exercises = self._exercise_service.get_exercises_by_date(date)
            else:
                exercises = self._exercise_service.get_exercises()
            for ex in exercises:
                tree.insert("", tk.END, values=ex)

        load_exercises()

        def on_edit():
            selection = tree.selection()
            if not selection:
                messagebox.showerror("Error", "Please select an exercise to edit.")
                return
            exercise_id = tree.item(selection[0])["values"][5]
            self._show_edit_exercise(exercise_id)

        def on_delete():
            selection = tree.selection()
            if not selection:
                messagebox.showerror("Error", "Please select an exercise to delete.")
                return
            exercise_id = tree.item(selection[0])["values"][5]
            confirmed = messagebox.askyesno(
                "Confirm Delete", f"Delete exercise '{exercise_id}'?"
            )
            if confirmed:
                self._exercise_service.delete_exercise(exercise_id)
                load_exercises()

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=8)
        tk.Button(
            btn_frame, text="Load / Filter", width=13, command=load_exercises
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame, text="Edit Selected", width=13, command=on_edit
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            btn_frame, text="Delete Selected", width=13, command=on_delete
        ).grid(row=0, column=2, padx=5)
        tk.Button(
            btn_frame, text="Back", width=13, command=self._show_main_menu
        ).grid(row=0, column=3, padx=5)

    # ── Edit exercise ─────────────────────────────────────────────────────────

    def _show_edit_exercise(self, exercise_id):
        self._clear()

        tk.Label(
            self._container, text="Edit Exercise", font=("Helvetica", 16, "bold")
        ).pack(pady=(40, 5))
        tk.Label(
            self._container,
            text=f"Exercise ID: {exercise_id}",
            font=("Helvetica", 10),
            fg="gray",
        ).pack(pady=(0, 20))

        form = tk.Frame(self._container)
        form.pack(pady=10)

        tk.Label(form, text="Field to change:", anchor="e", width=18).grid(
            row=0, column=0, pady=10
        )
        column_var = tk.StringVar()
        column_combo = ttk.Combobox(
            form,
            textvariable=column_var,
            values=self.VALID_COLUMNS,
            state="readonly",
            width=23,
        )
        column_combo.grid(row=0, column=1, pady=10, padx=8)
        column_combo.current(0)

        tk.Label(form, text="New value:", anchor="e", width=18).grid(
            row=1, column=0, pady=10
        )
        value_var = tk.StringVar()
        tk.Entry(form, textvariable=value_var, width=26).grid(
            row=1, column=1, pady=10, padx=8
        )

        def do_edit():
            column = column_var.get()
            new_value = value_var.get().strip()
            if not new_value:
                messagebox.showerror("Error", "New value cannot be empty.")
                return
            edited = self._exercise_service.edit_exercise(column, new_value, exercise_id)
            if edited:
                messagebox.showinfo("Success", "Exercise updated successfully.")
                self._show_view_exercises()
            else:
                messagebox.showerror("Error", "Failed to update exercise.")

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Save", width=15, command=do_edit).grid(
            row=0, column=0, padx=8
        )
        tk.Button(
            btn_frame, text="Cancel", width=15, command=self._show_view_exercises
        ).grid(row=0, column=1, padx=8)

    # ── Remove user ───────────────────────────────────────────────────────────

    def _show_remove_user(self):
        self._clear()

        tk.Label(
            self._container, text="Remove Profile", font=("Helvetica", 16, "bold")
        ).pack(pady=(25, 5))
        tk.Label(
            self._container,
            text="WARNING: This will permanently delete your account and all exercises.",
            fg="red",
            font=("Helvetica", 11, "bold"),
            wraplength=620,
        ).pack(pady=(0, 15))
        tk.Label(
            self._container, text="To confirm, enter your credentials below:"
        ).pack(pady=(0, 10))

        form = tk.Frame(self._container)
        form.pack(pady=5)

        tk.Label(form, text="Username:", anchor="e", width=15).grid(
            row=0, column=0, pady=8
        )
        username_var = tk.StringVar()
        tk.Entry(form, textvariable=username_var, width=26).grid(
            row=0, column=1, pady=8, padx=8
        )

        tk.Label(form, text="Password:", anchor="e", width=15).grid(
            row=1, column=0, pady=8
        )
        password_var = tk.StringVar()
        tk.Entry(form, textvariable=password_var, show="*", width=26).grid(
            row=1, column=1, pady=8, padx=8
        )

        def do_remove():
            username = username_var.get()
            password = password_var.get()
            confirmed = messagebox.askyesno(
                "Final Confirmation",
                "Are you absolutely sure you want to delete your profile?",
            )
            if not confirmed:
                return
            deleted = self._user_service.delete_user(username, password)
            if deleted:
                self._user_service.logout()
                messagebox.showinfo("Done", "Profile removed successfully.")
                self._show_login()
            else:
                messagebox.showerror("Error", "Invalid username or password.")

        btn_frame = tk.Frame(self._container)
        btn_frame.pack(pady=20)
        tk.Button(
            btn_frame, text="Delete Profile", width=15, fg="red", command=do_remove
        ).grid(row=0, column=0, padx=8)
        tk.Button(
            btn_frame, text="Cancel", width=15, command=self._show_main_menu
        ).grid(row=0, column=1, padx=8)

    # ── Run ───────────────────────────────────────────────────────────────────

    def start(self):
        self._root.mainloop()
