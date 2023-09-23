import sys

from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt

from .views_entrenadores import WindowEntrenadores
from .views_deportistas import WindowDeportistas
from .views_salas import WindowSalas
from .views_lecciones import WindowLecciones

class MainWindowIntro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Estudio de Baile Deportivo")
        self.resize(600, 300)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout  = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()

        self.windowEntrenadores = WindowEntrenadores()
        self.windowDeportistas = WindowDeportistas()
        self.windowLecciones = WindowLecciones()
        self.windowSalas = WindowSalas()

    def setupUI(self):
        self.label = QLabel("Selecciona la tabla")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.adjustSize()
        
        self.entrenadoresButton = QPushButton("Tabla Entrenadores")
        self.entrenadoresButton.clicked.connect(self.openEntrenadores)

        self.deportistasButton = QPushButton("Tabla Deportistas")
        self.deportistasButton.clicked.connect(self.openDeportistas)   
             
        self.leccionesButton = QPushButton("Tabla Lecciones")
        self.leccionesButton.clicked.connect(self.openLecciones)
        
        self.salasButton = QPushButton("Tabla Salas")
        self.salasButton.clicked.connect(self.openSalas)
        

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entrenadoresButton)
        layout.addWidget(self.deportistasButton)
        layout.addWidget(self.leccionesButton)
        layout.addWidget(self.salasButton)
        self.layout.addLayout(layout)

    def openEntrenadores(self):
        self.windowEntrenadores.show()

    def openDeportistas(self):
        self.windowDeportistas.show()

    def openLecciones(self):
        self.windowLecciones.show()

    def openSalas(self):
        self.windowSalas.show()
