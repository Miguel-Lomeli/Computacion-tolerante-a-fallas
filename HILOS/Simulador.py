import random
from Proceso import Proceso
from Lote import Lote

class Simulador:
    def __init__(self, interfaz):
        self.lotes_pendientes = []
        self.procesos_terminados = [] 
        self.reloj_global = 0
        self.total_procesos = 0
        self.capacidad_lote = 3 

        self.interfaz = interfaz

    def __str__(self):
        return "".join(
            str(lote)+"\n" for lote in self.lotes_pendientes
        )

    def crear_proceso_aleatorio(self):
        operacion = random.choice(['+', '-', '*', '/', '%', '^'])
        dato_operacion_1 = random.randint(0, 100)
        dato_operacion_2 = random.randint(0, 100)
        tiempo_maximo = random.randint(7, 18)

        proceso = Proceso(operacion, dato_operacion_1, dato_operacion_2, tiempo_maximo,self.total_procesos+1)
        return proceso

    def agregar_proceso(self, proceso):
        if not self.lotes_pendientes or not self.lotes_pendientes[-1].agregar_proceso(proceso):
            nuevo_lote = Lote(self.capacidad_lote, self, self.interfaz)
            nuevo_lote.agregar_proceso(proceso)
            self.lotes_pendientes.append(nuevo_lote)
            self.interfaz.actualizar_lotes_pendientes(len(self.lotes_pendientes))

        self.total_procesos += 1

    def agregar_procesos(self, numero_procesos):
        for _ in range(numero_procesos):
            self.agregar_proceso(self.crear_proceso_aleatorio())
    
    def ejecutar_lotes(self):
        while self.lotes_pendientes:
            lote_en_ejecucion = self.lotes_pendientes.pop(0)
            self.interfaz.actualizar_tabla_lote_en_ejecucion(lote_en_ejecucion)
            lote_en_ejecucion.ejecutar_lote()

            self.interfaz.actualizar_lotes_pendientes(len(self.lotes_pendientes))