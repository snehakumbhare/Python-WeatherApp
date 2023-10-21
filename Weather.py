#Weather App using Python
from tkinter import *
from tkinter import ttk
import requests


def data_get():
      city = city_name.get()
      data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dc513d342c2f9e1818f269623868ee86").json()
      #print(data)
      W_lable1.config(text=data["weather"][0]["main"])
      Wb_lable1.config(text=data["weather"][0]["description"])
      temp_lable1.config(text=str(int(data["main"]["temp"]-273.15)))
      per_lable1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather App")
win.config(bg = "lightgreen")
win.geometry("500x0")

name_lable = Label(win,text="Weather App",
                 font=("Time New Roman",30,"bold"))
name_lable.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["AndhraPradesh" ,"ArunachalPradesh" ,"Assam","Bihar","Chhattisgarh","Goa","Gujarat",
             "Haryana","HimachalPradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","MadhyaPradesh",
             "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","TamilNadu","Telangana",
             "Tripura","UttarPradesh","Uttarakhand","WestBengal","Andaman and NicobarIslands","Chandigarh","Dadra and NagarHaveli",
             "Daman and Diu","Lakshadweep","NationalCapitalTerritoryofDelhi","Puducherry"]
com = ttk.Combobox(win,text="Weather App",values=list_name,
                 font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)

W_lable = Label(win,text="Weather Climate",
                 font=("Time New Roman",15))
W_lable.place(x=25,y=260,height=50,width=210)

W_lable1 = Label(win,text="",
                 font=("Time New Roman",15))
W_lable1.place(x=250,y=260,height=50,width=210)



Wb_lable = Label(win,text="Weather Description",
                 font=("Time New Roman",15))
Wb_lable.place(x=25,y=330,height=50,width=210)

Wb_lable1 = Label(win,text="",
                 font=("Time New Roman",15))
Wb_lable1.place(x=250,y=330,height=50,width=210)



temp_lable = Label(win,text="Temperature",
                 font=("Time New Roman",15))
temp_lable.place(x=25,y=400,height=50,width=210)

temp_lable1 = Label(win,text="",
                 font=("Time New Roman",15))
temp_lable1.place(x=250,y=400,height=50,width=210)



per_lable = Label(win,text="Pressure",
                 font=("Time New Roman",15))
per_lable.place(x=25,y=470,height=50,width=210)

per_lable1 = Label(win,text="",
                 font=("Time New Roman",15))
per_lable1.place(x=250,y=470,height=50,width=210)

done_button=Button(win,text="Done",
                 font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()
