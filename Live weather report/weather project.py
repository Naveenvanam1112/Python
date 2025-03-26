from tkinter import*
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city+ "&appid=1bd9764469d9af29cf5ce6c51af5e964").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=(data["main"]["temp"])-273.15)
    wp_label1.config(text=data["main"]["pressure"])



win=Tk()
win.title("Naveen")
win.config(bg='#0E1733')
win.geometry("500x570")

name_label=Label(win,text="WEATHER APP",font=('Time New Roman',40,"bold"))
name_label.config(bg='#0E1733',fg='#F98603')


name_label.place(x=25,y=50,height=50,width=450)


city_name=StringVar()

list_name=["khammam","hyderabad","visakhapatnam","kurnool","chittoor","kadapa","nellore","warangal","vijayawada","rajahmundry","sangareddy","annavaram","tirupati","ongole","amaravati"]


com=ttk.Combobox(win,text="states",values=list_name,font=('Arial Black',25),textvariable=city_name)


com.place(x=25,y=120,height=50,width=450)




w_label=Label(win,text="Weather Climate",font=('Arial Black',15),bg='#0E1733',fg='#F98603')

w_label.place(x=25,y=260,height=50,width=210)


w_label1=Label(win,text="",font=('Arial Black',15))

w_label1.place(x=240,y=280,height=20,width=210)



wb_label=Label(win,text="Weather Description",font=('Arial Black',13),bg='#0E1733',fg='#F98603')

wb_label.place(x=25,y=330,height=50,width=210)

wb_label1=Label(win,text="",font=('Arial Black',15))

wb_label1.place(x=240,y=350,height=20,width=210)



wt_label=Label(win,text="Temperature",font=('Arial Black',15),bg='#0E1733',fg='#F98603')

wt_label.place(x=25,y=400,height=50,width=210)



wt_label1=Label(win,text="",font=('Arial Black',12))

wt_label1.place(x=240,y=420,height=20,width=210)




wp_label=Label(win,text="Pressure",font=('Arial Black',15),bg='#0E1733',fg='#F98603')

wp_label.place(x=25,y=470,height=50,width=210)

wp_label1=Label(win,text="",font=('Arial Black',15))

wp_label1.place(x=240,y=490,height=20,width=210)



done_button=Button(win,text="Done",bg='#0E1733',fg='#F98603',font=('Arial Black',15),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()

