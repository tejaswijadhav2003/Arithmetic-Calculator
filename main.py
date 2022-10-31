#GUI Applications using TKInterface
#Arithmetic Calculator

import tkinter as tk

#Step 1: Create a window and set its attributes
window = tk.Tk() #create a window
window.title('Arithmetic Calculator') #set window title
window.geometry('320x200') #set the window size ('widthxheight')

#step 4: define the event procedures (functions that are invoked (by tk) on events)
def addition():
    try:
        #Code in try block is monitored for runtime errors (exceptions)
        #If a runtime error (exception) occurs then instead of abnormal termination
        #the program control is transferred to an except block for handling (error is neutralized and post error action is taken).

        #fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        #process
        result =  n1+n2
        #output
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END) #clear the existing content of the text field
        ent_answer.insert(0, str(result)) #set the new content of the text field
        ent_answer['state'] = 'disabled'
    except:
        #this block runs : on error
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END) #clear the existing content of the text field
        ent_answer.insert(0, 'Not a Number') #set the new content of the text field
        ent_answer['state'] = 'disabled'

def subtraction():
    try:
        # Code in try block is monitored for runtime errors (exceptions)
        # If a runtime error (exception) occurs then instead of abnormal termination
        # the program control is transferred to an except block for handling (error is neutralized and post error action is taken).

        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        # process
        result = n1 - n2
        # output
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)  # clear the existing content of the text field
        ent_answer.insert(0, str(result))  # set the new content of the text field
        ent_answer['state'] = 'disabled'
    except:
        #this block runs : on error
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END) #clear the existing content of the text field
        ent_answer.insert(0, 'Not a Number') #set the new content of the text field
        ent_answer['state'] = 'disabled'

def multiplication():
    try:
        # Code in try block is monitored for runtime errors (exceptions)
        # If a runtime error (exception) occurs then instead of abnormal termination
        # the program control is transferred to an except block for handling (error is neutralized and post error action is taken).

        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        # process
        result = n1 * n2
        # output
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)  # clear the existing content of the text field
        ent_answer.insert(0, str(result))  # set the new content of the text field
        ent_answer['state'] = 'disabled'
    except:
        #this block runs : on error
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END) #clear the existing content of the text field
        ent_answer.insert(0, 'Not a Number') #set the new content of the text field
        ent_answer['state'] = 'disabled'

def division():
    try:
        # Code in try block is monitored for runtime errors (exceptions)
        # If a runtime error (exception) occurs then instead of abnormal termination
        # the program control is transferred to an except block for handling (error is neutralized and post error action is taken).

        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        # process
        result = n1 / n2
        # output
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)  # clear the existing content of the text field
        ent_answer.insert(0, str(result))  # set the new content of the text field
        ent_answer['state'] = 'disabled'
    except ValueError:
        #this block runs : on ValueError
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END) #clear the existing content of the text field
        ent_answer.insert(0, 'Not a Number') #set the new content of the text field
        ent_answer['state'] = 'disabled'
    except ZeroDivisionError:
        # this block runs : on ZeroDivisionError
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)  # clear the existing content of the text field
        ent_answer.insert(0, 'Infinity')  # set the new content of the text field
        ent_answer['state'] = 'disabled'


#Step 2: Create the widgets (Label, Entry, Button)
lbl_number1 = tk.Label(master=window, text= 'Enter First Number')
lbl_number2 = tk.Label(master=window, text= 'Enter Second Number')
lbl_answer = tk.Label(master=window, text= 'Answer')

ent_number1 = tk.Entry(master=window, width=20)
ent_number2 = tk.Entry(master=window, width=20)
ent_answer = tk.Entry(master=window, width=20)
#setting the answer field as disabled
ent_answer['state'] = 'disabled'

bttn_add = tk.Button(master=window, text='Add', width=8, command=addition)
bttn_sub = tk.Button(master=window, text='Subtract', width=8, command = subtraction)
bttn_mul = tk.Button(master=window, text='Multiply', width=8, command= multiplication)
bttn_div = tk.Button(master=window, text='Divide', width=8, command= division)


#Step 3: Add the widgets to the window
#window.place() : is the geometry manager used for explicit positioning of the widgets in the window
lbl_number1.place(x = 20, y = 20)
lbl_number2.place(x = 20, y = 60)
lbl_answer.place(x = 20, y = 100)

ent_number1.place(x= 160, y=20)
ent_number2.place(x= 160, y=60)
ent_answer.place(x= 160, y=100)

bttn_add.place(x = 10, y = 150)
bttn_sub.place(x = 85, y = 150)
bttn_mul.place(x = 160, y = 150)
bttn_div.place(x = 235, y = 150)


#Keep the window alive, listen for events and react
window.mainloop()