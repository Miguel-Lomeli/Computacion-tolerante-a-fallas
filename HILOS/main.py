import sys
from PySide2.QtWidgets import QApplication
from Interfaz import Interfaz

app = QApplication()
window = Interfaz()
window.show()

sys.exit(app.exec_())