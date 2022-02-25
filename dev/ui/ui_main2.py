# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SpectrumAnalyzer(object):
    def setupUi(self, SpectrumAnalyzer):
        SpectrumAnalyzer.setObjectName("SpectrumAnalyzer")
        SpectrumAnalyzer.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(SpectrumAnalyzer)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.mainFrame.setFont(font)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.spectrumTabWidget = QtWidgets.QTabWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrumTabWidget.sizePolicy().hasHeightForWidth())
        self.spectrumTabWidget.setSizePolicy(sizePolicy)
        self.spectrumTabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.spectrumTabWidget.setFont(font)
        self.spectrumTabWidget.setStyleSheet("QFrame#spectrumFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.spectrumTabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.spectrumTabWidget.setObjectName("spectrumTabWidget")
        self.spectrumFrame = QtWidgets.QWidget()
        self.spectrumFrame.setObjectName("spectrumFrame")
        self.spectrum_frame_layout = QtWidgets.QVBoxLayout(self.spectrumFrame)
        self.spectrum_frame_layout.setContentsMargins(5, 5, 5, 5)
        self.spectrum_frame_layout.setSpacing(5)
        self.spectrum_frame_layout.setObjectName("spectrum_frame_layout")
        self.frame_7 = QtWidgets.QFrame(self.spectrumFrame)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(0, 2, 3, 3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.spectrums_select = QtWidgets.QComboBox(self.frame_3)
        self.spectrums_select.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.spectrums_select.setFont(font)
        self.spectrums_select.setObjectName("spectrums_select")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.spectrums_select.addItem("")
        self.horizontalLayout_7.addWidget(self.spectrums_select)
        self.loaded_file_name = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loaded_file_name.sizePolicy().hasHeightForWidth())
        self.loaded_file_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.loaded_file_name.setFont(font)
        self.loaded_file_name.setText("")
        self.loaded_file_name.setWordWrap(True)
        self.loaded_file_name.setIndent(3)
        self.loaded_file_name.setObjectName("loaded_file_name")
        self.horizontalLayout_7.addWidget(self.loaded_file_name)
        self.spectrumType = QtWidgets.QComboBox(self.frame_3)
        self.spectrumType.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        self.spectrumType.setFont(font)
        self.spectrumType.setObjectName("spectrumType")
        self.horizontalLayout_7.addWidget(self.spectrumType)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.spectrum_frame_layout.addWidget(self.frame_7)
        self.spectrumTabWidget.addTab(self.spectrumFrame, "")
        self.render_frame = QtWidgets.QWidget()
        self.render_frame.setObjectName("render_frame")
        self.renderLayout = QtWidgets.QVBoxLayout(self.render_frame)
        self.renderLayout.setContentsMargins(0, 0, 0, 0)
        self.renderLayout.setSpacing(0)
        self.renderLayout.setObjectName("renderLayout")
        self.spectrumTabWidget.addTab(self.render_frame, "")
        self.verticalLayout_4.addWidget(self.spectrumTabWidget)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 160))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.zoom_out_btn = QtWidgets.QPushButton(self.frame_4)
        self.zoom_out_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.zoom_out_btn.setFont(font)
        self.zoom_out_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../icons/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out_btn.setIcon(icon)
        self.zoom_out_btn.setIconSize(QtCore.QSize(20, 20))
        self.zoom_out_btn.setObjectName("zoom_out_btn")
        self.horizontalLayout_6.addWidget(self.zoom_out_btn)
        self.tight_graph_btn = QtWidgets.QPushButton(self.frame_4)
        self.tight_graph_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.tight_graph_btn.setFont(font)
        self.tight_graph_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/aspect-ratio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tight_graph_btn.setIcon(icon1)
        self.tight_graph_btn.setIconSize(QtCore.QSize(20, 20))
        self.tight_graph_btn.setObjectName("tight_graph_btn")
        self.horizontalLayout_6.addWidget(self.tight_graph_btn)
        self.start_animation_btn = QtWidgets.QPushButton(self.frame_4)
        self.start_animation_btn.setEnabled(True)
        self.start_animation_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.start_animation_btn.setFont(font)
        self.start_animation_btn.setStyleSheet("")
        self.start_animation_btn.setText("")
        self.start_animation_btn.setIconSize(QtCore.QSize(20, 20))
        self.start_animation_btn.setAutoDefault(False)
        self.start_animation_btn.setDefault(False)
        self.start_animation_btn.setObjectName("start_animation_btn")
        self.horizontalLayout_6.addWidget(self.start_animation_btn)
        self.intensity_label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intensity_label.sizePolicy().hasHeightForWidth())
        self.intensity_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.intensity_label.setFont(font)
        self.intensity_label.setText("")
        self.intensity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.intensity_label.setWordWrap(True)
        self.intensity_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.intensity_label.setObjectName("intensity_label")
        self.horizontalLayout_6.addWidget(self.intensity_label)
        self.style_btn = QtWidgets.QPushButton(self.frame_4)
        self.style_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.style_btn.setFont(font)
        self.style_btn.setObjectName("style_btn")
        self.horizontalLayout_6.addWidget(self.style_btn)
        self.export_graph_btn = QtWidgets.QPushButton(self.frame_4)
        self.export_graph_btn.setMinimumSize(QtCore.QSize(110, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.export_graph_btn.setFont(font)
        self.export_graph_btn.setObjectName("export_graph_btn")
        self.horizontalLayout_6.addWidget(self.export_graph_btn)
        self.export_formats_select = QtWidgets.QComboBox(self.frame_4)
        self.export_formats_select.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.export_formats_select.setFont(font)
        self.export_formats_select.setObjectName("export_formats_select")
        self.horizontalLayout_6.addWidget(self.export_formats_select)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.frame_4)
        self.widget_2.setMinimumSize(QtCore.QSize(20, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_peaks_check = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.show_peaks_check.setFont(font)
        self.show_peaks_check.setObjectName("show_peaks_check")
        self.horizontalLayout_2.addWidget(self.show_peaks_check)
        self.peaks_select = QtWidgets.QComboBox(self.frame_4)
        self.peaks_select.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.peaks_select.setFont(font)
        self.peaks_select.setObjectName("peaks_select")
        self.horizontalLayout_2.addWidget(self.peaks_select)
        self.show_marks_check = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.show_marks_check.setFont(font)
        self.show_marks_check.setObjectName("show_marks_check")
        self.horizontalLayout_2.addWidget(self.show_marks_check)
        self.marks_select = QtWidgets.QComboBox(self.frame_4)
        self.marks_select.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.marks_select.setFont(font)
        self.marks_select.setObjectName("marks_select")
        self.horizontalLayout_2.addWidget(self.marks_select)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.broadening_inp = QtWidgets.QLineEdit(self.frame_4)
        self.broadening_inp.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.broadening_inp.setFont(font)
        self.broadening_inp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.broadening_inp.setObjectName("broadening_inp")
        self.horizontalLayout.addWidget(self.broadening_inp)
        self.broadening_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadening_btn.sizePolicy().hasHeightForWidth())
        self.broadening_btn.setSizePolicy(sizePolicy)
        self.broadening_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.broadening_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.broadening_btn.setFont(font)
        self.broadening_btn.setObjectName("broadening_btn")
        self.horizontalLayout.addWidget(self.broadening_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.broadening_slider = QtWidgets.QSlider(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.broadening_slider.setFont(font)
        self.broadening_slider.setMinimum(5)
        self.broadening_slider.setMaximum(200)
        self.broadening_slider.setProperty("value", 40)
        self.broadening_slider.setOrientation(QtCore.Qt.Horizontal)
        self.broadening_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.broadening_slider.setTickInterval(15)
        self.broadening_slider.setObjectName("broadening_slider")
        self.gridLayout_2.addWidget(self.broadening_slider, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.frame_2.setFont(font)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.broadening_check = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.broadening_check.setFont(font)
        self.broadening_check.setObjectName("broadening_check")
        self.horizontalLayout_3.addWidget(self.broadening_check)
        self.broadening_select = QtWidgets.QComboBox(self.frame_2)
        self.broadening_select.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.broadening_select.setFont(font)
        self.broadening_select.setObjectName("broadening_select")
        self.broadening_select.addItem("")
        self.broadening_select.addItem("")
        self.horizontalLayout_3.addWidget(self.broadening_select)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.export_values_btn = QtWidgets.QPushButton(self.frame_2)
        self.export_values_btn.setEnabled(False)
        self.export_values_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.export_values_btn.setFont(font)
        self.export_values_btn.setObjectName("export_values_btn")
        self.horizontalLayout_4.addWidget(self.export_values_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.hide_verticals_check = QtWidgets.QCheckBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hide_verticals_check.sizePolicy().hasHeightForWidth())
        self.hide_verticals_check.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.hide_verticals_check.setFont(font)
        self.hide_verticals_check.setObjectName("hide_verticals_check")
        self.horizontalLayout_5.addWidget(self.hide_verticals_check)
        self.scale_curve_check = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_curve_check.setFont(font)
        self.scale_curve_check.setObjectName("scale_curve_check")
        self.horizontalLayout_5.addWidget(self.scale_curve_check)
        self.scale_curve_inp = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_curve_inp.setFont(font)
        self.scale_curve_inp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.scale_curve_inp.setObjectName("scale_curve_inp")
        self.horizontalLayout_5.addWidget(self.scale_curve_inp)
        self.scale_curve_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_curve_btn.sizePolicy().hasHeightForWidth())
        self.scale_curve_btn.setSizePolicy(sizePolicy)
        self.scale_curve_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.scale_curve_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_curve_btn.setFont(font)
        self.scale_curve_btn.setObjectName("scale_curve_btn")
        self.horizontalLayout_5.addWidget(self.scale_curve_btn)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(350, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spectrum_table = QtWidgets.QTableWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrum_table.sizePolicy().hasHeightForWidth())
        self.spectrum_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(10)
        self.spectrum_table.setFont(font)
        self.spectrum_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.spectrum_table.setAlternatingRowColors(False)
        self.spectrum_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.spectrum_table.setShowGrid(True)
        self.spectrum_table.setGridStyle(QtCore.Qt.SolidLine)
        self.spectrum_table.setObjectName("spectrum_table")
        self.spectrum_table.setColumnCount(0)
        self.spectrum_table.setRowCount(0)
        self.spectrum_table.horizontalHeader().setCascadingSectionResizes(False)
        self.spectrum_table.horizontalHeader().setMinimumSectionSize(62)
        self.spectrum_table.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_8.addWidget(self.spectrum_table)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.optimization_list = QtWidgets.QListWidget(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(12)
        self.optimization_list.setFont(font)
        self.optimization_list.setObjectName("optimization_list")
        self.horizontalLayout_9.addWidget(self.optimization_list)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setContentsMargins(9, 9, 9, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 3)
        self.scale_y_inp = QtWidgets.QLineEdit(self.frame_6)
        self.scale_y_inp.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_y_inp.setFont(font)
        self.scale_y_inp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.scale_y_inp.setObjectName("scale_y_inp")
        self.gridLayout.addWidget(self.scale_y_inp, 4, 1, 1, 1)
        self.scale_x_check = QtWidgets.QCheckBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_x_check.sizePolicy().hasHeightForWidth())
        self.scale_x_check.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_x_check.setFont(font)
        self.scale_x_check.setObjectName("scale_x_check")
        self.gridLayout.addWidget(self.scale_x_check, 3, 0, 1, 1)
        self.scale_x_inp = QtWidgets.QLineEdit(self.frame_6)
        self.scale_x_inp.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_x_inp.setFont(font)
        self.scale_x_inp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly)
        self.scale_x_inp.setObjectName("scale_x_inp")
        self.gridLayout.addWidget(self.scale_x_inp, 3, 1, 1, 1)
        self.help_btn = QtWidgets.QPushButton(self.frame_6)
        self.help_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.help_btn.setFont(font)
        self.help_btn.setObjectName("help_btn")
        self.gridLayout.addWidget(self.help_btn, 6, 0, 1, 1)
        self.show_numbers_check = QtWidgets.QCheckBox(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.show_numbers_check.setFont(font)
        self.show_numbers_check.setObjectName("show_numbers_check")
        self.gridLayout.addWidget(self.show_numbers_check, 2, 0, 1, 3, QtCore.Qt.AlignBottom)
        self.copy_values_btn = QtWidgets.QPushButton(self.frame_6)
        self.copy_values_btn.setEnabled(False)
        self.copy_values_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.copy_values_btn.setFont(font)
        self.copy_values_btn.setObjectName("copy_values_btn")
        self.gridLayout.addWidget(self.copy_values_btn, 0, 2, 1, 1)
        self.scale_y_check = QtWidgets.QCheckBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scale_y_check.sizePolicy().hasHeightForWidth())
        self.scale_y_check.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_y_check.setFont(font)
        self.scale_y_check.setObjectName("scale_y_check")
        self.gridLayout.addWidget(self.scale_y_check, 4, 0, 1, 1)
        self.import_values_btn = QtWidgets.QPushButton(self.frame_6)
        self.import_values_btn.setEnabled(False)
        self.import_values_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.import_values_btn.setFont(font)
        self.import_values_btn.setObjectName("import_values_btn")
        self.gridLayout.addWidget(self.import_values_btn, 0, 0, 1, 2)
        self.close_btn = QtWidgets.QPushButton(self.frame_6)
        self.close_btn.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")
        self.gridLayout.addWidget(self.close_btn, 6, 2, 1, 1)
        self.scale_y_btn = QtWidgets.QPushButton(self.frame_6)
        self.scale_y_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.scale_y_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_y_btn.setFont(font)
        self.scale_y_btn.setObjectName("scale_y_btn")
        self.gridLayout.addWidget(self.scale_y_btn, 4, 2, 1, 1)
        self.scale_x_btn = QtWidgets.QPushButton(self.frame_6)
        self.scale_x_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.scale_x_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.scale_x_btn.setFont(font)
        self.scale_x_btn.setObjectName("scale_x_btn")
        self.gridLayout.addWidget(self.scale_x_btn, 3, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(10)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 3)
        self.verticalLayout_3.addWidget(self.frame_6, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout_10.addWidget(self.mainFrame)
        SpectrumAnalyzer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpectrumAnalyzer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        SpectrumAnalyzer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpectrumAnalyzer)
        self.statusbar.setObjectName("statusbar")
        SpectrumAnalyzer.setStatusBar(self.statusbar)

        self.retranslateUi(SpectrumAnalyzer)
        self.spectrumTabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SpectrumAnalyzer)

    def retranslateUi(self, SpectrumAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        SpectrumAnalyzer.setWindowTitle(_translate("SpectrumAnalyzer", "MainWindow"))
        self.spectrums_select.setItemText(0, _translate("SpectrumAnalyzer", "IR Intensities"))
        self.spectrums_select.setItemText(1, _translate("SpectrumAnalyzer", "Raman Activity"))
        self.spectrums_select.setItemText(2, _translate("SpectrumAnalyzer", "FRC Consts"))
        self.spectrums_select.setItemText(3, _translate("SpectrumAnalyzer", "Red Masses"))
        self.spectrums_select.setItemText(4, _translate("SpectrumAnalyzer", "Depolar (P)"))
        self.spectrums_select.setItemText(5, _translate("SpectrumAnalyzer", "Depolar (U)"))
        self.spectrumTabWidget.setTabText(self.spectrumTabWidget.indexOf(self.spectrumFrame), _translate("SpectrumAnalyzer", "Spectrum Graph"))
        self.spectrumTabWidget.setTabText(self.spectrumTabWidget.indexOf(self.render_frame), _translate("SpectrumAnalyzer", "3D Model"))
        self.style_btn.setText(_translate("SpectrumAnalyzer", "Style"))
        self.export_graph_btn.setText(_translate("SpectrumAnalyzer", "Export graph"))
        self.show_peaks_check.setText(_translate("SpectrumAnalyzer", "Show peaks"))
        self.show_marks_check.setText(_translate("SpectrumAnalyzer", "Show marks"))
        self.label.setText(_translate("SpectrumAnalyzer", "Broaden Sigma"))
        self.broadening_btn.setText(_translate("SpectrumAnalyzer", "OK"))
        self.broadening_check.setText(_translate("SpectrumAnalyzer", "Broaden bonds"))
        self.broadening_select.setItemText(0, _translate("SpectrumAnalyzer", "Gaussian Broadening"))
        self.broadening_select.setItemText(1, _translate("SpectrumAnalyzer", "Lorezeten Broadening"))
        self.pushButton_7.setText(_translate("SpectrumAnalyzer", "Interpolate coordinate"))
        self.export_values_btn.setText(_translate("SpectrumAnalyzer", "Export Values"))
        self.hide_verticals_check.setText(_translate("SpectrumAnalyzer", "Hide spikes"))
        self.scale_curve_check.setText(_translate("SpectrumAnalyzer", "Scale curve"))
        self.scale_curve_btn.setText(_translate("SpectrumAnalyzer", "OK"))
        self.spectrum_table.setSortingEnabled(True)
        self.scale_x_check.setText(_translate("SpectrumAnalyzer", "Scale X"))
        self.help_btn.setText(_translate("SpectrumAnalyzer", "Help"))
        self.show_numbers_check.setText(_translate("SpectrumAnalyzer", "Show numbers"))
        self.copy_values_btn.setText(_translate("SpectrumAnalyzer", "Copy"))
        self.scale_y_check.setText(_translate("SpectrumAnalyzer", "Scale Y"))
        self.import_values_btn.setText(_translate("SpectrumAnalyzer", "Import Values"))
        self.close_btn.setText(_translate("SpectrumAnalyzer", "Close"))
        self.scale_y_btn.setText(_translate("SpectrumAnalyzer", "OK"))
        self.scale_x_btn.setText(_translate("SpectrumAnalyzer", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpectrumAnalyzer = QtWidgets.QMainWindow()
    ui = Ui_SpectrumAnalyzer()
    ui.setupUi(SpectrumAnalyzer)
    SpectrumAnalyzer.show()
    sys.exit(app.exec_())