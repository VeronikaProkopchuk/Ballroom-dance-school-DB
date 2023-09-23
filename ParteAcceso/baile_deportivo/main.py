import sys

from PyQt6.QtWidgets import QApplication
from .database import createConnection
from .views_intro import MainWindowIntro

def main():
    # Crear la aplicación
    app = QApplication(sys.argv)
    # Conectar con la base de datos
    if not createConnection("baile_deportivo.sqlite"):
        sys.exit(1)

    #abrir la ventana de menu
    win = MainWindowIntro()
    win.show()

    
    # Ejecutar el bucle de eventos
    sys.exit(app.exec())