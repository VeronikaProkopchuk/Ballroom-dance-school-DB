from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    
)
from .model import SalasModel

class WindowSalas(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Salas")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.salasModel = SalasModel()
        self.setupUI()

    def setupUI(self):
        # Crear el widget de la tabla
        self.table = QTableView()
        self.table.setModel(self.salasModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.resizeColumnsToContents()
        # Crear botones
        self.addButton = QPushButton("Añadir")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Eliminar")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Borrar Todo")
        self.clearAllButton.clicked.connect(self.clearContacts)
        # Diseñar la GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.salasModel.addSala(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteContact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Cuidado!",
            "¿Seguro que quiere eliminar la sala?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )

        if messageBox == QMessageBox.StandardButton.Ok:
            self.salasModel.deleteSala(row)

    def clearContacts(self):
        messageBox = QMessageBox.warning(
            self,
            "Cuidado!",
            "Seguro que quiere eliminar todas las salas?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )

        if messageBox == QMessageBox.StandardButton.Ok:
            self.salasModel.clearSalas()

class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Añadir")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        # Crear objetos para entrada de datos
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Nombre")
        self.superficieField = QLineEdit()
        self.superficieField.setObjectName("Superficie")

        # Configurar los campos
        layout = QFormLayout()
        layout.addRow("Nombre:", self.nameField)
        layout.addRow("Superficie:", self.superficieField)
        self.layout.addLayout(layout)
        # Añadir y conectar botones
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        self.data = []
        for field in (self.nameField, self.superficieField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Debe introducir un {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()