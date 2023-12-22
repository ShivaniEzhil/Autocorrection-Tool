from textblob import TextBlob
from tkinter import *
from tkinter import filedialog

def Auto_correct(event=None):
    corrected_words = []
    text = Input_text.get(1.0, END).split(" ")
    for i in text:
        corrected_words.append(TextBlob(i).correct())
    Output_text.delete(1.0, END)
    for i in corrected_words:
        Output_text.insert(END, i + " ")

def Clear(event=None):
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)

def exit_full_screen():
    mainwin.attributes('-fullscreen', False)
    mainwin.overrideredirect(0)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            Input_text.delete(1.0, END)
            Input_text.insert(END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        content = Output_text.get(1.0, END)
        with open(file_path, 'w') as file:
            file.write(content)

mainwin = Tk()
mainwin.geometry('1200x620')
mainwin.resizable(False, False)
mainwin.attributes('-fullscreen', True)

mainwin.title("Auto Correct")
mainwin.config(bg='#8FBC8F')

Label(mainwin, text="Auto-Correction Tool", font='arial 30 bold', bg= '#228B22').place(x=540, y=30)
Label(mainwin, text="Enter Text", font='arial 18 bold', bg= '#228B22').place(x=280, y=90)
Input_text = Text(mainwin, font='arial 13', bg='white', height=13, wrap=WORD, padx=5, pady=5, width=60, insertbackground='black')
Input_text.place(x=80, y=130)
Label(mainwin, text="Corrected Text", font='arial 18 bold', bg= '#228B22').place(x=980, y=90)
Output_text = Text(mainwin, font='arial 13', bg='white', height=13, wrap=WORD, padx=5, pady=5, width=60, insertbackground='black')
Output_text.place(x=770, y=130)
auto_correct_btn = Button(mainwin, text="Correct", bg='lavender blush', width=30, font='arial 18 bold', pady=3, command=Auto_correct)
auto_correct_btn.place(x=240, y=420)
c1 = Button(mainwin, text="Clear", width=30, pady=3, bg='lavender blush', font='arial 18 bold', command=Clear)
c1.place(x=710, y=419)

mainwin.bind('<Control-c>', Clear) 
mainwin.bind('<Control-a>', Auto_correct) 

exit_fullscreen_button = Button(mainwin, text="Exit Full Screen", command=exit_full_screen)
exit_fullscreen_button.place(x=10, y=10)

load_file_button = Button(mainwin, text="Load File", command=load_file)
load_file_button.place(x=120, y=10)

save_file_button = Button(mainwin, text="Save File", command=save_file)
save_file_button.place(x=200, y=10)

mainwin.bind('<Escape>', exit_full_screen)

mainwin.mainloop()