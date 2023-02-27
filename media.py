from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QRegExpValidator, QStandardItemModel, QStandardItem
from PyQt5.QtCore import QRegExp, Qt
import uic

numeros = []
ultres = []

def calcular_media_edit():
    global model, media
    try:
        numero_lido = formulario.numlido.text()
        numeros.append(float(numero_lido))
        somanum = sum(numeros)
        qtdnum = len(numeros)
        media = somanum / qtdnum
        formulario.label.setText(f'A média é {media:.2f}')
        formulario.numlido.clear()
        model = QStandardItemModel()
        for i in numeros:
            item = QStandardItem("{:.2f}".format(i))
            model.appendRow(item)
        formulario.lista.setModel(model)
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Nenhum valor foi adicionado")
        msg.setWindowTitle("Erro")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

def reset():
    global model2
    try:
        numeros.clear()
        model.removeRows(0, model.rowCount())
        formulario.label.setText(f'A média é ')
        ultres.append(media)
        model2 = QStandardItemModel()
        for i in ultres:
            item = QStandardItem("{:.2f}".format(i))
            model2.appendRow(item)
        formulario.lista_2.setModel(model2)
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Nenhum valor foi adicionado")
        msg.setWindowTitle("Erro")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

def deletelista(event):
    global media
    if event.key() == Qt.Key_Delete:
        indexes = formulario.lista.selectedIndexes()
        if indexes:
            index = indexes[0]
            value = model.data(index)
            model.removeRow(index.row())
            numeros.remove(float(value))
    somanum = sum(numeros)
    qtdnum = len(numeros)
    try:
        mediadel = somanum / qtdnum
        formulario.label.setText(f'A média é {mediadel:.2f}')
        media = mediadel
        formulario.numlido.clear()
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Pilha Limpa')
        msg.setWindowTitle("Informação")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        formulario.label.setText(f'A média é ')
        media = 0

def deletelista_2(event):
    if event.key() == Qt.Key_Delete:
        indexes = formulario.lista_2.selectedIndexes()
        if indexes:
            index = indexes[0]
            value = model2.data(index)
            model2.removeRow(index.row())
            ultres.remove(float(value))


app = QApplication([])
formulario = uic.loadUi('media1.ui')



#BOTÕES
formulario.calc.clicked.connect(calcular_media_edit)
formulario.reset.clicked.connect(reset)
formulario.numlido.returnPressed.connect(calcular_media_edit)
app.installEventFilter(formulario.lista)
app.installEventFilter(formulario.lista_2)
formulario.lista.keyPressEvent = deletelista
formulario.lista_2.keyPressEvent = deletelista_2

validator = QRegExpValidator(QRegExp("[0-9.]*"))
formulario.numlido.setValidator(validator)


formulario.show()
app.exec()