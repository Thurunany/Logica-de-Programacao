from PyQt5.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QWidget,
    QLineEdit, QPushButton, QMessageBox
)
from PyQt5.QtCore import pyqtSlot

from cpf import verificarCPF

@pyqtSlot()
def verificarCPF1():
    alerta = QMessageBox()
    cpf_digitado = cpf.text()
    if verificarCPF(cpf_digitado):
        alerta.setText('CPF ' + cpf_digitado + ' é valido')
    else:
        alerta.setText('CPF ' + cpf_digitado + ' é inválido')
    alerta.exec_()

app = QApplication([])
janela = QWidget()
layout = QVBoxLayout()

titulo = QLabel("Meu verificador de CPF")
layout.addWidget(titulo)
cpf = QLineEdit()
layout.addWidget(cpf)
botao1 = QPushButton('Verificar CPF')
botao1.clicked.connect(verificarCPF1)
layout.addWidget(botao1)
janela.setLayout(layout)

janela.show()
app.exec_()