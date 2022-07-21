from csv import excel
from operator import index
from pickle import FALSE, TRUE
from statistics import geometric_mean
from turtle import window_height
from unittest import result
import PySimpleGUI as py
import pandas as pd
import _tkinter as tk

py.theme("Material2")

Excel="Humanos3DInventarioFilamentos.xlsx"
df=pd.read_excel("Humanos3DInventarioFilamentos.xlsx")


vista=[
    [py.Text("INGRESE LA INFORMACION REQUERIDA ")],
    [py.Text("ID",size=(15,1)),py.InputText(key="ID")],
    [(py.Text("PESO INICIAL (G/L)",size=(15,1)),py.InputText(key="PESO INICIAL (G/L)"))],
    [py.Text("CALIBRE",size=(15,1)),py.InputText(key="CALIBRE")],
    [py.Text("COLOR",size=(15,1)),py.InputText(key="COLOR")],
    [py.Text("MATERIAL",size=(15,1)),py.InputText(key="MATERIAL")],
    [py.Text("MARCA",size=(15,1)),py.InputText(key="MARCA")],
    [py.Text("PESO ACTUAL (G/L)",size=(15,1)),py.InputText(key="PESO ACTUAL (G/L)")],
    [py.Text("COSTO",size=(15,1)),py.InputText(key="COSTO")],
    [py.Submit("Guardar"),py.Button("Limpiar"),py.Button("Eliminar"),py.Button("Indices"),py.Button("Modificar PESO ACTUAL (G/L)"),py.Button("Modificar PESO INICIAL (G/L)"),py.Button("Cambiar Costo"),py.Exit("Salir")]
]

logoprincipalheader=py.set_global_icon ("H3D_logo.ico")
ventana= py.Window("HUMANOS-3D",vista,logoprincipalheader)

##################FUNCIONES############################################

def guardar():

    df_GUARDAR=df.append(values,ignore_index=True)
    df_GUARDAR.to_excel(Excel, index=False)


def limpiar():
    for key in values:
        ventana[key]("")
    return None


def eliminar():

    Excel="Humanos3DInventarioFilamentos.xlsx"
    df=pd.read_excel("Humanos3DInventarioFilamentos.xlsx")

    df.set_index("ID",inplace=True)

    form = py.FlexForm('Math')

    layout = [ [py.Txt('Entra ID')],
            [py.In(size=(8,1), key='numeratorID')],
            [py.Submit(),py.CloseButton("Cancelar")]]

    form.Layout(layout)
    
    button, values = form.Read()

    numeratorID = int(values['numeratorID'])
            

    aux=df.drop(index=numeratorID)
    aux.to_excel(Excel)
    

def modificarpesoactual():

    Excel="Humanos3DInventarioFilamentos.xlsx"
    df=pd.read_excel("Humanos3DInventarioFilamentos.xlsx")

    df.set_index("ID",inplace=True)

    form=py.FlexForm("Math")

    layout = [ [py.Txt("Ingrese el ID: ")],
           [py.In(size=(8,1), key="Ind")],
           [py.Txt("Ingrese el numero que implemento en Litros o Gramos: ")],
           [py.In(size=(8,1), key="cantidad")],
           [py.Submit(),py.Exit("Cancelar")]]

    form.layout(layout)
    button,values=form.read()
    Ind=int(values["Ind"])
    cantidad=float(values["cantidad"])
   
    aux=df["PESO ACTUAL (G/L)"]
    aux2=aux[Ind]
    valorfila=float(aux2)
    resultado= (valorfila-cantidad)
    df.loc[Ind,"PESO ACTUAL (G/L)"]=resultado
    df.to_excel(Excel)

def modificarpesoinicial():

    Excel="Humanos3DInventarioFilamentos.xlsx"
    df=pd.read_excel("Humanos3DInventarioFilamentos.xlsx")

    df.set_index("ID",inplace=True)

    form=py.FlexForm("Math")

    layout = [ [py.Txt("Ingrese el ID: ")],
           [py.In(size=(8,1), key="Ind")],
           [py.Txt("Ingrese el numero a agregar en Litros o Gramos")],
           [py.In(size=(8,1), key="cantidad")],
           [py.Submit(),py.CloseButton("Cancelar")]]

    form.layout(layout)
    button,values=form.read()
    Ind= int(values["Ind"])
    cantidad=abs(float(values["cantidad"]))
   
    aux=df["PESO INICIAL (G/L)"]
    aux2=aux[Ind]
    valorfila=float(aux2)
    resultado= (valorfila+cantidad)
    df.loc[Ind,"PESO INICIAL (G/L)"]=resultado

    aux3=df["PESO ACTUAL (G/L)"]
    aux4=aux3[Ind]
    valorfila1=float(aux4)
    resultado1=abs(valorfila1+cantidad)

    df.loc[Ind,"PESO ACTUAL (G/L)"]=resultado1
    df.to_excel(Excel)
    

def verindices():

    Excel="Humanos3DInventarioFilamentos.xlsx"
    df=pd.read_excel("Humanos3DInventarioFilamentos.xlsx")

    df.set_index("ID",inplace=True)

    informacion_indices=df[["MATERIAL","CALIBRE","COLOR"]]
    py.popup_scrolled(informacion_indices)
    


def costo():

    Excel="Humanos3DInventarioFilamentos.xlsx"
    df=pd.read_excel("Humanos3DInventarioFilamentos.xlsx")

    df.set_index("ID",inplace=True)


    form=py.FlexForm("Math")

    layout = [ [py.Txt("Ingrese el ID: ")],
           [py.In(size=(8,1), key="Ind")],
           [py.Txt("Ingrese el nuevo valor: ")],
           [py.In(size=(8,1), key="precio")],
           [py.Submit(),py.CloseButton("Cancelar")]]

    form.layout(layout)
    button,values=form.read()
    Ind= int(values["Ind"])
    cantidad=float(values["precio"])

    df.loc[Ind,"COSTO"]=cantidad
    df.to_excel(Excel)

while True:
    evento, values = ventana.read()
    if evento == py.WIN_CLOSED or evento== "Salir":
        break

    elif evento == "Limpiar":
        limpiar()

    elif evento == "Eliminar":
        eliminar()
        py.popup("Se Guardo tu cambio")
    
    elif evento == "Modificar PESO ACTUAL (G/L)":
        modificarpesoactual()
        py.popup("Se modifico el peso")

    elif evento == "Indices":
        verindices()

    elif evento == "Guardar":
        guardar()
        py.popup("Se Guardo Correctamente")


    elif evento=="Cambiar Costo":
        costo()
        py.popup("Se Guardo Correctamente")

    elif evento=="Modificar PESO INICIAL (G/L)":
        modificarpesoinicial()
        py.popup(" Se Modifico Correctamente")

ventana.close()

