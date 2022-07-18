from ast import Lambda
from ntpath import join
from shutil import which
import sys,csv #bibliotecas

#tosos estos on imput del usuario que voy a pedirle  
#POSICION CERO ES LA DEL PROGRAMA 
POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1  #Pasar al programa nombre archivo
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_NUMERO = 3

#datos de cheque que va a consultar
ETIQUETA_CABECERA_CSV_DNI ="DNI"
ETIQUETA_CABECERA_CSV_NUMCHEQUE = "NroCheque"
ETIQUETA_CABECERA_CSV_FECHAORIGEN = "FechaOrigen"
ETIQUETA_CABECERA_CSV_CUENTA = "NroCuenta"
ETIQUETA_CABECERA_CSV_VALOR = "Valor"
ETIQUETA_CABECERA_CSV_ESTADO = "Estado"
#VALIDO DATOS Y SE QUE VA A ETAR EN ESAS POSIIONES 

if __name__ == "__main__":

    with open (sys.argv [POSICION_ARGUMENTO_NOMBRE_ARCHIVO]) as archivo: #sys hasta ] devuelve string 'archivo.csv' es una forma de abrir y cerrar automatiamente el archivo
        lector = csv.reader(archivo) #leimos
        datos = list(lector) #traer a lista
        #indice 0 eat la primer fila ,la cabecera

    cabecera = datos[0]   #

    (posicion_dni,
    posicion_numero,
    posicion_fecha,
    posicion_estado) = (cabecera.index(ETIQUETA_CABECERA_CSV_DNI), 
                        cabecera.index(ETIQUETA_CABECERA_CSV_FECHAORIGEN), 
                        cabecera.index(ETIQUETA_CABECERA_CSV_NUMCHEQUE),
                        cabecera.index(ETIQUETA_CABECERA_CSV_ESTADO))    
#TENEMOS QUE FILTRAR 
    datos_cliente=list(filter(lambda registro: 
                                            registro[posicion_dni]== sys.argv[POSICION_ARGUMENTO_DNI], datos[1:]))
                 
               
    print (','.join(cabecera))#LAMBDA FUNCION SIMILAR A ARROW FUNCTION EN JS: PERTMITE declarar funciones anonimas en una misma linea no ahorra el return.(registro es el argumento )
    #funcion filter, filtra dentro de la lista valor de returno nos va a permitir traer datos del cliente 

    #guardamos el dato del clienteen una lista tenemos que iterarlio

    for t in datos_cliente:
        print(','.join(t))  