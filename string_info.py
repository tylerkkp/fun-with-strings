from tkinter import *
from tkinter import StringVar, Label, Entry

root = Tk()
# Set app name at top of window
root.title('String Info')
# Set initial app window dimensions
root.geometry('{}x{}'.format(600, 400))

# create all of the main containers
row1 = Frame(root, width=300, height=20, pady=3)
row2 = Frame(root, width=300, height=50, pady=3)
row3 = Frame(root, width=300, height=50, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

row1.grid(row=0, sticky="")
row2.grid(row=1, sticky="n")
row3.grid(row=2, sticky="n")
####################################
# Individual strings for the ASCII heading
desc1 = '   _______________  _____   _____________\n'
desc2 = '  / ___/_  __/ __ \/  _/ | / / ____/ ___/\n'
desc3 = '  \__ \ / / / /_/ // //  |/ / / __ \__ \ \n'
desc4 = ' ___/ // / / _, _// // /|  / /_/ /___/ / \n'
desc5 = '/____//_/ /_/ |_/___/_/ |_/\____//____/  \n'
fulldesc = desc1 + desc2 + desc3 + desc4 + desc5

# Create ASCII heading and place it in the window
# Note that we had to change font to Courier (because it's monospace)
heading = Label(row1, text=fulldesc, font=("Courier", 16))
heading.grid(row=0, column=0)

# create the widgets for row 2
string_label = Label(row2, text='Enter String:') # was called model_label
str_val = StringVar()
string_val = Entry(row2, width=36, textvariable=str_val) # was called width_label

# layout the widgets in the top frame
string_label.grid(row=0, column=0)
string_val.grid(row=0, column=1)

# Need to initialize result values with empty strings
charnum = StringVar()
charnum.set('0')
firstchar = StringVar()
firstchar.set('')
lastchar = StringVar()
lastchar.set('')
lowercase = StringVar()
lowercase.set('')
uppercase = StringVar()
uppercase.set('')
capitalized = StringVar()
capitalized.set('')
trimmed_str = StringVar()
trimmed_str.set('')
palindrome = StringVar()
palindrome.set('')

# Create function to test if input str is a palindrome
def paltest(theword):
    theword = theword.replace(" ", "")
    baseword = theword.lower()
    revword = baseword[::-1]
    if baseword == revword:
        return True
    else:
        return False

# Get the value of the string input
def update_fields(*args):
    textc = ''
    the_string = str(str_val.get())
    # find number of characters in the string, stored as a str value
    new_charnum = str(len(the_string))
    # update the num_chars Label with the new value
    num_chars_result.config(text = new_charnum)

    if new_charnum == '0':
        new_firstchar   = ''
        new_lastchar    = ''
        new_lowercase   = ''
        new_uppercase   = ''
        new_capitalized = ''
        new_trimmed_str = ''
        new_palindrome  = ''
    else:
        new_firstchar   = the_string[0]
        new_lastchar    = the_string[-1]
        new_lowercase   = the_string.lower()
        new_uppercase   = the_string.upper()
        new_capitalized = the_string[0].upper() + the_string[1:].lower()
        new_trimmed_str = the_string.strip()
        if paltest(the_string) == True:
            new_palindrome = "Now I draw an award. I won!"
            pal_result.config(fg = 'green')
        else:
            new_palindrome = "Drat, such custard!"
            pal_result.config(fg = 'red')

    first_char_result.config(text = new_firstchar)
    last_char_result.config(text = new_lastchar)
    l_case_result.config(text = new_lowercase)
    u_case_result.config(text = new_uppercase)
    capped_result.config(text = new_capitalized)
    trimmed_result.config(text = new_trimmed_str)
    pal_result.config(text = new_palindrome)

# create the widgets for the center (results) frame
num_chars = Label(row2, text='Number of characters:') #jobname
num_chars_result = Label(row2, text=charnum.get(), width=36, borderwidth=2, relief="ridge") # job1
first_char = Label(row2, text='First character:') # floatwidth
first_char_result = Label(row2, text=firstchar.get(), width=36, borderwidth=2, relief="ridge") # wide1
last_char = Label(row2, text='Last character:') # floatlength
last_char_result = Label(row2, text=lastchar.get(), width=36, borderwidth=2, relief="ridge") # length1
l_case = Label(row2, text='Lower case:') # floattubs
l_case_result = Label(row2, text=lowercase.get(), width=36, borderwidth=2, relief="ridge") # tubs1
u_case = Label(row2, text='Upper case:') # weight
u_case_result = Label(row2, text=uppercase.get(), width=36, borderwidth=2, relief="ridge") # wt1
capped = Label(row2, text='Capitalize:') # freeboard
capped_result = Label(row2, text=capitalized.get(), width=36, borderwidth=2, relief="ridge") # freebd1
trimmed = Label(row2, text='Without leading and trailing spaces:')
trimmed_result = Label(row2, text=trimmed_str.get(), width=36, borderwidth=2, relief="ridge")
pal_str = Label(row2, text='Is it a palindrome?')
pal_result = Label(row2, text=palindrome.get(), width=36, borderwidth=2, relief="ridge")

# layout the widgets in the center frame
num_chars.grid(row=1, column=0)
num_chars_result.grid(row=1, column=1)
first_char.grid(row=2, column=0)
first_char_result.grid(row=2, column=1)
last_char.grid(row=3, column=0)
last_char_result.grid(row=3, column=1)
l_case.grid(row=4, column=0)
l_case_result.grid(row=4, column=1)
u_case.grid(row=5, column=0)
u_case_result.grid(row=5, column=1)
trimmed.grid(row=6, column=0)
trimmed_result.grid(row=6, column=1)
pal_str.grid(row=7, column=0)
pal_result.grid(row=7, column=1)

# Add exit button for fun
exitButton = Button(row3, text="Exit",command=lambda: exit())
exitButton.grid(row=1, column=0)

# Watch for string entry to be changed
str_val.trace_add('write', update_fields)

root.mainloop()



