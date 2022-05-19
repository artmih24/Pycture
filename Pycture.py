from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from MainWindow import Ui_MainWindow
from Pycture_about import about_window
from Pycture_LineEdit import *
import sys, os, base64
import _icon.Pycture_icon_ as icon


class mywindow(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(icon.Get_icon(icon.icon_str))
        self.setGeometry(805, 400, 306, 193)
        self.setMinimumSize(306, 193)
        self.setStyleSheet('QMainWindow {background-color: white;}')
        #self.setMaximumHeight(193)
        self.ui.pushButton_2.setEnabled(False)
        self.about_window = about_window()
        #self.ui.lineEdit.setReadOnly(True)
        self.ui.lineEdit = MyLineEdit(self.ui.lineEdit)
        self.ui.gridLayout.addWidget(self.ui.lineEdit, 1, 0, 1, 2)
        self.ui.lineEdit.setFixedWidth(self.width() - 84)
        self.ui.lineEdit.setFixedHeight(40)
        self.ui.label.setText('Выберите изображение, или перетащите его на поле')
        self.ui.label_2.setText('Введите название изображения в .py-файле')
        m = self.menuBar().addMenu("Меню")
        a = m.addAction("О программе")
        a.triggered.connect(self.aboutClicked)
        self.ui.pushButton.clicked.connect(self.SelectButtonClicked)
        self.ui.pushButton_2.clicked.connect(self.GenerateButtonClicked)
        self.resized.connect(self.FormResized)
        self.ui.lineEdit_2.setFixedWidth(247)
        self.ui.lineEdit_2.textEdited.connect(self.TextEdited)
        self.ui.lineEdit_2.textChanged.connect(self.TextChanged)
        self.ui.lineEdit.textChanged.connect(self.FilePathEntered)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(mywindow, self).resizeEvent(event)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.about_window.close()

    def FormResized(self):
        self.ui.lineEdit_2.setFixedWidth(self.width() - 19)
        self.ui.lineEdit.setFixedWidth(self.width() - 84)

    def TextEdited(self):
        self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "")
        # if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "":
        #     self.ui.pushButton_2.setEnabled(True)
        # else:
        #     self.ui.pushButton_2.setEnabled(False)

    def TextChanged(self):
        self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "")
        # if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "":
        #     self.ui.pushButton_2.setEnabled(True)
        # else:
        #     self.ui.pushButton_2.setEnabled(False)

    def aboutClicked(self):
        self.about_window.show()
        """
        q = QMessageBox()
        q.setWindowIcon(icon.Get_icon(icon.icon_str))
        q.setStyleSheet('QMessageBox {background-color: white; font-family: Consolas; font-size: 13px;}')
        # q.setStyleSheet('QMessageBox {background-color: white; font-family: Consolas;}')
        QMessageBox.about(q, "О программе", '''Pycture 1.2\n
Автор программы:\n
   ____             _             _ _     ____  _  _
  / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
 / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
| | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
 \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
  \____/''')
"""

    def SelectButtonClicked(self):
        InputImageName = QFileDialog.getOpenFileName(self, "Выбрать изображение", "/home", "Все типы изображений (*.jpg *.jpeg *.jpe *.jfif *.png *.bmp *.gif *.ico);; Изображение JPEG (*.jpg *.jpeg *.jpe *.jfif);; Изображение PNG (*.png);; Изображение BMP (*.bmp);; Изображение GIF (*.gif);; Значок ICO (*.ico)")[0]
        self.ui.lineEdit.setText(InputImageName)
        self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "")
        # if self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "":
        #     self.ui.pushButton_2.setEnabled(True)
        # else:
        #     self.ui.pushButton_2.setEnabled(False)

    def FilePathEntered(self):
        self.ui.pushButton_2.setEnabled(self.ui.lineEdit.text() != "")
        # if self.ui.lineEdit.text() != "":
        #     self.ui.pushButton_2.setEnabled(True)
        # else:
        #     self.ui.pushButton_2.setEnabled(False)

    def GenerateButtonClicked(self):
        q = QMessageBox()
        q.setWindowIcon(icon.Get_icon(icon.icon_str))
        InputImageName = self.ui.lineEdit.text()
        TempPyFileName = '.'.join(InputImageName.split('.')[:-1]) + ".py"
        ShortPyFileName = TempPyFileName.split('/')[-1]
        ImageNameInPyFile = self.ui.lineEdit_2.text()
        ImageExtension = '.' + InputImageName.split('.')[-1]
        try:
            with open(InputImageName, "rb") as ImageFile:
                ImageFileStr = base64.b64encode(ImageFile.read())
            ImageFile.close()
        except:
            if os.path.exists(InputImageName) == True:
                QMessageBox.critical(q, "Pycture", f"Файл {InputImageName} повреждён.\nОперация прервана", QMessageBox.Ok)
                ImageFile.close()
            else:
                QMessageBox.critical(q, "Pycture", f"Файл {InputImageName} не существует.\nОперация прервана", QMessageBox.Ok)
        else:
            if ImageExtension == '.ico':
                PyFileContent = "# auto-generated source-code file " + ShortPyFileName + ''' with Pycture
# Pycture developed by
#    ____             _             _ _     ____  _  _
#   / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
#  / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
# | | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
#  \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
#   \____/

from PyQt5 import QtGui
import base64
import os

def Get_''' + ImageNameInPyFile + '''(image_str):
    ImageStr = base64.b64decode(image_str)
    with open("''' + ImageNameInPyFile + ImageExtension + '''", "wb") as ''' + ImageNameInPyFile + '''_text:
    ''' + ImageNameInPyFile + '''_text.write(ImageStr)
    ''' + ImageNameInPyFile + '''_text.close()
    qi = QtGui.QIcon("''' + ImageNameInPyFile + ImageExtension + '''")
    os.remove("''' + ImageNameInPyFile + ImageExtension + '''")
    return(qi)
        
''' + ImageNameInPyFile + '''_str = "''' + str(ImageFileStr)[2:-1] + '''"'''
            else:
                PyFileContent = "# auto-generated source-code file " + ShortPyFileName + ''' with Pycture
# Pycture developed by
#    ____             _             _ _     ____  _  _
#   / __ \  __ _ _ __| |_ _ __ ___ (_) |__ |___ \| || |
#  / / _` |/ _` | '__| __| '_ ` _ \| | '_ \  __) | || |_
# | | (_| | (_| | |  | |_| | | | | | | | | |/ __/|__   _|
#  \ \__,_|\__,_|_|   \__|_| |_| |_|_|_| |_|_____|  |_|
#   \____/

from PyQt5 import QtGui, QtCore
import base64
import os

def Get_''' + ImageNameInPyFile + '''(image_str):
    ImageStr = base64.b64decode(image_str)
    with open("''' + ImageNameInPyFile + ImageExtension + '''", "wb") as ''' + ImageNameInPyFile + '''_text:
    ''' + ImageNameInPyFile + '''_text.write(ImageStr)
    ''' + ImageNameInPyFile + '''_text.close()
    qp = QtGui.QPixmap("''' + ImageNameInPyFile + ImageExtension + '''").scaled(100, 100, transformMode=QtCore.Qt.SmoothTransformation)
    os.remove("''' + ImageNameInPyFile + ImageExtension + '''")
    return(qp)
        
''' + ImageNameInPyFile + '''_str = "''' + str(ImageFileStr)[2:-1] + '''"'''
            try:
                PyFileName = QFileDialog.getSaveFileName(self, "Сохранить файл", TempPyFileName, "Файл исходного кода Python (*.py)")[0]
            except:
                QMessageBox.critical(q, "Pycture", f"Не выбран путь для сохранения файла.\nОперация прервана", QMessageBox.Ok)
            else:
                try:
                    with open(PyFileName, "w") as PyFile:
                        PyFile.write(PyFileContent)
                    PyFile.close()
                except:
                    QMessageBox.critical(q, "Pycture", f"Возникла ошибка при записи файла {PyFileName}.\nОперация прервана", QMessageBox.Ok)
                    PyFile.close()
                else:
                    QMessageBox.information(q, "Pycture", "Файл " + PyFileName + " успешно создан!", QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()

    sys.exit(app.exec())