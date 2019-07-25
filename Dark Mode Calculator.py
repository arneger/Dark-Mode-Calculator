from tkinter import *
calculation_values = ""
state_of_equal = False #Determines if the equal button is clicked.
#If it's true, the next button clicked will delete the calculation values and the
#screen values as seen in the calculator function

# calculator, a function that calculates the user-input from the GUI window and
# controls how the values are displayed on the GUI Calculator Screen
def calculator(number):
    global calculation_values
    global state_of_equal
    operators = ["+", "/", "-", "*"]
    calculator_screen.config(state=NORMAL)
    try: #if statements that prevents user from typing multiple operators in a row.
        if number in operators and calculation_values[-1] in operators:
            calculator_screen.config(state=DISABLED)
            calculation_values = calculation_values[:-1]
        elif number == "." and calculation_values[-1] == ".":
            calculator_screen.config(state=DISABLED)
            calculation_values = calculation_values[:-1]
    except:
        pass
    if number == "=": #Calculates the given arithmetic problem
        state_of_equal = True
        calculator_screen.delete(0.0, END)
        calculation_numbers = ""
        index = 0
        for value in calculation_values:
            if calculation_values[index] in operators and calculation_values[index - 1] in operators:
                index += 1
                continue
            elif calculation_values[index] == "." and calculation_values[index - 1] == ".":
                index += 1
                continue
            else:
                calculation_numbers += calculation_values[index]
                index += 1
        try:
            product = eval(calculation_numbers)
        except:
            product = ""
        calculator_screen.insert(END, str(product))
        calculation_values = ""
    elif number == "erase": #Deletes the last index value of the calculation values and on the screen
        calculator_screen.delete(0.0, END)
        calculation_values = calculation_values[:-1]
        calculator_screen.insert(END, calculation_values)
    elif number == "clear": #Clears the calcualtor screen and the calculation values string data
        calculator_screen.delete(0.0, END)
        calculation_values = ""
    else: #Adds the user inputed values on the screen and to the calculation values.
        if state_of_equal == True:
            calculator_screen.delete(0.0, END)
            calculation_values += number
            calculator_screen.insert(END, number)
            state_of_equal = False
        else:
            calculation_values += number
            calculator_screen.insert(END, number)
    calculator_screen.config(state=DISABLED)

############ GUI ############

window = Tk()
canvas = Canvas(window, height=450, width=330)
canvas.pack()
window.title("Dark Mode Calculator")
window.resizable(False,False)

########## FRAME 1 ##########

frame_1 = Frame(window, bg="#1a1a1a", bd=10)
frame_1.place(relx=0.5, rely=0, relwidth=1, relheight=0.11, anchor="n")

calculator_screen = Text(frame_1, font="none 15 bold", bg="#0d0d0d", fg="white", state=DISABLED)
calculator_screen.place(relwidth=0.705, relheight=1)

button_Erase = Button(frame_1, text=u"\u2b60", bg="#1a1a1a", fg="white", font="none 29 bold", command=lambda: calculator("erase"))
button_Erase.place(relx=0.75, rely=0, relwidth=0.245, relheight=1)

########## FRAME 2 ##########

frame_2 = Frame(window, bg="#0d0d0d", bd=10)
frame_2.place(relx=0.5, rely=0.099, relwidth=1, relheight=0.7, anchor="n")

button_7 = Button(frame_2, text="7", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("7"))
button_7.place(relx=0, rely=0, relwidth=0.22, relheight=0.25)

button_8 = Button(frame_2, text="8", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("8"))
button_8.place(relx=0.24, rely=0, relwidth=0.22, relheight=0.25)

button_9 = Button(frame_2, text="9", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("9"))
button_9.place(relx=0.48, rely=0, relwidth=0.22, relheight=0.25)

button_Division = Button(frame_2, text="/", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("/"))
button_Division.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.25)

########## FRAME 3 ##########

frame_3 = Frame(window, bg="#0d0d0d", bd=10)
frame_3.place(relx=0.5, rely=0.284, relwidth=1, relheight=0.7, anchor="n")

button_4 = Button(frame_3, text="4", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("4"))
button_4.place(relx=0, rely=0, relwidth=0.22, relheight=0.25)

button_5 = Button(frame_3, text="5", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("5"))
button_5.place(relx=0.24, rely=0, relwidth=0.22, relheight=0.25)

button_6 = Button(frame_3, text="6", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("6"))
button_6.place(relx=0.48, rely=0, relwidth=0.22, relheight=0.25)

button_Multiplication = Button(frame_3, text="*", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("*"))
button_Multiplication.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.25)

########## FRAME 4 ##########

frame_4 = Frame(window, bg="#0d0d0d", bd=10)
frame_4.place(relx=0.5, rely=0.469, relwidth=1, relheight=0.7, anchor="n")

button_1 = Button(frame_4, text="1", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("1"))
button_1.place(relx=0, rely=0, relwidth=0.22, relheight=0.25)

button_2 = Button(frame_4, text="2", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("2"))
button_2.place(relx=0.24, rely=0, relwidth=0.22, relheight=0.25)

button_3 = Button(frame_4, text="3", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("3"))
button_3.place(relx=0.48, rely=0, relwidth=0.22, relheight=0.25)

button_Subtraction = Button(frame_4, text="-", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("-"))
button_Subtraction.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.25)

########## FRAME 5 ##########

frame_5 = Frame(window, bg="#0d0d0d", bd=10)
frame_5.place(relx=0.5, rely=0.654, relwidth=1, relheight=0.7, anchor="n")

button_0 = Button(frame_5, text="0", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("0"))
button_0.place(relx=0, rely=0, relwidth=0.22, relheight=0.25)

button_Addition = Button(frame_5, text="+", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("+"))
button_Addition.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.25)

button_Comma = Button(frame_5, text=",", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("."))
button_Comma.place(relx=0.24, rely=0, relwidth=0.22, relheight=0.25)

button_Equal = Button(frame_5, text="=", bg="#1a1a1a", fg="white", font="none 15 bold", command=lambda: calculator("="))
button_Equal.place(relx=0.48, rely=0, relwidth=0.22, relheight=0.25)

########## FRAME 6 ##########

frame_6 = Frame(window, bg="#0d0d0d", bd=10)
frame_6.place(relx=0.5, rely=0.85, relwidth=1, relheight=0.6, anchor="n")

label_name = Label (frame_6, text="Dark Mode Calculator", bg="#0d0d0d", fg="#1a1a1a", font="arial 15 bold")
label_name.place(relx=0.0, rely=0, relwidth=0.7, relheight=0.2)

button_Clear = Button(frame_6, text="Clear", bg="#1a1a1a", fg="white", font="none 11 bold", command=lambda: calculator("clear"))
button_Clear.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.18)

########## RUNS GUI ##########

window.mainloop()