from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
#----------------------------------------------------------------
#________________________________________________________________
#Function
def search():
    try:

        city=entrySearch.get()        
        geolocator=Nominatim(user_agent="geoapiExercises")       
        location=geolocator.geocode(city)       
        obj=TimezoneFinder()     
        lng1=int(location.longitude)
        lat1=int(location.latitude)      
        result=obj.timezone_at(lng=location.longitude,lat=location.longitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        
        name.config(text="CURRENT WEATHER")
        time.config(text=current_time)

        # API
        parametrs={"lat":str(lat1),"lon":str(lng1),"appid":"ef0593b766c8ce186824a4558cff8e52"}
        api="https://api.openweathermap.org/data/2.5/weather"
        data=requests.get(api,parametrs)
        jdata=data.json()

        condition=jdata['weather'][0]['main']
        description=jdata["weather"][0]["description"]
        temp=int(jdata['main']['temp']-273.15)
        pressure=jdata['main']['pressure']
        humidity=jdata['main']['humidity']
        wind=jdata['wind']['speed']


        # config
        t.config(text=(temp,'°'))
        c.config(text=(condition,'|','FEELS',"LIKE",temp,'°'))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception:
        messagebox.showerror("Weather app","envalid entry!")

#_________________________________________________________________________________________________________________
root=Tk()
root.title("Weather Applications")
root.iconbitmap("tkinter\\Weather App\\img\\weathericon.ico")

# window and openscreen
w=900
h=500
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))

#__________________________________________________________________________________________________________________
# Search box
searchImg=PhotoImage(file="tkinter\\Weather App\\img\\search.png")
Label(image=searchImg).place(x=35,y=25)

entrySearch=Entry(root,width=17,bd=0,font=("poppins",25,"bold"),bg="#404040",fg="white",justify="center")
entrySearch.place(x=68,y=50)
entrySearch.focus()

SearchPhoto=PhotoImage(file="tkinter\\Weather App\\img\\search_icon.png")
searchButton=Button(image=SearchPhoto,borderwidth=0,cursor="hand2",bg="#404040",command=search).place(x=413,y=38)
#__________________________________________________________________________________________________________________
# box infromations
boxPhoto=PhotoImage(file="tkinter\\Weather App\\img\\box_copy.png")
boxInfo=Label(root,image=boxPhoto).pack(padx=5,pady=15,side=BOTTOM)

info1=Label(root,text="WIND",fg="white",bg="#ffce00",font=("Helvetica",15,"bold")).place(x=120,y=400)
info2=Label(root,text="HUMIDITY",fg="white",bg="#ffce00",font=("Helvetica",15,"bold")).place(x=250,y=400)
info3=Label(root,text="DESCRIPTION",fg="white",bg="#ffce00",font=("Helvetica",15,"bold")).place(x=430,y=400)
info4=Label(root,text="PRESSURE",fg="white",bg="#ffce00",font=("Helvetica",15,"bold")).place(x=650,y=400)

t=Label(font=("arial",58,"bold"),fg="#ee666d")
t.place(x=460,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=460,y=240)

w=Label(text="",font=("arial",20,"bold"),bg="#ffce00")
w.place(x=120,y=430)
h=Label(text="",font=("arial",20,"bold"),bg="#ffce00")
h.place(x=250,y=430)
d=Label(text="",font=("arial",20,"bold"),bg="#ffce00")
d.place(x=430,y=430)
p=Label(text="",font=("arial",20,"bold"),bg="#ffce00")
p.place(x=650,y=430)

#__________________________________________________________________________________________________________________
# weather Logo
logoImage=PhotoImage(file="tkinter\Weather App\img\weather logo_resize2.png")
logolabel=Label(image=logoImage).place(x=230,y=140)
#__________________________________________________________________________________________________________________
#time and current message
name=Label(root,font=("arial",20,"bold"))
name.place(x=35,y=100)
time=Label(root,font=("arial",15))
time.place(x=35,y=130)


root.mainloop()