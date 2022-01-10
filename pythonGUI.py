import os
import sys

from dotenv          import load_dotenv
from os.path         import join, dirname
from PyQt5           import uic
from PyQt5.QtWidgets import QMainWindow,QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        dotenv_path = join(dirname(__file__), 'EnvFile.env')
        load_dotenv(dotenv_path)
        UI_FILE = os.environ.get("UI")
         
        #print(UI_FILE)
        uic.loadUi(UI_FILE,self)
        self.pb_Activar.clicked.connect(self.fn_activar)
        self.pb_Desactivar.clicked.connect(self.fn_desactivar)

    def fn_activar(self):
        self.l_Estado.setText("Activado")

    def fn_desactivar(self):
        self.l_Estado.setText("Desactivado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())