from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def _createEntrenadoresTable():
        createTableQuery = QSqlQuery()
        return createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS ENTRENADORES (
                DNI	TEXT PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Apellido TEXT,
                Telefono TEXT NOT NULL,
                FechaNacimiento TEXT,
                Clasificacion TEXT NOT NULL
            );
            """
        )
def _createDeportistasTable():
        createTableQuery = QSqlQuery()
        return createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS DEPORTISTAS (
                DNI	TEXT PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Apellido TEXT,
                Telefono TEXT NOT NULL,
                FechaNacimiento TEXT,
                Clasificacion TEXT NOT NULL
            );
            """
        )

def _createLeccionesTable():
        createTableQuery = QSqlQuery()
        return createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS LECCIONES (
	            Nombre TEXT PRIMARY KEY,
	            Longitud TEXT DEFAULT 1:45,
	            DNIEntrenador TEXT,
	            FOREIGN KEY(DNIEntrenador) REFERENCES ENTRENADORES(DNI),
            );
            """
        )

def _createSalasTable():
        createTableQuery = QSqlQuery()
        return createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS SALAS (
	            Nombre TEXT PRIMARY KEY,
	            Superficie INTEGER NOT NULL,
            );
            """
        )

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Baile Deportivo",
            f"DB Error: {connection.lastError().text()}",
        )
        return False

    _createEntrenadoresTable()
    _createDeportistasTable()
    _createLeccionesTable()
    _createSalasTable()
    return True