import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

DAYZ_FOLDER = os.path.join(os.getenv('LOCALAPPDATA'), 'DayZ')
FILE_EXTENSIONS = ('.log', '.RPT', '.mdmp')


def delete_files():
    total_size = 0
    files_deleted = False

    if not os.path.exists(DAYZ_FOLDER):
        messagebox.showerror("Error", "DayZ folder not found.")
        return

    for root, _, files in os.walk(DAYZ_FOLDER):
        for file in files:
            if file.lower().endswith(FILE_EXTENSIONS):
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    os.remove(file_path)
                    files_deleted = True
                except OSError:
                    pass

    if files_deleted:
        if total_size > 1024:
            if total_size > 1048576:
                total_size_mb = total_size / 1048576
                messagebox.showinfo("Cleanup Complete", f"Total size of deleted files: {total_size_mb:.2f} MB")
            else:
                total_size_kb = total_size / 1024
                messagebox.showinfo("Cleanup Complete", f"Total size of deleted files: {total_size_kb:.2f} KB")
        else:
            messagebox.showinfo("Cleanup Complete", f"Total size of deleted files: {total_size} bytes")
    else:
        messagebox.showinfo("Cleanup Complete", "No files were deleted.")


def start_dayz():
    os.system("start steam://rungameid/221100")
    exit()


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


if __name__ == '__main__':
    window = tk.Tk()
    window.title("DayZ Cleanup")

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 12), padding=10)
    style.configure('TLabel', font=('Arial', 12), padding=10)

    main_frame = ttk.Frame(window)
    main_frame.pack(pady=20)

    start_button = ttk.Button(main_frame, text="Start DayZ", command=start_dayz)
    start_button.pack(pady=10)

    cleanup_button = ttk.Button(main_frame, text="Clean Up Files", command=delete_files)
    cleanup_button.pack(pady=10)

    window_width = 400
    window_height = main_frame.winfo_height() + 200
    window.geometry(f"{window_width}x{window_height}")

    center_window(window)
    window.mainloop()
