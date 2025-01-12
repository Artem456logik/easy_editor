from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from ui import Ui_MainWindow, QFileDialog
import os

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

workdir = ""
extensions = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]

def filter(files: list[str]):
    filtered_files = []

    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                filtered_files.append(file)
    return filtered_files


ui.setupUi(win)
def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files_list = os.listdir(workdir)
    files_list = filter(files_list)

    ui.files_list.addItems
ui.chose_dir_btn.clicked.connect(choose_workdir)






app.exec()
win.show()