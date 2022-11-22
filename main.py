import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Случайные окружности')

        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

            self.do_paint = False

    def draw(self):
        size = random.randrange(10, 150)
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        self.qp.setBrush(QColor(r, g, b))
        x = random.randrange(50, 750)
        y = random.randrange(50, 550)

        self.qp.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())