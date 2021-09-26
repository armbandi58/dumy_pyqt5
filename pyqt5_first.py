import PyQt5.QtWidgets as qtw #Widgetekhez
import PyQt5.QtGui  as qtg
import ascii_art as art

class MainWindow(qtw.QWidget):
    def __init__(self, name):
        super().__init__()
        self.window_name = name
        self.setWindowTitle(name)
        self.show()
        self.setLayout(qtw.QVBoxLayout())



def main():
    app = qtw.QApplication([])
    root = MainWindow("Na mehet")
    firstlabel = qtw.QLabel("Kleti kleti")
    firstlabel.setFont(qtg.QFont('Helvetica',18))
    root.layout().addWidget(firstlabel)
    print("Window name: "+root.window_name)

    app.exec_()

if __name__ == "__main__":
    print("[+] UI indul")
    art.render("Welcome Mr. Stark",'slant')
    main()