import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK="✔"
reps=0
timer=""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    start_button.config(state="active")
    checkmark_label.config(text="")
    
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button.config(state="disabled")
    global reps
    reps +=1
    work_in_sec = WORK_MIN * 60
    short_break_in_sec = SHORT_BREAK_MIN * 60
    long_break_in_sec = LONG_BREAK_MIN * 60
    if  reps % 8 == 0:
        count_down(long_break_in_sec)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_in_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_in_sec)
        label.config(text="Work", fg=GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec<10:
        count_sec = f"0{count_sec}"
    if count_min <10:
        count_min = f"0{count_min}"    
    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for rep in range(work_sessions):
            marks += CHECKMARK
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = tkinter.Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0) 
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00" , fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW)
label.grid(column=1,row=0)
label.config(pady=10,font=(FONT_NAME,40,"bold"))

checkmark_label = tkinter.Label(fg=GREEN)
checkmark_label.grid(column=1,row=3)
checkmark_label.config(pady=10,bg=YELLOW)

start_button = tkinter.Button(text="Start", bg=GREEN, command=start_timer)
start_button.config(font=(FONT_NAME,12,"bold"),fg="white")
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text="Reset", bg=RED, command=reset_timer)
reset_button.config(font=(FONT_NAME,12,"bold"),fg="white")
reset_button.grid(column=2, row=2)








window.mainloop()