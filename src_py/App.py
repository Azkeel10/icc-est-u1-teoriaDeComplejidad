import Benchmarking as bm
import SortMethods as sm

if __name__ == "__main__":
    print("\n----------Programa Funciona----------")

    bench = bm.Benchmarking()
    metodosO = sm.SortMethods()

    tamaños = [5000,10000,30000,50000,100000]  # Creo los tamaños q voy a usar 
    resul = []

    arreglo_base = bench.build_arreglo(tamaños)    # Creo arreglos con las mismas variables al principio 
                                                    # y agrego nuevos variables

    for i in range(len(tamaños)):

        tam = tamaños[i]
        arreglo = arreglo_base[i]

        metodos_dic  = {        # Creo un diccionario que se va a ir actualizando con cada tamaño
            "Metodo Burbuja" : metodosO.sort_bubble,
            "Metodo Burbuja Mejorado" : metodosO.sort_burbuja_optimized,
            "Metodo Insercion" : metodosO.sort_insertion,
            "Metodo Seleccion" : metodosO.sort_seleccion,
            "Metodo Shell" : metodosO.sell_sort
        }    

        for name, fun_metodo in metodos_dic.items():

            tiempo_resul = bench.medir_tiempo(fun_metodo,arreglo)
            tupla_resul = (tam,name,tiempo_resul)
            resul.append(tupla_resul)

    for tam, name, tiempo_resul in resul:
        print(f"Tamaño: {tam}, Algoritmo: {name}, Tiempo: {tiempo_resul:.6f} segundos")
        print()

