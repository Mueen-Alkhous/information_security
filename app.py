from PySide6.QtWidgets import QApplication
from gui.gui import CipherApp
import numpy as np






if __name__ == "__main__":
    app = QApplication([])
    window = CipherApp()
    window.show()
    app.exec()