from pytinyexr import PyEXRImage
import numpy as np
from PIL import Image

import os
import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtMultimedia import *
from PySide2.QtMultimediaWidgets import *
# from PySide2 import QtWidgets, QtMultimedia, QtCore
from gui import main_window
import subprocess
from pymediainfo import MediaInfo
import yaml
from collections import OrderedDict
from pathlib import Path





class MainWindow(QWidget, main_window.Ui_AddNewRecord):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        # QtWidgets.QDialog.__init__(self, parent)
        # self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__), "form.ui"), self)

        self.setupUi(self)
        # self.get_codecs()
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # file = os.path.join(os.path.dirname(__file__), "video", "small.mp4")
        # self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))
        # self.player.setVideoOutput(self.prv_media_player)
        # self.player.play()
        self.asset_list = []

        self.tbl_assets.verticalHeader().setVisible(False)
        self.tbl_assets.horizontalHeader().setFixedHeight(50)
        self.tbl_assets.setSelectionBehavior(QTableView.SelectRows)
        self.tbl_assets.setColumnWidth(0, 200)
        self.tbl_assets.setColumnWidth(1, 190)
        self.tbl_assets.setColumnWidth(2, 100)
        self.tbl_assets.setColumnWidth(3, 80)

        self.tbl_assets.setColumnWidth(4, 90)

        self.tbl_assets.setColumnWidth(5, 60)
        self.tbl_assets.setColumnWidth(6, 60)
        self.tbl_assets.setColumnWidth(7, 90)
        self.tbl_assets.setColumnWidth(8, 50)
        self.tbl_assets.setColumnWidth(9, 80)
        self.tbl_assets.setColumnWidth(10, 80)
        self.tbl_assets.setColumnWidth(11, 70)

        self.tbl_assets.setHorizontalHeaderLabels(
            ['Thumbnail', 'Name', 'Vendor', 'Channels', 'Colorspace', 'Width', 'Height', 'Aspect Ratio', 'FPS', 'Start Frame', 'End Frame', 'Length'])
        self.tbl_assets.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tbl_assets.customContextMenuRequested.connect(self.context_menu)
        # self.tbl_assets.insertRow(self.tbl_assets.rowCount())

    def get_codecs(self):
        cmd = 'ffmpeg -codecs'
        x = subprocess.check_output(cmd, shell=True)
        x = x.split(b'\n')
        for e in x:
            print(e)



    def context_menu(self):
        menu = QMenu()
        add_data = menu.addAction("Add New Asset")
        # add_data.setIcon(QIcon(":/icons/images/add-icon.png"))
        add_data.triggered.connect(lambda: self.Add_New_Asset())
        if self.tbl_assets.selectedIndexes():
            remove_data = menu.addAction("Convert EXR to mp4")
            # remove_data.setIcon(QIcon(":/icons/images/remove.png"))
            remove_data.triggered.connect(lambda: self.Convert_EXR_MP4(self.tbl_assets.currentRow()))
        cursor = QCursor()
        menu.exec_(cursor.pos())

    def Add_New_Asset(self):

        self.tbl_assets.insertRow(self.tbl_assets.rowCount())
        self.Open_File()

        self.Make_Thumbnail(self.file_info['full_path'])
        self.Display_Info()

    def Open_File(self):

        filename, _ = QFileDialog.getOpenFileName(self, "Open EXR Sequence")
        media_info = MediaInfo.parse(filename)
        js = media_info.to_data()

        self.file_info = OrderedDict()

        self.file_info['name'] = js['tracks'][0]['folder_name'].split('/')[-1]
        self.file_info['path'] = js['tracks'][0]['folder_name']
        self.file_info['full_path'] = js['tracks'][0]['complete_name']
        self.file_info['filename'] = js['tracks'][0]['file_name_extension']
        self.file_info['category'] = js['tracks'][0]['folder_name'].split('/')[-3]
        self.file_info['vendor'] = js['tracks'][0]['folder_name'].split('/')[-4]
        self.file_info['width'] = js['tracks'][1]['width']
        self.file_info['height'] = js['tracks'][1]['height']
        self.file_info['fps'] = '24'
        self.file_info['aspectratio'] = js['tracks'][1]['pixel_aspect_ratio']
        self.file_info['colorspace'] = 'Linear sRGB'
        self.file_info['startf'] = js['tracks'][0]['file_name_extension'].split('.')[-2]
        self.file_info['endf'] = js['tracks'][0]['filenameextension_last'].split('.')[-2]
        self.file_info['length'] = js['tracks'][0]['frame_count']



    def Display_Info(self):

        ### Display in the Info panel
        # self.lbl_file_info.setText(yaml.dump(self.file_info, default_flow_style=False))

        ### Display in the table
        self.tbl_assets.setRowHeight(self.tbl_assets.rowCount()-1, 115)

        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 1, QTableWidgetItem(self.file_info['name']))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 2, QTableWidgetItem(self.file_info['vendor']))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 3, QTableWidgetItem('RGB'))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 4, QTableWidgetItem(self.file_info['colorspace']))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 5, QTableWidgetItem(str(self.file_info['width'])))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 6, QTableWidgetItem(str(self.file_info['height'])))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 7, QTableWidgetItem(str(self.file_info['aspectratio'])))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 8, QTableWidgetItem(self.file_info['fps']))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 9, QTableWidgetItem(self.file_info['startf']))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 10, QTableWidgetItem(self.file_info['endf']))
        self.tbl_assets.setItem(self.tbl_assets.rowCount()-1, 11, QTableWidgetItem(self.file_info['length']))

        self.thumb = QLabel()
        self.thumb.setPixmap(self.file_info['thumbnail'])
        self.tbl_assets.setCellWidget(self.tbl_assets.rowCount()-1, 0, self.thumb)

        self.asset_list.append(self.file_info)

        print(self.asset_list)



    def Make_Thumbnail(self, filename):

        # Load an EXR image (tinyexr backend)
        img = PyEXRImage(filename)

        # Print basic details
        # print(img)
        # print(img.filename)
        # print(img.width)
        # print(img.height)

        new_width  = 200
        # new_height = 180
        new_height = int(new_width * img.height / img.width)

        print ('--------------------------')

        # Numpy:
        rgb = np.reshape(np.array(img, copy = False), (img.height, img.width, 4))
        # a matrix of (height x width x channels)

        # PIL
        img = Image.fromarray(np.clip(np.uint8(rgb*255.0), 0, 255))
        thumb = img.resize((new_width, new_height), Image.ANTIALIAS)
        # thumb.show()

        conv_img  = thumb.tobytes('raw', 'RGBA')
        image = QImage(conv_img, thumb.size[0], thumb.size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(image)
        self.file_info['thumbnail'] = pix


    def Convert_EXR_MP4(self, index):
        print("Converting file: {0} at row {1} ...".format(self.asset_list[index]['full_path'], index))
        input = str(self.asset_list[index]['full_path'])[:-8] +'%04d' + str(self.asset_list[index]['full_path'])[-4:]
        print(input)
        s = self.asset_list[index]['path'].split('/')[1:-2]
        output = str(Path('/').joinpath(*s) / 'thumbnails' / self.asset_list[index]['name']) + '_thumbnail.mov'
        start_frame = self.asset_list[index]['startf']
        frame_rate = self.asset_list[index]['fps']
        print(output)
        cmd = f"ffmpeg -start_number {start_frame} -f image2 -y -gamma 2.2 -i {input} -vf scale=240:115 -r {frame_rate} {output}"
        print(cmd)
        subprocess.check_output(cmd, shell=True)

       ### ffmpeg -start_number 1001 -f image2 -y -gamma 2.2 -i /Volumes/mutha/jobs/AssLib/ActionVFX/SmokePlume/exr/SmokePlume_1_0221/SmokePlume_1_0221.%04d.exr -vf scale=240:115 -vcodec libx264 -pix_fmt yuv420p -r 24 /Volumes/mutha/jobs/AssLib/ActionVFX/SmokePlume/thumbnails/SmokePlume_1_0221_thumbnail.mov
       ### ffmpeg -start_number 1001 -f image2 -y -gamma 2.2 -i /Volumes/mutha/jobs/AssLib/ActionVFX/SmokePlume/exr/SmokePlume_1_0221/SmokePlume_1_0221.%04d.exr -vf scale=240:115 -r 24 /Volumes/mutha/jobs/AssLib/ActionVFX/SmokePlume/thumbnails/SmokePlume_1_0221_thumbnail.mp4
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    ret = app.exec_()
    sys.exit(ret)


