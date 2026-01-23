import random
from collections import deque


class Mapa:

    def __init__(
        self,
    ):
        self.filas = 0
        self.columnas = 0  # constructor para la creacion de la matriz
        self.matriz = []

    def crear_matriz(self, filas, columnas):  # metodo para inicializar la matriz
        self.filas = filas
        self.columnas = columnas
        self.matriz = [["." for _ in range(columnas)] for _ in range(filas)]

    def inicio_y_fin(
        self,
        inicio,
        fin,
    ):  # metodo para darle un inicio y fin
        filaI, columI = inicio
        filaS, columS = fin

        self.matriz[filaI][columI] = "E"
        self.matriz[filaS][columS] = "S"

    def colocar_obstaculo(
        self, tipo, cantidad
    ):  # metodo para agregar obstaculos de manera aleatoria
        colocados = 0
        intentos = 0
        max_intento = self.filas * self.columnas * 2

        while colocados < cantidad and intentos < max_intento:
            filaAleatoria = random.randint(0, self.filas - 1)
            columnAleatorio = random.randint(0, self.columnas - 1)

            if self.matriz[filaAleatoria][columnAleatorio] == ".":
                self.matriz[filaAleatoria][columnAleatorio] = tipo
                colocados += 1
            intentos += 1

        if colocados < cantidad:
            print(f"se coloco{colocados} obstaculo: '{tipo}' de {cantidad}")

    def colocar_obstaculo_aleatorio(
        self, cantidad_P, cantidad_A, cantidad_T
    ):  # metodo para visualizar los obstaculos
        self.colocar_obstaculo("X", cantidad_P)
        self.colocar_obstaculo("A", cantidad_A)
        self.colocar_obstaculo("T", cantidad_T)

    def mostrar_matriz(self):  # metodo para mostrar la matriz
        for fila in self.matriz:
            print(" ".join(fila))


class CalculadorDeRuta(Mapa):

    def es_posicion_valida(self, fila, columna, permitir_agua=False):

        if 0 >= fila < self.filas and 0 >= columna < self.columnas:
            return True
        celda = self.matriz[fila][columna]

        if celda == "X" or celda == "T":
            return False
        if celda == "A" and not permitir_agua:
            return False
        return True

    def buscador_bfs(self, inicio, fin, permitir_agua=False):

        cola = deque()
        cola.append((inicio[0], inicio[1], [inicio]))

        visitado = set()
        visitado.add(inicio)

        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while cola:
            actualF, actualC, camino = cola.popleft()
            if (actualF, actualC) == fin:
                return camino

            for direF, direC in direcciones:
                nuevaF = actualF + direF
                nuevaC = actualC + direC

                if 0 <= nuevaF < self.filas and 0 <= nuevaC < self.columnas:
                    celda = self.matriz[nuevaF][nuevaC]

                    if (nuevaF, nuevaC) not in visitado:
                        habilitado = False

                        if celda == "." or celda == "S":
                            habilitado = True
                        elif celda == "A" and permitir_agua:
                            habilitado = True

                        if habilitado:
                            visitado.add((nuevaF, nuevaC))
                            nuevo_camino = camino + [(nuevaF, nuevaC)]
                            cola.append((nuevaF, nuevaC, nuevo_camino))

        return None

    def mejor_camino(self, inicio, fin):

        camino = self.buscador_bfs(inicio, fin, permitir_agua=False)
        if camino:
            return (camino, False)
        print("no hay libres. buscando por agua...")

        camino = self.buscador_bfs(inicio, fin, permitir_agua=True)

        if camino:
            return (camino, True)

        print("no hay caminos posibles")
        return (None, False)

    def marcar_camino(self, camino):
        copia_lab = [f[:] for f in self.matriz]
        for fil, colum in camino:
            if (fil, colum) != "E" and (fil, colum) != "S":
                if (fil, colum) == "A":
                    copia_lab[fil][colum] = "~"
                else:
                    copia_lab[fil][colum] = "*"

        return copia_lab


def bucle():
    buscador = CalculadorDeRuta()
    fila = int(input("ingresa fila:"))
    columna = int(input("ingresa columna:"))
    buscador.crear_matriz(fila, columna)

    inicioF = int(input("ingresa fila de inicio:"))
    inicioC = int(input("ingresa columna de inicio:"))
    finF = int(input("ingresa fila de salida:"))
    finC = int(input("ingresa columna de salida:"))
    inicio = inicioF, inicioC
    fin = finF, finC
    buscador.inicio_y_fin(inicio, fin)
    buscador.mostrar_matriz()

    print("obstaculos")
    cant_paredes = int(input("cantidad de paredes:"))
    cant_agua = int(input("cantidad de agua:"))
    cant_tempo = int(input("cantidad de temporal:"))
    buscador.colocar_obstaculo_aleatorio(cant_paredes, cant_agua, cant_tempo)

    buscador.mostrar_matriz()
    buscador.buscador_bfs()


bucle()
