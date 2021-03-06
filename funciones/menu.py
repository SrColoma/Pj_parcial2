import pandas as pd
import os

##
# mostrarMenu:  muestra el menu en base a una lista y un tiutulo
# crada en:     6/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      2
##
def mostrarMenu(l_opciones,titulo): # l_opciones: lista con strings de opciones # titulo: cabecera del menu
    os.system("cls")
    print("\n*****",titulo,"*****\n")
    print(pd.Series(l_opciones,index=range(1,len(l_opciones)+1)))
    print("\n*****","*"*len(titulo),"*****\n")

##
# presentar:    toma un dataframe y lo presenta sin repeticiones
# crada en:     7/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      3
##
def presentar(df,titulo): #df: del dataframeo que se extraera #titulo: fracmento del diccionario
    #l1 = df.drop_duplicates(titulo,keep="first")
    #return l1[titulo]
    listado = list(set(df[titulo].to_dict().values()))
    return pd.Series(listado)

##
# input_int:    convierte un input en entero mientras pueda, sino vuelve a preguntar
# crada en:     7/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def input_int(str):
    entrada = "SrColoma"
    while not entrada.isdigit():
        entrada = input(str)
        if entrada.isdigit():
            return int(entrada)

##
# Buscar_en:    retorna un dataframe con la busqueda de la palabra en la columna indicada
# crada en:     12/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def buscar_en(df,colunm,inp):
    df_dato = pd.DataFrame()

    while df_dato.empty:
        print("Ingrese:",inp)
        jugador = input(">> ")
        df_dato = df.loc[df[colunm].str.startswith(jugador)]

    df_dato = df_dato.drop_duplicates(colunm)
    return df_dato
