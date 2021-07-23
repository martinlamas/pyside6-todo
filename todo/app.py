import sys

from PySide6.QtWidgets import QApplication
from todo.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
