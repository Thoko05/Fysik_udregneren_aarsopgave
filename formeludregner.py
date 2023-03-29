# import html5lib
# import requests
# import pprint
# pi=(math.pi)
# def tyngdekraft():
#     print("Tyngdekraft: \n")
#     #Input til udregning af tyngdekraft
#     masse = float(input("Skriv massen på legemet i kg: "))
#     tyngdeacceleration=(9.82)
#     #Udregner resultatet
#     resultat = (masse * tyngdeacceleration)

#     #skriver resultatet til brugeren i output
#     print(f"Tyngdekraften trækker i legemet med = {resultat} N")
# tyngdekraft()

# def effekt():
#     print("Effekt: \n")
#     #Input til udregning af effekt
#     energi=float(input("Skriv energi målt i joule: "))

#Evt. kilder: https://equplus.net/sheets/Equations-26.html
#Kilde 2? https://johanw.home.xs4all.nl/#formularium
#evt. kilde 3? http://www.equationsheet.com/
#print("Vælg fysik kategorien")
#muligheder=["Fysikkens grundlag",""]

import PySimpleGUI as sg
import copy
import math
import numpy
#printer en velkomst
welcome =[[sg.Text("Velkommen til fysik udregneren. Hvilken formel vil du bruge?", justification="center")],
          [sg.Text('Du kan gå et vindue tilbage ved at klikke på krydset (X) i øvre højre hjørne. \nDu kan afslutte ved at gå ind på et emne og vælge "Exit",\neller ved at klikke på X i hovedmenuen.')]]

#Viser en listbox i hovedmenuen af mulighederne
listboxmainmenu=[[sg.Listbox(values=["Fysikkens grundlag", "Energi"], size=(60, 12), enable_events=True)]]

#printer vinduet hvor formelemne vælges
welcomeformula=[[sg.Text("Vælg en formel", justification="center")]]

#printer vinduet hvor enheder og tal indtastes
welcomeformula2=[[sg.Text("Indtast de korrekte værdier, og programmet vil udregne for dig!", justification="center")]]

#viser en listbox i formelvælger - fysikkens grundlag af mulighederne
listboxformulabasis=[[sg.Listbox(values=["Tyngdekraft", "Densitet"], size=(60, 12), enable_events=True)]]

#Tyngdekraftudregner: Hovedmenu, fysikkens grundlag, tyngdekraft.
calcgravity=[[sg.Text("Formel for beregning af tyngdekraft: F_t = m · g \n \n m = masse, g = tyngdeacceleration = 9.82m/s^2")], 
            [sg.Text(" \n \n Indtast masse i kg:")],
            [sg.InputText("", key="inputmass")],
            [sg.Button("Beregn tyngdekraft"), sg.Exit()]]

#Densitetsudregner: Hovedmenu, fysikkens grundlag, densitet (u03C1 = rho)
calcdensity=[[sg.Text("Formel for beregning af densitet: \u03C1 = m/V \n \n m = masse, V = volumen")], 
            [sg.Text(" \n \n Indtast masse i kg:")],
            [sg.InputText("", key="inputmass")],
            [sg.Text(" \n \n Indtast volumen/rumfang i m^3:")],
            [sg.InputText("", key="inputvolume")],
            [sg.Button("Beregn densitet"), sg.Exit()]]

#viser en listbox i formelvælger - energi af mulighederne
listboxformulaenergy=[[sg.Listbox(values=["Effekt", "Specifik varmekapicitet", "Nyttevirkning"], size=(60, 12), enable_events=True)]]

#Laver hovedvinduet til programmet
windowmain=sg.Window(title="Fysik formel udregner", layout=welcome+listboxmainmenu, margins=(25, 25))
#laver vinduet til fysikkens grundlag
# windowbasis.finalize()
# windowbasis.hide()
#laver vinduet til energi
#windowenergy=sg.Window(title="Formelvælger - Energi", layout=welcomeformula+listboxformulaenergy, margins=(25, 25))


#påbegynder smartere måde at læse vinduer
eventbasis=-1
eventgravity=-1
eventdensity=-1
windowstate="main"

#Forhindrer NameError fejl - valuesgravity is not defined. Ved ikke hvad den skal printe - linje 128
valuesgravity=None

#Læser fra de korrekte vinduer alt efter hvor brugeren befinder sig
while True:
    #Hovedmenu
    if windowstate=="main":
           eventmain, values=windowmain.read()
    
    #Vindue for fysikkens grundlag
    elif windowstate=="basis":
        eventbasis, valuesbasis=windowbasis.read()
    
    #Vindue for tyngdekraftudregner
    elif windowstate=="gravity":
        eventgravity, valuesgravity=windowgravity.read()
        
        #Udregner tyngdekraft
        if eventgravity=="Beregn tyngdekraft":
            try:
                inputmass=float(valuesgravity["inputmass"]) #gemmer input som en variabel og gør det til float
                resultgravity=inputmass*9.82 #udregner
            except ValueError:
                sg.popup(f"Ugyldig masse input til udregning af tyngdekraft")
            else:
                sg.popup(f"Tyngdekraften trækker i legemet med = {resultgravity} N")
        if eventgravity=="Exit":
            break
        
        #vindue for densitetsudregner
    elif windowstate=="density":
        eventdensity, valuesdensity=windowdensity.read()
        
        #udregner densitet
        if eventdensity=="Beregn densitet":
            try:
                inputmass=float(valuesdensity["inputmass"]) #gemmer input som en variabel og gør det til float
                inputvolume=float(valuesdensity["inputvolume"]) #gemmer input som en variabel og gør det til float
                resultdensity=inputmass/inputvolume #udregner
            except ValueError:
                sg.popup(f"Ugyldig masse/volumen/rumfang input til udregning af densitet")
            else:
                sg.popup(f"Densiteten af legemet er = {resultdensity} kg/m^3")
        if eventdensity=="Exit":
            break

        print(f"{eventmain=}, {values=}")        
        print(f"{eventbasis=}, {valuesbasis=}")
        print(f"{eventgravity}{valuesgravity}")
        print(f"{eventdensity}{valuesdensity}")


#eventmain, values=windowenergy.read()
    #eventmain loop
    #    print(f"Du har valgt: {values[0][0]}")
    
    
    #Muliggører det at gå frem og tilbage mellem vinduer
    if eventmain == sg.WIN_CLOSED or eventmain == "Exit": #Hvis hovedvinduet bliver lukket stopper programmet
        break
    
    #Hvis vinduet for fysikkens grundlag bliver lukket gåes der tilbage til hovedmenu
    if eventbasis==sg.WIN_CLOSED:
        windowstate="main"
        windowmain.un_hide()
        eventbasis = -1
    
    #Hvis vinduet for tyngdekraftudregner bliver lukket gåes der tilbage til fysikkens grundlag
    elif eventgravity==sg.WIN_CLOSED:
        windowstate="basis"
        windowbasis.un_hide()
        eventgravity = -1
    
    #Hvis vinduet for densitetsudregner bliver lukket gåes der tilbage til fysikkens grundlag
    elif eventdensity==sg.WIN_CLOSED:
        windowstate="basis"
        windowbasis.un_hide()
        eventdensity = -1
    
    #Skjuler de korrekte vinduer og giver titler
    elif windowstate=="main" and values[0][0]=="Fysikkens grundlag":
        windowmain.hide()
        eventmain = -1
        layoutbasis=copy.deepcopy(welcomeformula+listboxformulabasis)
        windowbasis=sg.Window(title="Formelvælger - Fysikkens grundlag", layout=layoutbasis, margins=(25, 25))
        windowstate="basis"
    
    elif windowstate=="basis" and valuesbasis[0][0]=="Tyngdekraft":
        windowbasis.hide()
        layoutgravity=copy.deepcopy(welcomeformula2+calcgravity)
        windowgravity=sg.Window(title="Formeludregner - Tyngdekraft", layout=layoutgravity, margins=(25, 25))
        windowstate="gravity"
    
    elif windowstate=="basis" and valuesbasis[0][0]=="Densitet":
        windowbasis.hide()
        layoutdensity=copy.deepcopy(welcomeformula2+calcdensity)
        windowdensity=sg.Window(title="Formeludregner - Densitet", layout=layoutdensity, margins=(25, 25))
        windowstate="density"
    # if values[0][0]=="Energi":
    #     windowmain.hide()
#        windowenergy.un_hide()


#Forhindrer NameError fejl - hvis brugeren ikke klikker ind på et vindue kommer if/else statements ikke til at trigger
#og programmet bliver forvirret over hvad den skal lukke.
#Hovedmenu
if windowmain in locals():
    windowmain.close()

#Basisvindue    
if 'windowbasis' in locals():
    windowbasis.close()
    
#windowenergy.close()

#Tyngdekraft-vindue
if 'windowgravity' in locals():
    windowgravity.close()

#Densitet-vindue
if 'windowdensity' in locals():
    windowdensity.close()