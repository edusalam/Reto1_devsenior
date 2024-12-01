#librerias importadas
from datetime import datetime
import statistics
#Codigo actualizado primero de diciembre del 2024
#lista para almacenar los datos ingresados por el usuario
listaExperimentos = []

#clase creada para el programa 
class Experimento:

    #metodo constructor 
    def __init__(self, nombreExperimento, fechaDeRealizacion, tipoExperimento, resultadosExperimento):
        self.nombreExperimento = nombreExperimento
        self.fechaDeRealizacion = fechaDeRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultadosExperimento = resultadosExperimento

def agregarExperimento(listaExperimentos):
    #funsion que permite que el usuario agrege experimentos
    nombreExperimento = input('\npor favor ingrese el nombre del experimento :  ')
    fechaDeRealizacion = input('ingresar la fecha de realizacion del proyecto (DD/MM/YYYY): ')
    try:
        fechaDeRealizacion = datetime.strptime(fechaDeRealizacion, "%d/%m/%Y")
    except Exception as ex:
        print(f"fecha no valida:  {ex}")
        return 
    except ValueError:
        print("fecha no valida.")
        return  
    tipoExperimento = input('ingrese el tipo de experimento que desea agregar(Qumica, fisica o biologia): ')  
    resultadosExperimento = list(map(float,input('ingrese los resultados obtenidos del experimento, separando cada resultado con coma (,):').split(",")))
    listaExperimentos.append([nombreExperimento, fechaDeRealizacion, tipoExperimento, resultadosExperimento])
    print("\x1b[1;32m"+"Experimento agregado con exito....")
    print() 
  
def visualizarExperimentos(listaExperimentos):   
    #funsion para ver todos los experimentos agregados   
    print("\x1b[1;35m"+"Lista de experimento")
    print("\x1b[1;37m") 
    if not listaExperimentos:
        print("no hay experimentos agregados")
        return            
    for i, experimento in enumerate(listaExperimentos):
        print(f"{i + 1}.{experimento[0]} - {experimento[1]} - {experimento[2]} - {experimento[3]} \n")

def eliminarExperimento(listaExperimentos):
    #funsion que permite al usuario eliminar un experimento
    if not listaExperimentos:
        print("\x1b[1;31m"+"No hay experimentos agregados") 
        return    
    print(visualizarExperimentos(listaExperimentos))        
    indiceExperimento = int(input("\x1b[1;34m"+"Digite el numero del experimento que desea eliminar: ")) - 1
    if 0 <= indiceExperimento < len(listaExperimentos):
        try:                        
            listaExperimentos.pop(indiceExperimento) 
            print(visualizarExperimentos(listaExperimentos))
        except ValueError:
            print("no existe experimento")
            return        

def calcularEstadisticas(listaExperimentos):
    #funsion la cual calcula los datos de uno de los experimentos agregados
    if not listaExperimentos:
        print("\x1b[1;31m"+"No hay experimentos agregados") 
        return
    print(visualizarExperimentos(listaExperimentos))    
    print("digite 0 para volver al menu..")
    index = int(input("ingrese el numero del experimento: ")) - 1
    if(0 <= index < len(listaExperimentos)):
        resultados = listaExperimentos[index][3]
        promedio = sum(resultados)/len(resultados)
        maximo = max(resultados)
        minimo = min(resultados)
        print(f"estadisticas del experimento {listaExperimentos[index][0]}")
        print(f"promedio: {promedio}")
        print(f"maximo: {maximo}")
        print(f"minimo: {minimo}")
    elif index + 1 == 0:
        print("gracias..")
        mostrarMenu()
    else:
        print("obcion invalida..")    

def compararExperimento(listaExperimentos):
    #funsion que permite comparar los datos de dos o mas experimentos agregados 
    if not listaExperimentos:
        print("no hay experimentos agregados")
        return   
    visualizarExperimentos(listaExperimentos)
    indices = list(map(int, input("ingrese los indices de los experimentos que desesa comparar separados  por comas: ").split(",")))
    resultados_comparacion = []
    for index in indices:
        if(1 <= index <= len(listaExperimentos)):
            promedio = sum(listaExperimentos[index - 1][3]) / len(listaExperimentos[index-1 ][3])
            resultados_comparacion.append((index,promedio))
    else:
        print(f"indice {index} invalido")
        resultados_comparacion.sort(key=lambda x: x[1])
        print("resultados comparados")
    for index, promedio in resultados_comparacion:
        print(f"{index}.{listaExperimentos[index-1][0]} - {promedio:.2f}")   
    pass

def generarInforme(listaExperimentos):
    #funsion que permite al usuario generar un informe(.txt) con todos los datos y experimentos agregados 
    if not listaExperimentos:
        print("\x1b[1;31m"+"No hay experimentos agregados") 
        return
    with open('informe_resultados_experimento.txt','w') as archivo:
        for experimento in listaExperimentos:
            archivo.write(f"Nombre: {experimento[0]}\n")
            archivo.write(f"Fecha de realizacion: {experimento[1]}\n")
            archivo.write(f"Tipos de experimento: {experimento[2]}\n")
            archivo.write(f"resultados del experimento: {experimento[3]}\n")
            archivo.write("\n")
    print("el informe solicitado con los analizis se a generado correctamente como 'informe_resultados_experimento.txt")            

def mostrarMenu():
    ##funsion menu
    while True:
        print("\x1b[1;35m"+"   =====MENU PRINCIPAL==GESTION DE EXPERIMENTO=====") 
        print("\x1b[1;35m"+"1."+ "\x1b[1;37m "+"Agregar experimento")  
        print("\x1b[1;35m"+"2."+ "\x1b[1;37m "+"Visualizar experimento") 
        print("\x1b[1;35m"+"3."+ "\x1b[1;37m "+"Eliminar experimento") 
        print("\x1b[1;35m"+"      ====Analisis de datos====      ") 
        print("\x1b[1;35m"+"4."+ "\x1b[1;37m "+"Calcular estadisticas")
        print("\x1b[1;35m"+"5."+ "\x1b[1;37m "+"Comparar experimento") 
        print("\x1b[1;35m"+"       ===Informes=== ")
        print("\x1b[1;35m"+"6."+ "\x1b[1;37m "+"Generar informe") 
        print("\x1b[1;35m"+"7."+ "\x1b[1;37m "+"Salir") 
        print("-------------------------------------------------") 

        opcion = int(input("Seleccione un opcion:"))
        if opcion == 1:
            agregarExperimento(listaExperimentos)
        elif opcion == 2:
            visualizarExperimentos(listaExperimentos)
        elif opcion == 3:
            eliminarExperimento(listaExperimentos)
        elif opcion == 4:
            calcularEstadisticas(listaExperimentos)
        elif opcion == 5:
            compararExperimento(listaExperimentos)
        elif opcion == 6:
            generarInforme(listaExperimentos)
        elif opcion == 7:
            print("\x1b[1;31m"+"Has salido del programa") 
            break
        else:
            print("\n¡Opción no valida!. \n ")   
            
if __name__ == "__main__":
    mostrarMenu()

