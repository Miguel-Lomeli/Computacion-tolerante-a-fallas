class Proceso:
    def __init__(self, operacion, dato_operacion_1, dato_operacion_2, tiempo_maximo, numero_programa):
        self.operacion = operacion
        self.dato_operacion_1 = dato_operacion_1
        self.dato_operacion_2 = dato_operacion_2
        self.tiempo_maximo = tiempo_maximo
        self.tiempo_restante = self.tiempo_maximo
        self.tiempo_transcurrido = 0
        self.numero_programa = numero_programa
        self.error = False

    def __str__(self):
        return(
            "Numero de Programa: " + str(self.numero_programa) + "\n" +
            "Operación: " + str(self.dato_operacion_1) + " " + self.operacion + " " + str(self.dato_operacion_2) +"\n" +
            "Tiempo Maximo Estimado: " + str(self.tiempo_maximo) + "\n" +
            "------------------------------------"
        )
    
    def validar_operacion(self):
        operaciones_validas = ['+', '-', '*', '/', '%', '^']
        return self.operacion in operaciones_validas

    def validar_tiempo_maximo(self):
        return self.tiempo_maximo > 0
    
    def actualizar_tiempo(self):
        self.tiempo_transcurrido += 1
        self.tiempo_restante -= 1

    def actualizar_tiempo_maximo(self):
        self.tiempo_maximo = self.tiempo_restante
        self.tiempo_transcurrido = 0

    def actualizar_error(self):
        self.error = not self.error

    def realizar_operacion(self):
        if not self.validar_operacion():
            return None
        
        if self.operacion == '+':
            return self.dato_operacion_1 + self.dato_operacion_2
        elif self.operacion == '-':
            return self.dato_operacion_1 - self.dato_operacion_2
        elif self.operacion == '*':
            return self.dato_operacion_1 * self.dato_operacion_2
        elif self.operacion == '/':
            if self.dato_operacion_2 != 0:
                return self.dato_operacion_1 / self.dato_operacion_2
            else:
                self.error = True
                return None
        elif self.operacion == '%':
            if self.dato_operacion_2 != 0:
                return self.dato_operacion_1 % self.dato_operacion_2
            else:
                self.error = True
                return None
        elif self.operacion == '^':
            return self.dato_operacion_1 ** self.dato_operacion_2
