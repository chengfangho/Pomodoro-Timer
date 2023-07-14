from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def start_timer():
    global rep
    rep += 1
    work_second = WORK_MIN*60
    short_break_second = SHORT_BREAK_MIN*60
    long_break_second = LONG_BREAK_MIN*60
    if rep % 8 == 0:
        count_down(long_break_second)
        label_timer.config(text="Break", fg=RED)
    elif rep % 2 == 0:
        count_down(short_break_second)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_second)
        label_timer.config(text="Work", fg=GREEN)

def count_down(time):
    global timer
    minute = time//60
    second = time%60
    if second == 0 or second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if time > 0:
        timer = window.after(1000, count_down, time-1)
    else:
        start_timer()
        marks = ""
        global rep
        for _ in range(rep//2):
            marks += "✓"
        label_check.config(text=marks)
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    global rep
    rep = 0

    
    




# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW, pady=20)
label_timer.grid(row=0, column=1)

button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(row=2, column=0)

button_rest = Button(text="Reset", highlightbackground=YELLOW, command=reset)
button_rest.grid(row=2, column=2)

label_check = Label(text="", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)
label_check.grid(row=3, column=1)

window.mainloop()
