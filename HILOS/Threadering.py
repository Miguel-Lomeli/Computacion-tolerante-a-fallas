from PySide2.QtCore import QThread
from PySide2.QtCore import Signal
from PySide2.QtCore import Slot

import keyboard

class SimulacionThread(QThread):
    finalizada = Signal()

    def __init__(self, simulador):
        super().__init__()
        self.simulador = simulador

    def run(self):
        self.simulador.ejecutar_lotes()
        self.finalizada.emit()

class TecladoThread(QThread):
    tecla_presionada = Signal(str)
    finalizada = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        keyboard.on_press(self.manejar_tecla_presionada)
        self.exec_()
        """self.detener = False
        while not self.detener:
            keyboard.on_press(self.manejar_tecla_presionada)"""

    def manejar_tecla_presionada(self, event):
        key = event.name
        if key in ('i', 'e', 'p', 'c'):
            self.tecla_presionada.emit(key)

    @Slot()
    def detener(self):
        self.quit()