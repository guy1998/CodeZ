from tkinter import *
import sys

def Take_input(inputtxt,Output):
        wr = open("Runfiles/reasons to live.txt", "w")
        sys.stdout = wr
        INPUT = inputtxt.get("1.0", END)
        INPUT = INPUT.replace("input()", "open('Runfiles/Exercises/Ex.1/inputs/I1.txt','r').read()")
        exec(INPUT)
        wr.close()
        out = open("Runfiles/reasons to live.txt", "r")
        Output.delete("1.0",END)
        Output.insert(END,out.read())
        out.close()
        
def Save_code(inputtxt,Output):
        wr = open("Runfiles/Code.txt","w")
        INPUT = inputtxt.get("1.0",END)
        wr.write(INPUT)
        Output.delete("1.0",END)
        Output.insert(END,"Your code is saved ^_^")
        wr.close()
        
def End(root):
        wr = open("Runfiles/reasons to live.txt","w")
        wr.truncate(0)
        wr.write("There may be some, but I prefer saying 'None'")
        wr.close()
        root.destroy()
        
def Addfor(inputtxt):
        inputtxt.insert(END,"\nfor i in range(a):\n    ")
        
def Submit(inputtxt,Output):
        Take_input(inputtxt,Output)
        re=open("Runfiles/reasons to live.txt","r")
        ch=open("Runfiles/Exercises/Ex.1/outputs/O1.txt","r")
        CHECK = ch.read()
        REGGIE = re.read()
        CHECK = CHECK.replace("\n","")
        REGGIE = REGGIE.replace("\n","")
        re.close()
        ch.close()
        Output.delete("1.0",END)
        if CHECK==REGGIE:
                Output.insert(END,"Level passed!. RESPECT")
        else:
                Output.insert(END,"Wrong answer. Try it again.")

def RunCode():
        root = Tk()
        root.geometry("480x540")
        root.title("Code Runner")
        root.resizable(0,0)

        inputtxt = Text(root, height = 14,
                                        width = 60,
                                        bg = "light yellow",
                                        yscrollcommand = True,
                                        xscrollcommand = True)
        inputtxt.insert(END,"#Insert a code that prints the square of 0 up to a number\n")
        inputtxt.insert(END,"#exluding that number\n")
        inputtxt.insert(END,"#using int(input()) will take the input value as 10\n")
        inputtxt.insert(END,"#as an example\n")
        Output = Text(root, height = 14,
                                width = 60,
                                bg = "light cyan",
                                yscrollcommand = True,
                                xscrollcommand = True)

        Display = Button(root, height = 2,
                                        width = 25,
                                        text ="Run code",
                                        command = lambda:Take_input(inputtxt,Output))

        SaveButton = Button(root, height = 2,
                            width = 25,
                            text = "Save code",
                            command = lambda:Save_code(inputtxt,Output))

        ExitButton = Button(root, height = 1,
                            width = 25,
                            text = "Exit",
                            command = lambda:End(root))

        AddforButton = Button(root, height = 2,
                              width = 25,
                              text="Add a for-loop",
                              command= lambda: Addfor(inputtxt))

        SubButton = Button(root, height = 2,
                           width = 25,
                           text="Submit",
                           command= lambda: Submit(inputtxt,Output))

        inputtxt.grid(row=0,column=0,columnspan=2)

        Display.grid(row=1,column=0)

        SaveButton.grid(row=1,column=1)

        AddforButton.grid(row=2,column=1)

        SubButton.grid(row=3,column=1)

        Output.grid(row=2,column=0,columnspan=2,rowspan=5)

        ExitButton.grid(row=7,columnspan=2)


        mainloop()
