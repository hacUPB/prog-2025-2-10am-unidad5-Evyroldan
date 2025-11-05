homicidios = []
import os
import csv
import matplotlib.pyplot as plt


def c_palabras_caracteres():
    if not os.path.exists("homicolombia.txt"):
        print("No se encontró el archivo homicolombia.txt.")
        return

    with open("homicolombia.txt", "r") as archivo:
        contenido = archivo.read()

    palabras = contenido.split()
    n_palabras = len(palabras)
    n_caracteres_con_espacios = len(contenido)
    n_caracteres_sin_espacios = len(contenido.replace(" ", ""))

    print("\n Resultados (homicolombia.txt):")
    print("Número de palabras:", n_palabras)
    print("Número de caracteres (con espacios):", n_caracteres_con_espacios)
    print("Número de caracteres (sin espacios):", n_caracteres_sin_espacios)

def reemplazar_palabra():
    if not os.path.exists("homicolombia.txt"):
        print("No se encontró el archivo homicolombia.txt.")
        return

    palabra_buscar = input("Ingresa la palabra que deseas reemplazar: ")
    palabra_nueva = input("Ingresa la nueva palabra: ")

    with open("homicolombia.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    if palabra_buscar not in contenido:
        print(f"La palabra '{palabra_buscar}' no se encontró en el texto.")
        return

    nuevo_contenido = contenido.replace(palabra_buscar, palabra_nueva)
    cantidad = contenido.count(palabra_buscar)

    with open("homicolombia.txt", "w", encoding="utf-8") as archivo:
        archivo.write(nuevo_contenido)

    print(f"\n Se reemplazaron {cantidad} apariciones de '{palabra_buscar}' por '{palabra_nueva}'.")
    print("Los cambios se guardaron en el archivo homicolombia.txt.")

def histograma_vocales():
    if not os.path.exists("homicolombia.txt"):
        print("No se encontró el archivo homicolombia.txt.")
        return

    with open("homicolombia.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    contenido = contenido.lower()

    vocales = ['a', 'e', 'i', 'o', 'u']
    conteo = []

    for v in vocales:
        cantidad = contenido.count(v)
        conteo.append(cantidad)

    print("\n Cantidad de vocales en el archivo:")
    for i in range(len(vocales)):
        print(vocales[i], ":", conteo[i])

    # Gráfico histograma
    plt.bar(vocales, conteo)
    plt.title("Histograma de Vocales - homicolombia.txt")
    plt.xlabel("Vocales")
    plt.ylabel("Cantidad de ocurrencias")
    plt.show()


# submenú del archivo .txt
def submenu_txt():
    while True:
        print("\n Submenú del archivo homicolombia.txt ")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra ")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")

        opcion_txt = input("Selecciona una opción: ")

        if opcion_txt == "1":
            c_palabras_caracteres()
        elif opcion_txt == "2":
          reemplazar_palabra()

        elif opcion_txt == "3":
         histograma_vocales()

        elif opcion_txt == "4":
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")



def mostrar_15_filas():
    if not os.path.exists("homicidios.csv"):
        print(" No se encontró el archivo homicidios.csv.")
        return

    with open("homicidios.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        filas = []
        for i, fila in enumerate(lector):
            if i < 15:
                filas.append(fila)
            else:
                break

    print("\n Primeras 15 filas de homicidios.csv:")
    for fila in filas:
        print(fila)
def calcular_estadisticas():
    if not os.path.exists("homicidios.csv"):
        print("No se encontró el archivo homicidios.csv.")
        return

    with open("homicidios.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  
        
        datos = []
        for fila in lector:
            
            valor = fila[-1].replace('"', '')
            if valor.isdigit():
                datos.append(int(valor))

    if len(datos) == 0:
        print("No hay datos numéricos válidos.")
        return

    
    suma = 0
    for d in datos:
        suma += d

    promedio = suma / len(datos)

    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]

    # Desviación estándar 
    suma_dif = 0
    for d in datos:
        suma_dif += (d - promedio) ** 2
    desviacion = (suma_dif / len(datos)) ** 0.5

    maximo = max(datos)
    minimo = min(datos)

    print("\n Estadísticas de la cantidad:")
    print("Cantidad de datos:", len(datos))
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Desviación estándar:", desviacion)
    print("Valor máximo:", maximo)
    print("Valor mínimo:", minimo)

def cargar_csv():
    global homicidios
    homicidios = []

    if not os.path.exists("homicidios.csv"):
        print(" No se encontró homicidios.csv")
        return
    
    with open("homicidios.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # nombres a minúscula de las columnas
            fila = {k.lower(): v for k,v in fila.items()}
            homicidios.append(fila)

    print("\n Archivo homicidios.csv cargado correctamente.\n")


# Submenú del archivo .csv
def submenu_csv():
    while True:
        print("\n Submenú del archivo homicidios.csv")
        print("1. Cargar archivo homicidios.csv")
        print("2. Mostrar las 15 primeras filas")
        print("3. Calcular estadísticas ")
        print("4. Graficar datos")
        print("5. Volver al menú principal")

        opcion_csv = input("Selecciona una opción: ")

        if opcion_csv == "1":
            cargar_csv()
        elif opcion_csv == "2":
            mostrar_15_filas()
        elif opcion_csv == "3":
            calcular_estadisticas()
        elif opcion_csv == "4":
            if len(homicidios) == 0:
                print("Primero debes cargar el archivo (opción 1)")
            else:
                columna = input("Ingresa el nombre de la columna a graficar (por ejemplo: cantidad): ").lower()

                valores = []
                for fila in homicidios:
                    if columna in fila:
                        v = fila[columna].replace('"', '')
                        if v.isdigit():
                            valores.append(int(v))   

                if len(valores) == 0:
                    print("La columna no contiene datos numéricos válidos.")
                else:
                    # Gráfica de dispersión
                    plt.scatter(range(len(valores)), valores)
                    plt.title(f"Gráfico de Dispersión - {columna}")
                    plt.xlabel("Índice de fila")
                    plt.ylabel(columna)
                    plt.show()

                    # Gráfico de barras
                    plt.bar(range(len(valores)), valores)
                    plt.title(f"Gráfico de Barras - {columna}")
                    plt.xlabel("Índice de fila")
                    plt.ylabel(columna)
                    plt.show()

        elif opcion_csv == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Función que lista los archivos en la carpeta
def listar_archivos():
    print("\n Archivos en la carpeta actual:")
    archivos = os.listdir()
    for archivo in archivos:
        print(" -", archivo)


# Menú
def main():
    while True:
        print("\n Menú principal")
        print("1. Listar archivos en la carpeta actual")
        print("2. Procesar archivo de texto (homicolombia.txt)")
        print("3. Procesar archivo separado por comas (homicidios.csv)")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print(" Programa finalizado.")
            break
        else:
            print(" Opción no válida. Intenta de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    main()

