import time

class Lote:
    def __init__(self, capacidad_maxima, simulador, interfaz):
        self.capacidad_maxima = capacidad_maxima
        self.procesos = []
        self.simulador = simulador
        self.interfaz = interfaz

    def __str__(self):
        return "".join(
            str(proceso)+"\n" for proceso in self.procesos
        )

    def agregar_proceso(self, proceso):
        if len(self.procesos) < self.capacidad_maxima:
            self.procesos.append(proceso)
            return True
        return False

    def ejecutar_lote(self):
        while self.procesos:
            proceso_en_ejecucion = self.procesos.pop(0)
            self.interfaz.actualizar_tabla_proceso_en_ejecucion(proceso_en_ejecucion)
            while proceso_en_ejecucion.tiempo_restante > 0:
                
                if self.interfaz.tecla_precionada == 'i':
                    self.interrumpir_proceso_entrada_salida(proceso_en_ejecucion)
                    break
                elif self.interfaz.tecla_precionada == 'e':
                    self.terminar_proceso_error(proceso_en_ejecucion)
                    break
                elif self.interfaz.tecla_precionada == 'p':
                    self.pausar_proceso()
                elif self.interfaz.tecla_precionada == 'c':
                    self.continuar_proceso()
                else:
                    self.simulador.reloj_global += 1
                    proceso_en_ejecucion.actualizar_tiempo()
                    time.sleep(1)

                    self.interfaz.actualizar_tiempos_proceso(proceso_en_ejecucion)
                    self.interfaz.actualizar_reloj()
            
            if self.interfaz.tecla_precionada == 'i':
                self.interfaz.reiniciar_tecla_precionada()
            else:
                self.simulador.procesos_terminados.append(proceso_en_ejecucion)
                self.interfaz.actualizar_tabla_procesos_terminados()

    def interrumpir_proceso_entrada_salida(self, proceso):
        proceso.actualizar_tiempo_maximo()
        self.agregar_proceso(proceso)
        self.interfaz.actualizar_tabla_lote_en_ejecucion(self)

    def terminar_proceso_error(self, proceso):
        proceso.actualizar_error()
        self.interfaz.reiniciar_tecla_precionada()

    def pausar_proceso(self):
        pass

    def continuar_proceso(self):
        self.interfaz.reiniciar_tecla_precionada()