from ast import Lambda
from asyncore import write
from ntpath import join
from shutil import which
from datetime import datetime
import sys,csv, time #bibliotecas

#tosos estos on imput del usuario que voy a pedirle  
#POSICION CERO ES LA DEL PROGRAMA 
POSICION_ARGUMENTO_NOMBRE_ARCHIVO = 1  #Pasar al programa nombre archivo
POSICION_ARGUMENTO_DNI = 2
POSICION_ARGUMENTO_SALIDA = 3
POSICION_ARGUMENTO_TIPO= 4 #TIPO
POSICION_ARGUMENTO_OPCION1 = 5 #FECHA   
POSICION_ARGUMENTO_OPCION2 = 6   

#datos de cheque que va a consultar
ETIQUETA_CABECERA_CSV_DNI ="DNI"
ETIQUETA_CABECERA_CSV_NUMCHEQUE = "NroCheque"
ETIQUETA_CABECERA_CSV_FECHAORIGEN = "FechaOrigen"
ETIQUETA_CABECERA_CSV_FECHAPAGO = "FechaPago"
ETIQUETA_CABECERA_CSV_CUENTA = "NroCuenta"
ETIQUETA_CABECERA_CSV_VALOR = "Valor"
ETIQUETA_CABECERA_CSV_TIPO = "Tipo"
ETIQUETA_CABECERA_CSV_ESTADO = "Estado"
#VALIDO DATOS Y SE QUE VA A ETAR EN ESAS POSIIONES 

ESTADO_CHEQUE_APROBADO = "Aprobado"
ESTADO_CHEQUE_PENDIENTE = "Pendiente"
ESTADO_CHEQUE_RECHAZADO = "Rechazado"

TIPO_SALIDA_PANTALLA= "PANTALLA"
TIPO_CSV = "CSV"
RANGO_FECHAINICIO= 0
RANGO_FECHAFIN = 1

CANTIDAD_CON_DOS_ATRIBUTOS_OPCIONALES=6
CANTIDAD_CON_UN_ATRIBUTOS_OPCIONALES=7

if __name__ == "__main__":

    with open (sys.argv [POSICION_ARGUMENTO_NOMBRE_ARCHIVO]) as archivo: #sys hasta ] devuelve string 'archivo.csv' es una forma de abrir y cerrar automatiamente el archivo
        lector = csv.reader(archivo) #leimos
        datos = list(lector) #traer a lista
        #indice 0 eat la primer fila ,la cabecera

    cabecera = datos[0]   #

    (posicion_dni,
    posicion_numero_cheque,
    posicion_tipo_cheque,
    posicion_fecha_origen,
    posicion_fecha_pago,
    posicion_estado) = (cabecera.index(ETIQUETA_CABECERA_CSV_DNI), 
                        cabecera.index(ETIQUETA_CABECERA_CSV_NUMCHEQUE),
                        cabecera.index(ETIQUETA_CABECERA_CSV_TIPO),
                        cabecera.index(ETIQUETA_CABECERA_CSV_FECHAORIGEN), 
                        cabecera.index(ETIQUETA_CABECERA_CSV_FECHAPAGO), 
                        cabecera.index(ETIQUETA_CABECERA_CSV_ESTADO))   

estado= None
fecha= None                         
#TENEMOS QUE FILTRAR 
if len(sys.argv) == CANTIDAD_CON_DOS_ATRIBUTOS_OPCIONALES:

        estado = sys.argv[POSICION_ARGUMENTO_OPCION1]

        fecha = tuple(map(lambda f: datetime.timestamp(datetime.strptime(f,'%d-%m-%Y')), sys.argv[POSICION_ARGUMENTO_OPCION2].split(":")))

elif len(sys.argv) == CANTIDAD_CON_UN_ATRIBUTOS_OPCIONALES:

        if sys.argv[POSICION_ARGUMENTO_OPCION1] in [ESTADO_CHEQUE_APROBADO,ESTADO_CHEQUE_RECHAZADO,ESTADO_CHEQUE_PENDIENTE]:

            estado = sys.argv[POSICION_ARGUMENTO_OPCION1 ]

else:

            fecha = tuple(map(lambda f: datetime.timestamp(datetime.strptime(f,'%d-%m-%Y')), sys.argv[POSICION_ARGUMENTO_OPCION1].split(":")))    
                 
               
    #print (','.join(cabecera))#LAMBDA FUNCION SIMILAR A ARROW FUNCTION EN JS: PERTMITE declarar funciones anonimas en una misma linea no ahorra el return.(registro es el argumento )
    #funcion filter, filtra dentro de la lista valor de returno nos va a permitir traer datos del cliente 

    #guardamos el dato del clienteen una lista tenemos que iterarlio

datos_cliente = list(filter(

        lambda registro: 

            registro[posicion_dni] == sys.argv[POSICION_ARGUMENTO_DNI] and 

            registro[posicion_tipo_cheque]==sys.argv[POSICION_ARGUMENTO_TIPO],

            datos[1:]))

#comprobamos nr cheque
listado_numero_cheques = list(map(lambda registro : registro[posicion_numero_cheque], datos_cliente))  
if len (listado_numero_cheques) !=len(set(listado_numero_cheques)):      
    print("numero heques repetidos")
    sys.exit()  

  #filtramo estado
if estado is not None:
     datos_cliente = list(filter(lambda registro: registro[posicion_estado]==estado, datos_cliente))

 #filtramos por fecha
if fecha is not None:
    datos_cliente = list(filter(lambda registro: 
    float (registro[posicion_fecha_origen])>fecha [RANGO_FECHAINICIO] and float(registro [posicion_fecha_origen])< fecha[RANGO_FECHAFIN],datos_cliente))

salida = sys.argv[POSICION_ARGUMENTO_SALIDA]
if salida== TIPO_SALIDA_PANTALLA:
    print(",". join(cabecera))
    for t in datos_cliente:
        print(",".join(t))
elif salida==TIPO_CSV:
    posicion_cuenta_origen= cabecera.index
    (ETIQUETA_CABECERA_CSV_CUENTA)
    posicion_valor = cabecera.index(ETIQUETA_CABECERA_CSV_VALOR)

    with open ("{}_{}.csv".format(
        sys.argv[POSICION_ARGUMENTO_DNI],time.time()),"w") as f: 
        writer= csv.writer(f)
        writer.writerow([cabecera[posicion_fecha_origen],cabecera
        [posicion_fecha_pago],cabecera
        [posicion_cuenta_origen],cabecera
        [posicion_valor],cabecera
        [posicion_estado]])
        for t in datos_cliente:
            writer.writerow([t [posicion_fecha_origen],t
            [posicion_fecha_pago],t
            [posicion_cuenta_origen],t
            [posicion_valor],t [posicion_estado]])
            print("CSV CREADO")

        else: 
            print("Error con parametro salida, deb ser del tipo {} o {}".format (TIPO_SALIDA_PANTALLA,TIPO_CSV)  )    

   


    