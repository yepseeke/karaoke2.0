import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from database import DataBase, Filter


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

        self.main_menu = MainMenu(self)

        self.mainloop()


class MainMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.language_page = LanguagePage(self)
        self.setting_page = SettingsPage(self)

        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text='KARAЁКЕ', background='red')
        label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        play_button = tk.Button(self, text='PLAY', command=self.show_language_page)
        play_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        settings_button = tk.Button(self, text='SETTINGS', command=self.show_settings_page)
        settings_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        exit_button = tk.Button(self, text='EXIT', command=self.master.quit)
        exit_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def show_language_page(self):
        self.language_page.create_widgets()
        self.language_page.tkraise()

    def show_settings_page(self):
        self.setting_page.create_widgets()
        self.setting_page.tkraise()


class LanguagePage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        flags_path = 'data/flags'
        self.image_russia = ImageTk.PhotoImage(Image.open(flags_path + '/russia-flag.jpg'))
        self.image_ukraine = ImageTk.PhotoImage(Image.open(flags_path + '/ukraine-flag.jpg'))
        self.image_usa = ImageTk.PhotoImage(Image.open(flags_path + '/usa-flag.jpg'))
        self.image_france = ImageTk.PhotoImage(Image.open(flags_path + '/france-flag.png'))

        self.place(x=0, y=0, relwidth=1, relheight=1)

        self.columnconfigure((0, 1), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')

        self.songs_list = None

        # self.create_widgets()

        # self.create_widgets()

    def set_language(self, language: str):
        self.songs_list = SongsList(self, language)
        self.songs_list.create_widgets()
        self.songs_list.tkraise()

    def create_widgets(self):
        button_russian = tk.Button(self, image=self.image_russia, command=lambda: self.set_language('russian'))
        button_ukrainian = tk.Button(self, image=self.image_ukraine, command=lambda: self.set_language('ukrainian'))
        button_english = tk.Button(self, image=self.image_usa, command=lambda: self.set_language('english'))
        button_french = tk.Button(self, image=self.image_france, command=lambda: self.set_language('french'))

        back_button = tk.Button(self, text='BACK', command=self.show_main_menu)

        button_russian.grid(row=0, column=0, sticky='nsew')
        button_ukrainian.grid(row=0, column=1, sticky='nsew')
        button_english.grid(row=1, column=0, sticky='nsew')
        button_french.grid(row=1, column=1, sticky='nsew')
        back_button.grid(row=2, column=0, columnspan=2)

    def show_main_menu(self):
        self.destroy()
        self.parent.create_widgets()
        self.parent.tkraise()


class SongsList(tk.Frame):
    def __init__(self, parent, language):
        super().__init__(parent)
        self.parent = parent
        self.language = language
        self.db = DataBase()

        self.place(x=0, y=0, relwidth=1, relheight=1)

    def create_widgets(self):
        table = ttk.Treeview(self, columns=('singer', 'song'), show='headings')
        table.heading('singer', text='Song name')
        table.heading('song', text='Singer')

        table.pack(fill='both', expand=True)

        language_filter = Filter({'language': self.language})
        filtered = self.db.filter_db(language_filter)

        for i in range(len(filtered)):
            singer = filtered[i].get('singer')
            song = filtered[i].get('song')
            insert_data = (singer, song)
            table.insert(parent='', index=0, values=insert_data)


class SettingsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.place(x=0, y=0, relwidth=1, relheight=1)

    def create_widgets(self):
        back_button = tk.Button(self, text="BACK", width=15, command=self.show_main_menu)
        back_button.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

    def show_main_menu(self):
        self.pack_forget()
        self.parent.create_widgets()
        # self.parent.tkraise()


App(title='Classes based app', size=(800, 600))
