from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog
from ui import Ui_MainWindow
import os
from PIL import Image, ImageFilter
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

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
    ui.files_list.clear()
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    if os.path.isdir(workdir):
        files_list = os.listdir(workdir)

        files_list = filter(files_list)
        ui.files_list.addItems(files_list)

ui.chose_dir_btn.clicked.connect(choose_workdir)

class ImageProcessor():
    def __init__(self):
        self.image:Image.Image = None
        self.filename:str = ""
        self.modifed_subfolder = "modifed"

    def openImage(self, filename:str):
        self.filename = filename
        self.full_path = os.path.join(workdir, filename)
        self.image = Image.open(self.full_path)

    def showImage(self):
        if self.image is not None:
            ui.image_lb.hide()
            pixmap = QPixmap(self.full_path)
            w,h = ui.image_lb.width(), ui.image_lb.height()

            pixmapimage = pixmap.scaled(w,h, Qt.AspectRatioMode.KeepAspectRatio)
            ui.image_lb.setPixmap(pixmapimage)
            ui.image_lb.show()

    def saveImage(self):
        save_dir_path = os.path.join(workdir, self.modifed_subfolder)
        if not os.path.isdir(save_dir_path):
            os.mkdir(save_dir_path)

        full_path = os.path.join(save_dir_path, self.filename)
        self.image.save(full_path)

    def makeBW(self):
        if self.image is not None:
            self.image = self.image.convert("L")
            self.saveImage()
            modifed_path = os.path.join(workdir, self.modifed_subfolder, self.filename)
            self.full_path = modifed_path
            self.showImage()

    def makeFlip(self):
        if self.image is not None:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            modifed_path = os.path.join(workdir, self.modifed_subfolder, self.filename)
            self.full_path = modifed_path
            self.showImage()

    def TurnLeft(self):
        if self.image is not None:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()
            modifed_path = os.path.join(workdir, self.modifed_subfolder, self.filename)
            self.full_path = modifed_path
            self.showImage()

    def TurnRight(self):
        if self.image is not None:     
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            modifed_path = os.path.join(workdir, self.modifed_subfolder, self.filename)
            self.full_path = modifed_path
            self.showImage()

    def makeSharpen(self):
        if self.image is not None:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.saveImage()
            modifed_path = os.path.join(workdir, self.modifed_subfolder, self.filename)
            self.full_path = modifed_path
            self.showImage()

ip = ImageProcessor()
def show_choosen_image():
    if ui.files_list.selectedItems():
        choosen_filename = ui.files_list.currentItem().text()
        ip.openImage(choosen_filename)
        ip.showImage()

ui.files_list.currentItemChanged.connect(show_choosen_image)
ui.bw_btn.clicked.connect(ip.makeBW)
ui.mirror_btn.clicked.connect(ip.makeFlip)
ui.left_btn.clicked.connect(ip.TurnLeft)
ui.right_btn.clicked.connect(ip.TurnRight)
ui.sharp_btn.clicked.connect(ip.makeSharpen)





ui.files_list.currentItemChanged.connect(show_choosen_image)
win.show()
app.exec()