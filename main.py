from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import requests
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('map.ui', self)
        self.map_zoom = 16
        self.map_ll = [37.530887, 55.703118]
        self.t = 'map'
        self.render_map()

    def render_map(self):
        params = {
            'll': f"{self.map_ll[0]},{self.map_ll[1]}",
            'l': self.t,
            'z': self.map_zoom
        }
        request = f"http://static-maps.yandex.ru/1.x/"
        response = requests.get(request, params=params)

        pixmap = QPixmap()
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        pixmap.load(map_file)
        self.label.setPixmap(pixmap)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_PageDown:
            if self.map_zoom > 1:
                self.map_zoom -= 1
            self.render_map()
        if e.key() == Qt.Key_PageUp:
            if self.map_zoom < 17:
                self.map_zoom += 1
            self.render_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


