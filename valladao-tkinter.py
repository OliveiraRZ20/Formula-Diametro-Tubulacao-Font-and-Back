from tkinter import *
import tkinter.messagebox as msgbox
from tkinter import filedialog
import sys

win = Tk()
win.resizable(False,False)


# o icone do EXECUTAVEL COMPILADO vai ser tambem o icone da barra de tarefas e do app em janela tbm.
win.iconbitmap(sys.executable)

# window specs
win_width = "768"
win_height = "500"
win.geometry("%sx%s" % (win_width, win_height))


# screen specs
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# final position
final_pos_x = screen_width // 2 - int(win_width) // 2
final_pos_y = screen_height // 2 - int(win_height) // 2
win.geometry(f"+{final_pos_x}+{final_pos_y}")

win.title("Calculadora de diâmetro de tubulação (Código Valladão 3.0)")

# functions - back end

def confirm_exit():
    answer = msgbox.askyesno("Confirmação", "Você realmente deseja sair?")
    if answer:
        win.destroy()

def result():
    if not box_entry_Q.get() == "" and not box_entry_L.get() == "" and not box_entry_Dp.get() == "" and not box_entry_P.get() == "":
        Q = float(box_entry_Q.get())
        L = float(box_entry_L.get())
        Dp = float(box_entry_Dp.get())
        P = float(box_entry_P.get())
        ans = round((((1.663785 * 0.001 * (Q ** 1.85) * L)/(Dp * P))**(1/5))*10, 3)
        text_result.set(f"{ans} mm")
    else:
        msgbox.showerror("Erro","Alguma entrada está incompleta, tente novamente...")
    
    


# labels - front end
label_title = Label(
    win,
    text="Bem vindo a caluladora da fórmula do valladão!",
    font="JetBrains 20",
    justify="center"
)
label_title.place(x=384,y=50, anchor='center')
# |=====================================================================|
label_var_Q = Label(
    win,
    text="Variável Q :",
    font="JetBrains 12",
)
label_var_Q.place(x=20,y=100)

box_text_Q = StringVar()
box_entry_Q = Entry(
    win,
    justify="left",
    font="JetBrains 12 italic",
    textvariable=box_text_Q
)
box_entry_Q.place(x=20,y=125)
# |=====================================================================|
label_var_L = Label(
    win,
    text="Variável L :",
    font="JetBrains 12",
)
label_var_L.place(x=20,y=175)

box_text_L = StringVar()
box_entry_L = Entry(
    win,
    justify="left",
    font="JetBrains 12 italic",
    textvariable=box_text_L
)
box_entry_L.place(x=20,y=200)
# |=====================================================================|
label_var_Dp = Label(
    win,
    text="Variável Dp :",
    font="JetBrains 12",
)
label_var_Dp.place(x=20,y=250)

box_text_Dp = StringVar()
box_entry_Dp = Entry(
    win,
    justify="left",
    font="JetBrains 12 italic",
    textvariable=box_text_Dp
)
box_entry_Dp.place(x=20,y=275)
# |=====================================================================|
label_var_P = Label(
    win,
    text="Variável P :",
    font="JetBrains 12",
)
label_var_P.place(x=20,y=325)

box_text_P = StringVar()
box_entry_P = Entry(
    win,
    justify="left",
    font="JetBrains 12 italic",
    textvariable=box_text_P
)
box_entry_P.place(x=20,y=350)
# |=====================================================================|
label_result = Label(
    win,
    text="Resultado:",
    font="JetBrains 30",
    justify="center"
)
label_result.place(x=400,y=125)
text_result = StringVar()
label_result = Label(win,
    text="",
    font="JetBrains 30",
    fg="blue",
    textvariable=text_result,
    )
label_result.place(x=500,y=200, anchor="center")


# buttons - front end
butt_result = Button(
    win,
    text="Confirmar",
    fg="green",
    font="JetBrains 15",
    width=12,
    height=2,
    command=result
)
butt_result.place(x=20,y=400)

# app binds - back end
win.bind("<Escape>", lambda Event: confirm_exit())

# inicialization command
win.mainloop()