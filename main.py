
ListaExperimentos = [
    "experimento 1", "16/11/2024", "quimica", [5,3,4,5,6,44],
    "experimento 2", "24/11/2024", "fisica", [8,9,4,6,7],
    "experimento 3", "25/11/2024", "biologia", [8,9,4,6,7],
]

from datetime import datetime
import statistics

class Experimento:

    #metodo constructor 
    def __init__(self, nombreExperimento, fechaDeRealizacion, tipoExperimento, resultadosExperimento):
        self.nombreExperimento = nombreExperimento
        self.fechaDeRealizacion = fechaDeRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultadosExperimento = resultadosExperimento
   ## funcion agregar experimento 
def agregarExperimento(listaExperimentos):
    nombreExperimento = input('\npor favor ingrese el nombre del experimento:  ')
    fechaDeRealizacion = input('ingresar la fecha de realizacion del proyecto (DD/MM/YYYY): ')
    try:
        fechaDeRealizacion = datetime.strptime(fechaDeRealizacion, "%d/%m/%Y ")
    except Exception as ex:
        print(f"fecha no valida:  {ex}")
        return 
    
    
    tipoExperimento = input('ingrese el tipo de experimento que desea agregar: ')
    resultadosExperimento = input('ingrese los resultados obtenidos del experimento, separando cada resultado con coma (,):')

    try:
        resultadosExperimento(list(map(float, resultadosExperimento.split(","))))
    except ValueError:
        print("datos no validos...")
        return
    
## creacion de un objeto para almacenar la informacion
    experimento = Experimento(nombreExperimento, fechaDeRealizacion, tipoExperimento, resultadosExperimento)
    listaExperimentos.append(experimento)
    print("Experimento agregado con exito...")

#permite eliminar un experimento,             xxxxxxxxxxxxxxxxx   
def eliminarExperimento(listaExperimentos):
    ListaExperimentos.remove(Experimento)
    print("se elimino correctamente el experimento")
    visualizarExperimentos(listaExperimentos)

    #pass

## funsion para ver todos los experimentos agregados
def visualizarExperimentos(listaExperimentos):
    # print("Lista de experimentos")
    # if not listaExperimentos:
    #     print("no hay experimentos agregados")
    #     return
            
    for i, experimento in enumerate(listaExperimentos):
        print(f"{i}.{experimento[0]} - {experimento[1]} - {experimento[2]} - {experimento[3]} ")

    
    for i,experimento in enumerate(listaExperimentos, start=1):
        print(f"\nexperimento {i}")
        print(f"nombre: {experimento.nombreExperimento}")
        print(f"fecha limite: {experimento.fechaDeRealizacion.strftime('%d, %m, %Y')}")
        print(f"categoria: {experimento.tipoExperimento}")
        print(f"horas dedicadas: {experimento.resultadosExperimento}")
        
#calcular estadisticasbasicas, promedio maximos y minimos de un experimento, requiere el uso de funcion agrear experimento prioridad 2
## analisis de resultados
def calcularEstadisticas(listaExperimentos):
    #1visualizarExperimentos()
    print("listado de experimentos")
    index = int(input("ingrese el numero del experimento: ")) 
    if(0 <= index < len(listaExperimentos)):
        resultados = listaExperimentos[index][3]
        promedio = sum(resultados)/len(resultados)
        maximo = max(resultados)
        minimo = (resultados)
        print(f"estadisticas del experimento {listaExperimentos[index][0]}")
        print(f"promedio: {promedio}")
        print(f"maximo: {maximo}")
        print(f"minimo: {minimo}")

    #if not listaExperimentos:
    #   print("no hay experimentos agregados")
        #  return  
    
    # for experimento in listaExperimentos:
    #     promedio = statistics.mean(experimento.resultadosExperimento)
    #     maximo = max(experimento.resultadosExperimento)
    #     minimo = min(experimento.resultadosExperimentos)
    #     print(f'\nestadisticas de {experimento.nombreExperimento}')
    #     print(f"promedio de los resultados: {promedio}")
    #     print(f"puntaje maximo de los resultados{maximo} ")
    #     print(f"puntaje minimo de los resultados{minimo}")

def compararExperimento(listaExperimentos):   
    visualizarExperimentos()
    indices = list(map(int, input("ingrese los indices de los equipos que desesa comparar separados  por comas: ").split(","))) 

    resultados_comparacion = []   
    for index in indices:
        if(0 <= index < len(listaExperimentos)):
            promedio = sum(ListaExperimentos[index][3]) / len(ListaExperimentos[index][3])
            resultados_comparacion.append(promedio)
    else:
        print(f"indice {index} invalido")
    resultados_comparacion.sort(key=lambda x: x[1])
    print("resultados comparados")
    for index, promedio in resultados_comparacion:
        print(f"{index +1}.{ListaExperimentos[index][0]} - {promedio}") 
        


    #compara 2 o mas experimentos para determinar los mejores o peores resultados, requiere el uso de calcular estadistica dificula 2
    #parar comparar requiere de visualizar los experimentos
    #pass

#generar un informe resumido de los experimentos y sus estadisticas
def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("no hay experimentos agregados")
        return

    with open('informe_resultados_experimento.txt','w') as archivo:
        for experimento in listaExperimentos:
            archivo.write(f"Nombre: {experimento.nombreExperimento}\n")
            archivo.write(f"Fecha de realizacion: {experimento.fechaDeRealizacion}\n")
            archivo.write(f"Tipos de experimento: {experimento.tipoExperimento}\n")
            archivo.write(f"resultados del experimento: {experimento.resultadoExperimento}\n")
            archivo.write("\n")

    print("el informe solicitado con los analizis se a generado correctamente como 'informe_resultados_experimento.txt'")            


#muestra el menu principal del programa
#mejorar el menu 1
#mejorar el informe por que re  quiere el uso de ufnciones y calcular para su uso

def mostrarMenu():
    listaExperimentos = []
    while True:
        print("=====MENU PRINCIPAL==GESTION DE EXPERIMENTO=====")       
        print("1. agregarexperimento")
        print("2. visualizar expeimento")        
        print("3. eliminar expeimento")        
        print("=========Analisis de datos=========")
        print("4.calcular estadisticas")
        print("5.comparar experimentos\n")
        print("=========informes=========")
        print("6.Generar informe")
        print("7. salir\n\n")

        opcion = int(input("seleccione una opcion: "))

        if opcion == 1:
            agregarExperimento(listaExperimentos)
        elif opcion == 2:
            visualizarExperimentos(listaExperimentos)
        elif opcion == 3:
            eliminarExperimento(listaExperimentos)
            print("seleccione el experimento que desea eliminar: ")
        elif opcion == 4:
            calcularEstadisticas(listaExperimentos)
        elif opcion == 5:
            compararExperimento(listaExperimentos)
        elif opcion == 6:
            generarInforme(listaExperimentos)
        elif opcion == 7:
            print("has salido del programas. ")
            break
        else:
            print("\n¡Opción no valida!. \n ")           
#funcion principal controla el flujo general del sistema
#def main():    
#conrola el flujo
#if __name__ == "__main__":
 #mostrarMenu()
mostrarMenu()
    



