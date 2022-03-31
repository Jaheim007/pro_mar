import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from Widget.command import Project


def main():
    app = QApplication(sys.argv)
    home = Project()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
