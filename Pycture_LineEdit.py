from PyQt5.QtWidgets import *

class MyLineEdit(QLineEdit):
    def __init__(self, parent):
        super(MyLineEdit, self).__init__(parent)
        self.setReadOnly(True)
        self.setDragEnabled(True)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            PDF_Exists_flag = False
            if len(event.mimeData().urls()) == 1:
                if event.mimeData().urls()[0].path().split('.')[-1] == 'jpg'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'png'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'gif'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'ico':
                    PDF_Exists_flag = True
            if PDF_Exists_flag == True:
                self.setStyleSheet('QLineEdit {background-color: #DDFFDD; border: 1px solid rgb(122, 122, 122)}')
                #self.setStyleSheet('QLineEdit {background-color: #DDFFDD;}')
                event.acceptProposedAction()
            else:
                #self.setStyleSheet('QTableWidget {background-color: #FFDDDD;}  QHeaderView {background-color: white;}')
                super(MyLineEdit, self).dragEnterEvent(event)
        else:
            #self.setStyleSheet('QTableWidget {background-color: #FFDDDD;}  QHeaderView {background-color: white;}')
            pass
            #super(MyTableWidget, self).dragEnterEvent(event)

    def dragLeaveEvent(self, event):
        self.setStyleSheet('QLineEdit {background-color: white;}')
        super(MyLineEdit, self).dragLeaveEvent(event)

    def dragMoveEvent(self, event):
        super(MyLineEdit, self).dragMoveEvent(event)

    def dropEvent(self, event):
        self.setStyleSheet('QLineEdit {background-color: white;}')
        if event.mimeData().hasUrls():
            if len(event.mimeData().urls()) == 1:
                if event.mimeData().urls()[0].path().split('.')[-1] == 'jpg'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jpeg'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jpe'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'jfif'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'png'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'bmp'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'gif'\
                        or event.mimeData().urls()[0].path().split('.')[-1] == 'ico':
                    self.setText(event.mimeData().urls()[0].path()[1:])
            event.acceptProposedAction()
        else:
            pass
            #super(MyTableWidget,self).dropEvent(event)