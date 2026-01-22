import random
class Mapa:

    def __init__(self):
        self.filas = 0
        self.columnas = 0
        self.matriz = []

    def crear_matriz(self,filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [["."for _ in range(columnas)]for _ in range(filas)]

    def inicio_y_fin(self,inicio,fin,):
        filaI,columI = inicio
        filaS,columS = fin

        self.matriz[filaI][columI] = "E"
        self.matriz[filaS][columS] = "S"

    def colocar_obstaculo(self,tipo,cantidad):
        colocados = 0
        intentos = 0
        max_intento = self.filas * self.columnas * 2

        while colocados < cantidad and intentos < max_intento:
            filaAleatoria = random.randint(0,self.filas -1)
            columnAleatorio = random.randint(0,self.columnas -1)

            if self.matriz[filaAleatoria][columnAleatorio] == ".":
                self.matriz[filaAleatoria][columnAleatorio] = tipo
                colocados += 1
            intentos += 1

        if colocados < cantidad:
            print(f"se coloco{colocados} obstaculo: '{tipo}' de {cantidad}")
    def colocar_obstaculo_aleatorio(self,cantidad_P,cantidad_A,cantidad_T):
        self.colocar_obstaculo("X",cantidad_P)
        self.colocar_obstaculo("A",cantidad_A)
        self.colocar_obstaculo("T",cantidad_T)

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(" ".join(fila))

def bucle():
    mapa = Mapa()
    fila = int(input("ingresa fila:"))
    columna = int(input("ingresa columna:"))
    mapa.crear_matriz(fila,columna)

    inicioF = int(input("ingresa fila de inicio:"))
    inicioC = int(input("ingresa columna de inicio:"))
    finF =  int(input("ingresa fila de salida:"))
    finC = int(input("ingresa columna de salida:"))
    inicio = inicioF,inicioC
    fin = finF,finC
    mapa.inicio_y_fin(inicio,fin)
    mapa.mostrar_matriz()

    print("obstaculos")
    cant_paredes = int(input("cantidad de paredes:"))
    cant_agua =  int(input("cantidad de agua:"))
    cant_tempo =  int(input("cantidad de temporal:"))
    mapa.colocar_obstaculo_aleatorio(cant_paredes,cant_agua,cant_tempo)

    mapa.mostrar_matriz()
bucle()