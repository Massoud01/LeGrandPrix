from tkinter import *
from tkinter import ttk
from tkinter import font
import math
import requests
import json
import webbrowser
import matplotlib.pyplot as plt
#from newsapi import NewsApiClient


fenetre = Tk()
fenetre.resizable(False,False)
fenetre.minsize(1020,750)
link=StringVar()
Frame1=ttk.Frame(fenetre)
Frame1.grid()
Frame2=ttk.Frame(fenetre)
Frame2.grid()
Frame3=ttk.Frame(fenetre)
Frame3.grid()
fenetre.title("LE GRAND PRIX")

filename=PhotoImage(file="f1.png")
bglabel=Label(Frame2, image=filename)
bglabel.grid(padx=0,pady=0,row=2 ,columnspan=5)
def links():
    webbrowser. open(link.get())
st1=PhotoImage(file='standings 1.png')
st2=PhotoImage(file='standings 2.png')
pr=PhotoImage(file='previous races results.png')
r1=PhotoImage(file='r1.png')
r2=PhotoImage(file='r2.png')
r3=PhotoImage(file='r3.png')
r4=PhotoImage(file='r4.png')
r5=PhotoImage(file='r5.png')
r6=PhotoImage(file='r6.png')
r7=PhotoImage(file='r7.png')
r8=PhotoImage(file='r8.png')
r9=PhotoImage(file='r9.png')
r10=PhotoImage(file='r10.png')
r11=PhotoImage(file='r11.png')
r12=PhotoImage(file='r12.png')
r13=PhotoImage(file='r13.png')
r14=PhotoImage(file='r14.png')
r15=PhotoImage(file='r15.png')
r16=PhotoImage(file='r16.png')
r17=PhotoImage(file='r17.png')
r18=PhotoImage(file='r18.png')
r19=PhotoImage(file='r19.png')
r20=PhotoImage(file='r20.png')
r21=PhotoImage(file='r21.png')
r22=PhotoImage(file='r22.png')
r23=PhotoImage(file='r23.png')
c1=PhotoImage(file='c1.png')
c2=PhotoImage(file='c2.png')
c3=PhotoImage(file='c3.png')
c4=PhotoImage(file='c4.png')
c5=PhotoImage(file='c5.png')
c6=PhotoImage(file='c6.png')
c7=PhotoImage(file='c7.png')
c8=PhotoImage(file='c8.png')
c9=PhotoImage(file='c9.png')
c10=PhotoImage(file='c10.png')
c11=PhotoImage(file='c11.png')
c12=PhotoImage(file='c12.png')
c13=PhotoImage(file='c13.png')
c14=PhotoImage(file='c14.png')
c15=PhotoImage(file='c15.png')
c16=PhotoImage(file='c16.png')
c17=PhotoImage(file='c17.png')
c18=PhotoImage(file='c18.png')
c19=PhotoImage(file='c19.png')
c20=PhotoImage(file='c20.png')
c21=PhotoImage(file='c21.png')
c22=PhotoImage(file='c22.png')
c23=PhotoImage(file='c23.png')
d1=PhotoImage(file='lewis.png')
d2=PhotoImage(file='georges.png')
d3=PhotoImage(file='max.png')
d4=PhotoImage(file='checo.png')
d5=PhotoImage(file='charles.png')
d6=PhotoImage(file='carlos.png')
d7=PhotoImage(file='lando.png')
d8=PhotoImage(file='dani.png')
d9=PhotoImage(file='fernando.png')
d10=PhotoImage(file='esty.png')
d11=PhotoImage(file='pierre.png')
d12=PhotoImage(file='yuki.png')
d13=PhotoImage(file='seb.png')
d14=PhotoImage(file='lance.png')
d15=PhotoImage(file='logan.png')
d16=PhotoImage(file='alex.png')
d17=PhotoImage(file='valterri.png')
d18=PhotoImage(file='zhou.png')
d19=PhotoImage(file='kmag.png')
d20=PhotoImage(file='hulk.png')
s41=PhotoImage(file='mercedes.png')
s42=PhotoImage(file="alfaromeo.png")
s43=PhotoImage(file="alfatauri.png")
s44=PhotoImage(file="alpine.png")
s45=PhotoImage(file="redbull.png")  
s46=PhotoImage(file="aston.png")
s47=PhotoImage(file="williams.png")
s48=PhotoImage(file="ferrari.png")
s49=PhotoImage(file="mclaren.png")
s410=PhotoImage(file='haas.png')
immap=PhotoImage(file='map.png')
insta=PhotoImage(file='ins.png')
#newsapi = NewsApiClient(api_key='c7d746525bd3476897d37a9ee3c9a66e')
#qualybg=PhotoImage(file='qualybg.png')
wiki=PhotoImage(file='wiki.png')
abt=PhotoImage(file='about us.png')
yt=PhotoImage(file='youtube.png')
esib=PhotoImage(file='logo usj.png')
d1111=PhotoImage(file='d1111.png')
d21=PhotoImage(file='d21.png')
d31=PhotoImage(file='d31.png')
d41=PhotoImage(file='d41.png')
d51=PhotoImage(file='d51.png')
d61=PhotoImage(file='d61.png')
d71=PhotoImage(file='d71.png')
d81=PhotoImage(file='d81.png')
d91=PhotoImage(file='d91.png')
d101=PhotoImage(file='d101.png')
d111=PhotoImage(file='d111.png')
d121=PhotoImage(file='d121.png')
d131=PhotoImage(file='d131.png')
d141=PhotoImage(file='d141.png')
d151=PhotoImage(file='d151.png')
d161=PhotoImage(file='d161.png')
d171=PhotoImage(file='d171.png')
d181=PhotoImage(file='d181.png')
d191=PhotoImage(file='d191.png')
d201=PhotoImage(file='d201.png')

class driver():
    def __init__(self,fenetre,driverid):
        self.fenetree=fenetre
        self.driveridd=driverid
    def review(self):
        response=requests.get("http://ergast.com/api/f1/drivers/"+self.driveridd+".json")
        data=response.json()
        dic=data['MRData']
        webbrowser. open(dic['DriverTable']['Drivers'][0]['url'])
    s356=ttk.Style()
    s356.configure('S356pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black',background='white')
    
    def afficher1(self):

        self.fenetree.configure(bg='white')
        response=requests.get("http://ergast.com/api/f1/drivers/"+self.driveridd+".json")
        data=response.json()
        dic=data['MRData']
        ttk.Label(self.fenetree,text='\n\nPermanent Number: ',style='S356pecial.TLabel',foreground='red',background='white').grid(row=0,column=0)
        ttk.Label(self.fenetree,text='\n\n'+dic['DriverTable']['Drivers'][0]['permanentNumber'],style='S356pecial.TLabel',background='white').grid(row=0,column=1)
        ttk.Label(self.fenetree,text='Code: ',style='S356pecial.TLabel',foreground='red',background='white').grid(row=1,column=0)
        ttk.Label(self.fenetree,text=dic['DriverTable']['Drivers'][0]['code'],style='S356pecial.TLabel',background='white').grid(row=1,column=1)
        ttk.Button(self.fenetree,image=wiki,command=self.review).grid(padx=10,row=10,column=3)
        ttk.Label(self.fenetree,text='FIRST NAME: ',style='S356pecial.TLabel',foreground='red',background='white').grid(row=2,column=0)
        ttk.Label(self.fenetree,text=dic['DriverTable']['Drivers'][0]['givenName'],style='S356pecial.TLabel',background='white').grid(row=2,column=1)
        ttk.Label(self.fenetree,text='FAMILY NAME:',style='S356pecial.TLabel',foreground='red',background='white').grid(row=3,column=0)
        ttk.Label(self.fenetree,text=  dic['DriverTable']['Drivers'][0]['familyName'],style='S356pecial.TLabel',background='white').grid(row=3,column=1)
        ttk.Label(self.fenetree,text='Date of birth: ',style='S356pecial.TLabel',foreground='red',background='white').grid(row=4,column=0)
        ttk.Label(self.fenetree,text=dic['DriverTable']['Drivers'][0]['dateOfBirth'],style='S356pecial.TLabel',background='white').grid(row=4,column=1)
        ttk.Label(self.fenetree,text='Nationality: ',style='S356pecial.TLabel',foreground='red',background='white').grid(row=5,column=0)
        ttk.Label(self.fenetree,text=dic['DriverTable']['Drivers'][0]['nationality'],style='S356pecial.TLabel',background='white').grid(row=5,column=1)
        ttk.Label(self.fenetree,text='Team',style='S356pecial.TLabel',foreground='red',background='white').grid(row=6,column=0)
        ttk.Label(self.fenetree,text='World championships',style='S356pecial.TLabel',foreground='red',background='white').grid(row=7,column=0)
        ttk.Button(self.fenetree,image=insta,command=links).grid(row=10,column=0)
        ttk.Label(self.fenetree,text='Biography',style='S356pecial.TLabel',foreground='red',background='white').grid(row=9,column=0)
        



class circuits():
    def __init__(self,fenetree,circuitidd):
        self.fenetre=fenetree
        self.circuitid=circuitidd
    def review(self):
        response=requests.get("http://ergast.com/api/f1/circuits/"+self.circuitid+".json")
        data=response.json()
        dic=data['MRData']
        dic2=dic['CircuitTable']['Circuits'][0]
        webbrowser. open(dic2['url'])
    s0=ttk.Style()
    s0.configure('S0pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black')
    def afficherCircuit(self):
        self.fenetre.minsize(420,200)
        ttk.Label(self.fenetre,image=img1).place(x=0,y=0)
        response=requests.get("http://ergast.com/api/f1/circuits/"+self.circuitid+".json")
        data=response.json()
        dic=data['MRData']
        dic2=dic['CircuitTable']['Circuits'][0]
        ttk.Label(self.fenetre,text="\nCircuit Name :",style='S0pecial.TLabel',foreground='red',background='white').grid(padx=20,row=0,column=0)
        ttk.Label(self.fenetre,text='\n'+dic2['circuitName'],style='S0pecial.TLabel',background='white').grid(row=0,column=1)
        ttk.Label(self.fenetre,text='CITY: ',style='S0pecial.TLabel',foreground='red',background='white').grid(row=1,column=0)
        ttk.Label(self.fenetre,text=dic2['Location']['locality'],style='S0pecial.TLabel',background='white').grid(row=1,column=1)
        ttk.Label(self.fenetre,text='Coordinates :',style='S0pecial.TLabel',foreground='red',background='white').grid(row=2,column=0)
        ttk.Label(self.fenetre,text='Lattitude:',style='S0pecial.TLabel',foreground='red',background='white').grid(row=3,column=0)
        ttk.Label(self.fenetre,text= dic2['Location']['lat'],style='S0pecial.TLabel',background='white').grid(row=4,column=0)
        ttk.Label(self.fenetre,text='Longitude:',style='S0pecial.TLabel',foreground='red',background='white').grid(row=3,column=1)
        ttk.Label(self.fenetre,text=dic2['Location']['long'],style='S0pecial.TLabel',background='white').grid(row=4,column=1)
        ttk.Label(self.fenetre,text='COUNTRY: ',style='S0pecial.TLabel',foreground='red',background='white').grid(row=5,column=0)
        ttk.Label(self.fenetre,text= dic2['Location']['country'],style='S0pecial.TLabel',background='white').grid(row=5,column=1)
        ttk.Button(self.fenetre,image=wiki,command=self.review).grid(row=6,column=2)
        ttk.Button(self.fenetre,image=immap,command=links).grid(row=6,column=0,pady=20)
stats=PhotoImage(file='lallous.png')



class constructors():
     def __init__(self,fenetree,constructoridd,teamc,techc,wc,base,chassis,pu):
         self.fenetre=fenetree
         self.constructorid=constructoridd
         self.teamc=teamc
         self.techc=techc
         self.wc=wc
         self.base=base
         self.chassis=chassis
         self.pu=pu
     def review(self):
        response=requests.get("http://ergast.com/api/f1/constructors/"+self.constructorid+".json")
        data=response.json()
        dic=data['MRData']
        webbrowser. open(dic['ConstructorTable']['Constructors'][0]['url'])
     s1=ttk.Style()
     s1.configure('S1pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='white',background='black')
     s2=ttk.Style()
     s2.configure('S22pecial.TLabel', font=('Formula1 Display Bold', 20, 'bold'), foreground='red',background='black')
     def afficher(self):
         self.fenetre.configure(bg='black')
         self.fenetre.minsize(450,280)
         response=requests.get("http://ergast.com/api/f1/constructors/"+self.constructorid+".json")
         data=response.json()
         dic=data['MRData']
         ttk.Label(self.fenetre,text=dic['ConstructorTable']['Constructors'][0]['name'],style='S22pecial.TLabel').grid(padx=10,pady=20,row=0,column=1)
         ttk.Label(self.fenetre,text="Constructor",style='S1pecial.TLabel',foreground='red').grid(row=1,column=0)
         ttk.Label(self.fenetre,text=dic['ConstructorTable']['Constructors'][0]['name'],style='S1pecial.TLabel').grid(row=1,column=1)
         ttk.Button(self.fenetre,image=wiki,command=self.review).grid(row=0,column=0)
         ttk.Label(self.fenetre,text="Nationality",style='S1pecial.TLabel',foreground='red').grid(row=11,column=0)
         ttk.Label(self.fenetre,text=dic['ConstructorTable']['Constructors'][0]['nationality'],style='S1pecial.TLabel').grid(row=11,column=1)
         ttk.Label(self.fenetre,text='Team Chief',style='S1pecial.TLabel',foreground='red').grid(row=5,column=0)
         ttk.Label(self.fenetre,text=self.teamc,style='S1pecial.TLabel',foreground='white').grid(row=5,column=1)
         ttk.Label(self.fenetre,text='World Championships',style='S1pecial.TLabel',foreground='red').grid(row=6,column=0,padx=10)
         ttk.Label(self.fenetre,text='Technical Chief',style='S1pecial.TLabel',foreground='red').grid(row=7,column=0)
         ttk.Label(self.fenetre,text='Base',style='S1pecial.TLabel',foreground='red').grid(row=8,column=0)
         ttk.Label(self.fenetre,text='Chassis',style='S1pecial.TLabel',foreground='red').grid(row=9,column=0)
         ttk.Label(self.fenetre,text='Power Unit',style='S1pecial.TLabel',foreground='red').grid(row=10,column=0)
         ttk.Label(self.fenetre,text=self.techc,style='S1pecial.TLabel',foreground='white').grid(row=7,column=1)
         ttk.Label(self.fenetre,text=self.pu,style='S1pecial.TLabel',foreground='white').grid(row=10,column=1)
         ttk.Label(self.fenetre,text=self.chassis,style='S1pecial.TLabel',foreground='white').grid(row=9,column=1)
         ttk.Label(self.fenetre,text=self.wc,style='S1pecial.TLabel',foreground='white').grid(row=6,column=1)
         ttk.Label(self.fenetre,text=self.base,style='S1pecial.TLabel',foreground='white').grid(row=8,column=1)

class schedule():
    def __init__(self,fenetree,yearroundd):
        self.fenetre=fenetree
        self.yearround=yearroundd
    def review(self):
        yr=str(self.yearround)
        response=requests.get("http://ergast.com/api/f1/2023/"+yr+".json")
        data=response.json()
        dic=data['MRData']
        webbrowser. open(dic['RaceTable']['Races'][0]['url'])
    s2=ttk.Style()
    s2.configure('S2pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black',background='white')
    style=ttk.Style()
    style.configure('TButton',font=('Formula1 Display Bold,',10,'bold'),borderwidth='3')
    style.map('TButton',background=[('active','!disabled','white')],foreground=[('active','!disabled','red')])
    def afficherS(self):
        self.fenetre.configure(bg='white')
        yr=str(self.yearround)
        response=requests.get("http://ergast.com/api/f1/2022/"+yr+".json")
        data=response.json()
        dic=data['MRData']
        try:
            ttk.Label(self.fenetre,text="\nFirst Practice",style='S2pecial.TLabel',foreground='red').grid(row=0,column=0)
            ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=1,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['FirstPractice']['date'],style='S2pecial.TLabel').grid(row=1,column=1)
            ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=2,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['FirstPractice']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=2,column=1)
            ttk.Label(self.fenetre,text="Second Practice",style='S2pecial.TLabel',foreground='red').grid(padx=10,row=3,column=0)
            ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=4,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['SecondPractice']['date'],style='S2pecial.TLabel').grid(row=4,column=1)
            ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=5,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['SecondPractice']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=5,column=1)
           
            ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=7,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['ThirdPractice']['date'],style='S2pecial.TLabel').grid(row=7,column=1)
            ttk.Label(self.fenetre,text="Third Practice",style='S2pecial.TLabel',foreground='red').grid(row=6,column=0)
            ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=8,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['ThirdPractice']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=8,column=1)
            ttk.Label(self.fenetre,text="Qualifying",style='S2pecial.TLabel',foreground='red').grid(row=9,column=0)
            ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=10,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['Qualifying']['date'],style='S2pecial.TLabel').grid(row=10,column=1)
            ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=11,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['Qualifying']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=11,column=1)
            ttk.Label(self.fenetre,text="Final Race",style='S2pecial.TLabel',foreground='red').grid(row=12,column=0)
            ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=13,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['date'],style='S2pecial.TLabel').grid(row=13,column=1)
            ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=14,column=0)
            ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=14,column=1)

        except Exception:
            try:
                ttk.Label(self.fenetre,text="\nFirst Practice",style='S2pecial.TLabel',foreground='red').grid(row=0,column=0)
                ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=1,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['FirstPractice']['date'],style='S2pecial.TLabel').grid(row=1,column=1)
                ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=2,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['FirstPractice']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=2,column=1)
                ttk.Label(self.fenetre,text="Second Practice",style='S2pecial.TLabel',foreground='black').grid(row=3,column=0)
                ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=4,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['SecondPractice']['date'],style='S2pecial.TLabel').grid(row=4,column=1)
                ttk.Label(self.fenetre,text='Time:',style='S2pecial.TLabel',foreground='black').grid(row=5,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['SecondPractice']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=5,column=1)
                ttk.Label(self.fenetre,text="Sprint Race",style='S2pecial.TLabel',foreground='red').grid(row=6,columnspan=1)
                ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=7,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['Sprint']['date'],style='S2pecial.TLabel').grid(row=7,column=1)
                ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=8,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['Sprint']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=8,column=1)
                ttk.Label(self.fenetre,text="Qualifying",style='S2pecial.TLabel',foreground='red').grid(row=9,column=0)
                 
                ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=10,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['Qualifying']['date'],style='S2pecial.TLabel').grid(row=10,column=1)
                ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=11,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['Qualifying']['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=11,column=1)
                ttk.Label(self.fenetre,text="Final Race",style='S2pecial.TLabel',foreground='red').grid(row=12,column=0)
                ttk.Label(self.fenetre,text="Date:",style='S2pecial.TLabel',foreground='black').grid(row=13,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['date'],style='S2pecial.TLabel').grid(row=13,column=1)
                ttk.Label(self.fenetre,text="Time:",style='S2pecial.TLabel',foreground='black').grid(row=14,column=0)
                ttk.Label(self.fenetre,text=dic['RaceTable']['Races'][0]['time'].strip("Z")+" UTC",style='S2pecial.TLabel').grid(row=14,column=1)
            
            finally:
                None




def rasme():
    response=requests.get("http://ergast.com/api/f1/constructorStandings/1.json?limit=80&offset=0")
    data=response.json()
    dic=data['MRData']['StandingsTable']['StandingsLists']
    dictionnaire={}
    for k in dic:
        dictionnaire[k['ConstructorStandings'][0]['Constructor']['name']]=0
        
    for i in dictionnaire.keys():
        for j in dic:
            if  i == j['ConstructorStandings'][0]['Constructor']['name']:
                dictionnaire[i]=dictionnaire[i]+1
    clist=[]
    wlist=[]
    for keys in dictionnaire:
        clist.append(keys)
    for i in dictionnaire.keys():
        if dictionnaire[i]>2:
            wlist.append(dictionnaire[i])
        else:
            clist.remove(i)
    ln=len(clist)
    mx=max(wlist)
    ix=wlist.index(mx)
    
    expl=[0]*ln
    expl[ix]=0.1
    plt.pie(wlist,labels=clist,autopct="%2.1f%%",explode=expl)
    plt.show()

def creermalyounfenetre1():
    global fenetrec1
    #nzid s+ google maps location
    link.set('https://www.google.com/maps/d/edit?mid=1qYcVPP53MTQfygv3NjAvKGUEU7k&source=embed&hl=en&geocode&ie=UTF8&t=h&msa=0&ll=26.035885,50.515308&spn=0.023136,0.025749&z=14')
    fenetrec1= Toplevel(fenetre2) 
    fenetrec1.title("Bahrain International Circuit")
    fenetrec1.minsize(200,200)
    circuitidd='bahrain'
    circuits(fenetrec1,circuitidd).afficherCircuit()
def creermalyounfenetre2():
    global fenetre2
    link.set('https://maps.google.com/maps/ms?msid=211694346031887027115.0004b1bcc624d6b28a0f3&msa=0&ie=UTF8&t=m&vpsrc=6&ll=22.674847')
    fenetrec2= Toplevel(fenetre2) 
    fenetrec2.title("Jeddah Circuit")
    fenetrec2.minsize(200,200)
    circuitidd='jeddah'
    circuits(fenetrec2,circuitidd).afficherCircuit()
def creermalyounfenetre3():
    global fenetre2
    fenetrec3 = Toplevel(fenetre2) 
    fenetrec3.title("Melbourne Circuit")
    fenetrec3.minsize(200,200)
    circuitidd='albert_park'
    circuits(fenetrec3,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/d/viewer?mid=zA-uh8QmJ0ig.kP0AWldqBkXk&hl=en_US')
    
def creermalyounfenetre4():
    global fenetre2
    
    fenetrec4 = Toplevel(fenetre2) 
    fenetrec4.title("Autodromo De Monza")
    fenetrec4.minsize(200,200)
    circuitidd='monza'
    circuits(fenetrec4,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?oe=UTF8&ie=UTF8&t=h&msa=0&msid=100972855643583900632.000474526ae93fee6b827')

def creermalyounfenetre5():
    global fenetre2
    
    fenetrec5 = Toplevel(fenetre2) 
    fenetrec5.title("Miami International Circuit")
    fenetrec5.minsize(200,200)
    circuitidd='miami'
    circuits(fenetrec5,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/dir/33.8853888,35.5565568/miami+circuit+google+maps/@1.8355984,-109.1451946,3z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x88d9af406b8720d7:0x74c3a0ed602754ae!2m2!1d-80.2313937!2d25.9568736')
    
def creermalyounfenetre6():
    global fenetre2
    fenetrec6 = Toplevel(fenetre2) 
    fenetrec6.title("Barcelona Circuit")
    fenetrec6.minsize(200,200)
    circuitidd='catalunya'
    circuits(fenetrec6,circuitidd).afficherCircuit()
    link.set('https://www.google.com/mymaps/viewer?mid=1R0UX0BNuGx8xC15AKcPCrpBrmCc&hl=en')
    
def creermalyounfenetre7():
    global fenetre2
    
    fenetrec7 = Toplevel(fenetre2) 
    fenetrec7.title("Monaco Circuit")
    fenetrec7.minsize(200,200)
    circuitidd='monaco'
    circuits(fenetrec7,circuitidd).afficherCircuit()
    link.set('https://www.google.com/mymaps/viewer?mid=ziboiLFy8Sg8.k4i9qLraWmR8&hl=en_US')
    
def creermalyounfenetre8():
    global fenetre2
    fenetrec8 = Toplevel(fenetre2) 
    fenetrec8.title("Baku")
    fenetrec8.minsize(200,200)
    circuitidd='BAK'
    circuits(fenetrec8,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/dir/33.8853888,35.5565568/baku+circuit+google+maps/@36.7883048,33.7058213,5z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x40307db472eb07d1:0x529ac68af9a1cec2!2m2!1d49.8531816!2d40.3729181')
def creermalyounfenetre9():
    global fenetre2
    fenetrec9 = Toplevel(fenetre2) 
    fenetrec9.title("Canada")
    fenetrec9.minsize(200,200)
    circuitidd='villeneuve'
    circuits(fenetrec9,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/d/viewer?ie=UTF8&hl=en&msa=0&ll=45.505204000000035%2C-73.52857600000002&spn=0.021054%2C0.042915&z=14&source=embed&mid=12IbfMKiJJCDMZiXIcZeAT616hmY')
def creermalyounfenetre10():
    global fenetre2
    fenetrec10= Toplevel(fenetre2) 
    fenetrec10.title("SILVERSTONE-UNITED KINGDOM")
    fenetrec10.minsize(200,200)
    circuitidd='silverstone'
    circuits(fenetrec10,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?msa=0&msid=205505632969226629874.0004cb67c804249bc2ea1')
def creermalyounfenetre11():
    global fenetre2
    
    fenetrec11= Toplevel(fenetre2) 
    fenetrec11.title("SIELBURG")
    fenetrec11.minsize(200,200)
    circuitidd='red_bull_ring'
    circuits(fenetrec11,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/d/viewer?mid=1ttCI9jsgmG0TvoklQZmc7KF7uM4&hl=en_US')

def creermalyounfenetre12():
    global fenetre2
    
    fenetrec123 = Toplevel(fenetre2) 
    fenetrec123.title("CIRCUIT PAUL RICARD")
    fenetrec123.minsize(200,200)
    circuitidd='ricard'
    circuits(fenetrec123,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?ie=UTF8&oe=UTF8&msa=0&msid=201675188937812768046.0004a06464679ae163259')

def creermalyounfenetre13():
    global fenetre2
    
    fenetre122 = Toplevel(fenetre2) 
    fenetre122.title("Hongaroring")
    fenetre122.minsize(200,200)
    circuitidd='hungaroring'
    circuits(fenetre122,circuitidd).afficherCircuit()
    link.set('https://www.google.com/mymaps/viewer?mid=1fOpuIp8i83Fr2wDA6cKO7aRVaZU&hl=en_US')


def creermalyounfenetre14():
    global fenetre2
    
    fenetrec13 = Toplevel(fenetre2) 
    fenetrec13.title("Spa")
    fenetrec13.minsize(200,200)
    circuitidd='spa'
    circuits(fenetrec13,circuitidd).afficherCircuit()
    link.set('http://mapsengine.google.com/map/embed?mid=z6GKDtpCtj1U.kdkZJl4JTHXA')

def creermalyounfenetre15():
    global fenetre2
    
    fenetrec14 = Toplevel(fenetre2) 
    fenetrec14.title("Zandvoort IC")
    fenetrec14.minsize(200,200)
    circuitidd='zandvoort'
    circuits(fenetrec14,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/d/embed?mid=1VI7ONE4WlsSKErPG_rsFHCOjOQs&t=m&msa=0&source=embed&ie=UTF8&z=13&output=embed')

def creermalyounfenetre16():
    global fenetre2
    
    fenetrec15 = Toplevel(fenetre2) 
    fenetrec15.title("Autodromo Nazionale di Monza")
    fenetrec15.minsize(200,200)
    circuitidd='monza'
    circuits(fenetrec15,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?oe=UTF8&ie=UTF8&t=h&msa=0&msid=100972855643583900632.000474526ae93fee6b827')
    
def creermalyounfenetre17():
    global fenetre2

    fenetrec16 = Toplevel(fenetre2) 
    fenetrec16.title("Sochi Autodrom")
    fenetrec16.minsize(200,200)
    circuitidd='sochi'
    circuits(fenetrec16,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?ie=UTF8&oe=UTF8&msa=0&msid=215652610817091085991.0004e913ad298be918de3')

def creermalyounfenetre18():
    global fenetre2
    
    fenetrec17 = Toplevel(fenetre2) 
    fenetrec17.title("Marina Bay Street Circuit")
    fenetrec17.minsize(200,200)
    circuitidd='marina_bay'
    circuits(fenetrec17,circuitidd).afficherCircuit()
    link.set('https://mapsengine.google.com/map/edit?mid=zA-uh8QmJ0ig.kq8c0cQmMQz8')

def creermalyounfenetre19():
    global fenetre2
    
    fenetrec19 = Toplevel(fenetre2) 
    fenetrec19.title("Suzuka Circuit")
    fenetrec19.minsize(200,200)
    circuitidd='suzuka'
    circuits(fenetrec19,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?ie=UTF8&hl=en&msa=0&msid=114275729164008064732.0004786811016e795085a&ll=34.853504,136.55578&spn=0.042762,0.067791&output=embed')
    
def creermalyounfenetre20():
    global fenetre2
    
    fenetrec20 = Toplevel(fenetre2) 
    fenetrec20.title("Americas  Circuit")
    fenetrec20.minsize(200,200)
    circuitidd='americas'
    circuits(fenetrec20,circuitidd).afficherCircuit()
    link.set('https://maps.google.com/maps/ms?msa=0&msid=216135017197510429296.0004c974ba355268d7e67&ie=UTF8&t=m&ll=30.059586,-97.053223&spn=1.663987,3.295898&z=8&source=embed')
def creermalyounfenetre21():
    global fenetre2
    
    fenetrec21= Toplevel(fenetre2) 
    fenetrec21.title("Autódromo Hermanos Rodríguez")
    fenetrec21.minsize(200,200)
    circuitidd='rodriguez'
    circuits(fenetrec21,circuitidd).afficherCircuit()
    link.set('https://www.google.com/mymaps/viewer?mid=17K5FSw9YNj9Eh7X27-aLpJZdwBo&hl=en_US')

def creermalyounfenetre22():
    global fenetre2
    
    fenetrec22 = Toplevel(fenetre2) 
    fenetrec22.title("Autódromo José Carlos Pace")
    fenetre.minsize(200,200)
    circuitidd='interlagos'
    circuits(fenetrec22,circuitidd).afficherCircuit()
    link.set('https://mapcarta.com/N205160244')


def creermalyounfenetre23():
    global fenetre2
    
    fenetrec23= Toplevel(fenetre2) 
    fenetrec23.title("Yas Marina Circuit")
    fenetrec23.minsize(200,200)
    circuitidd='yas_marina'
    circuits(fenetrec23,circuitidd).afficherCircuit()
    link.set('https://www.google.com/maps/d/edit?mid=1ZTINHYdeXtKGkyRLaLEeEniirls&vpsrc=6&ctz=240&ie=UTF8&t=m&oe=UTF8&msa=0')

def creermalyounfenetre24():
    global fenetre3
    driveridd='hamilton'
    fenetred1= Toplevel(fenetre3) 
    fenetred1.title("Lewis Hamilton")
    fenetred1.minsize(300,300)
    driver(fenetred1,'hamilton').afficher1()
    ttk.Label(fenetred1,image=d111).place(x=650,y=25)
    link.set('https://www.instagram.com/lewishamilton/')
    ttk.Label(fenetred1,text='Mercedes',style='S356pecial.TLabel',foreground='black',background='white').grid(row=6,column=1)
    ttk.Label(fenetred1,text='7',style='S356pecial.TLabel',foreground='black',background='white').grid(row=7,column=1)
    ttk.Label(fenetred1,background='white',text="‘Still I Rise’ – these are the words emblazoned across the back of Lewis Hamilton’s \nhelmet and tattooed across his shoulders, and ever since annihilating expectations \nwith one of the greatest rookie performances in F1 history in 2007, that’s literally all \nhe’s done: risen to the top of the all-time pole positions list ahead of his hero Ayrton \nSenna, surged into first place in the wins column surpassing the inimitable Michael \nSchumacher, and then matched the legendary German’s seven world titles.\n\nIs he the G.O.A.T? Few would deny that he’s in the conversation – and what’s more \nhe’s got there his way, twinning his relentless speed with a refusal to conform to \nstereotypes for how a racing driver should think, dress or behave.\n\nRespect is hard earned in F1, but Hamilton – now Sir Lewis Hamilton to be precise – has it from \nevery one of his peers. Why? Because they know that whatever the track, whatever \nthe conditions, whatever the situation, when his visor goes down and the lights go \nout, it’s Hammertime.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)

def creermalyounfenetre25():
    global fenetre3
    driveridd='russell'
    fenetred2 = Toplevel(fenetre3) 
    fenetred2.title("Georges Russel")
    fenetred2.minsize(300,300)
    driver(fenetred2,driveridd).afficher1()
    ttk.Label(fenetred2,image=d21).place(x=650,y=25)
    link.set('https://www.instagram.com/georgerussell63/')
    ttk.Label(fenetred2,text='Mercedes',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred2,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred2,background='white',text="He’s the driver with the motto: “If in doubt, go flat out”.\n\nGeorge Russell has lived by it in his F1 career to date, out-qualifying seasoned team mate Robert Kubica at all 21 \nGrands Prix in his rookie season, putting Williams back on the podium in 2021, and \nlanding a Mercedes race seat alongside Lewis Hamilton for 2022.\n\nThat brilliant baseline speed served Russell well as he totted up titles on his way to Formula 1. \nThe Briton stormed to the 2017 GP3 championship and delivered the 2018 Formula 2\n crown under immense pressure.\n\nSpotting his potential, world champions Mercedes swooped to sign him to their junior programme in 2017,\n when Russell already had a DTM deal on the table. He banked more experience with \npractice sessions with Force India and tests for the Silver Arrows, before landing \nhis Mercedes-powered Williams race drive.\nA refusal to cede ground to his rivals - and commitment to a tricky pass – underpins Russell’s winning mentality. \nAnd it’s what got him the call-up to replace Lewis Hamilton for a one-off Mercedes\n appearance for Sakhir 2020 when the reigning champ was struck down by Covid-19.\n\nThat star turn saw Russell miss out on pole by just 0.026s and then outrace Mercedes stalwart Valtteri Bottas.\n Only a bungled pit stop and a heart-breaking late puncture prevented a near-certain\nmaiden win for the up-and-coming super-sub. \nHe kept his head down at Williams in 2021, scoring his first points and podium, all \nthe while keeping his eye on the bigger prize. Having proved himself a hard worker \nand a tenacious talent, that prize arrived in the form of a chance to take on \ncompatriot and seven-time champion Hamilton in identical machinery.\nHuge challenge, but as always, ‘Russell the Rocket’ will be going flat out.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)

def creermalyounfenetre26():
    global fenetre3
    fenetred3 = Toplevel(fenetre3) 
    fenetred3.title("verstappen")
    fenetred3.minsize(300,300)
    driveridd='max_verstappen'
    driver(fenetred3,driveridd).afficher1()
    ttk.Label(fenetred3,image=d31).place(x=650,y=25)
    link.set('https://www.instagram.com/maxverstappen1/')
    ttk.Label(fenetred3,text='Redbull',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred3,text='1',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred3,text="He’s Max by name, and max by nature.\nArriving as Formula 1’s youngest ever competitor at just 17 years old, Verstappen \npushed his car, his rivals and the sport’s record books to the limit. \nThe baby-faced Dutchman with the heart of a lion took the Toro Rosso – and then \nthe Red Bull – by the horns with his instinctive racing style.\n\nF1’s youngest points scorer soon became its youngest race winner – at the age of 18\nyears and 228 days – with an opportunistic but controlled drive on debut for Red Bull\n in Barcelona 2016. A true wheel-to-wheel racer, another stunning drive in Brazil\n from the back of the pack to the podium on a treacherous wet track kept the \nplaudits coming.\n\nVerstappen’s no-holds-barred attitude and hard defending have sometimes landed \nhim in hot water with his peers and paymasters. But the mistakes that initially \nmarred his potential have given way to maturity, while the bravado and energy that \nmake him a blockbuster talent have remained – and the victories have kept on \ncoming, culminating in his first F1 drivers’ title following that already legendary,\nfinal-round showdown with Lewis Hamilton in 2021.\n\nThe son of former F1 driver Jos Verstappen and super-quick karting Mum Sophie Kumpen,\n racing runs through his genes. Despite moving out of Dad’s house to live in Monaco,\nVerstappen remains close to his family, and though he’s not afraid to speak his mind,\nhe can still be surprisingly shy.\n\nHaving become the Netherlands' first world champion aged just 24, \nthe expectations for the next generation’s leading light are sky high – but with \nVerstappen there’s a feeling that the sky’s the limit.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    
def creermalyounfenetre27():
    global fenetre3

    fenetred4= Toplevel(fenetre3) 
    fenetred4.title("Sergio Checo Perez")
    fenetred4.minsize(300,300)
    driveridd='perez'
    driver(fenetred4,driveridd).afficher1()
    
    ttk.Label(fenetred4,image=d41).place(x=650,y=25)
    link.set('https://www.instagram.com/schecoperez/')
    ttk.Label(fenetred4,text='Redbull',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred4,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred4,text="He’s the fighter with a gentle touch from the land of the Lucha Libre.\n\nPerez’s reputation in F1 has been built on opposite approaches to Grand Prix racing.\n On the one hand, he is a punchy combatant who wrestles his way through the \npack and into the points. Never afraid to add a bit of spice to his on-track encounters,\neven his team mates don’t always escape the Mexican’s heat.\n\nThen on the other hand, Perez is a smooth operator, a master at managing tyres \nto eke out extra performance and give him the upper hand on strategy. \nA firm favourite on the grid after his time with Sauber, McLaren, Force India and Racing Point,\n Perez has matured into an analytical racer and team player.\n\nA proud countryman, the Guadalajara gunslinger has amassed more points \nthan any other Mexican in the history of F1. In Sakhir 2020 he also matched hero \nand compatriot Pedro Rodriguez by taking the chequered flag in first – a performance \nthat landed him a seat with title contenders Red Bull.\n\nThere he provided strong \nsupport to Max Verstappen’s 2021 championship-winning campaign, also adding another\n victory to his own tally. More wins may not be assured, especially with Verstappen \nas team mate, but Perez working hard and racing with his heart are.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
def creermalyounfenetre28():
    global fenetre3
    
    fenetred5 = Toplevel(fenetre3) 
    fenetred5.title("Charles Leclerc")
    fenetred5.minsize(300,300)
    driveridd='leclerc'
    driver(fenetred5,driveridd).afficher1()
    ttk.Label(fenetred5,image=d51).place(x=650,y=25)
    link.set('https://www.instagram.com/charles_leclerc/')
    ttk.Label(fenetred5,text='Ferrari',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred5,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred5,text="Born in the Mediterranean idyll of Monaco, Leclerc arrived in F1 on a tidal wave of expectation.\n\nPractically peerless on his way to the GP3 and Formula 2 crowns, he showcased a \ndazzling array of skills from scorching pole positions, commanding victories – even\n when his car caught fire twice at Silverstone – to an ability to muscle his way \nthrough the pack. Winning back-to-back championships also taught Leclerc how to \nhandle pressure, another useful tool in the big pond of Formula 1 racing.\n\nStepping up to F1 in 2018, Leclerc showed flashes of ballistic pace on Saturdays \nand racing brilliance on Sundays, dragging his Sauber beyond its limits – and earning \nhimself a money-can’t-buy race seat at Ferrari for 2019, stepping into the shoes of \nthe Scuderia’s last world champion, Kimi Raikkonen.\n\nThere he immediately put the cat among the proverbial pigeons, unafraid to go\n wheel-to-wheel with established number one, Sebastian Vettel. A maiden F1 \nvictory at Spa was followed by another a week later on Ferrari’s hallowed home turf \nof Monza. The tifosi had found another new hero – who then became the first man\nto out-score Vettel over a season with the Scuderia, a feat he repeated in crushing \nfashion the following year.\n\nOut of the car, Leclerc is modest and thoughtful - but then he is on his own very \npersonal mission. This exciting young talent is racing for his late father Herve and his \nfriend and mentor Jules Bianchi, the F1 driver who died in 2015. \n\nOn the evidence so far, he is doing them both proud.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)


def creermalyounfenetre29():
    global fenetre3
    
    fenetred6 = Toplevel(fenetre3) 
    fenetred6.title("Carlos Sainz")
    fenetred6.minsize(300,300)
    driveridd='sainz'
    driver(fenetred6,driveridd).afficher1()
    ttk.Label(fenetred6,image=d61).place(x=650,y=25)
    link.set('https://www.instagram.com/carlossainz55/')
    ttk.Label(fenetred6,text='Ferrari',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred6,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred6,text="He’s the matador from Madrid racing royalty. \n\nAfter entering F1’s Bull Ring paired alongside Max Verstappen at Toro Rosso in 2015,\n Sainz quickly showed his fighting spirit. A tenacious racer, he puts the car on \nthe edge as he hustles his way through the pack. No wonder Sainz has earned the \nnickname Chilli.\n\nBut the Spaniard is intelligent as well as instinctive, thinking his way through a race\n and into the points. This calm temperament follows him off track where he remains \nunfazed by the pressures of forging a Grand Prix career with a famous name. \n\nSainz is the son of double World Rally champion, also his namesake, and has brought\n some of Dad’s driving skills to the F1 circuit – junior loves a delicious dose of drift \nfor one. \n\nAfter following in his famous father’s tyre tracks, Sainz has had big racing boots to \nfill – first at McLaren where he replaced his childhood hero Fernando Alonso, \nand now at Ferrari, in the seat formerly owned by Sebastian Vettel. It is never \neasy living in the shadow of sporting giants, but Sainz has shown the drive and \ndisposition to deal with it. Vamos!\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)

def creermalyounfenetre30():
    global fenetre3
    
    fenetred7 = Toplevel(fenetre3) 
    fenetred7.title("Lando Norris")
    fenetred7.minsize(300,300)
    driveridd='norris'
    driver(fenetred7,driveridd).afficher1()
    ttk.Label(fenetred7,image=d71).place(x=650,y=25)
    link.set('https://www.instagram.com/landonorris/')
    ttk.Label(fenetred7,text='McLaren',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred7,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred7,text="Lando Norris may not be named after Star Wars rebel Lando Calrissian\n - his Mum just liked the moniker - but he has flair and fighting spirit in bountiful supply.\n\nMcLaren had the British teenager on their books for two years before fast-tracking \nhim into F1’s galaxy of stars in 2019. A firecracker in his junior career, with a penchant\n for pole positions and wheel-to-wheel tussles, Norris didn’t let them down.\n\nPaired with the highly-rated – and far more experienced – Carlos Sainz, his rookie \nseason was impressive, edging the Spaniard in their head-to-head qualifying battle, \nscoring points on 11 occasions, and only narrowly missing out on a top-10 championship\n placing. It was a similar pattern in 2020, with the affable Brit securing a maiden \npodium and moving up to ninth overall.\nHis unstoppable rise continued in 2021, with a further four podiums and almost a \nrace win as he dominated another more senior team mate, Daniel Ricciardo, to move \nup to P6 in the final driver standings.\n\nAn exciting talent on track, away from it Norris brims with a modest charm and an \nartistic side sees him design and paint his own race gear as a hobby. The focus for \nthe future is allying artistry and ambition on track as McLaren rely on the promise of \nyouth to take them back to the top.\n\nNorris hopes the downforce will be with him…\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    
    
   

def creermalyounfenetre31():
    global fenetre3
    
    fenetred8 = Toplevel(fenetre3) 
    fenetred8.title("Daniel Ricciardo")
    fenetre.minsize(300,300)
    driveridd='ricciardo'
    driver(fenetred8,driveridd).afficher1()
    ttk.Label(fenetred8,image=d81).place(x=650,y=25)
    link.set('https://www.instagram.com/danielricciardo/')
    ttk.Label(fenetred8,text='McLaren',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred8,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred8,text="The self-styled “Honey Badger” is fuzzy on the outside and feisty on the inside. \nDrivers beware because behind Ricciardo’s laidback persona and big grin is a \nrazor-sharp racer with a bite. \n\nThe Australian combines all-out speed with impressive race craft. Never afraid \nto push to the limits if it means pulling off a pass, Ricciardo is a proven race-winner, \ncapable of consistently finishing at the business end of the championship table given \nthe right machinery.\n\nA regular podium-finisher in his days with Red Bull, Ricciardo has christened \nthe steps around the world with a dousing of Aussie culture – the ‘Shoey’ – as he \nquaffed champagne from a soggy racing boot. Yes it’s goofy, but the trademark \ncelebration illustrates why he is loved for his sense of humour but never \nunderestimated on track.\n\nHis career’s next move to Renault’s works team in 2019 brought fresh challenges for the \nPerth pilot, but failed to deliver his dream of following Jack Brabham and Alan \nJones as the next world champion from Down Under and he moved on to McLaren for 2021.\n\nThere he has found a tough young team mate in Lando Norris, but has nevertheless \nreturned to winning ways. Whatever happens next, Ricciardo is sure to keep on smiling.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)

def creermalyounfenetre32():
    global fenetre3
    
    fenetred9= Toplevel(fenetre3) 
    fenetred9.title("Fernando Alonso")
    fenetred9.minsize(300,300)
    driveridd='alonso'
    driver(fenetred9,driveridd).afficher1()
    ttk.Label(fenetred9,image=d91).place(x=650,y=25)
    link.set('https://www.instagram.com/fernandoalo_oficial/')
    ttk.Label(fenetred9,text='Alpine',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred9,text='2',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred9,text="Michael Schumacher was the undisputed king of Formula 1 in the early 2000s, \npicking up wins and championships at a rate that was simply unheard of at the time. \nIt was going to take someone very special to topple the Ferrari legend from his \nthrone – and that it was Fernando Alonso who did it, tells you all you need to know \nabout the Spaniard.\n\nFiercely competitive, Alonso is not shy about his talent, rating himself as 9/10 \n“in everything”, and few in the know would disagree, with his performances in F1 \ncharacterised by blistering speed, brilliant tactical thinking, exemplary race craft,\na razor-sharp eye for detail and a relentless determination to win.\n\nA serial record breaker in his early days, he was – at one time – F1’s youngest\n polesitter, race winner, world champion and double world champion as he gobbled \nup success with the Renault team. Even Alonso couldn’t continue that amazing \nrun in his later career though, failing to add another title to his collection despite \nspells at McLaren and Ferrari.\n\nBut after two years away from Formula 1 racing – and with two Le Mans wins in his pocket\n – Alonso returned with Alpine in 2021. And he has unfinished business with F1…\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
def creermalyounfenetre33():
    global fenetre3
    
    fenetred10 = Toplevel(fenetre3) 
    fenetred10.title("Esteban Ocon")
    fenetred10.minsize(300,300)
    driveridd='ocon'
    driver(fenetred10,driveridd).afficher1()
    ttk.Label(fenetred10,image=d101).place(x=650,y=25)
    link.set('https://www.instagram.com/estebanocon/')
    ttk.Label(fenetred10,text='Alpine',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred10,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred10,text="If there’s one word that dominates Esteban Ocon’s career, it’s ‘sacrifice’.\n\nBack when he was just a promising karter, Ocon’s parents sold their house,\n put their jobs on hold, and began a life on the road, living in a caravan and travelling \nfrom circuit to circuit to support their son’s burgeoning career.\n\nSacrifice, see – but it worked. 2014 saw Ocon break through in the world of single-seaters,\n as he beat a certain Max Verstappen to the European F3 title. Backed by Mercedes,\n he won the GP3 title the following year and was halfway through a season of DTM\n in 2016 when he was offered the chance to replace Rio Haryanto at the minnow \nManor team from the Belgian Grand Prix onwards.\n\nThat opportunity led to a full-time seat the following year with Force India, \nwhere his wheel-to-wheel duels with highly-rated team mate Sergio Perez quickly \nmarked him out as a rising star. But when Lawrence Stroll, father of racer \nLance, stepped in midway through 2018 to secure the squad’s financial future, the \nwriting was on the wall for Ocon, who was moved aside at the end of the year to \nallow Stroll Jnr to join from Williams.\n\nOcon bided his time, though, and after a year on the sidelines as Mercedes’ reserve \ndriver, he found his way back into a race seat for 2020 with Renault, who became \nAlpine for 2021 – when his wait finally paid off, as he scored his – and the famous \nFrench marque’s – first F1 win.\n\nNothing in Ocon’s motorsport career has come easy – but if Ocon has managed to \nreturn to the F1 grid and step atop the podium, it’s through a combination of self-belief,\n determination and a talent that’s up there with the very best.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)

def creermalyounfenetre34():
    global fenetre3
    
    fenetred11 = Toplevel(fenetre3) 
    fenetred11.title("Pierre Gasly")
    fenetred11.minsize(300,300)
    driveridd='gasly'
    driver(fenetred11,driveridd).afficher1()
    ttk.Label(fenetred11,image=d1111).place(x=650,y=25)
    link.set('https://www.instagram.com/pierregasly/')
    ttk.Label(fenetred11,text='AlphaTauri',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred11,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred11,text="If there’s one man who knows how big a rollercoaster ride an F1 driver’s career can \nbe, it’s Pierre Gasly!\n\nThe flying Frenchman was called up to make his 2017 debut in Malaysia in place\n of Daniil Kvyat and, after proving his mettle, he was named a Toro Rosso driver\n the following year.  A further 21 races into his fledgling career, Gasly was moved up\n again – this time to replace Red Bull big gun Daniel Ricciardo.\n\nGasly seemed to have a knack of being in the right place at the right time – a quality\n that’s equally handy on track. A series of impressive 2018 performances for\n Toro Rosso – including a brilliant fourth place in Bahrain – showed exciting \npromise for what he might do with the ‘A’ team in 2019.\n\nUnfortunately that promise only appeared in flashes – and he quickly suffered \nfrom unfavourable comparisons with superstar team mate Max Verstappen.\nSo much so that after the summer break, he was sent back to Toro Rosso, with \nanother young up-and-comer – Alex Albon – being given a shot in the ‘senior’ Red Bull seat.\nBut Gasly bounced back, as only Gasly can. In the season’s remaining nine races \nhe scored almost as many points as team mate Kvyat managed over the \nentire year – and secured his best-ever race result with P2 in Brazil. That trajectory \ncontinued in 2020, peaking with an emotional maiden win at the renamed AlphaTauri\n team’s home race in Italy, and didn’t let up in 2021 when he was back on the \npodium and scored 110 of the squad’s 142 points.\nThe question now is can he maintain momentum and earn himself another shot\n at the F1 bigtime…\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    


def creermalyounfenetre35():
    global fenetre3
    
    fenetred12= Toplevel(fenetre3) 
    fenetred12.title("Yuki Tsunoda")
    fenetred12.minsize(300,300)
    driveridd='tsunoda'
    driver(fenetred12,driveridd).afficher1()
    ttk.Label(fenetred12,image=d121).place(x=650,y=25)
    link.set('https://www.instagram.com/yukitsunoda0511/')
    ttk.Label(fenetred12,text='AlphaTauri',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred12,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred12,text="In the entire history of Formula 1, no Japanese driver has ever won a World \nChampionship Grand Prix. Could Yuki Tsunoda be the first? Red Bull certainly think \nso, with the youngster very much on the path to their senior team if he continues to \nimpress as he has done over the past few years.\nTsunoda's ascent to the top tier of motorsport was astonishingly rapid: he went from \nracing in Japanese F4 to a Formula 1 seat with AlphaTauri in just over three years,\n having arrived in Europe in 2019 with no knowledge of the circuits.\n\nBut after a slow start in F3, followed by a hugely impressive debut F2 campaign that\n saw him finish third in the championship and pick up three wins along the way, Tsunoda\n proved he had the speed and the race craft to force his way on to the F1 grid.\n\nHe may not have adapted to Grand Prix racing quite as quickly as he did to F2, \nbut given time he could yet find himself battling at the very sharp end in a Red Bull.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    


def creermalyounfenetre36():
    global fenetre3
    
    fenetred13 = Toplevel(fenetre3) 
    fenetred13.title("Sebastian Vettel")
    fenetred13.minsize(300,300)
    driveridd='vettel'
    driver(fenetred13,driveridd).afficher1()
    ttk.Label(fenetred13,image=d131).place(x=650,y=25)
    link.set('https://www.instagram.com/vettelofficial/')
    ttk.Label(fenetred13,text='Aston Martin',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred13,text='4',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred13,text="Born and raised a Bull, then a Prancing Horse, and now the face of Aston Martin’s \nFormula 1 revival, F1's poster boy of early achievement had won more than all but \ntwo drivers in history by the time he was just 26, including back-to-back world titles \nbetween 2010 and 2013.\nVettel’s trademark is pure pace – and of course his one-finger victory salute. In the \nchase to the chequered flag, he likes to lead from the front and just like his hero,\nMichael Schumacher. But for all his competitive streak, Vettel has a playful side too\n and has been known to let loose with a spot of Beatles karaoke - and baby can he \ndrive a car.\nAlongside his four world crowns he can boast more than 50 pole positions and \nrace victories, ranking him – statistically - above many of the biggest names in F1 \nhistory. No wonder then that he has twice been hand-picked to return some of Grand\n Prix oldest names to glory.Following his move to Maranello, that mission didn’t \nexactly go to plan as Vettel’s \nrivalry with Lewis Hamilton intensified. Then came an additional thorn in his\nside – young-gun Ferrari team mate Charles Leclerc, the first man to outscore him\n over a season at the Scuderia.\n\nHis latest challenge is as Aston Martin’s team leader. He has already put them\n on the podium, but Vettel will need to call on all his speed and experience if he’s\nto regularly reassert himself over his rivals – and re-establish his reputation as one\nof the sport’s all-time greats.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)


def creermalyounfenetre37():
    global fenetre3
    
    fenetred14 = Toplevel(fenetre3) 
    fenetred14.title("Lance Stroll")
    fenetred14.minsize(300,300)
    driveridd='stroll'
    driver(fenetred14,driveridd).afficher1()
    ttk.Label(fenetred14,image=d141).place(x=650,y=25)
    link.set('https://www.instagram.com/lance_stroll/')
    ttk.Label(fenetred14,text='Aston Martin',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred14,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred14,text="There is no such thing as too much too soon for Stroll, a teenage sensation with a \nwet weather predilection. One of the cool kids on the grid, Stroll was unveiled \nshortly after his 18th birthday by Williams – before he finished high school and got \nhis road licence. \n\nStroll meant business in his debut 2017 season, setting records on the way. \nAn opportunistic racer he bounded onto the podium in Baku, the youngest rookie \nto do so. As the son of a wealthy entrepreneur, Stroll is used to a champagne lifestyle\n but now he knows the fizz tastes all the sweeter on the rostrum. Then in Monza\n he mastered the downpours to become the youngest driver in history to line up on the\n front row.\n\nA single-minded starter, the Canadian loves to make up places on the opening lap \nand fight through to the points. Stroll has the potential to be a long-term fixture in \nFormula 1 – as amply illustrated by a maiden pole and another two podiums in 2020.\n\nThose came after his father Lawrence led the consortium that took over Force India \nmidway through the 2018 season, and then transformed it from Racing Point to \nAston Martin for 2021. The future looks bright for both the team and their young \ndriver – and even if it rains then Stroll can keep on motoring at the sharp end of the pack.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)


def creermalyounfenetre38():
    global fenetre3
    
    fenetred15 = Toplevel(fenetre3) 
    fenetred15.title("Nicholas Latifi")
    fenetred15.minsize(300,300)
    driveridd='latifi'
    driver(fenetred15,driveridd).afficher1()
    ttk.Label(fenetred15,image=d151).place(x=650,y=25)
    link.set('https://www.instagram.com/nicholaslatifi/')
    ttk.Label(fenetred15,text='Williams',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred15,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred15,text="Thirteen is an advanced age to begin your karting career these days. But that’s how \nold Toronto native Nicholas Latifi was when he took his first steps in motorsport. \nJust 11 years later, he became a fully-fledged Formula 1 driver.\n\nThat ascension into racing's top category was largely thanks to his most impressive \nseason to date in Formula 2 in 2019, with Latifi – who’d finished a disappointing \nninth in the series’ 2018 standings – pulling up his bootstraps to claim second in the \nchampionship. That result, combined with the Williams/Robert Kubica union failing\n to mesh in 2019, meant Williams made the call to promote their affable Canadian\n reserve driver to a full-time drive alongside George Russell for 2020.\n\nLatifi’s first taste of F1 machinery actually came all the way back in 2017, when he\n was given a test by Renault. Further duties with Force India followed in 2018 before\n he joined the Williams family in 2019. It was an annus horribilis for the squad,\nno doubt – but Latifi’s straightforward, friendly attitude and insightful feedback \nhelped swing the vote in his favour for 2020.\n\nNow, after two seasons living in Russell’s shadow – and with Williams' form on the \nrise and a new team mate in the shape of ex-Red Bull racer Alex Albon – the goal \nis to show that that his eye-catching F2 year wasn’t just a fluke, and finally prove that \nhe really has got what it takes to mix it with the best drivers in the world.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    


def creermalyounfenetre39():
    global fenetre3
    
    fenetred16 = Toplevel(fenetre3) 
    fenetred16.title("Alex Albon")
    fenetred16.minsize(300,300)
    driveridd='albon'
    driver(fenetred16,driveridd).afficher1()
    ttk.Label(fenetred16,image=d161).place(x=650,y=25)
    link.set('https://www.instagram.com/alex_albon/')
    ttk.Label(fenetred16,text='Williams',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred16,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred16,text="Born in London but racing under the flag of Thailand, Alexander Albon’s first word was in \nfact Italian. That word was Ferrari – though it was with another Italian team that he got \nhis big F1 break.\nIdolising Michael Schumacher and dreaming of one day racing in Formula 1, the junior\n Albon was pipped to the 2016 GP3 title by a certain Charles Leclerc. He then left \nhis great friendship with George Russell trackside as he took the 2018 Formula 2 title \nfight down to the wire.\n\nGraduating to the F1 big league along with yet another contemporary – Lando Norris – in\n 2019, Albon did his talking on track with Toro Rosso in the opening races, earning a \nmid-season promotion to Red Bull Racing.\n\nA stylish over-taker with a championship mentality, Albon was unfazed by partnering \nMax Verstappen for the second half of his rookie season, taking top-six finishes in \neight of his nine 2019 races with Red Bull.\n\nStaying in touch with the future champion proved tougher in 2020 and Red Bull \ndropped him from their race line-up. Crucially, though, Albon was retained as test and \nreserve driver, keeping him very much on team bosses’ radar, leading to his 2022 return\n to the grid with Williams.\n\nLaidback and cheerful with a cheeky grin, the Thai racer is popular among his peers – not \nalways easy in motorsport’s cauldron of competition – but you don’t succeed in \nFormula 1 by being popular. Albon’s challenge now is a big one – to make the most of a \nrare second F1 opportunity.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)

def creermalyounfenetre40():
    global fenetre3
    
    fenetred17 = Toplevel(fenetre3) 
    fenetred17.title("Valterri Bottas")
    fenetred17.minsize(300,300)
    driveridd='bottas'
    driver(fenetred17,driveridd).afficher1()
    ttk.Label(fenetred17,image=d171).place(x=650,y=25)
    link.set('https://www.instagram.com/valtteribottas/')
    ttk.Label(fenetred17,text='Alfa Romeo',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred17,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred17,text="Learning his craft on Finnish roads of ice and snow, he was born to be a Grand Prix racer.\n\nBottas explains that if you can drive on the frozen roads of his homeland then you can \ndrive anywhere. Then there’s the Finnish mentality –reserved, diligent and calm the fast \nlane of F1 doesn’t faze him.\n\nMaking his F1 debut with Williams in 2013, Bottas soon became part of the family. \nPoints and podiums followed with the reliable racer even amassing the most points \nwithout a win, a record he resented but that showcased his ability. The fact the Finn \nwas such a points machine saw him suddenly promoted to the most coveted seat in \nF1 - Nico Rosberg’s vacant championship-winning seat at Mercedes.\n\nBottas blossomed at the Silver Arrows in 2017, unleashing his pace to clock up personal \npole positions and victories as well as a team championship for the famous \nMercedes marque alongside Lewis Hamilton. He even tied with Hamilton and Sebastian \nVettel with 13 podiums.\n\nFor a shy guy, it brought a confidence boost and a new swagger – albeit in a very \ndemur Finnish fashion. He would need all that confidence in 2018 – a season Bottas \ndescribed as his worst in F1, as he took zero wins to Hamilton’s 11. That, though, was \na reflection more of his team mate’s brilliance than of any shortcomings on his own part.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    


def creermalyounfenetre41():
    global fenetre3
    
    fenetred18= Toplevel(fenetre3) 
    fenetred18.title("Gyuan Zhou")
    fenetred18.minsize(300,300)
    driveridd='zhou'
    driver(fenetred18,driveridd).afficher1()
    ttk.Label(fenetred18,image=d181).place(x=650,y=25)
    link.set('https://www.instagram.com/zhouguanyu24/')
    ttk.Label(fenetred18,text='Alfa Romeo',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred18,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred18,text="China has never boasted a Grand Prix starter among its citizens – but Zhou Guanyu is the\n driver charged with changing that state of affairs, after receiving the call-up to \nmake his F1 debut for Alfa Romeo in 2022. \nThe Shanghai-born racer attended his home city’s inaugural Grand Prix in 2004 at the\n age of five, cheering on his hero Fernando Alonso. But having caught the racing \nbug, the Chinese driver then set himself the ambitious goal of becoming his country’s \nfirst-ever F1 racer – achieving a feat that Ma Qinghua, the only other Chinese driver to \ntake part in a Formula 1 weekend, never managed. \n\nShowing boldness and dedication, Zhou put his plan into action by moving to England with\n his family aged just 12 to pursue his motorsport ambitions. A second-place finish in \nthe 2015 Italian F4 championship proved Zhou was possessed of the right stuff – a \nfact already noted by Ferrari, who’d signed him to their driver academy a year earlier. \n\nA move to Renault’s academy for 2019 coincided with his debut in Formula 2, with \nZhou building his confidence in the series via multiple wins and pole positions across \nthree seasons, leading to him challenging for the drivers’ title in 2021. \n\nThat was enough to convince Alfa Romeo Team Principal Fred Vasseur to put his faith\nin Zhou for 2022 and field him alongside ex-Mercedes racer Valtteri Bottas – allowing\nZhou to achieve his dream of racing in F1, and even to see how he fares against his own \nchildhood hero, Fernando Alonso.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
drivers1=PhotoImage(file='drivers bg.png')

def creermalyounfenetre42():
    global fenetre3
    
    fenetred19 = Toplevel(fenetre3) 
    fenetred19.title("Kevin Magnunssen")
    fenetred19.minsize(300,300)
    driveridd='kevin_magnussen'
    driver(fenetred19,driveridd).afficher1()
    ttk.Label(fenetred19,image=d191).place(x=650,y=25)
    link.set('https://www.instagram.com/kevinmagnussen/')
    ttk.Label(fenetred19,text='Haas',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred19,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred19,text="Call him a lone ranger or a maverick, but Magnussen is back in Formula 1 for one \nreason only – to race.\n\nHe may be a second-generation F1 driver – following his father, Jan, onto the \ngrid – but Magnussen’s idols are from the ‘golden era’ of Grand Prix racing when \nthe likes of Juan Manuel Fangio and Stirling Moss risked it all for the love of the sport.\n\nThe Roskilde racer’s own prowess was proven on debut for McLaren, who guided\nhim through the junior ranks, when he cruised into the top-three at the 2014 \nAustralian Grand Prix, becoming the first Dane to claim a podium in F1.\n\nOther champagne moments have been more difficult to find, as he left McLaren\nbehind for a season with Renault, before settling in for four among kindred \nspirits at Haas. And now he’s back with the US team – after a year away in the \nStates, racing Indy and sportscars among other things.\n\nHis meaty manoeuvres and elbows-out approach have earned him a bad-boy \nreputation on track, something that still leaves him baffled. Out of the car \nMagnussen is laidback and affable. After all he has his dream job – and he is only \nhere to race.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    


def creermalyounfenetre43():
    global fenetre3
    
    fenetred20 = Toplevel(fenetre3) 
    fenetred20.title("Mick Schumacher")
    fenetred20.minsize(300,300)
    driveridd='mick_schumacher'
    driver(fenetred20,driveridd).afficher1()
    ttk.Label(fenetred20,image=d201).place(x=650,y=25)
    link.set('https://www.instagram.com/mickschumacher/')
    ttk.Label(fenetred20,text='Haas',style='S356pecial.TLabel',foreground='black').grid(row=6,column=1)
    ttk.Label(fenetred20,text='0',style='S356pecial.TLabel',foreground='black').grid(row=7,column=1)
    ttk.Label(fenetred20,text="Plenty of sons of former F1 drivers have joined the sport over the years – two have even\nemulated their fathers to become world champions – but carrying the Schumacher \nname is surely an extra level of pressure for Mick, given his father Michael’s \nextraordinary achievements in Formula 1.\n\nBut Schumacher Junior, a member of the Ferrari Driver Academy, arrived in F1 in 2021\n with Haas after clinching the previous season’s F2 title in 2020, to add to the F3 \nchampionship he won in 2018 – so there was zero suggestion he had been elevated to \nthe top level of motorsport because of his name.\n\nIt’s talent that brought him this far and he showed more of the same as he acclimatized\n to F1 in a tough rookie season, consistently outclassing his team mate in their \nuncompetitive machinery.\n\nNow Schumacher must continue to impress if he is to one day follow in his father’s \nfootsteps and claim a race seat with the Scuderia.\n\n",style='S356pecial.TLabel',foreground='black').grid(row=10,column=1)
    
teamc=StringVar()
techc=StringVar()
wc=StringVar()
base=StringVar()
chassis=StringVar()
pu=StringVar()

        
        

def creermalyounfenetre44():
    global fenetre4
    
    fenetres41= Toplevel(fenetre4) 
    fenetres41.title("Mercedes")
    fenetres41.minsize(300,300)
    constructoridd='mercedes'
    ttk.Label(fenetres41,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres41,text="Lewis Hamilton & Georges Russel",style='S1pecial.TLabel').grid(row=2,column=1)
    teamc='Toto Wolf'
    techc='Mike Elliot'
    wc='8'
    base='Brackley'
    chassis='W13'
    pu='Mercedes'
    constructors(fenetres41,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()

    
def creermalyounfenetre45():
    global fenetre4
    teamc='Frederic Vasseur'
    techc='Jan Monchaux'
    wc='0'
    base='Hinwil'
    chassis='C42'
    pu='Ferrari'
    fenetres42 = Toplevel(fenetre4) 
    fenetres42.title("AlfaRomeo")
    fenetres42.minsize(300,300)
    constructoridd='alfa'
    constructors(fenetres42,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres42,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres42,text="Valterri Bottas /Gyuan Zhou",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre46():
    global fenetre4
    teamc='Franz Tost'
    techc='Jody Egginton'
    wc='0'
    base='Faenza'
    chassis='ATO3'
    pu='Red Bull Powertrains'
    fenetres43 = Toplevel(fenetre4) 
    fenetres43.title("AlphaTauri")
    fenetres43.minsize(300,300)
    constructoridd='alphatauri'
    constructors(fenetres43,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres43,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres43,text="Pierre Gasly & Yuki Tsunoda",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
    
def creermalyounfenetre47():
    global fenetre4
    teamc='Otmar Szafnaurer'
    techc='Pat Fry'
    wc='2'
    base='Enstone'
    chassis='A522'
    pu='Renault'
    fenetres44 = Toplevel(fenetre4) 
    fenetres44.title("Alpine")
    fenetres44.minsize(300,300)
    constructoridd='alpine'
    constructors(fenetres44,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres44,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres44,text="Fernando Alonso & Esteban Oconl",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre48():
    global fenetre4
    teamc='Christian Horner'
    techc='Pierre Wache'
    wc='4'
    base='Milton Keynes'
    chassis='RB18'
    pu='Red Bull Powertrains'
    fenetres45 = Toplevel(fenetre4) 
    fenetres45.title("RedBull")
    fenetres45.minsize(300,300)
    constructoridd='red_bull'
    constructors(fenetres45,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres45,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres45,text="Max Verstappen & Sergio Perez",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre49():
    global fenetre4
    teamc='Mike Krack'
    techc='Andrew Green'
    wc='0'
    base='Silverstone'
    chassis='AMR22'
    pu='Mercedes'
    fenetres46 = Toplevel(fenetre4) 
    fenetres46.title("Aston Martin")
    fenetres46.minsize(300,300)
    constructoridd='aston_martin'
    constructors(fenetres46,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres46,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres46,text="Sebastian Vettel & Lance Strolll",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
    
def creermalyounfenetre50():
    global fenetre4
    teamc='Jost Capito'
    techc='FRancois-Xavier Demaison'
    wc='9'
    base='Grove'
    chassis='FW44'
    pu='Mercedes'
    fenetres47 = Toplevel(fenetre4) 
    fenetres47.title("Williams")
    fenetres47.minsize(300,300)
    constructoridd='williams'
    constructors(fenetres47,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres47,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres47,text="Alex Albon & Nicolas Latifi",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre51():
    global fenetre4
    teamc='Mattia Binotto'
    techc='Enrico Cardile'
    wc='16'
    base='Maranello'
    chassis='F1-75'
    pu='Ferrari'
    fenetres49= Toplevel(fenetre4) 
    fenetres49.title("Ferrari")
    fenetres49.minsize(300,300)
    constructoridd='ferrari'
    constructors(fenetres49,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres49,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres49,text="Charles Leclerc & Carlos Sainz",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre52():
    global fenetre4
    teamc='Andreas Seidl'
    techc='James Key'
    wc='8'
    base='Woking'
    chassis='MCL36'
    pu='Mercedes'
    fenetres410 = Toplevel(fenetre4) 
    fenetres410.title("Mclaren")
    fenetres410.minsize(300,300)
    
    constructoridd='mclaren'
    constructors(fenetres410,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres410,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres410,text="Lando Norris & Daniel Ricciardo",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre53():
    global fenetre4
    teamc='Guenther Steiner'
    techc='Simone Resta'
    wc='0'
    base='Kannapolis'
    chassis='VF-22'
    pu='Ferrari'
    fenetres411= Toplevel(fenetre4) 
    fenetres411.title("Haas")
    fenetres411.minsize(300,300)
    fenetres411.configure(bg='light grey')
    constructoridd='haas'
    constructors(fenetres411,constructoridd,teamc,techc,wc,base,chassis,pu).afficher()
    ttk.Label(fenetres411,text="Drivers",style='S1pecial.TLabel',foreground='red').grid(row=2,column=0)
    ttk.Label(fenetres411,text="Mick Schumacher & Kevin Magnussen",style='S1pecial.TLabel').grid(row=2,column=1)
    
    
def creermalyounfenetre54():
    global fenetre8
    s5=ttk.Style()
    s5.configure('S5pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black',background='white')
    s55=ttk.Style()
    s55.configure('S55pecial.TLabel', font=('Formula1 Display Bold', 12, 'bold','underline'), foreground='red',background='white')
    
    fenetrest1= Toplevel(fenetre8) 
    fenetrest1.title(" All Time Constructors Champions")
   
    fenetrest1.minsize(900,600)
    mf=ttk.Frame(fenetrest1)
    mf.pack(fill=BOTH,expand=1)
    myc=Canvas(mf)
    myc.pack(side=LEFT, fill=BOTH , expand=1)
    mscb=ttk.Scrollbar(mf,orient=VERTICAL,command=myc.yview)
    mscb.pack(side=RIGHT,fill=Y)
    myc.configure(yscrollcommand=mscb.set)
    myc.bind('<Configure>',lambda e: myc.configure(scrollregion=myc.bbox('all')))
    sf=Frame(myc)
    sf.configure(background='white')
    myc.create_window((0,0),window=sf,anchor='nw')
    response=requests.get("http://ergast.com/api/f1/constructorStandings/1.json?limit=80&offset=0")
    data=response.json()
    dic=data['MRData']['Table']['StandingsLists']
    
    ttk.Label(sf,text='Season',style='S55pecial.TLabel',foreground='red').grid(row=0,column=0,padx=50)
    ttk.Label(sf,text='Points',style='S55pecial.TLabel',foreground='red').grid(row=0,column=3)
    ttk.Label(sf,text='Wins',style='S55pecial.TLabel',foreground='red').grid(row=0,column=4,padx=50)
    ttk.Label(sf,text='Nationality',style='S55pecial.TLabel',foreground='red').grid(row=0,column=6,padx=50)
    ttk.Label(sf,text='Constructor',style='S55pecial.TLabel',foreground='red').grid(row=0,column=1,padx=50)
    m=2
    for i in dic:
        ttk.Label(sf,text=i['season'],style='S5pecial.TLabel').grid(row=m,column=0,padx=50)
        ttk.Label(sf,text=i['ConstructorStandings'][0]['points'] ,style='S5pecial.TLabel').grid(row=m,column=3,padx=50)
        ttk.Label(sf,text=i['ConstructorStandings'][0]['wins'],style='S5pecial.TLabel').grid(row=m,column=4,padx=50)
        ttk.Label(sf,text=i['ConstructorStandings'][0]['Constructor']['nationality'],style='S5pecial.TLabel').grid(row=m,column=6,padx=50)
        ttk.Label(sf,text=i['ConstructorStandings'][0]['Constructor']['name'] ,style='S5pecial.TLabel').grid(row=m,column=1,padx=50)
        m=m+1
        
        

        
    
    
    
def creermalyounfenetre55():
    global fenetre8
    s5=ttk.Style()
    s5.configure('S5pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black',background='white')
    s55=ttk.Style()
    s55.configure('S55pecial.TLabel', font=('Formula1 Display Bold', 12, 'bold','underline'), foreground='red',background='white')
    fenetrest2 = Toplevel(fenetre8)
    fenetrest2.configure(bg='white')
    fenetrest2.title("All Time Drivers World Champions")
    fenetrest2.minsize(1220,600)
    mf=ttk.Frame(fenetrest2)
    mf.pack(fill=BOTH,expand=1)
    myc=Canvas(mf)
    myc.pack(side=LEFT, fill=BOTH , expand=1)
    mscb=ttk.Scrollbar(mf,orient=VERTICAL,command=myc.yview)
    mscb.pack(side=RIGHT,fill=Y)
    myc.configure(yscrollcommand=mscb.set)
    myc.bind('<Configure>',lambda e: myc.configure(scrollregion=myc.bbox('all')))
    sf=Frame(myc)
    sf.configure(background='white')
    myc.create_window((0,0),window=sf,anchor='nw')
    response=requests.get("http://ergast.com/api/f1/driverStandings/1.json?limit=80&offset=0")
    data=response.json()
    dic=data['MRData']['StandingsTable']['StandingsLists']
    m=2
    ttk.Label(sf,text='Season',style='S55pecial.TLabel',foreground='red').grid(row=0,column=0,padx=30)
    ttk.Label(sf,text='Points',style='S55pecial.TLabel',foreground='red').grid(row=0,column=3,padx=30)
    ttk.Label(sf,text='Wins',style='S55pecial.TLabel',foreground='red').grid(row=0,column=4,padx=30)
    ttk.Label(sf,text='Name',style='S55pecial.TLabel',foreground='red').grid(row=0,column=1,padx=30)
    ttk.Label(sf,text='Family Name',style='S55pecial.TLabel',foreground='red').grid(row=0,column=2,padx=30)
    ttk.Label(sf,text='Date of birth',style='S55pecial.TLabel',foreground='red').grid(row=0,column=5,padx=30)
    ttk.Label(sf,text='Nationality',style='S55pecial.TLabel',foreground='red').grid(row=0,column=6,padx=30)
    ttk.Label(sf,text='Constructors',style='S55pecial.TLabel',foreground='red').grid(row=0,column=7,padx=30)
    
    for i in dic:
        ttk.Label(sf,text=i['season'],style='S5pecial.TLabel').grid(row=m,column=0,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['points'],style='S5pecial.TLabel').grid(row=m,column=3,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['wins'],style='S5pecial.TLabel').grid(row=m,column=4,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['Driver']['givenName'],style='S5pecial.TLabel').grid(row=m,column=1,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['Driver']['familyName'],style='S5pecial.TLabel').grid(row=m,column=2,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['Driver']['dateOfBirth'],style='S5pecial.TLabel').grid(row=m,column=5,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['Driver']['nationality'],style='S5pecial.TLabel').grid(row=m,column=6,padx=30)
        ttk.Label(sf,text=i['DriverStandings'][0]['Constructors'][0]['name'],style='S5pecial.TLabel').grid(row=m,column=7,padx=30)
        m=m+1
            


                
def creermalyounfenetre56():
    global fenetre6
    
    fenetres54 = Toplevel(fenetre6) 
    fenetres54.title("Gulf Air Bahrain GP schedule")
    fenetres54.minsize(300,300)
    yearround=1
    schedule(fenetres54,yearround).afficherS()
    

def creermalyounfenetre57():
    global fenetre6
    
    fenetres55 = Toplevel(fenetre6) 
    fenetres55.title("STC Saudi Arabian GP schedule")
    fenetres55.minsize(300,300)
    yearround=2
    schedule(fenetres55,yearround).afficherS()


def creermalyounfenetre58():
    global fenetre6
    
    fenetres56 = Toplevel(fenetre6) 
    fenetres56.title("Heinken Australian GP schedule")
    fenetres56.minsize(300,300)
    yearround=3
    schedule(fenetres56,yearround).afficherS()
def creermalyounfenetre59():
    global fenetre6
    
    fenetres57 = Toplevel(fenetre6) 
    fenetres57.title("Rolex Gran Premio del Made in Italy e Dell'Emilia Romagna schedule")
    fenetres57.minsize(300,300)
    yearround=4
    schedule(fenetres57,yearround).afficherS()

def creermalyounfenetre60():
    global fenetre6
    
    fenetres58= Toplevel(fenetre6) 
    fenetres58.title("Crypto.com Miami GP schedule")
    fenetres58.minsize(300,300)
    yearround=5
    schedule(fenetres58,yearround).afficherS()


def creermalyounfenetre61():
    global fenetre6
    
    fenetres59 = Toplevel(fenetre6) 
    fenetres59.title("Pirelli Gran Premio de Espana schedule")
    fenetres59.minsize(300,300)
    yearround=6
    schedule(fenetres59,yearround).afficherS()


def creermalyounfenetre62():
    global fenetre6
    
    fenetres60 = Toplevel(fenetre6) 
    fenetres60.title("Grand Prix de Monaco schedule")
    fenetres60.minsize(300,300)
    yearround=7
    schedule(fenetres60,yearround).afficherS()


def creermalyounfenetre63():
    global fenetre6
    
    fenetres61 = Toplevel(fenetre6) 
    fenetres61.title("Azerbaijan GP schedule")
    fenetres61.minsize(300,300)
    yearround=8
    schedule(fenetres61,yearround).afficherS()


def creermalyounfenetre64():
    global fenetre6
    
    fenetres62= Toplevel(fenetre6) 
    fenetres62.title("Grand Prix du Canada schedule")
    fenetres62.minsize(300,300)
    yearround=9
    schedule(fenetres62,yearround).afficherS()   

def creermalyounfenetre65():
    global fenetre6
    
    fenetres63 = Toplevel(fenetre6) 
    fenetres63.title("Lenovo British GP schedule")
    fenetres63.minsize(300,300)
    yearround=10
    schedule(fenetres63,yearround).afficherS()    

def creermalyounfenetre66():
    global fenetre6
    
    fenetres64 = Toplevel(fenetre6) 
    fenetres64.title("Grosser Preis Von Osterrich schedule")
    fenetres64.minsize(300,300)
    yearround=11
    schedule(fenetres64,yearround).afficherS()
def creermalyounfenetre67():
    global fenetre6
    
    fenetres65 = Toplevel(fenetre6) 
    fenetres65.title("Lenovo Grand Prix de France schedule")
    fenetres65.minsize(300,300)
    yearround=12
    schedule(fenetres65,yearround).afficherS()

def creermalyounfenetre68():
    global fenetre6
    
    fenetres66 = Toplevel(fenetre6) 
    fenetres66.title("Aramco Magyar Nagydij schedule")
    fenetres66.minsize(300,300)
    yearround=13
    schedule(fenetres66,yearround).afficherS()

def creermalyounfenetre69():
    global fenetre6
    
    fenetres67 = Toplevel(fenetre6) 
    fenetres67.title("Rolex Belgian GP schedule")
    fenetres67.minsize(300,300)
    yearround=14
    schedule(fenetres67,yearround).afficherS()    

def creermalyounfenetre70():
    global fenetre6
    fenetres68 = Toplevel(fenetre6) 
    fenetres68.title("Heineken Dutch GP schedule")
    fenetres68.minsize(300,300)
    yearround=15
    schedule(fenetres68,yearround).afficherS() 
def creermalyounfenetre71():
    global fenetre6
    fenetres69 = Toplevel(fenetre6) 
    fenetres69.title("Pirelli Gran Premio d'Italia schedule")
    fenetres69.minsize(300,300)
    yearround=16
    schedule(fenetres69,yearround).afficherS() 
def creermalyounfenetre72():
    global fenetre6
    fenetres70 = Toplevel(fenetre6) 
    fenetres70.title("Russian GP schedule")
    fenetres70.minsize(300,300)
    s35=ttk.Style()
    s35.configure('S35pecial.TLabel', font=('Formula1 Display Bold', 16, 'bold'), foreground='red')
    ttk.Label(fenetres70,text="Due To Political Reasons \nthis round is cancelled.",style='S35pecial.TLabel').grid(row=0,column=0)  
def creermalyounfenetre73():
    global fenetre6
    fenetres71 = Toplevel(fenetre6) 
    fenetres71.title("Singapore GP schedule")
    fenetres71.minsize(300,300)
    yearround=17
    schedule(fenetres71,yearround).afficherS()
def creermalyounfenetre74():
    global fenetre6
    fenetres72 = Toplevel(fenetre6) 
    fenetres72.title("Japanese GP schedule")
    fenetres72.minsize(300,300)
    yearround=18
    schedule(fenetres72,yearround).afficherS() 
def creermalyounfenetre75():
    global fenetre6
    fenetres73 = Toplevel(fenetre6) 
    fenetres73.title("Aramco United States GP schedule")
    fenetres73.minsize(300,300)
    yearround=19
    schedule(fenetres73,yearround).afficherS() 
def creermalyounfenetre76():
    global fenetre6
    fenetres74 = Toplevel(fenetre) 
    fenetres74.title("Gran Premio de la Ciudad de Mexico schedule")
    fenetres74.minsize(300,300)
    yearround=20
    schedule(fenetres74,yearround).afficherS() 
def creermalyounfenetre77():
    global fenetre2
    
    fenetres75 = Toplevel(fenetre6) 
    fenetres75.title("Heineken Grande Prêmio de Sao Paulo schedule")
    fenetres75.minsize(300,300)
    yearround=21
    schedule(fenetres75,yearround).afficherS() 
def creermalyounfenetre78():
    global fenetre6
    fenetres76 = Toplevel(fenetre6) 
    fenetres76.title("Etihad Airways ABu Dhabi GP schedule")
    fenetres76.minsize(300,300)
    yearround=22
    schedule(fenetres76,yearround).afficherS() 

def creermalyounfenetre80():
    def respr():
        year=a.get()
        roundd=b.get()
        response=requests.get("http://ergast.com/api/f1/"+year+"/"+roundd+"/results.json")
        data=response.json()
        dic=data['MRData']
        dic1=dic['RaceTable']
        dic2=list(dic1.values())
        url=" http://ergast.com/api/f1/{{year}}/{{round}}/results"
        def hdar():
            webbrowser. open("https://www.youtube.com/results?search_query="+dic2[2][0]['raceName']+" "+dic2[2][0]['date']+"highlights")
        def review():
              webbrowser. open(dic2[2][0]['Circuit']['url'])
        s6=ttk.Style()
        s6.configure('S6pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='white',background='midnightblue')
        s61=ttk.Style()
        s61.configure('S61pecial.TLabel', font=('Formula1 Display Bold', 12, 'bold','underline'), foreground='white',background='midnightblue')
        ttk.Label(fenetres79, text='Round='+dic2[1],style='S6pecial.TLabel').grid(row=3, column=1)
        ttk.Label(fenetres79,text=dic2[2][0]['raceName'],style='S61pecial.TLabel',foreground='red').grid(row=0,column=2)
        ttk.Label(fenetres79,text=dic2[2][0]['date'],style='S6pecial.TLabel').grid(row=3,column=0)
        ttk.Label(fenetres79,text='Time='+dic2[2][0]['time']+' EEST',style='S6pecial.TLabel').grid(row=3,column=2)
        j=1
        ttk.Button(fenetres79,image=yt,command=hdar).grid(row=6,column=4) 
        ttk.Label(fenetres79,text='Circuit:',style='S6pecial.TLabel').grid(row=6,column=0)
        ttk.Button(fenetres79,image=wiki,command=review).grid(row=6,column=3)
        ttk.Label(fenetres79,text=dic2[2][0]['Circuit']['Location']['country']+','+dic2[2][0]['Circuit']['Location']['locality'],style='S6pecial.TLabel').grid(column=2,row=6)
        ttk.Label(fenetres79,text=dic2[2][0]['Circuit']['circuitName'],style='S6pecial.TLabel').grid(column=1,row=6)
        j=15
        ttk.Label(fenetres79, text='Position',style='S61pecial.TLabel',foreground='red').grid(row=12,column=0,pady=20)
        ttk.Label(fenetres79, text='Points',style='S61pecial.TLabel',foreground='red').grid(row=12,column=1)
        ttk.Label(fenetres79, text='Driver',style='S61pecial.TLabel',foreground='red').grid(row=12,column=2)
        ttk.Label(fenetres79, text='Constructor',style='S61pecial.TLabel',foreground='red').grid(row=12,column=3)
        ttk.Label(fenetres79, text='Status',style='S61pecial.TLabel',foreground='red').grid(row=12,column=4)
        m=0
        for i in dic2[2][0]['Results']:
            try:
                ttk.Label(fenetres79,text=i['position'],style='S6pecial.TLabel').grid(column=0,row=j)
                ttk.Label(fenetres79,text=i['points'],style='S6pecial.TLabel').grid(column=1,row=j)
                ttk.Label(fenetres79,text=i['Driver']['familyName'],style='S6pecial.TLabel').grid(column=2,row=j)
                ttk.Label(fenetres79,text=i['Constructor']['name'],style='S6pecial.TLabel').grid(column=3,row=j)
                ttk.Label(fenetres79,text=i['Time']['time'],style='S6pecial.TLabel').grid(column=4,row=j)
                j=j+1
                m=m+1
            except Exception:
                try:
                    ttk.Label(fenetres79,text=i['position'],style='S6pecial.TLabel').grid(column=0,row=j)
                    ttk.Label(fenetres79,text=i['points'],style='S6pecial.TLabel').grid(column=1,row=j)
                    ttk.Label(fenetres79,text=i['Driver']['familyName'],style='S6pecial.TLabel').grid(column=2,row=j)
                    ttk.Label(fenetres79,text=i['Constructor']['name'],style='S6pecial.TLabel').grid(column=3,row=j)
                    ttk.Label(fenetres79,text=i['status'],style='S6pecial.TLabel').grid(column=4,row=j)
                    j=j+1
                finally:
                    None
    global fenetre9
    fenetres79 = Toplevel(fenetre9)
    fenetres79.title("Previous Races Results")
    fenetres79.minsize(400,300)
    fenetres79.configure(bg='midnightblue')
    a=StringVar()
    b=StringVar()
    s6=ttk.Style()
    s6.configure('S6pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='white',background='midnightblue')
    ttk.Button(fenetres79,text = "Close",command = fenetres79.destroy).grid(row=1,column=10)
    ttk.Label(fenetres79,text="Enter The Season That Your are looking for : ",style='S6pecial.TLabel', foreground='white',background='midnightblue').grid(row=0,column=0,pady=10)
    ttk.Entry(fenetres79,textvariable=a).grid(row=0,column=1)
    ttk.Label(fenetres79,text="Enter The Round That Your are looking for : ",style='S6pecial.TLabel', foreground='white',background='midnightblue').grid(row=1,column=0,pady=10)
    ttk.Entry(fenetres79,textvariable=b).grid(row=1,column=1)
    ttk.Button(fenetres79,text='Search',command=respr).grid(row=0,column=10,padx=20)
    ttk.Label(fenetres79,text='\n\n',foreground='midnightblue',background='midnightblue').grid(row=60)
def creefenetre1():
    global fenetre1
    s7=ttk.Style()
    s7.configure('S7pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black')
    
    fenetre1 = Toplevel(fenetre) 
    fenetre1.title("ABOUT US")
    fenetre1.minsize(300,300)
    label = ttk.Label(fenetre1,text ="\nFormula One is the highest class of international racing for open-wheel single-seater formula racing cars sanctioned \nby the Fédération Internationale de l'Automobile.\nThis site was created by three big fans of Formula 1.\nYou can find here everything you need to know about this sport since its Inaugural season in 1950.\n\n\nFor more information or if there’s any issue, please contact our team:\nMelissa DIB EL OJAIMI : melissa.dibelojaimi@net.usj.edu.lb\nMassoud NOHRA : massoud.nohra@net.usj.edu.lb\nElie IBRAHIM : elie.ibrahim2@net.usj.edu.lb",style='S7pecial.TLabel',background='white')
    label.grid(padx=10)
    ttk.Label(fenetre1,image=esib).grid(pady=10)
    fenetre1.configure(bg='white')
img1=PhotoImage(file="bgcircuit.png")
def creefenetre2():
    global fenetre2
    
    fenetre2 = Toplevel(fenetre) 
    fenetre2.title("Circuits")
    ttk.Label(fenetre2,image=img1).place(x=0,y=0)
    ttk.Button(fenetre2,image=c1,command=creermalyounfenetre1).grid(column=0, row=0,padx=30,pady=1)
    ttk.Button(fenetre2,image=c2,command=creermalyounfenetre2).grid(column=1, row=0,padx=30)
    ttk.Button(fenetre2,image=c3,command=creermalyounfenetre3).grid(column=2, row=0,padx=30,pady=1)
    ttk.Button(fenetre2,image=c4,command=creermalyounfenetre4).grid(column=3, row=0,padx=30)
    ttk.Button(fenetre2,image=c5,command=creermalyounfenetre5).grid(column=4, row=0,padx=30,pady=1)
    ttk.Button(fenetre2,image=c6,command=creermalyounfenetre6).grid(column=5, row=0,padx=30)
    ttk.Button(fenetre2,image=c7,command=creermalyounfenetre7).grid(column=0, row=1,padx=30,pady=1)
    ttk.Button(fenetre2,image=c8,command=creermalyounfenetre8).grid(column=1, row=1,padx=30)
    ttk.Button(fenetre2,image=c9,command=creermalyounfenetre9).grid(column=2, row=1,padx=30,pady=1)
    ttk.Button(fenetre2,image=c10,command=creermalyounfenetre10).grid(column=3, row=1,padx=30)
    ttk.Button(fenetre2,image=c11,command=creermalyounfenetre11).grid(column=4, row=1,padx=30,pady=1)
    ttk.Button(fenetre2,image=c12,command=creermalyounfenetre12).grid(column=5, row=1,padx=30)
    ttk.Button(fenetre2,image=c13,command=creermalyounfenetre13).grid(column=0, row=2,padx=30,pady=1)
    ttk.Button(fenetre2,image=c14,command=creermalyounfenetre14).grid(column=1, row=2,padx=30)
    ttk.Button(fenetre2,image=c15,command=creermalyounfenetre15).grid(column=2, row=2,padx=30,pady=1)
    ttk.Button(fenetre2,image=c16,command=creermalyounfenetre16).grid(column=3, row=2,padx=30)
    ttk.Button(fenetre2,image=c17,command=creermalyounfenetre17).grid(column=4, row=2,padx=30,pady=1)
    ttk.Button(fenetre2,image=c18,command=creermalyounfenetre18).grid(column=5, row=2,padx=30)
    ttk.Button(fenetre2,image=c19,command=creermalyounfenetre19).grid(column=0, row=3,padx=30,pady=1)
    ttk.Button(fenetre2,image=c20,command=creermalyounfenetre20).grid(column=1, row=3,padx=30)
    ttk.Button(fenetre2,image=c21,command=creermalyounfenetre21).grid(column=2, row=3,padx=30)
    ttk.Button(fenetre2,image=c22,command=creermalyounfenetre22).grid(column=3, row=3,padx=30)
    ttk.Button(fenetre2,image=c23,command=creermalyounfenetre23).grid(column=4, row=3,padx=30)

    fenetre2.minsize(300,500)
    
    ttk.Button(fenetre2,text = "Close",command = fenetre2.destroy).grid(row=3,column=5)
def creefenetre3():
    global fenetre3
    fenetre3 = Toplevel(fenetre)
    fenetre3.title("Drivers")
    fenetre3.configure(background='white')
    fenetre3.minsize(300,300)
   
    ttk.Button(fenetre3,image=d1,command=creermalyounfenetre24).grid(column=0, row=0,padx=30,pady=1)
    ttk.Button(fenetre3,image=d2,command=creermalyounfenetre25).grid(column=1, row=0,padx=30)
    ttk.Button(fenetre3,image=d3,command=creermalyounfenetre26).grid(column=2, row=0,padx=30,pady=1)
    ttk.Button(fenetre3,image=d4,command=creermalyounfenetre27).grid(column=3, row=0,padx=30)
    ttk.Button(fenetre3,image=d5,command=creermalyounfenetre28).grid(column=0, row=1,padx=30,pady=1)
    ttk.Button(fenetre3,image=d6,command=creermalyounfenetre29).grid(column=1, row=1,padx=30)
    ttk.Button(fenetre3,image=d7,command=creermalyounfenetre30).grid(column=2, row=1,padx=30,pady=1)
    ttk.Button(fenetre3,image=d8,command=creermalyounfenetre31).grid(column=3, row=1,padx=30)
    ttk.Button(fenetre3,image=d9,command=creermalyounfenetre32).grid(column=0, row=2,padx=30,pady=1)
    ttk.Button(fenetre3,image=d10,command=creermalyounfenetre33).grid(column=1, row=2,padx=30)
    ttk.Button(fenetre3,image=d11,command=creermalyounfenetre34).grid(column=2, row=2,padx=30,pady=1)
    ttk.Button(fenetre3,image=d12,command=creermalyounfenetre35).grid(column=3, row=2,padx=30)
    ttk.Button(fenetre3,image=d13,command=creermalyounfenetre36).grid(column=0, row=3,padx=30,pady=1)
    ttk.Button(fenetre3,image=d14,command=creermalyounfenetre37).grid(column=1, row=3,padx=30)
    ttk.Button(fenetre3,image=d15,command=creermalyounfenetre38).grid(column=2, row=3,padx=30,pady=1)
    ttk.Button(fenetre3,image=d16,command=creermalyounfenetre39).grid(column=3, row=3,padx=30)
    ttk.Button(fenetre3,image=d17,command=creermalyounfenetre40).grid(column=0, row=4,padx=30,pady=1)
    ttk.Button(fenetre3,image=d18,command=creermalyounfenetre41).grid(column=1, row=4,padx=30)
    ttk.Button(fenetre3,image=d19,command=creermalyounfenetre42).grid(column=2, row=4,padx=30,pady=1)
    ttk.Button(fenetre3,image=d20,command=creermalyounfenetre43).grid(pady=10,column=3, row=4,padx=30)
    
def creefenetre4():
    global fenetre4
    fenetre4 = Toplevel(fenetre)
    fenetre4.configure(background="black")
    ttk.Button(fenetre4,image=s41,command=creermalyounfenetre44).grid(column=0, row=1,padx=30,pady=1)
    ttk.Button(fenetre4,image=s42,command=creermalyounfenetre45).grid(column=0, row=3,padx=30)
    ttk.Button(fenetre4,image=s43,command=creermalyounfenetre46).grid(column=1, row=3,padx=30)
    ttk.Button(fenetre4,image=s44,command=creermalyounfenetre47).grid(column=2, row=3,padx=30,pady=0)
    ttk.Button(fenetre4,image=s45,command=creermalyounfenetre48).grid(column=3, row=3,padx=30,pady=0)
    ttk.Button(fenetre4,image=s46,command=creermalyounfenetre49).grid(column=1, row=4,padx=30,pady=1)
    ttk.Button(fenetre4,image=s47,command=creermalyounfenetre50).grid(column=2, row=4,padx=30,pady=1)
    ttk.Button(fenetre4,image=s48,command=creermalyounfenetre51).grid(column=3, row=1,padx=30,pady=1)
    ttk.Button(fenetre4,image=s49,command=creermalyounfenetre52).grid(column=1, row=1,padx=30,pady=1)
    ttk.Button(fenetre4,image=s410,command=creermalyounfenetre53).grid(column=2, row=1,padx=30,pady=1)
    ttk.Button(fenetre4,image=stats,command=rasme).grid(column=3,row=4)
    fenetre4.title("Constructors")
    fenetre4.minsize(300,300)
    ttk.Button(fenetre4,text = "Close",command = fenetre4.destroy).grid(row=5,column=3)
img3=PhotoImage(file="resultsbg.png")
def creefenetre5():
    global fenetre5
    
    fenetre5 = Toplevel(fenetre)
    fenetre5.resizable(False,False)
    fenetre5.title("Standings")
    s35=ttk.Style()
    fenetre5.minsize(700,400)
    e_canvas= Canvas(fenetre5,width=645,height=350)
    e_canvas.pack(fill="both",expand=True)
    e_canvas.create_image(0,0,image=img3,anchor="nw")
    s35.configure('S35pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black',background='white')
    s351=ttk.Style()
    s351.configure('S35pecial.TLabel', font=('Formula1 Display Regular', 12, 'bold','underline'), foreground='black',background='white')
    response=requests.get("http://ergast.com/api/f1/current/driverStandings.json")
    data=response.json()
    dic=data['MRData']
    dic1=dic['StandingsTable']
    dic2=list(dic1.values())
    e_canvas.create_text(300,30,text='Standings',font=('Formula1 Display Bold', 24, 'bold'),fill="white")
    e_canvas.create_text(90,70,text="Position",font=('Formula1 Display Bold', 12, 'bold','underline'),fill="red")
    e_canvas.create_text(180,70,text="Wins",font=('Formula1 Display Bold', 12, 'bold','underline'),fill="red")
    e_canvas.create_text(270,70,text="Driver",font=('Formula1 Display Bold', 12, 'bold','underline'),fill="red")
    e_canvas.create_text(360,70,text="Code",font=('Formula1 Display Bold', 12, 'bold','underline'),fill="red")
    e_canvas.create_text(450,70,text="Points",font=('Formula1 Display Bold', 12, 'bold','underline'),fill="red")
    e_canvas.create_text(540,70,text="Team",font=('Formula1 Display Bold', 12, 'bold','underline'),fill="red")
    
    m=0
    j=90
    for i in dic2[1][0]['DriverStandings']:
         e_canvas.create_text(90,j,text=i['position'],font=('Formula1 Display Regular', 8, 'bold'),fill="black")
         e_canvas.create_text(180,j,text=i['wins'],font=('Formula1 Display Regular', 8, 'bold'),fill="black")
         e_canvas.create_text(270,j,text=i['Driver']['familyName'],font=('Formula1 Display Regular', 8, 'bold'),fill="black")
         e_canvas.create_text(360,j,text=i['Driver']['code'],font=('Formula1 Display Regular', 8, 'bold'),fill="black")
         e_canvas.create_text(450,j,text=i['points'],font=('Formula1 Display Regular', 8, 'bold'),fill="black")
         e_canvas.create_text(540,j,text=i['Constructors'][0]['name'],font=('Formula1 Display Regular', 8, 'bold'),fill="black")
         j=j+12
         m+=1
    
    fenetre5.minsize(300,300)
def creefenetre6():
    global fenetre6
    
    fenetre6 = Toplevel(fenetre) 
    fenetre6.title("Schedule")
    fenetre6.configure(bg='firebrick4')
    fenetre6.minsize(300,300)
    ttk.Button(fenetre6,image=r1,command=creermalyounfenetre56).grid(column=0, row=0,padx=30,pady=1)
    ttk.Button(fenetre6,image=r2,command=creermalyounfenetre57).grid(column=1, row=0,padx=30)
    ttk.Button(fenetre6,image=r3,command=creermalyounfenetre58).grid(column=2, row=0,padx=30,pady=1)
    ttk.Button(fenetre6,image=r4,command=creermalyounfenetre59).grid(column=3, row=0,padx=30)
    ttk.Button(fenetre6,image=r5,command=creermalyounfenetre60).grid(column=0, row=1,padx=30,pady=1)
    ttk.Button(fenetre6,image=r6,command=creermalyounfenetre61).grid(column=1, row=1,padx=30)
    ttk.Button(fenetre6,image=r7,command=creermalyounfenetre62).grid(column=2, row=1,padx=30,pady=1)
    ttk.Button(fenetre6,image=r8,command=creermalyounfenetre63).grid(column=3, row=1,padx=30)
    ttk.Button(fenetre6,image=r9,command=creermalyounfenetre64).grid(column=0, row=2,padx=30,pady=1)
    ttk.Button(fenetre6,image=r10,command=creermalyounfenetre65).grid(column=1, row=2,padx=30)
    ttk.Button(fenetre6,image=r11,command=creermalyounfenetre66).grid(column=2, row=2,padx=30,pady=1)
    ttk.Button(fenetre6,image=r12,command=creermalyounfenetre67).grid(column=3, row=2,padx=30)
    ttk.Button(fenetre6,image=r13,command=creermalyounfenetre68).grid(column=0, row=3,padx=30,pady=1)
    ttk.Button(fenetre6,image=r14,command=creermalyounfenetre69).grid(column=1, row=3,padx=30)
    ttk.Button(fenetre6,image=r15,command=creermalyounfenetre70).grid(column=2, row=3,padx=30,pady=1)
    ttk.Button(fenetre6,image=r16,command=creermalyounfenetre71).grid(column=3, row=3,padx=30)
    ttk.Button(fenetre6,image=r17,command=creermalyounfenetre72).grid(column=0, row=4,padx=30,pady=1)
    ttk.Button(fenetre6,image=r18,command=creermalyounfenetre73).grid(column=1, row=4,padx=30)
    ttk.Button(fenetre6,image=r19,command=creermalyounfenetre74).grid(column=2, row=4,padx=30,pady=1)
    ttk.Button(fenetre6,image=r20,command=creermalyounfenetre75).grid(column=3, row=4,padx=30)
    ttk.Button(fenetre6,image=r21,command=creermalyounfenetre76).grid(column=0, row=5,padx=30)
    ttk.Button(fenetre6,image=r22,command=creermalyounfenetre77).grid(column=1, row=5,padx=30)
    ttk.Button(fenetre6,image=r23,command=creermalyounfenetre78).grid(column=2, row=5,padx=30)
    ttk.Button(fenetre6,text = "Close",command = fenetre6.destroy).grid(row=5,column=3)

    
def creefenetre7():
    global fenetre7
    s8=ttk.Style()
    s8.configure('S8pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black')
    s81=ttk.Style()
    s81.configure('S81pecial.TLabel', font=('Formula1 Display Bold', 12, 'bold','underline'), foreground='red',background='white')
    fenetre7 = Toplevel(fenetre) 
    fenetre7.title("Qualifying")
    fenetre7.configure(bg='white')
    a=StringVar()
    b=StringVar()
    fenetre7.minsize()
    def resdequaly():
        year=a.get()
        roundd=b.get()
        response=requests.get("http://ergast.com/api/f1/"+year+"/"+roundd+"/qualifying.json")
        data=response.json()
        dic=data['MRData']
        dic1=dic['RaceTable']
        dic2=list(dic1.values())
        def review():
            webbrowser. open(dic2[2][0]['Circuit']['url'])
   
            
        
        ttk.Label(fenetre7, text='Round='+dic2[1],style='S81pecial.TLabel',background='white').grid(row=3, column=1)
        ttk.Label(fenetre7,text=dic2[2][0]['raceName'],style='S81pecial.TLabel',foreground='red',background='white').grid(row=0,column=2)
        ttk.Label(fenetre7,text=dic2[2][0]['date'],style='S8pecial.TLabel',background='white').grid(row=3,column=0)
        if  int(year)>2005:
            
            ttk.Label(fenetre7,text='Time='+dic2[2][0]['time'].strip("Z")+'EEST',style='S8pecial.TLabel',background='white').grid(row=3,column=2)
        j=1
        ttk.Label(fenetre7,text='Circuit:',style='S8pecial.TLabel',background='white').grid(row=6,column=0)
        ttk.Button(fenetre7,image=wiki,command=review).grid(row=6,column=3)
        ttk.Label(fenetre7,background='white',text=dic2[2][0]['Circuit']['Location']['country']+','+dic2[2][0]['Circuit']['Location']['locality'],style='S8pecial.TLabel').grid(column=2,row=6)
        ttk.Label(fenetre7,background='white',text=dic2[2][0]['Circuit']['circuitName'],style='S81pecial.TLabel').grid(column=1,row=6)
        
        j=15
        ttk.Label(fenetre7, text='Position',style='S81pecial.TLabel',foreground='red',background='white').grid(row=12,column=0,pady=20)
        ttk.Label(fenetre7, text='Time',style='S81pecial.TLabel',foreground='red',background='white').grid(row=12,column=1)
        ttk.Label(fenetre7, text='Driver',style='S81pecial.TLabel',foreground='red',background='white').grid(row=12,column=2)
        ttk.Label(fenetre7, text='Constructor',style='S81pecial.TLabel',foreground='red',background='white').grid(row=12,column=3)
        m=0
        for i in dic2[2][0]['QualifyingResults']:
            try:
                ttk.Label(fenetre7,text=i['position'],style='S8pecial.TLabel',background='white').grid(column=0,row=j)
                ttk.Label(fenetre7,text=i['Q3'],style='S8pecial.TLabel',background='white').grid(column=1,row=j)
                ttk.Label(fenetre7,text=i['Driver']['familyName'],style='S8pecial.TLabel',background='white').grid(column=2,row=j)
                ttk.Label(fenetre7,text=i['Constructor']['name'],style='S8pecial.TLabel',background='white').grid(column=3,row=j)
                j=j+1
                m=m+1
         

            except Exception :
                try:
                        ttk.Label(fenetre7,text=i['position'],style='S8pecial.TLabel',background='white').grid(column=0,row=j)
                        ttk.Label(fenetre7,text=i['Q2'],style='S8pecial.TLabel',background='white').grid(column=1,row=j)
                        ttk.Label(fenetre7,text=i['Driver']['familyName'],style='S8pecial.TLabel',background='white').grid(column=2,row=j)
                        ttk.Label(fenetre7,text=i['Constructor']['name'],style='S8pecial.TLabel',background='white').grid(column=3,row=j)
                     
                        
                        j=j+1
                except Exception:
                            try:
                                ttk.Label(fenetre7,text=i['position'],style='S8pecial.TLabel',background='white').grid(column=0,row=j)
                                ttk.Label(fenetre7,text=i['Q1'],style='S8pecial.TLabel',background='white').grid(column=1,row=j)
                                ttk.Label(fenetre7,text=i['Driver']['familyName'],style='S8pecial.TLabel',background='white').grid(column=2,row=j)
                                ttk.Label(fenetre7,text=i['Constructor']['name'],style='S8pecial.TLabel',background='white').grid(column=3,row=j)
                                j+=1
                            finally:
                                None
                                
                                
                
        
        

    ttk.Label(fenetre7,text="Enter The Year That Your are looking for : ",style='S8pecial.TLabel', foreground='red',background='white').grid(pady=30,padx=20,row=0,column=0)
    ttk.Entry(fenetre7,textvariable=a).grid(row=0,column=1)
    ttk.Label(fenetre7,text="Enter The Round: ",style='S8pecial.TLabel', foreground='red',background='white').grid(row=1,column=0)
    ttk.Entry(fenetre7,textvariable=b).grid(row=1,column=1)
    ttk.Button(fenetre7,text='Search',command=resdequaly).grid(row=0,column=3)
    ttk.Button(fenetre7,text = "Close",command = fenetre7.destroy).grid(row=105,column=3,padx=40,pady=40)

def creefenetre8():
    global fenetre8
    import webbrowser
    s00=ttk.Style()
    s00.configure('S00pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='black')
    def reviews():
        x=a.get()
        x=x-1950
        webbrowser. open(dic1['Seasons'][x]['url'])

    fenetre8 = Toplevel(fenetre) 
    fenetre8.title("History")
    fenetre8.minsize(800,300)
    fenetre8.configure(bg='red4')
    a=IntVar()
    ttk.Button(fenetre8,text = "Close",command = fenetre8.destroy).grid(row=22,column=2)
    url = "http://ergast.com/api/f1/seasons.json"
    response=requests.get("http://ergast.com/api/f1/seasons.json?limit=80&offset=0")
    data=response.json()
    dic=data['MRData']
    dic1=dic['SeasonTable']
    ttk.Label(fenetre8,text="Enter The Season That Your are looking for : ",style='S00pecial.TLabel', foreground='white',background='red4').grid(row=0,column=0,padx=20,pady=40)
    ttk.Entry(fenetre8,textvariable=a).grid(row=0,column=1)
    ttk.Button(fenetre8,text='Search',command=reviews).grid(row=0,column=2)
    ttk.Button(fenetre8,image=st1,command=creermalyounfenetre54).grid(column=1, row=22,padx=30,pady=1)
    ttk.Button(fenetre8,image=st2,command=creermalyounfenetre55).grid(column=0, row=22,padx=30,pady=1)

def creefenetre9():
    global fenetre9
    fenetre9 = Toplevel(fenetre) 
    fenetre9.title("Last Race Results")
    fenetre9.configure(bg='midnightblue')
    ttk.Button(fenetre9,image=pr,command=creermalyounfenetre80).grid(column=11, row=15,rowspan=15,padx=30)
    
    fenetre9.minsize(300,700)
    url = "http://ergast.com/api/f1/current/last/20/results"
    
    response=requests.get("http://ergast.com/api/f1/current/last/results.json")
    data=response.json()
    dic=data['MRData']
    dic1=dic['RaceTable']
    dic2=list(dic1.values())
    def hdar():
        webbrowser. open("https://www.youtube.com/results?search_query="+dic2[2][0]['raceName']+" "+dic2[2][0]['date']+"highlights")
    
    def review():
        webbrowser. open(dic2[2][0]['Circuit']['url'])
    s9=ttk.Style()
    s9.configure('S9pecial.TLabel', font=('Formula1 Display Regular', 8, 'bold'), foreground='white',background='midnightblue')
    s91=ttk.Style()
    s91.configure('S91pecial.TLabel', font=('Formula1 Display Bold', 12, 'bold','underline'), foreground='white',background='midnightblue')
    ttk.Button(fenetre9,image=yt,command=hdar).grid(row=6,column=4)  
    ttk.Label(fenetre9,text='LAST RACE RESULTS',style='S91pecial.TLabel').grid(row=0,column=1,pady=15)
    ttk.Label(fenetre9, text='Round='+dic2[1],style='S9pecial.TLabel').grid(row=4, column=1)
    ttk.Label(fenetre9,text=dic2[2][0]['raceName'],style='S91pecial.TLabel',foreground='red').grid(row=2,column=1,pady=10)
    ttk.Label(fenetre9,text=dic2[2][0]['date'],style='S9pecial.TLabel').grid(row=4,column=0,padx=30)
    ttk.Label(fenetre9,text='Time='+dic2[2][0]['time']+' EEST',style='S9pecial.TLabel').grid(row=5,column=2)
    j=1
    ttk.Label(fenetre9,text='Circuit:',style='S9pecial.TLabel').grid(row=6,column=0)
    ttk.Button(fenetre9,image=wiki,command=review).grid(row=6,column=3)
    ttk.Label(fenetre9,text=dic2[2][0]['Circuit']['Location']['country']+','+dic2[2][0]['Circuit']['Location']['locality'],style='S9pecial.TLabel').grid(column=2,row=6)
    ttk.Label(fenetre9,text=dic2[2][0]['Circuit']['circuitName'],style='S9pecial.TLabel').grid(column=1,row=6)
    
    j=15
    ttk.Label(fenetre9, text='Position',style='S91pecial.TLabel',foreground='red').grid(row=12,column=0,pady=20)
    ttk.Label(fenetre9, text='Points',style='S91pecial.TLabel',foreground='red').grid(row=12,column=1)
    ttk.Label(fenetre9, text='Driver',style='S91pecial.TLabel',foreground='red').grid(row=12,column=2)
    ttk.Label(fenetre9, text='Constructor',style='S91pecial.TLabel',foreground='red').grid(row=12,column=3)
    ttk.Label(fenetre9, text='Status',style='S91pecial.TLabel',foreground='red').grid(row=12,column=4)
    m=0
    for i in dic2[2][0]['Results']:
        try:
            ttk.Label(fenetre9,text=i['position'],style='S9pecial.TLabel').grid(column=0,row=j)
            ttk.Label(fenetre9,text=i['points'],style='S9pecial.TLabel').grid(column=1,row=j)
            ttk.Label(fenetre9,text=i['Driver']['familyName'],style='S9pecial.TLabel').grid(column=2,row=j)
            ttk.Label(fenetre9,text=i['Constructor']['name'],style='S9pecial.TLabel').grid(column=3,row=j)
            ttk.Label(fenetre9,text=i['Time']['time'],style='S9pecial.TLabel').grid(column=4,row=j)
            j=j+1
            m=m+1
        except Exception:
            try:
                ttk.Label(fenetre9,text=i['position'],style='S9pecial.TLabel').grid(column=0,row=j)
                ttk.Label(fenetre9,text=i['points'],style='S9pecial.TLabel').grid(column=1,row=j)
                ttk.Label(fenetre9,text=i['Driver']['familyName'],style='S9pecial.TLabel').grid(column=2,row=j)
                ttk.Label(fenetre9,text=i['Constructor']['name'],style='S9pecial.TLabel').grid(column=3,row=j)
                ttk.Label(fenetre9,text=i['status'],style='S9pecial.TLabel').grid(column=4,row=j)
                j=j+1
            finally:
                None
#news=StringVar()
s=ttk.Style()
s.configure('Special.TLabel', font=('Formula1 Display Bold', 24, 'bold','underline'), foreground='red')
s000=ttk.Style()
s000.configure('S000pecial.TLabel', font=('Formula1 Display Bold', 10, 'bold'), foreground='black')
APITN=StringVar()
I1=PhotoImage(file="images.png")
I2=PhotoImage(file="drivers.png")
I3=PhotoImage(file="cst.png")
I4=PhotoImage(file="LD.png")
I5=PhotoImage(file="download.png")
I6=PhotoImage(file="qfg.png")
I7=PhotoImage(file="f1oldd.png")
I8=PhotoImage(file="schdl.png")
ttk.Label(Frame1,text='The Home of Formula 1 Racing',style='Special.TLabel').grid(pady=20,row=0,column=2,sticky=W)
ttk.Button(Frame2,image=abt,command=creefenetre1).grid(column=0,row=100,padx=30,pady=20,sticky=W)
#top_headlines = newsapi.get_top_headlines(q='formula 1',
                                          #category='sports',
                                          #language='en')
#news=top_headlines['articles'][0]['description']
i=IntVar()
i=1
#def update():
    #my_label.config(text=news[:len(news)//2])
    #my_label.after(3000,update1)
def update1():
    my_label.config(text=news[len(news)//2:])
    my_label.after(3000,update)
ttk.Label(Frame3,text="Latest News  : ",style='S000pecial.TLabel',foreground='red').grid(column=0,row=0,sticky=W)
#my_label=ttk.Label(Frame3,text=news[:len(news)//2],style='S000pecial.TLabel')

latest=PhotoImage(file='latest.png')
ttk.Button(Frame2,image=I1,command=creefenetre2).grid(column=0, row=1,padx=30,pady=1)
ttk.Button(Frame2,image=I2,command=creefenetre3).grid(column=0, row=3,padx=30)
ttk.Button(Frame2,image=I3,command=creefenetre4).grid(column=1, row=3,padx=30)
ttk.Button(Frame2,image=I4,command=creefenetre5).grid(column=2, row=3,padx=30,pady=0)
ttk.Button(Frame2,image=I5,command=creefenetre6).grid(column=3, row=3,padx=30,pady=0)
ttk.Button(Frame2,image=I6,command=creefenetre7).grid(column=1, row=1,padx=30,pady=1)
ttk.Button(Frame2,image=I7,command=creefenetre8).grid(column=2, row=1,padx=30,pady=1)
ttk.Button(Frame2,image=I8,command=creefenetre9).grid(column=3, row=1,padx=30,pady=1)
def newsmore ():
   webbrowser. open(top_headlines['articles'][0]['url'])
ttk.Label(Frame3,text=" ").grid(column=1,row=0,sticky=W)
ttk.Label(Frame3,text=" ").grid(column=3,row=0,sticky=W)
ttk.Button(Frame3,image=latest,command=newsmore).grid(column=5, row=0,padx=20,sticky=E)


fenetre.mainloop()
