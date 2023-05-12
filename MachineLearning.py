import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(":memory:")
    if not db.open():
        QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                       "Unable to establish a database connection.\n"
                                       "This example needs SQLite support. Please read "
                                       "the Qt SQL driver documentation for information how "
                                       "to build it.\n\n"
                                       "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
        return False
    query = QSqlQuery()
    query.exec("create table contacts (id int primary key, "
               "firstname varchar(20), lastname varchar(20), phone varchar(20), email varchar(30))")
    return True

def initializeModel(model):
    model.setTable("contacts")
    model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Last name")
    model.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "Phone")
    model.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Email")

def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if not createConnection():
        sys.exit(-1)
    model = QSqlTableModel()
    initializeModel(model)
    view = createView("Contacts", model)
    view.show()
    sys.exit(app.exec())