import configparser
import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import os
import pygame

window = Tk()
config = configparser.ConfigParser()
import shutil

window.geometry('285x675')
window.minsize(285, 285)
window.maxsize(285, 825)
window.title('GTA4 Codes')
config.read("cheat_codes.ini")

pygame.mixer.init()  # Initialize the mixer
pygame.mixer.music.load('GTA4_Music.mp3')  # Load your music file
pygame.mixer.music.play(-1)

def main():
    shutil.copy("cheat_codes.ini", config['Settings']['backup_dir'])
    def default_theme():
        if font == "arial":
            window.geometry('285x695')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        print(font)
        global bg_color
        global fg_color
        bg_color = config['Settings']['bg_color']
        fg_color = config['Settings']['fg_color']
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def lightblue_theme():
        if font == "arial":
            window.geometry('285x695')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        print(font)
        global bg_color
        global fg_color
        bg_color = 'light sky blue'
        fg_color = 'RoyalBlue4'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def darkblue_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'midnight blue'
        fg_color = 'RoyalBlue1'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def red_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'red4'
        fg_color = 'ivory2'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def yellow_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'goldenrod'
        fg_color = 'lightgoldenrod'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def black_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'gray1'
        fg_color = 'gray64'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def lightpurple_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'MediumPurple1'
        fg_color = 'purple4'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def darkpurple_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'purple4'
        fg_color = 'MediumPurple1'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def lightpink_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'orchid1'
        fg_color = 'DeepPink4'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def darkpink_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'maroon4'
        fg_color = 'orchid1'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def blackpink_theme():
        if font == "arial":
            window.geometry('285x690')
        elif font == "cambria":
            window.geometry('285x708')
        elif font == "sylfaen":
            window.geometry('285x825')
        elif font == "candara":
            window.geometry('285x715')
        global bg_color
        global fg_color
        bg_color = 'gray5'
        fg_color = 'orchid1'
        window.configure(bg=bg_color)
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def default_font():
        global font
        window.geometry('285x695')
        font = 'arial'
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def cambria_font():
        global font
        window.geometry('285x708')
        text1.destroy()
        font = 'cambria'
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def sylfaen_font():
        global font
        window.geometry('285x825')
        text1.destroy()
        font = 'sylfaen'
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def candara_font():
        global font
        window.geometry('285x715')
        text1.destroy()
        font = 'candara'
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        main()

    def s_default_theme():
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        window.geometry("285x285")
        def next():
            theme = menu.get()
            if theme == 'Light Blue':
                global bg_color
                global fg_color
                bg_color = 'light sky blue'
                fg_color = 'RoyalBlue4'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Dark Blue':
                bg_color = 'midnight blue'
                fg_color = 'RoyalBlue1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Red':
                bg_color = 'red4'
                fg_color = 'ivory2'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Yellow':
                bg_color = 'goldenrod'
                fg_color = 'lightgoldenrod'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Black':
                bg_color = 'gray1'
                fg_color = 'gray64'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Light Purple':
                bg_color = 'MediumPurple1'
                fg_color = 'purple4'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Dark Purple':
                bg_color = 'purple4'
                fg_color = 'MediumPurple1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Light Pink':
                bg_color = 'orchid1'
                fg_color = 'DeepPink4'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Dark Pink':
                bg_color = 'maroon4'
                fg_color = 'orchid1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")

            elif theme == 'Blackpink':
                bg_color = 'gray5'
                fg_color = 'orchid1'
                window.configure(background=bg_color)
                config['Settings'] = {'bg_color': bg_color,
                                      'fg_color': fg_color,
                                      'font': config['Settings']['font'],
                                      'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                t_drop_title.destroy()
                t_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{theme} saved as your default theme successfully")
            if font == "arial":
                window.geometry('285x690')
            elif font == "cambria":
                window.geometry('285x708')
            elif font == "sylfaen":
                window.geometry('285x825')
            elif font == "candara":
                window.geometry('285x715')
            main()

        def changed_option(selected_option):
            theme = menu.get()
            global fg_color
            global bg_color

            if theme == 'Light Blue':
                global bg_color
                global fg_color
                bg_color = 'light sky blue'
                fg_color = 'RoyalBlue4'
                window.configure(background=bg_color)

            elif theme == 'Dark Blue':
                bg_color = 'midnight blue'
                fg_color = 'RoyalBlue1'
                window.configure(background=bg_color)

            elif theme == 'Red':
                bg_color = 'red4'
                fg_color = 'ivory2'
                window.configure(background=bg_color)

            elif theme == 'Yellow':
                bg_color = 'goldenrod'
                fg_color = 'lightgoldenrod'
                window.configure(background=bg_color)

            elif theme == 'Black':
                bg_color = 'gray1'
                fg_color = 'gray64'
                window.configure(background=bg_color)

            elif theme == 'Light Purple':
                bg_color = 'MediumPurple1'
                fg_color = 'purple4'
                window.configure(background=bg_color)

            elif theme == 'Dark Purple':
                bg_color = 'purple4'
                fg_color = 'MediumPurple1'
                window.configure(background=bg_color)

            elif theme == 'Light Pink':
                bg_color = 'orchid1'
                fg_color = 'DeepPink4'
                window.configure(background=bg_color)
                config.read("cheat_codes.ini")

            elif theme == 'Dark Pink':
                bg_color = 'maroon4'
                fg_color = 'orchid1'
                window.configure(background=bg_color)

            elif theme == 'Blackpink':
                bg_color = 'gray5'
                fg_color = 'orchid1'
                window.configure(background=bg_color)

            t_style.configure("TMenubutton", background=fg_color, foreground=bg_color)
            t_drop_title.configure(fg=fg_color, bg=bg_color)
            Next.configure(fg=fg_color, bg=bg_color)
            Back.configure(fg=fg_color, bg=bg_color)

        menubar.destroy()
        menu = StringVar(window)
        options = ['Light Blue', 'Dark Blue', 'Red', 'Yellow', 'Black', 'Light Purple', 'Dark Purple', 'Light Pink',
                   'Dark Pink', 'Blackpink']
        global fg_color
        global bg_color
        t_drop_title = Label(window, text='Select a theme to set as default theme', fg=fg_color, bg=bg_color,
                             activebackground=fg_color, activeforeground=bg_color, font=(font, 12))
        t_drop_title.pack(pady=(0, 10))
        t_drop = ttk.OptionMenu(window, menu, 'Select a theme', *(options), command=changed_option)
        t_drop.pack(pady=(0, 20))

        t_style = ttk.Style()
        t_style.configure("TMenubutton", background=fg_color, foreground=bg_color, font=font)

        Next = Button(window, text='Save changes', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=next)
        Next.pack(pady=(10, 0))

        def back():
            if font == "arial":
                window.geometry('285x690')
            elif font == "cambria":
                window.geometry('285x708')
            elif font == "sylfaen":
                window.geometry('285x825')
            elif font == "candara":
                window.geometry('285x715')

            global fg_color
            global bg_color
            fg_color = config['Settings']['fg_color']
            bg_color = config['Settings']['bg_color']
            window.configure(background=bg_color)
            t_drop.destroy()
            t_drop_title.destroy()
            Next.destroy()
            Back.destroy()
            main()

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.place(y=260)

    def s_default_font():
        text1.destroy()
        for variable in config["Cheats"]:
            button_name = f"section_{variable}"
            if button_name == "section_Settings":
                continue
            else:
                section_buttons[button_name].destroy()
        window.geometry("285x285")
        def next():
            theme = menu.get()
            global font
            if theme == 'arial':
                font = "arial"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")

            elif theme == 'cambria':
                font = "cambria"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")

            elif theme == 'sylfaen':
                font = "sylfaen"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
                showinfo("Saved", f"{font.title()} saved as your default font successfully")

            elif theme == 'candara':
                font = "candara"
                config['Settings'] = {'bg_color': config['Settings']['bg_color'],
                                      'fg_color': config['Settings']['fg_color'],
                                      'font': font, 'backup_dir': config['Settings']['backup_dir']}
                with open("cheat_codes.ini", 'w') as config_file:
                    config.write(config_file)
                showinfo("Saved", f"{font.title()} saved as your default font successfully")
                f_drop_title.destroy()
                f_drop.destroy()
                Next.destroy()
                Back.destroy()
            if font == "arial":
                window.geometry('285x690')
            elif font == "cambria":
                window.geometry('285x708')
            elif font == "sylfaen":
                window.geometry('285x825')
            elif font == "candara":
                window.geometry('285x715')
            main()

        def changed_option(selected_option):
            theme = menu.get()
            global font

            if theme == 'arial':
                font = 'arial'

            elif theme == 'cambria':
                font = 'cambria'


            elif theme == 'sylfaen':
                font = 'sylfaen'

            elif theme == 'candara':
                font = 'candara'

            f_style.configure("TMenubutton", font=font)
            f_drop_title.configure(font=font)
            Next.configure(font=font)

        global fg_color
        global bg_color
        global font
        menubar.destroy()
        menu = StringVar(window)
        f_options = ['arial', 'cambria', 'sylfaen', 'candara']
        f_drop_title = Label(window, text='Select a font to set as default font', fg=fg_color, bg=bg_color,
                             activebackground=fg_color, activeforeground=bg_color, font=(font, 12))
        f_drop_title.pack(pady=(0, 10))
        f_drop = ttk.OptionMenu(window, menu, 'Choose one', *(f_options), command=changed_option)
        f_drop.pack(pady=(0, 20))

        f_style = ttk.Style()
        f_style.configure("TMenubutton", background=fg_color, foreground=bg_color, font=font)

        Next = Button(window, text='Save changes', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=next)
        Next.pack(pady=(10, 0))

        def back():
            if font == "arial":
                window.geometry('285x690')
            elif font == "cambria":
                window.geometry('285x708')
            elif font == "sylfaen":
                window.geometry('285x825')
            elif font == "candara":
                window.geometry('285x715')

            global fg_color
            global bg_color
            fg_color = config['Settings']['fg_color']
            bg_color = config['Settings']['bg_color']
            window.configure(background=bg_color)
            f_drop.destroy()
            f_drop_title.destroy()
            Next.destroy()
            Back.destroy()
            main()

        Back = Button(window, text='Back', fg=fg_color, bg=bg_color, activebackground=fg_color,
                      activeforeground=bg_color, command=back)
        Back.place(y=260)
    global bg_color
    global fg_color
    global font
    menubar = Menu(window, fg=fg_color, bg=bg_color)

    themes = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    themes.add_command(label='Default', activebackground=fg_color, activeforeground=bg_color, command=default_theme,
                       font=font)
    themes.add_command(label='Light Blue', activebackground=fg_color, activeforeground=bg_color,
                       command=lightblue_theme, font=font)
    themes.add_command(label='Dark Blue', activebackground=fg_color, activeforeground=bg_color, command=darkblue_theme,
                       font=font)
    themes.add_command(label='red', activebackground=fg_color, activeforeground=bg_color, command=red_theme, font=font)
    themes.add_command(label='yellow', activebackground=fg_color, activeforeground=bg_color, command=yellow_theme,
                       font=font)
    themes.add_command(label='black', activebackground=fg_color, activeforeground=bg_color, command=black_theme,
                       font=font)
    themes.add_command(label='Black Pink', activebackground=fg_color, activeforeground=bg_color,
                       command=blackpink_theme, font=font)
    themes.add_command(label='Light Purple', activebackground=fg_color, activeforeground=bg_color,
                       command=lightpurple_theme, font=font)
    themes.add_command(label='Dark Purple', activebackground=fg_color, activeforeground=bg_color,
                       command=darkpurple_theme, font=font)
    themes.add_command(label='Light Pink', activebackground=fg_color, activeforeground=bg_color,
                       command=lightpink_theme, font=font)
    themes.add_command(label='Dark Pink', activebackground=fg_color, activeforeground=bg_color, command=darkpink_theme,
                       font=font)
    menubar.add_cascade(label='Themes', activebackground=fg_color, activeforeground=bg_color, menu=themes, font=font)

    fonts = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    fonts.add_command(label='arial', activebackground=fg_color, activeforeground=bg_color, command=default_font,
                      font='arial')
    fonts.add_command(label='Cambria', activebackground=fg_color, activeforeground=bg_color, command=cambria_font,
                      font='cambria')
    fonts.add_command(label='Sylfaen', activebackground=fg_color, activeforeground=bg_color, command=sylfaen_font,
                      font='sylfaen')
    fonts.add_command(label='Candara', activebackground=fg_color, activeforeground=bg_color, command=candara_font,
                      font='candara')
    menubar.add_cascade(label='Fonts', activebackground=fg_color, activeforeground=bg_color, menu=fonts, font=font)

    setting = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    setting.add_command(label='set a default theme', activebackground=fg_color, activeforeground=bg_color,
                        command=s_default_theme, font=font)
    setting.add_command(label='Set a default font', activebackground=fg_color, activeforeground=bg_color,
                        command=s_default_font, font=font)
    menubar.add_cascade(label='Setting', activebackground=fg_color, activeforeground=bg_color, menu=setting, font=font)

    credit = Menu(menubar, fg=fg_color, bg=bg_color, activebackground=fg_color, activeforeground=bg_color, tearoff=0)
    credit.add_command(label='Github', activebackground=fg_color, activeforeground=bg_color,
                       command=lambda: os.system('python -m webbrowser -t "https://github.com/BPGalaxy"'), font=font)
    credit.add_command(label='Telegram', activebackground=fg_color, activeforeground=bg_color,
                       command=lambda: os.system('python -m webbrowser -t "https://t.me/BP_Galaxy"'), font=font)
    menubar.add_cascade(label='Made by alireza', activebackground=fg_color, activeforeground=bg_color, menu=credit,
                        font=font)

    window.config(menu=menubar)

    text1 = Label(window, text="There's all GTA4 cheat codes\n for pc in this program", fg=fg_color, bg=bg_color, activebackground=fg_color,
                  activeforeground=bg_color, font=font)
    text1.pack(pady=(0,20))
    section_buttons = {}
    for variable in config["Cheats"]:
        button_name = f"section_{variable}"
        if button_name == 'section_Settings':
            continue
        else:
            section_buttons[button_name] = Button(window, text=variable, fg=fg_color, bg=bg_color,
                                                  activebackground=fg_color, activeforeground=bg_color,
                                                  font=font, command=lambda variable=variable: showinfo(message=config["Cheats"][variable]))
            section_buttons[button_name].pack(anchor='center',pady=(2,2))

def backup_folder():
    b_dir = tkinter.filedialog.askdirectory(mustexist=True, title='Select a backup dir')
    if b_dir == '':
        showerror("Error", "You must select a directory")
        backup_folder()
    else:
        config['Settings'] = {'bg_color': config['Settings']['bg_color'], 'fg_color': config['Settings']['fg_color'],
                              'font': config['Settings']['font'], 'backup_dir': b_dir}
        with open("cheat_codes.ini", 'w') as config_file:
            config.write(config_file)
        showinfo('Backup dir', 'Default backup dir saved successfully\nYou can change it anytime from menubar')
        global bg_color
        global fg_color
        global font
        bg_color = config['Settings']['bg_color']
        fg_color = config['Settings']['fg_color']
        font = config['Settings']['font']
        window.configure(bg=bg_color)
        return main()

def Setting():

    def recovery():
        yesno = askyesno("Question",
                         "Do you wanna recover your data?\n(only if you have a backup from database in database folder!)")
        if yesno is True:
            showinfo("Recovery",
                     f"You must select 'cheat_codes.ini' file to recovery your data\n(Hint:go to that directory")
            file = tkinter.filedialog.askopenfilename(title="Select 'cheat_codes.ini file'",
                                                      filetypes=[('Ini files', '*.ini')])

            if file == '':
                window.destroy()
            elif "cheat_codes.ini" in file and '#Database of "GTA4_Codes" app' in open(file, 'r').read():
                global bg_color
                global fg_color
                global font
                shutil.copyfile(file, "cheat_codes.ini")
                showinfo('copy', 'Datas recovered successfully')
                config.read('"cheat_codes.ini')
                config.read("cheat_codes.ini")
                bg_color = config['Settings']['bg_color']
                fg_color = config['Settings']['fg_color']
                font = config['Settings']['font']
                window.configure(bg=bg_color)
                return Setting()
            else:
                showerror("info", 'This is not a "My movies" database file')
                yesno = askyesno("Question", "Do you wanna try again?")
                if yesno is True:
                    recovery()
                else:
                    window.destroy()
        else:
            showinfo("Recovery", f"This app will make another database automatically\nBut your data will be removed")
            f = open("cheat_codes.ini", 'x')
            f.write(
                '#Database of "My movies" app\n[Settings]\nbg_color = snow\nfg_color = gainsboro\nfont = arial\nbackup_dir = none')
            f.close()

            config.read("cheat_codes.ini")
            bg_color = config['Settings']['bg_color']
            fg_color = config['Settings']['fg_color']
            font = config['Settings']['font']
            window.configure(bg=bg_color)
            return Setting()

    if os.path.exists("cheat_codes.ini"):
        config.read("cheat_codes.ini")
        if config['Settings']['backup_dir'] == 'none':
            showinfo('Backup dir',
                     'You must select a "cheat_codes.ini" to app be able to make auto backup from your datas there')
            backup_folder()
        else:
            config.read("cheat_codes.ini")
            global bg_color
            global fg_color
            global font
            bg_color = config['Settings']['bg_color']
            fg_color = config['Settings']['fg_color']
            font = config['Settings']['font']
            window.configure(bg=bg_color)
            return main()

    else:
        showerror('Error', "Database file(cheat_codes.ini) not found at 'G:/Alireza/Programing/#Files/PythonFiles'")
        recovery()
Setting()
window.mainloop()