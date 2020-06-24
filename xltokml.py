import sys

from PySide2.QtWidgets import QApplication

from kmldata.ui import Main


def main():
    app = QApplication(sys.argv)
    mainwindow = Main()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
