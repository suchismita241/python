from tkinter import *
import os
import sqlite3


'''        GUI (1)       '''



#here the username is Suchismita and password is 123. this will be used to login as a .txt file was created.



def loggedin():
    
    global screen2
    global name
    global branch
    global regdid
    global name_entry
    global branch_entry
    global regdid_entry

    screen2 = Toplevel(screen)
    screen2.title("Student Records")
    screen2.geometry("500x500")
    screen2.configure(bg = "white")
    
    name = StringVar()
    branch = StringVar()
    regdid = StringVar()

    
    Label(screen2, text = "Name :",font = ("arial",11,"bold")).place(x = 40,y = 70)

    name_entry = Entry(screen2,textvariable = name)
    name_entry.place(x = 150,y = 70)
   
    Label(screen2, text = "Branch :",font = ("arial",11,"bold")).place(x = 40,y = 120)

    branch_entry = Entry(screen2,textvariable = branch)
    branch_entry.place(x = 150,y = 120)

   
    Label(screen2, text = "Regd Id :",font = ("arial",11,"bold")).place(x = 40,y = 170)

    regdid_entry = Entry(screen2,textvariable = regdid)
    regdid_entry.place(x = 150,y = 170)

   
    Button(screen2, text = "Continue",fg ='green',width = 14,font = ("arial",11,"bold"), relief = RAISED , command = do).place(x = 180,y = 250)

    
  
    
'''           GUI(2)           '''


   
def open_window():
    
    tip = Toplevel()
    tip.title("SUBJECTS")
    tip.geometry("500x500")
    tip.configure(bg = "white")
    
    Label(tip, text = "MARKS SUBMISSION",font = ("arial",14,"bold")).place(x=140,y=40)
    
    Label(tip, text = "Input for respective marks :",font = ("arial",11,"bold")).place(x=50,y=90)
    
    Button(tip, text = "MATH",width = 10,bg = "blue", command = open_window_math).place(x=70,y=130)
    
    Button(tip, text = "NT", width =10,bg = "blue", command = open_window_nt).place(x=70,y=200)

    Button(tip, text = "EEM", width = 10,bg = "blue", command = open_window_eem).place(x=70,y=270)

    Button(tip, text = "SS", width = 10,bg = "blue",command = open_window_ss).place(x=210,y=130)

    Button(tip, text = "AEC", width = 10,bg = "blue",command = open_window_aec).place(x=210,y=200)

    Button(tip, text = "SUBMIT",fg = "white",bg = "green",font = ("arial",9,"bold"),width =10, command = open_window3).place(x=160,y=350)


    
 
'''             SUBJECTS MARK SUBMISSION             '''

    
def open_window_math():
    global math_marks
    global math_entry
    math_marks = IntVar()
    
    math = Toplevel()
    math.title("MATH")
    math.geometry("300x300")
    Label(math, text = "Enter the marks obtained :").pack()
    
    math_entry = Entry(math,textvariable = math_marks)
    math_entry.pack()
    
    Button(math, text = "Done", command = math_submission).pack()
    Button(math, text = "Back", command = back).pack()

def back():
    open_window()

def math_submission():
            
    math1 = math_marks.get()
    name1 = name.get()
        
    conn = sqlite3.connect("registration.db")
    with conn:
        cur = conn.cursor()
    cur.execute( '''UPDATE DETAILS SET MATH == "%s" WHERE Name == "%s"''' %(math1,name1))
    conn.commit()
    cur.close()    
    conn.close()

    
    
def open_window_nt():
    global nt_marks
    global nt_entry
    nt_marks = IntVar()
    
    nt = Toplevel()
    nt.title("NT")
    nt.geometry("300x300")
    Label(nt, text = "Enter the marks obtained :").pack()
    
    nt_entry = Entry(nt,textvariable = nt_marks)
    nt_entry.pack()
    
    Button(nt, text = "Done", command = nt_submission).pack()
    Button(nt, text = "Back", command = back).pack()

def back():
    open_window()
    
def nt_submission():
            
    nt1 = nt_marks.get()
    name1 = name.get()
        
    conn = sqlite3.connect("registration.db")
    with conn:
        cur = conn.cursor()

    cur.execute( '''UPDATE DETAILS SET NT == "%s" WHERE Name == "%s"''' %(nt1,name1))
    conn.commit()
    cur.close()    
    conn.close()     
    

    
def open_window_eem():
    global eem_marks
    global eem_entry
    eem_marks = IntVar()
    
    eem = Toplevel()
    eem.title("EEM")
    eem.geometry("300x300")
    Label(eem, text = "Enter the marks obtained :").pack()
    
    eem_entry = Entry(eem,textvariable = eem_marks)
    eem_entry.pack()
    
    Button(eem, text = "Done", command = eem_submission).pack()
    Button(eem, text = "Back", command = back).pack()

def back():
    open_window()
    
    
def eem_submission():
            
    eem1 = eem_marks.get()
    name1 = name.get()
        
    conn = sqlite3.connect("registration.db")
    with conn:
        cur = conn.cursor()

    cur.execute( '''UPDATE DETAILS SET EEM == "%s" WHERE Name == "%s"''' %(eem1,name1))
    conn.commit()
    cur.close()    
    conn.close()
    
 
 
def open_window_ss():
    global ss_marks
    global ss_entry
    ss_marks = IntVar()
    
    ss = Toplevel()
    ss.title("SS")
    ss.geometry("300x300")
    Label(ss, text = "Enter the marks obtained :").pack()
    
    ss_entry = Entry(ss,textvariable = ss_marks)
    ss_entry.pack()
    
    Button(ss, text = "Done", command = ss_submission).pack()
    Button(ss, text = "Back", command = back).pack()

def back():
    open_window()
    
    
def ss_submission():
            
    ss1 = ss_marks.get()
    name1 = name.get()
        
    conn = sqlite3.connect("registration.db")
    with conn:
        cur = conn.cursor()

    cur.execute( '''UPDATE DETAILS SET SS == "%s" WHERE Name == "%s"''' %(ss1,name1))
    conn.commit()
    cur.close()    
    conn.close()
    
    
 
 
def open_window_aec():
    global aec_marks
    global aec_entry
    aec_marks = IntVar()
    
    aec = Toplevel()
    aec.title("AEC")
    aec.geometry("300x300")
    Label(aec, text = "Enter the marks obtained :").pack()
    
    aec_entry = Entry(aec,textvariable = aec_marks)
    aec_entry.pack()
    
    Button(aec, text = "Done", command = aec_submission).pack()
    Button(aec, text = "Back", command = back).pack()

def back():
    open_window()
    
    
def aec_submission():
            
    aec1 = aec_marks.get()
    name1 = name.get()
        
    conn = sqlite3.connect("registration.db")
    with conn:
        cur = conn.cursor()

    cur.execute( '''UPDATE DETAILS SET aec == "%s" WHERE Name == "%s"''' %(aec1,name1))
    conn.commit()
    cur.close()    
    conn.close() 
    
def do():
    open_window()
    put()

    

'''            INVALID SIGN IN        '''    
    
def invalid():
    screen3 = Toplevel(screen)
    screen3.title("Checking")
    screen3.geometry("250x150")
    Label(screen3, text = "Invalid UserID or Password.",font = (10), fg = "red").pack()
    
    
'''                CGPA CALCULATION             '''

def cgpa_func():
     global cgpa
     math1 = math_marks.get()
        
     nt1 = nt_marks.get()
    
     eem1 = eem_marks.get()

     ss1 = ss_marks.get()

     aec1 = aec_marks.get() 
        
     avg = 0   
     tot = 0
     avg_per = 0 
     cgpa = 0
    
     tot = math1 + nt1 + eem1 + ss1 + aec1
     avg = tot/500 
     avg_per = avg * 100
     
     cgpa = (avg_per)/9.5
     print("cgpa obtained is:", cgpa ) 
        
def display_cgpa():
    
    tuf = Toplevel()
    tuf.title("Displaying CGPA")
    tuf.geometry("300x300")
    Label(tuf , text = "THE CGPA OBTAINED IS :",font = ("arial",9,"bold"),bg = "white",fg = "blue").place(x = 79, y = 40)
    Label(tuf, text= float(cgpa),bg = "green",fg = "white").place(x = 89,y = 90)
        
def do1():
    cgpa_func()
    display_cgpa()

   
'''            GRADE CALCULATION     '''
#       CGPA          GRADE
#     9 - 10.0          O
#     8 - 8.9           E
#     7 - 7.9           A
#     6 - 6.9           B
#     5 - 5.9           C
#     below 5           D
 


def grade_func():
    global grade    
    
    if (cgpa < 5.0):
        grade = "D"
    elif(cgpa < 6.0):
        grade = "C"
    elif(cgpa < 7.0):
        grade = "B"
    elif(cgpa < 8.0):
        grade = "A"
    elif(cgpa < 9.0):
        grade = "E"
    elif(cgpa < 10.1):
        grade = "O"
    elif(cgpa < 11):
        grade = "O"
    
    print("The grade obtained is:", grade)    
        
def display_grade(): 
    tub = Toplevel()
    tub.title("Displaying Grade")
    tub.geometry("300x300")
    
    Label(tub , text = "THE GRADE OBTAINED IS :",font = ("arial",9,"bold"),bg = "white",fg = "blue").place(x = 78, y = 40)
    Label(tub, text= str(grade),width = 10,bg = "green",fg = "white").place(x = 96,y = 90)
    
def do2():
    grade_func()
    display_grade()
    

    
    
'''                 GUI 3                '''

def open_window3():
    
    tom = Toplevel()
    tom.title("FINAL PAGE")
    tom.geometry("500x500")
    tom.configure(bg = "white")
    
    Label(tom, text = "RESULTS",font = ("arial",14,"bold")).place(x=145,y=40)
    
    Label(tom, text = "Input options :",font = ("arial",11,"bold")).place(x=50,y=90)
    
    Button(tom, text = "CGPA",width = 10,bg = "light blue",command = do1).place(x=70,y=130)
    
    Button(tom, text = "GRADE", width =10,bg = "light blue", command = do2).place(x=70,y=200)

    Button(tom, text = "NEW INPUT", width = 10,bg = "light blue",command = new_input).place(x=200,y=130)
    
    Button(tom, text = "LOGOUT", width = 10,bg = "light blue",command = logout).place(x=200,y=200)
    
        
    
'''         LOGOUT         '''
def logout():
    screen.destroy()

    
    
'''        NEW INPUT        '''
def new_input():
    
    loggedin()

    
    

'''                DATABASE CONNECTION                '''    
    
conn = sqlite3.connect('registration.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS DETAILS(Name TEXT, Branch TEXT, RegdID REAL)")

conn.commit()

    

def put():
    name1 = name.get()
    branch1 = branch.get()
    regdid1 = regdid.get()
    conn = sqlite3.connect('registration.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO DETAILS (Name,Branch, RegdID) VALUES (?,?,? )",(name1,branch1,regdid1))
    conn.commit()


    

'''            LOGIN CHECKING            '''    

def login_verify():
    user1 = userid.get()
    password1 = password.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    list_of_files = os.listdir()
    
    
    if user1 in list_of_files:
        
        file1 = open(user1, "r")
        verify = file1.read().splitlines()
        
        if password1 in verify:
            
            loggedin()
           
        else:
            invalid()
    else:
        invalid()



        
'''            OPENING GUI              '''

def signin():
    global screen
    global userid
    global password
    global username_entry
    global password_entry
    screen = Tk()
    screen.geometry("400x400")
    screen.title("Login In")   
    Label(screen, text = "Username").pack()
    userid = StringVar()
    username_entry = Entry(textvariable = userid)
    username_entry.pack()
    Label(screen, text = "Password :").pack()
    password = StringVar()
    password_entry = Entry(textvariable = password, show = "*")
    password_entry.pack()
    Button(screen, text = "Enter", command = login_verify).pack()
    screen.mainloop()
   

signin()
cur.close()
conn.close()




