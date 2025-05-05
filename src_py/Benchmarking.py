import random
import time

class Benchmarking:
#--------------------------------------------------------------------------------------------------------------
    def __init__(self):
        print("\n-----Benchmarking funcionando-----")
#--------------------------------------------------------------------------------------------------------------
    def medir_tiempo(self, funcion, array):     # Cree un metodo que mide el tiempo de una manera percisa
        inicio = time.perf_counter()            # Se usa con la libreria "time"
        funcion(array)
        fin = time.perf_counter()
        return fin - inicio
#--------------------------------------------------------------------------------------------------------------
    def build_arreglo(self, tamanios):          # Cree un metodo que crea el arreglo y en este caso
        arreglo = []                            # agrega nuevos caracteres al arreglo
        arreglo_anterior = []   
        
        for tam in tamanios:
            faltan = tam - len(arreglo_anterior)    # Esta linea se encarga de ver cuantos elementos
            nuevos = []                             # ahora necesita

            for _ in range(faltan):
                nuevos.append(random.randint(1, 100000))
                # Aqui creo nuevos caracteres para AGREGAR al arreglo base

            arreglo_actual = arreglo_anterior + nuevos  # Aqui creo un nuevo arreglo con los antiguos
                                                        # caracteres y los nuevos

            arreglo.append(arreglo_actual)
            # Aqui uno los arreglos asi para no cambiar los valores principales

            arreglo_anterior = arreglo_actual
            # Aqui guardo los caracteres actuales para usarlos de nuevo 
            # a la siguiente vuelta como amtiguaos caracteres
        
        return arreglo
