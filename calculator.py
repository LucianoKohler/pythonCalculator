from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)

display = Entry(root, width=40)
display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10
)


def buttonCreator(location, style, text, value):
    button = Button(
        location,
        text=text,
        padx=20,
        pady=20,
        borderwidth=.5,
        command=lambda: handleClick(value)
    )

    if style == "red":
        button["fg"] = "white"
        button["bg"] = "red"
        button["activebackground"] = "red"
        button["activeforeground"] = "white"
    return button


def handleClick(value):
    match value:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            display.insert("end", value)
        case "+" | "-" | "x" | "/":
            if len(display.get()) == 0:
                return
            if len(display.get()) >= 2:
                lastSymbol = display.get()[-2]  # two chars back because of the spaces
                if (lastSymbol == "+" or
                        lastSymbol == "-" or
                        lastSymbol == "x" or
                        lastSymbol == "/"):
                    display.delete(len(display.get()) - 3, 'end')

            display.insert("end", " " + value + " ")

        case ".":
            if len(display.get()) == 0: return
            lastChar = display.get()[-1]
            if lastChar.isnumeric(): display.insert("end", value)

        case "C":
            display.delete(0, "end")

        case "=":
            result = (display.get()
                      .replace("x", "*")
                      .replace(" ", ""))
            display.delete(0, "end")

            if "/0" not in result:
                display.insert(0, eval(result))
        case _:
            print(f"Invalid value: {value}")


C = buttonCreator(root, "red", "C", value="C")
divide = buttonCreator(root, "default", "/", value="/")

button7 = buttonCreator(root, "default", "7", value=7)
button8 = buttonCreator(root, "default", "8", value=8)
button9 = buttonCreator(root, "default", "9", value=9)
times = buttonCreator(root, "default", "x", value="x")

button4 = buttonCreator(root, "default", "4", value=4)
button5 = buttonCreator(root, "default", "5", value=5)
button6 = buttonCreator(root, "default", "6", value=6)
minus = buttonCreator(root, "default", "-", value="-")

button1 = buttonCreator(root, "default", "1", value=1)
button2 = buttonCreator(root, "default", "2", value=2)
button3 = buttonCreator(root, "default", "3", value=3)
plus = buttonCreator(root, "default", "+", value="+")

button0 = buttonCreator(root, "default", "0", value=0)
point = buttonCreator(root, "default", ".", value=".")
enter = buttonCreator(root, "default", "=", value="=")

C.grid(row=1, column=0, columnspan=2, sticky='ew')
divide.grid(row=1, column=2, columnspan=2, sticky='ew')

button7.grid(row=2, column=0, sticky='ew')
button8.grid(row=2, column=1, sticky='ew')
button9.grid(row=2, column=2, sticky='ew')
times.grid(row=2, column=3, sticky='ew')

button4.grid(row=3, column=0, sticky='ew')
button5.grid(row=3, column=1, sticky='ew')
button6.grid(row=3, column=2, sticky='ew')
minus.grid(row=3, column=3, sticky='ew')

button1.grid(row=4, column=0, sticky='ew')
button2.grid(row=4, column=1, sticky='ew')
button3.grid(row=4, column=2, sticky='ew')
plus.grid(row=4, column=3, sticky='ew')

button0.grid(row=5, column=0, sticky='ew')
point.grid(row=5, column=1, sticky='ew')
enter.grid(row=5, column=2, columnspan=2, sticky='ew')

root.mainloop()
