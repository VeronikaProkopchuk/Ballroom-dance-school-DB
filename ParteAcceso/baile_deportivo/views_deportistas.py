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
from .model import DeportistasModel

class WindowDeportistas(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Deportistas")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.deportistasModel = DeportistasModel()
        self.setupUI()

    def setupUI(self):
        # Crear el widget de la tabla
        self.table = QTableView()
        self.table.setModel(self.deportistasModel.model)
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
            self.deportistasModel.addDeportista(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteContact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Cuidado!",
            "¿Seguro que quiere eliminar el deportista?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )

        if messageBox == QMessageBox.StandardButton.Ok:
            self.deportistasModel.deleteDeportista(row)

    def clearContacts(self):
        messageBox = QMessageBox.warning(
            self,
            "Cuidado!",
            "Seguro que quiere eliminar todos los deportistas?",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )

        if messageBox == QMessageBox.StandardButton.Ok:
            self.deportistasModel.clearDeportistas()

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
        self.dniField = QLineEdit()
        self.dniField.setObjectName("DNI")
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Nombre")
        self.apellidoField = QLineEdit()
        self.apellidoField.setObjectName("Apellido")
        self.telefonoField = QLineEdit()
        self.telefonoField.setObjectName("Telefono")
        self.nacimientoField = QLineEdit()
        self.nacimientoField.setObjectName("FechaNacimiento")
        self.clasificacionField = QLineEdit()
        self.clasificacionField.setObjectName("Clasificacion")
        # Configurar los campos
        layout = QFormLayout()
        layout.addRow("DNI:", self.dniField)
        layout.addRow("Nombre:", self.nameField)
        layout.addRow("Apellido:", self.apellidoField)
        layout.addRow("Teléfono:", self.telefonoField)
        layout.addRow("FechaNacimiento:", self.nacimientoField)
        layout.addRow("Calificacion:", self.clasificacionField)
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
        for field in (self.dniField, self.nameField, self.apellidoField, self.telefonoField, self.nacimientoField, self.clasificacionField):
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