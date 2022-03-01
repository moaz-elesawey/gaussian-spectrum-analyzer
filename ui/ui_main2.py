# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SpectrumAnalyzer(object):
    def setupUi(self, SpectrumAnalyzer):
        if not SpectrumAnalyzer.objectName():
            SpectrumAnalyzer.setObjectName(u"SpectrumAnalyzer")
        SpectrumAnalyzer.resize(1108, 700)
        SpectrumAnalyzer.setStyleSheet(u"")
        self.centralwidget = QWidget(SpectrumAnalyzer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        font = QFont()
        font.setFamily(u"Noto Mono")
        font.setPointSize(10)
        self.mainFrame.setFont(font)
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.mainFrame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFont(font)
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.spectrumTabWidget = QTabWidget(self.frame)
        self.spectrumTabWidget.setObjectName(u"spectrumTabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.spectrumTabWidget.sizePolicy().hasHeightForWidth())
        self.spectrumTabWidget.setSizePolicy(sizePolicy1)
        self.spectrumTabWidget.setMinimumSize(QSize(0, 0))
        self.spectrumTabWidget.setFont(font)
        self.spectrumTabWidget.setStyleSheet(u"QFrame#spectrumFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.spectrumTabWidget.setTabPosition(QTabWidget.West)
        self.spectrumFrame2 = QWidget()
        self.spectrumFrame2.setObjectName(u"spectrumFrame2")
        self.spectrum_frame_layout2 = QVBoxLayout(self.spectrumFrame2)
        self.spectrum_frame_layout2.setSpacing(5)
        self.spectrum_frame_layout2.setObjectName(u"spectrum_frame_layout2")
        self.spectrum_frame_layout2.setContentsMargins(5, 5, 5, 5)
        self.spectrumFrame = QFrame(self.spectrumFrame2)
        self.spectrumFrame.setObjectName(u"spectrumFrame")
        font1 = QFont()
        font1.setFamily(u"Noto Mono")
        self.spectrumFrame.setFont(font1)
        self.spectrumFrame.setFrameShape(QFrame.NoFrame)
        self.spectrumFrame.setFrameShadow(QFrame.Raised)
        self.spectrum_frame_layout = QVBoxLayout(self.spectrumFrame)
        self.spectrum_frame_layout.setSpacing(6)
        self.spectrum_frame_layout.setObjectName(u"spectrum_frame_layout")
        self.spectrum_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.spectrumFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 2, 3, 3)
        self.spectrums_select = QComboBox(self.frame_3)
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.setObjectName(u"spectrums_select")
        self.spectrums_select.setMinimumSize(QSize(0, 28))
        self.spectrums_select.setFont(font)

        self.horizontalLayout_7.addWidget(self.spectrums_select)

        self.loaded_file_name = QLabel(self.frame_3)
        self.loaded_file_name.setObjectName(u"loaded_file_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loaded_file_name.sizePolicy().hasHeightForWidth())
        self.loaded_file_name.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamily(u"Noto Mono")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.loaded_file_name.setFont(font2)
        self.loaded_file_name.setWordWrap(True)
        self.loaded_file_name.setIndent(3)

        self.horizontalLayout_7.addWidget(self.loaded_file_name)

        self.spectrumType = QComboBox(self.frame_3)
        self.spectrumType.setObjectName(u"spectrumType")
        self.spectrumType.setMinimumSize(QSize(0, 28))
        self.spectrumType.setFont(font1)

        self.horizontalLayout_7.addWidget(self.spectrumType)


        self.spectrum_frame_layout.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.spectrum_frame_layout2.addWidget(self.spectrumFrame)

        self.spectrumTabWidget.addTab(self.spectrumFrame2, "")
        self.render_frame = QWidget()
        self.render_frame.setObjectName(u"render_frame")
        self.renderLayout = QVBoxLayout(self.render_frame)
        self.renderLayout.setSpacing(0)
        self.renderLayout.setObjectName(u"renderLayout")
        self.renderLayout.setContentsMargins(0, 0, 0, 0)
        self.spectrumTabWidget.addTab(self.render_frame, "")
        self.log_file_frame = QWidget()
        self.log_file_frame.setObjectName(u"log_file_frame")
        self.log_file_ui = QVBoxLayout(self.log_file_frame)
        self.log_file_ui.setSpacing(0)
        self.log_file_ui.setObjectName(u"log_file_ui")
        self.log_file_ui.setContentsMargins(0, 0, 0, 0)
        self.log_file_text = QTextBrowser(self.log_file_frame)
        self.log_file_text.setObjectName(u"log_file_text")
        font3 = QFont()
        font3.setFamily(u"Courier")
        font3.setPointSize(12)
        self.log_file_text.setFont(font3)

        self.log_file_ui.addWidget(self.log_file_text)

        self.spectrumTabWidget.addTab(self.log_file_frame, "")

        self.verticalLayout_4.addWidget(self.spectrumTabWidget)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 160))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.zoom_out_btn = QPushButton(self.frame_4)
        self.zoom_out_btn.setObjectName(u"zoom_out_btn")
        self.zoom_out_btn.setMinimumSize(QSize(0, 28))
        self.zoom_out_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u"../icons/zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_out_btn.setIcon(icon)
        self.zoom_out_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.zoom_out_btn)

        self.tight_graph_btn = QPushButton(self.frame_4)
        self.tight_graph_btn.setObjectName(u"tight_graph_btn")
        self.tight_graph_btn.setMinimumSize(QSize(0, 28))
        self.tight_graph_btn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../icons/aspect-ratio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tight_graph_btn.setIcon(icon1)
        self.tight_graph_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.tight_graph_btn)

        self.start_animation_btn = QPushButton(self.frame_4)
        self.start_animation_btn.setObjectName(u"start_animation_btn")
        self.start_animation_btn.setEnabled(True)
        self.start_animation_btn.setMinimumSize(QSize(0, 28))
        self.start_animation_btn.setFont(font)
        self.start_animation_btn.setStyleSheet(u"")
        self.start_animation_btn.setIconSize(QSize(20, 20))
        self.start_animation_btn.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.start_animation_btn)

        self.intensity_label = QLabel(self.frame_4)
        self.intensity_label.setObjectName(u"intensity_label")
        sizePolicy2.setHeightForWidth(self.intensity_label.sizePolicy().hasHeightForWidth())
        self.intensity_label.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamily(u"Noto Mono")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.intensity_label.setFont(font4)
        self.intensity_label.setAlignment(Qt.AlignCenter)
        self.intensity_label.setWordWrap(True)
        self.intensity_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_6.addWidget(self.intensity_label)

        self.style_btn = QPushButton(self.frame_4)
        self.style_btn.setObjectName(u"style_btn")
        self.style_btn.setMinimumSize(QSize(0, 28))
        self.style_btn.setFont(font)

        self.horizontalLayout_6.addWidget(self.style_btn)

        self.export_graph_btn = QPushButton(self.frame_4)
        self.export_graph_btn.setObjectName(u"export_graph_btn")
        self.export_graph_btn.setMinimumSize(QSize(110, 28))
        self.export_graph_btn.setFont(font)

        self.horizontalLayout_6.addWidget(self.export_graph_btn)

        self.export_formats_select = QComboBox(self.frame_4)
        self.export_formats_select.setObjectName(u"export_formats_select")
        self.export_formats_select.setMinimumSize(QSize(0, 28))
        self.export_formats_select.setFont(font)

        self.horizontalLayout_6.addWidget(self.export_formats_select)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.frame_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(20, 0))
        self.widget_2.setFont(font)

        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.show_peaks_check = QCheckBox(self.frame_4)
        self.show_peaks_check.setObjectName(u"show_peaks_check")
        self.show_peaks_check.setFont(font)

        self.horizontalLayout_2.addWidget(self.show_peaks_check)

        self.peaks_select = QComboBox(self.frame_4)
        self.peaks_select.setObjectName(u"peaks_select")
        self.peaks_select.setMinimumSize(QSize(0, 28))
        self.peaks_select.setFont(font)

        self.horizontalLayout_2.addWidget(self.peaks_select)

        self.show_marks_check = QCheckBox(self.frame_4)
        self.show_marks_check.setObjectName(u"show_marks_check")
        self.show_marks_check.setFont(font)

        self.horizontalLayout_2.addWidget(self.show_marks_check)

        self.marks_select = QComboBox(self.frame_4)
        self.marks_select.setObjectName(u"marks_select")
        self.marks_select.setMinimumSize(QSize(0, 28))
        self.marks_select.setFont(font)

        self.horizontalLayout_2.addWidget(self.marks_select)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.broadening_inp = QLineEdit(self.frame_4)
        self.broadening_inp.setObjectName(u"broadening_inp")
        self.broadening_inp.setMinimumSize(QSize(0, 28))
        self.broadening_inp.setFont(font)
        self.broadening_inp.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhPreferNumbers)

        self.horizontalLayout.addWidget(self.broadening_inp)

        self.broadening_btn = QPushButton(self.frame_4)
        self.broadening_btn.setObjectName(u"broadening_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.broadening_btn.sizePolicy().hasHeightForWidth())
        self.broadening_btn.setSizePolicy(sizePolicy3)
        self.broadening_btn.setMinimumSize(QSize(0, 28))
        self.broadening_btn.setMaximumSize(QSize(40, 16777215))
        self.broadening_btn.setFont(font)

        self.horizontalLayout.addWidget(self.broadening_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.broadening_slider = QSlider(self.frame_4)
        self.broadening_slider.setObjectName(u"broadening_slider")
        self.broadening_slider.setFont(font)
        self.broadening_slider.setMinimum(5)
        self.broadening_slider.setMaximum(200)
        self.broadening_slider.setValue(40)
        self.broadening_slider.setOrientation(Qt.Horizontal)
        self.broadening_slider.setTickPosition(QSlider.TicksBothSides)
        self.broadening_slider.setTickInterval(15)

        self.gridLayout_2.addWidget(self.broadening_slider, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.line_2 = QFrame(self.frame_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 2)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(350, 0))
        self.frame_2.setFont(font)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.broadening_check = QCheckBox(self.frame_2)
        self.broadening_check.setObjectName(u"broadening_check")
        self.broadening_check.setFont(font)

        self.horizontalLayout_3.addWidget(self.broadening_check)

        self.broadening_select = QComboBox(self.frame_2)
        self.broadening_select.addItem("")
        self.broadening_select.addItem("")
        self.broadening_select.setObjectName(u"broadening_select")
        self.broadening_select.setMinimumSize(QSize(0, 28))
        self.broadening_select.setFont(font)

        self.horizontalLayout_3.addWidget(self.broadening_select)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setMinimumSize(QSize(0, 28))
        self.pushButton_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.export_values_btn = QPushButton(self.frame_2)
        self.export_values_btn.setObjectName(u"export_values_btn")
        self.export_values_btn.setEnabled(False)
        self.export_values_btn.setMinimumSize(QSize(0, 28))
        self.export_values_btn.setFont(font)

        self.horizontalLayout_4.addWidget(self.export_values_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.hide_verticals_check = QCheckBox(self.frame_2)
        self.hide_verticals_check.setObjectName(u"hide_verticals_check")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hide_verticals_check.sizePolicy().hasHeightForWidth())
        self.hide_verticals_check.setSizePolicy(sizePolicy4)
        self.hide_verticals_check.setFont(font)

        self.horizontalLayout_5.addWidget(self.hide_verticals_check)

        self.scale_curve_check = QCheckBox(self.frame_2)
        self.scale_curve_check.setObjectName(u"scale_curve_check")
        self.scale_curve_check.setFont(font)

        self.horizontalLayout_5.addWidget(self.scale_curve_check)

        self.scale_curve_inp = QLineEdit(self.frame_2)
        self.scale_curve_inp.setObjectName(u"scale_curve_inp")
        self.scale_curve_inp.setFont(font)
        self.scale_curve_inp.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)

        self.horizontalLayout_5.addWidget(self.scale_curve_inp)

        self.scale_curve_btn = QPushButton(self.frame_2)
        self.scale_curve_btn.setObjectName(u"scale_curve_btn")
        sizePolicy3.setHeightForWidth(self.scale_curve_btn.sizePolicy().hasHeightForWidth())
        self.scale_curve_btn.setSizePolicy(sizePolicy3)
        self.scale_curve_btn.setMinimumSize(QSize(0, 28))
        self.scale_curve_btn.setMaximumSize(QSize(40, 16777215))
        self.scale_curve_btn.setFont(font)

        self.horizontalLayout_5.addWidget(self.scale_curve_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        font5 = QFont()
        font5.setFamily(u"Noto Sans CJK TC")
        font5.setPointSize(10)
        self.label_2.setFont(font5)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.splitter.addWidget(self.frame)
        self.frame_5 = QFrame(self.splitter)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy5)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_8 = QHBoxLayout(self.page)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.spectrum_table = QTableWidget(self.page)
        self.spectrum_table.setObjectName(u"spectrum_table")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.spectrum_table.sizePolicy().hasHeightForWidth())
        self.spectrum_table.setSizePolicy(sizePolicy6)
        font6 = QFont()
        font6.setFamily(u"Serif")
        font6.setPointSize(10)
        self.spectrum_table.setFont(font6)
        self.spectrum_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.spectrum_table.setAlternatingRowColors(False)
        self.spectrum_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.spectrum_table.setShowGrid(True)
        self.spectrum_table.setGridStyle(Qt.SolidLine)
        self.spectrum_table.setSortingEnabled(True)
        self.spectrum_table.horizontalHeader().setCascadingSectionResizes(False)
        self.spectrum_table.horizontalHeader().setMinimumSectionSize(62)
        self.spectrum_table.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_8.addWidget(self.spectrum_table)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_9 = QHBoxLayout(self.page_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.optimization_list = QListWidget(self.page_2)
        self.optimization_list.setObjectName(u"optimization_list")
        font7 = QFont()
        font7.setFamily(u"Noto Mono")
        font7.setPointSize(12)
        self.optimization_list.setFont(font7)

        self.horizontalLayout_9.addWidget(self.optimization_list)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 200))
        self.frame_6.setMaximumSize(QSize(16777215, 220))
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 5)
        self.line = QFrame(self.frame_6)
        self.line.setObjectName(u"line")
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 5, 0, 1, 3)

        self.scale_y_inp = QLineEdit(self.frame_6)
        self.scale_y_inp.setObjectName(u"scale_y_inp")
        self.scale_y_inp.setMinimumSize(QSize(0, 28))
        self.scale_y_inp.setFont(font)
        self.scale_y_inp.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)

        self.gridLayout.addWidget(self.scale_y_inp, 4, 1, 1, 1)

        self.scale_x_check = QCheckBox(self.frame_6)
        self.scale_x_check.setObjectName(u"scale_x_check")
        sizePolicy4.setHeightForWidth(self.scale_x_check.sizePolicy().hasHeightForWidth())
        self.scale_x_check.setSizePolicy(sizePolicy4)
        self.scale_x_check.setFont(font)

        self.gridLayout.addWidget(self.scale_x_check, 3, 0, 1, 1)

        self.scale_x_inp = QLineEdit(self.frame_6)
        self.scale_x_inp.setObjectName(u"scale_x_inp")
        self.scale_x_inp.setMinimumSize(QSize(0, 28))
        self.scale_x_inp.setFont(font)
        self.scale_x_inp.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhFormattedNumbersOnly)

        self.gridLayout.addWidget(self.scale_x_inp, 3, 1, 1, 1)

        self.help_btn = QPushButton(self.frame_6)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setMinimumSize(QSize(0, 28))
        self.help_btn.setFont(font)

        self.gridLayout.addWidget(self.help_btn, 6, 0, 1, 1)

        self.show_numbers_check = QCheckBox(self.frame_6)
        self.show_numbers_check.setObjectName(u"show_numbers_check")
        self.show_numbers_check.setFont(font)

        self.gridLayout.addWidget(self.show_numbers_check, 2, 0, 1, 3, Qt.AlignBottom)

        self.copy_values_btn = QPushButton(self.frame_6)
        self.copy_values_btn.setObjectName(u"copy_values_btn")
        self.copy_values_btn.setEnabled(False)
        self.copy_values_btn.setMinimumSize(QSize(0, 28))
        self.copy_values_btn.setFont(font)

        self.gridLayout.addWidget(self.copy_values_btn, 0, 2, 1, 1)

        self.scale_y_check = QCheckBox(self.frame_6)
        self.scale_y_check.setObjectName(u"scale_y_check")
        sizePolicy4.setHeightForWidth(self.scale_y_check.sizePolicy().hasHeightForWidth())
        self.scale_y_check.setSizePolicy(sizePolicy4)
        self.scale_y_check.setFont(font)

        self.gridLayout.addWidget(self.scale_y_check, 4, 0, 1, 1)

        self.import_values_btn = QPushButton(self.frame_6)
        self.import_values_btn.setObjectName(u"import_values_btn")
        self.import_values_btn.setEnabled(False)
        self.import_values_btn.setMinimumSize(QSize(0, 28))
        self.import_values_btn.setFont(font)

        self.gridLayout.addWidget(self.import_values_btn, 0, 0, 1, 2)

        self.close_btn = QPushButton(self.frame_6)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 28))
        self.close_btn.setFont(font)

        self.gridLayout.addWidget(self.close_btn, 6, 2, 1, 1)

        self.scale_y_btn = QPushButton(self.frame_6)
        self.scale_y_btn.setObjectName(u"scale_y_btn")
        self.scale_y_btn.setMinimumSize(QSize(0, 28))
        self.scale_y_btn.setMaximumSize(QSize(16777215, 16777215))
        self.scale_y_btn.setFont(font)

        self.gridLayout.addWidget(self.scale_y_btn, 4, 2, 1, 1)

        self.scale_x_btn = QPushButton(self.frame_6)
        self.scale_x_btn.setObjectName(u"scale_x_btn")
        self.scale_x_btn.setMinimumSize(QSize(0, 28))
        self.scale_x_btn.setMaximumSize(QSize(16777215, 16777215))
        self.scale_x_btn.setFont(font)

        self.gridLayout.addWidget(self.scale_x_btn, 3, 2, 1, 1)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.splitter.addWidget(self.frame_5)

        self.verticalLayout_2.addWidget(self.splitter)


        self.horizontalLayout_10.addWidget(self.mainFrame)

        SpectrumAnalyzer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SpectrumAnalyzer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1108, 22))
        SpectrumAnalyzer.setMenuBar(self.menubar)

        self.retranslateUi(SpectrumAnalyzer)

        self.spectrumTabWidget.setCurrentIndex(0)
        self.start_animation_btn.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SpectrumAnalyzer)
    # setupUi

    def retranslateUi(self, SpectrumAnalyzer):
        SpectrumAnalyzer.setWindowTitle(QCoreApplication.translate("SpectrumAnalyzer", u"MainWindow", None))
        self.spectrums_select.setItemText(0, QCoreApplication.translate("SpectrumAnalyzer", u"IR Spectrum", None))
        self.spectrums_select.setItemText(1, QCoreApplication.translate("SpectrumAnalyzer", u"Raman Activity", None))
        self.spectrums_select.setItemText(2, QCoreApplication.translate("SpectrumAnalyzer", u"FRC Constants", None))
        self.spectrums_select.setItemText(3, QCoreApplication.translate("SpectrumAnalyzer", u"Red Masses", None))
        self.spectrums_select.setItemText(4, QCoreApplication.translate("SpectrumAnalyzer", u"Depolar (P)", None))
        self.spectrums_select.setItemText(5, QCoreApplication.translate("SpectrumAnalyzer", u"Depolar (U)", None))

        self.loaded_file_name.setText("")
        self.spectrumTabWidget.setTabText(self.spectrumTabWidget.indexOf(self.spectrumFrame2), QCoreApplication.translate("SpectrumAnalyzer", u"Spectrum Graph", None))
        self.spectrumTabWidget.setTabText(self.spectrumTabWidget.indexOf(self.render_frame), QCoreApplication.translate("SpectrumAnalyzer", u"3D Optimization", None))
        self.log_file_text.setHtml(QCoreApplication.translate("SpectrumAnalyzer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Courier'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>", None))
        self.log_file_text.setPlaceholderText(QCoreApplication.translate("SpectrumAnalyzer", u"LOG File", None))
        self.spectrumTabWidget.setTabText(self.spectrumTabWidget.indexOf(self.log_file_frame), QCoreApplication.translate("SpectrumAnalyzer", u"LOG File", None))
        self.zoom_out_btn.setText("")
        self.tight_graph_btn.setText("")
        self.start_animation_btn.setText("")
        self.intensity_label.setText("")
        self.style_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Style", None))
        self.export_graph_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Export graph", None))
        self.show_peaks_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Show peaks", None))
        self.show_marks_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Show marks", None))
        self.label.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Broaden Sigma", None))
        self.broadening_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"OK", None))
        self.broadening_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Broaden bonds", None))
        self.broadening_select.setItemText(0, QCoreApplication.translate("SpectrumAnalyzer", u"Gaussian Broadening", None))
        self.broadening_select.setItemText(1, QCoreApplication.translate("SpectrumAnalyzer", u"Lorezeten Broadening", None))

        self.pushButton_7.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Interpolate coordinate", None))
        self.export_values_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Export Values", None))
        self.hide_verticals_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Hide spikes", None))
        self.scale_curve_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Scale curve", None))
        self.scale_curve_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"OK", None))
        self.label_2.setText(QCoreApplication.translate("SpectrumAnalyzer", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#204a87;\">Created and maintained by: Moaz Mohammed El-Essawey</span></p></body></html>", None))
        self.scale_x_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Scale X", None))
        self.help_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Help", None))
        self.show_numbers_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Show numbers", None))
        self.copy_values_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Copy", None))
        self.scale_y_check.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Scale Y", None))
        self.import_values_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Import Values", None))
        self.close_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"Close", None))
        self.scale_y_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"OK", None))
        self.scale_x_btn.setText(QCoreApplication.translate("SpectrumAnalyzer", u"OK", None))
    # retranslateUi

