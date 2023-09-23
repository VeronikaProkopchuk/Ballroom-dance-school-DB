from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlTableModel

class EntrenadoresModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("entrenadores")
        tableModel.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        tableModel.select()
        headers = ("DNI", "Nombre", "Apellido", "Teléfono", "FechaNacimiento", "Calificacion")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)
        return tableModel

    def addEntrenador(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()

    def deleteEntrenador(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearEntrenadores(self):
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.model.select()

class DeportistasModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("deportistas")
        tableModel.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        tableModel.select()
        headers = ("DNI", "Nombre", "Apellido", "Teléfono", "FechaNacimiento", "Calificacion")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)
        return tableModel

    def addDeportista(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()

    def deleteDeportista(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearDeportistas(self):
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.model.select()

class LeccionesModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("lecciones")
        tableModel.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        tableModel.select()
        headers = ("Nombre", "Longitud", "DNIEntrtenador")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)
        return tableModel

    def addLeccion(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()

    def deleteLeccion(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearLecciones(self):
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.model.select()

class SalasModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        tableModel = QSqlTableModel()
        tableModel.setTable("salas")
        tableModel.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        tableModel.select()
        headers = ("Nombre", "Superficie")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Orientation.Horizontal, header)
        return tableModel

    def addSala(self, data):
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()

    def deleteSala(self, row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearSalas(self):
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        self.model.select()


    

