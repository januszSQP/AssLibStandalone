# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtMultimediaWidgets import QVideoWidget


class Ui_AddNewRecord(object):
    def setupUi(self, AddNewRecord):
        if not AddNewRecord.objectName():
            AddNewRecord.setObjectName(u"AddNewRecord")
        AddNewRecord.resize(1724, 1243)
        self.horizontalLayout = QHBoxLayout(AddNewRecord)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(AddNewRecord)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.tbl_assets = QTableWidget(self.groupBox)
        if (self.tbl_assets.columnCount() < 12):
            self.tbl_assets.setColumnCount(12)
        self.tbl_assets.setObjectName(u"tbl_assets")
        self.tbl_assets.setGeometry(QRect(15, 31, 1161, 1191))
        self.tbl_assets.setColumnCount(12)
        self.tbl_assets.horizontalHeader().setVisible(True)
        self.tbl_assets.verticalHeader().setVisible(True)

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(AddNewRecord)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(500, 0))
        self.groupBox_2.setFlat(True)
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 461, 1186))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.prv_media_player = QVideoWidget(self.layoutWidget)
        self.prv_media_player.setObjectName(u"prv_media_player")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.prv_media_player.sizePolicy().hasHeightForWidth())
        self.prv_media_player.setSizePolicy(sizePolicy1)
        self.prv_media_player.setMinimumSize(QSize(0, 300))

        self.verticalLayout.addWidget(self.prv_media_player)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_play = QToolButton(self.layoutWidget)
        self.btn_play.setObjectName(u"btn_play")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_play.sizePolicy().hasHeightForWidth())
        self.btn_play.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.btn_play)

        self.sld_progress = QSlider(self.layoutWidget)
        self.sld_progress.setObjectName(u"sld_progress")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sld_progress.sizePolicy().hasHeightForWidth())
        self.sld_progress.setSizePolicy(sizePolicy3)
        self.sld_progress.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.sld_progress)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.groupBox_3 = QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setMinimumSize(QSize(0, 800))
        self.groupBox_3.setMaximumSize(QSize(16777215, 750))
        self.groupBox_3.setFlat(False)
        self.lbl_file_info = QLabel(self.groupBox_3)
        self.lbl_file_info.setObjectName(u"lbl_file_info")
        self.lbl_file_info.setGeometry(QRect(10, 30, 441, 721))

        self.verticalLayout.addWidget(self.groupBox_3)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(AddNewRecord)

        QMetaObject.connectSlotsByName(AddNewRecord)
    # setupUi

    def retranslateUi(self, AddNewRecord):
        AddNewRecord.setWindowTitle(QCoreApplication.translate("AddNewRecord", u"AssLib - Adding New Record(s)", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddNewRecord", u"Task", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AddNewRecord", u"Output", None))
        self.btn_play.setText(QCoreApplication.translate("AddNewRecord", u"...", None))
        self.label.setText(QCoreApplication.translate("AddNewRecord", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("AddNewRecord", u"Info", None))
        self.lbl_file_info.setText(QCoreApplication.translate("AddNewRecord", u"TextLabel", None))
    # retranslateUi

