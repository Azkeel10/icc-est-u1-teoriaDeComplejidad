import Benchmarking as bm
import SortMethods as sm
import matplotlib.pyplot as plt
import datetime

if __name__ == "__main__":
    print("\n----------Programa Funciona----------")
#----------------------------------------------------------------------------------
    bench = bm.Benchmarking()
    metodosO = sm.SortMethods()
#----------------------------------------------------------------------------------
    tamaños = [5000, 10000, 30000, 50000, 100000]   # Creo los tamaños q voy a usar 
    resul = []
#----------------------------------------------------------------------------------
    arreglo_base = bench.build_arreglo(tamaños)     # Creo arreglos con las mismas variables al principio 
                                                    # y agrego nuevos variables
#----------------------------------------------------------------------------------
    for i in range(len(tamaños)):
        tam = tamaños[i]
        arreglo = arreglo_base[i]
#----------------------------------------------------------------------------------
        metodos_dic = {             # Creo un diccionario que se va a ir actualizando con cada tamaño
            "Metodo Burbuja": metodosO.sort_bubble,
            "Metodo Burbuja Mejorado": metodosO.sort_burbuja_optimized,
            "Metodo Insercion": metodosO.sort_insertion,
            "Metodo Seleccion": metodosO.sort_seleccion,
            "Metodo Shell": metodosO.sell_sort
        }
#----------------------------------------------------------------------------------
        for name, fun_metodo in metodos_dic.items():    #Busca los tiempos,nombre y el tam de cada metodo
            tiempo_resul = bench.medir_tiempo(fun_metodo, arreglo)
            resul.append((tam, name, tiempo_resul))
#----------------------------------------------------------------------------------
    for tam, name, tiempo_resul in resul:   #Se impime los distintos tiempos,nombre y tamaños
        print(f"Tamaño: {tam}, Algoritmo: {name}, Tiempo: {tiempo_resul:.6f} segundos")
        print()
#----------------------------------------------------------------------------------
    ## Desde aqui es para crear la grafica

    fecha_hora_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    titulo_general = f"Jaime Loja y Ivanna Nievecela - {fecha_hora_actual}"
#----------------------------------------------------------------------------------
    tiempos_by_metodos = {
        "Metodo Burbuja": [],
        "Metodo Burbuja Mejorado": [],
        "Metodo Insercion": [],
        "Metodo Seleccion": [],
        "Metodo Shell": []
    }
#----------------------------------------------------------------------------------
    for tam, nombre, tiempo in resul:
        tiempos_by_metodos[nombre].append(tiempo)
#----------------------------------------------------------------------------------
    plt.figure(figsize=(10, 6))
#----------------------------------------------------------------------------------
    for nombre, tiempos in tiempos_by_metodos.items():
        plt.plot(tamaños, tiempos, label=nombre, marker="o")
#----------------------------------------------------------------------------------
    plt.title("Comparativa de tiempos para cada metodo de ordenamiento")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.legend()
    plt.grid(True)
#----------------------------------------------------------------------------------
    plt.suptitle(titulo_general, fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()