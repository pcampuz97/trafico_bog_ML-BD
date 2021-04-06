#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:11:19 2021

@author: cpablo
"""

import fiona
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def cargar_datos(archivo):
    datos = gpd.read_file(archivo)
    return datos

def mostrar_capas(archivo):
    for layers in fiona.listlayers(archivo):
        todos = gpd.read_file(archivo, layer="UPZ")
        #print(layers)
        i = 0
        for name in todos.columns:
            print(name)
            i+=1

def visualizar_todos(archivo, datos_bog):
    #Cargar ciclorutas
    ciclorutas = gpd.read_file(datos_bog, layer="Cicl")
    upz_bog = gpd.read_file(datos_bog, layer="UPZ")
    
    #Cargar siniestros y agrupar por columna gravedad y geometria
    siniestros = archivo
    siniestros = siniestros[["GRAVEDAD", "geometry"]]
    #Cantidad maxima de datos que me deja graficar
    siniestros = siniestros.iloc[0:1418]
    
    #Graficar mapa y datos
    fig, ax = plt.subplots(figsize=(15,20))
    ax.set_aspect('equal')
    upz_bog.plot(ax=ax, facecolor="none", edgecolor="black", legend=True)
    #ciclorutas.plot(ax=ax, facecolor="none", edgecolor="black", legend=True)
    siniestros.plot(ax=ax, column="GRAVEDAD", legend=True)

    
    plt.title("Siniestros",{"fontsize":20})
    plt.show()


def visualizar_muertes(archivo, datos_bog):
    ciclorutas = gpd.read_file(datos_bog, layer="Cicl")
    upz = gpd.read_file(datos_bog , layer="UPZ")
    
    muertes = archivo
    muertes = muertes[["GRAVEDAD", "geometry"]]
    muertes = muertes.loc[muertes["GRAVEDAD"]=="CON MUERTOS"]
    
    upz = upz.loc
    
    fig, ax = plt.subplots(figsize=(15,20))
    ax.set_aspect('equal')
    #ciclorutas.plot(ax=ax, facecolor="none", edgecolor="black", legend=True)
    upz.plot(ax=ax, facecolor="none", edgecolor="black", legend=True)
    muertes.plot(ax=ax, color="red")
    
    return upz
    plt.title("Siniestros con muertes",{"fontsize":20})
    plt.show()
    
def nodos_transporte(archivo, datos_bog):
    localidades = gpd.read_file(datos_bog, layer="Loca")
    
    nodos = archivo
    
    fig, ax = plt.subplots(figsize=(15,20))
    ax.set_aspect('equal')
    localidades.plot(ax=ax, facecolor="none", edgecolor="black", legend=True)
    nodos.plot(ax=ax, column="NTRNOMBRE", legend=False)
    
    plt.title("Nodos",{"fontsize":20})
    plt.show()
    
def ver_datos_danos(archivo):
    danos = archivo
    danos = danos[["GRAVEDAD", "LOCALIDAD"]]
    danos = danos.loc[danos["GRAVEDAD"]=="SOLO DANOS"].value_counts()
    
    danos.plot.bar()
    plt.title("Siniestros con solo daños por localidad")
    plt.show()

def ver_datos_heridos(archivo):
    heridos = archivo
    heridos = heridos[["GRAVEDAD", "LOCALIDAD"]]
    heridos = heridos.loc[heridos["GRAVEDAD"]=="CON HERIDOS"].value_counts()
    
    heridos.plot.bar()
    plt.title("Siniestros con heridos por localidad")
    plt.show()

def ver_datos_muertes(archivo):
    muertes = archivo
    muertes = muertes[["GRAVEDAD", "LOCALIDAD"]]
    muertes = muertes.loc[muertes["GRAVEDAD"]=="CON MUERTOS"].value_counts()
    
    muertes.plot.bar()
    plt.title("Siniestros con muertos por localidad")
    plt.show()