from funciones import funciones_obligatorias as funo
from funciones import menu
import pandas as pd

##
# primera opcion del menu reportes
# creada en:    8/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def opcion_1(df_dataset):
    print("""
                    Top Ten de los jugadores
                    por un torneo determminado 
                    en un año determinado
                    """)
    input("[ENTER]")

    # pide el año
    df_anios = pd.Series(range(2000, 2017))
    print(df_anios)
    int_anio = menu.input_int("\nelija una año (indice):\n>> ")

    #pide el torneop
    df_torn = menu.presentar(df_dataset[df_dataset["Date"].str.endswith(str(int_anio))], "Tournament")
    print(df_torn)
    int_torneo = menu.input_int("\nelija una torneo (indice):\n>> ")

    # si el torneo y año existen llama al top ten
    if (int_torneo in df_torn.keys()) and (int_anio in df_anios.keys()):

        df_topTen = funo.getTopTenJugadores(df_dataset.set_index("Tournament"), df_torn[int_torneo], df_anios[int_anio])
        print(df_topTen)
        input("[ENTER]")

    else:
        print("selecciono un indice que no se encuentra en las lista, vuela a intentarlo")
        input("[ENTER]")

##
# segunda opcion del menu reportes
# creada en:    13/agosto/2017
# autor:        Coloma Ortiz Alfred
# version:      1
##
def opcion_2(df_dataset):
    print("""
                    estadisticas
                    por un jugador 
                    predeterminado
                    """)
    input("[ENTER]")

    #filtra el dataframe para pbuscar el jugador
    df_jugador = menu.buscar_en(df_dataset,"Winner","el apellido del jugador")
    print(df_jugador["Winner"])

    # si hay mas de una coinsidencia preguntqar pcual se queda
    int_selec  = menu.input_int("seleccione un jugador(indice):\n>>")

    if int_selec in df_jugador["Winner"].keys():

        str_nombre = df_jugador["Winner"][int_selec]
        print("selecciono: ",str_nombre)
        funo.getEstadisticasJugador(df_dataset.set_index("Winner"),str_nombre)

    else:
        print("selecciono un indice que no se encuentra en las lista, vuela a intentarlo")
        input("[ENTER]")

def opcion_3(df_dataset):
    print("""
                    Eficiencia
                    por tipo de 
                    superficie
                    """)
    input("[ENTER]")

    # filtra el dataframe para pbuscar el jugador
    df_jugador = menu.buscar_en(df_dataset, "Winner", "el apellido del jugador")
    print(df_jugador["Winner"])

    # si hay mas de una coinsidencia preguntqar pcual se queda
    int_selec = menu.input_int("seleccione un jugador(indice):\n>>")


    # filtra el dataframe para buscar las superficies
    df_superficie = menu.buscar_en(df_dataset,"Surface","terreno o superficie [ENTER]")
    print(df_superficie["Surface"])

    int_superficie = menu.input_int("seleccione una superficie(indice):\n>>")

    if int_selec in df_jugador["Winner"].keys() and int_superficie in df_superficie["Surface"].keys():

        str_nombre = df_jugador["Winner"][int_selec]
        str_sup    = df_superficie["Surface"][int_superficie]
        print("selecciono: ", str_nombre)
        print("selecciono: ", str_sup)
        funo.getEficienciaJugadorXsuperficie(df_dataset, str_nombre,str_sup)

    else:
        print("selecciono un indice que no se encuentra en las lista, vuela a intentarlo")
        input("[ENTER]")

def opcion_4(df_dataset):
    pass

def opcion_5(df_dataset):
    pass

def opcion_6(df_dataset):
    pass
