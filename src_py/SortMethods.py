class SortMethods:
#--------------------------------------------------------------------------------------------------------------
    def sort_bubble(self, array):       # Metodo de ordenamiento Burbuja
        arreglo = array.copy()
        tam = len(arreglo)

        for i in range(tam):

            for j in range(0, tam - i - 1):

                if arreglo[j] > arreglo[j + 1]:

                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

        return arreglo
#--------------------------------------------------------------------------------------------------------------
    def sort_burbuja_optimized(self,array): # Metodo de ordenamiento Burbuja mejorado
        arreglo = array.copy()
        tam = len(arreglo)

        for i in range(tam):

            intercambio = False

            for j in range(0, tam - i - 1):

                if arreglo[j] > arreglo[j + 1]:

                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                    intercambio = True

            if not intercambio:
                
                break

        return arreglo
#--------------------------------------------------------------------------------------------------------------
    def sort_insertion(self,array):     # Metodo de ordenamiento Incersion
        arreglo = array.copy()
        tam = len(arreglo)

        for i in range(1, tam):

            key = arreglo[i]
            j = i - 1

            while j >= 0 and arreglo[j] > key:
                arreglo[j + 1] = arreglo[j]
                j -= 1

            arreglo[j + 1] = key

        return arreglo
#--------------------------------------------------------------------------------------------------------------
    def sort_seleccion(self, array):    # Metodo de ordenamiento seleccion
        arreglo = array.copy()
        tam = len(arreglo)

        for i in range(tam - 1):

            indiceMinimo = i

            for j in range(i + 1, tam):

                if arreglo[j] < arreglo[indiceMinimo]:
                    indiceMinimo = j
        
            arreglo[i], arreglo[indiceMinimo] = arreglo[indiceMinimo], arreglo[i]

        return arreglo
#--------------------------------------------------------------------------------------------------------------
    def sell_sort(self,array):          # Metodo de ordenamiento Shell
        arreglo = array.copy()
        tam = len(arreglo)

        gap = tam // 2

        while gap > 0:

            for i in range(gap, tam):
                temp = arreglo[i]
                j = i

                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp

            gap //= 2

        return arreglo
    