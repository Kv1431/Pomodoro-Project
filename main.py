
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ''

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    tick_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def time_started():
    global reps
    reps += 1
    if reps % 2 == 0:
        timer_label.config(text='Break Time', fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
        global marks
        marks += '✔'
        tick_label.config(text=marks)
    elif reps % 8 == 0:
        timer_label.config(text='Take a Long Break', fg=RED)
        count_down(LONG_BREAK_MIN*60)
    else:
        timer_label.config(text='Work Time', fg=GREEN)
        count_down(WORK_MIN*60)
        tick_label.config(text='')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(WORK_MIN):
    minutes = (WORK_MIN)//60
    seconds = WORK_MIN%60
    canvas.itemconfig(timer_text, text=f'{minutes:02d}:{seconds:02d}')
    if WORK_MIN > 0:
        global timer
        timer = window.after(1000, count_down, WORK_MIN-1)
    else:
        time_started()
    

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=150, pady=100, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file=r'.\pomodoro project\tomato.png')
canvas.create_image(100,112, image=img)
timer_text = canvas.create_text(108,130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))


canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), command=time_started)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(fg=GREEN, font=(FONT_NAME, 18, 'bold'))
tick_label.grid(row=3, column=1)


window.mainloop()
