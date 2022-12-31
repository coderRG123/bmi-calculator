#BMI caculator
# wieght/height*height
# if bmi lesss than 18.5 under wegiht
# greater than 18.5, less than or equal 24.9 normal weight
#greater than 25 less than eqaul to29.9 over weight
# greaer than 30 obese
#else something wrong
from tkinter import *

window=Tk()

window.title("BMI Calculator")
window.configure(bg="cadetblue")
window.geometry("400x400")

def cal():
    name=user.get()
    msg=""
    output=Label(resultf, text=name)
    output.place(x=20,y=20)

apptitle=Label(window, text="BMI Calculator", bg="cadetblue", fg="blue", font=("Times new roman", 25), bd=2)
apptitle.place(x=100, y=20)

userName=Label(window, text="ENTER NAME:", bg="cadetblue", fg="blue")
userName.place(x=30, y=75)

user=Entry(window, text="", width=20)
user.place(x=120, y=75)

heightL=Label(window, text="Height(cm):", bg="cadetblue", fg="blue")
heightL.place(x=30, y=100)

height=Entry(window, text="", width=10)
height.place(x=120, y=100)

weightL=Label(window, text="weight(kg):", bg="cadetblue", fg="blue")
weightL.place(x=30, y=125)

weight=Entry(window, text="", width=10)
weight.place(x=120, y=125)

sumbit=Button(window, text="CALCULATE", bg="white", fg="cadetblue", command=cal)
sumbit.place(x=150, y=160)

resultf=LabelFrame(window, text="result", bg="black")
resultf.place(x=20, y=200)
resultf.pack(padx=20, pady=20)

resultL=Label(resultf, text="", bg="white", width=30)
resultL.place(x=10, y=10)

window.mainloop()