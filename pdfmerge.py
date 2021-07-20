# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfmerge.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import PyPDF2
import sys

def merge_page(writer, merge_file):
    # 获取 PdfFileReader 对象
    pdf_file_reader = PyPDF2.PdfFileReader(merge_file)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    num_pages = pdf_file_reader.getNumPages()

    for index in range(0, num_pages):
        page_obj = pdf_file_reader.getPage(index)
        writer.addPage(page_obj)  # 根据每页返回的 PageObject,写入到文件

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # if not MainWindow.objectName():
        
        MainWindow.resize(866, 663)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_out = QLineEdit(self.centralwidget)
        self.lineEdit_out.setObjectName(u"lineEdit_out")

        self.horizontalLayout.addWidget(self.lineEdit_out)

        self.pushButton_select = QPushButton(self.centralwidget)
        self.pushButton_select.setObjectName(u"pushButton_select")

        self.horizontalLayout.addWidget(self.pushButton_select)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget_file = QListWidget(self.groupBox)
        self.listWidget_file.setObjectName(u"listWidget_file")

        self.gridLayout.addWidget(self.listWidget_file, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_add = QPushButton(self.groupBox)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.verticalLayout.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(self.groupBox)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout.addWidget(self.pushButton_delete)

        self.pushButton_up = QPushButton(self.groupBox)
        self.pushButton_up.setObjectName(u"pushButton_up")

        self.verticalLayout.addWidget(self.pushButton_up)

        self.pushButton_down = QPushButton(self.groupBox)
        self.pushButton_down.setObjectName(u"pushButton_down")

        self.verticalLayout.addWidget(self.pushButton_down)

        self.pushButton_clear = QPushButton(self.groupBox)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.verticalLayout.addWidget(self.pushButton_clear)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_do = QPushButton(self.centralwidget)
        self.pushButton_do.setObjectName(u"pushButton_do")

        self.horizontalLayout_2.addWidget(self.pushButton_do)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 15)
        self.gridLayout_2.setRowStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        MainWindow.setWindowTitle(u"PDF合并工具")
        QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_select.clicked.connect(self.selectOutputFile)
        self.pushButton_add.clicked.connect(self.addFile)
        self.pushButton_delete.clicked.connect(self.deleteFile)
        self.pushButton_clear.clicked.connect(self.clearFiles)
        self.pushButton_do.clicked.connect(self.generatePdf)
        self.pushButton_up.clicked.connect(self.pushUpFile)
        self.pushButton_down.clicked.connect(self.pushDownFile)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pushButton_select.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u6587\u4ef6\u5217\u8868", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_up.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u79fb", None))
        self.pushButton_down.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u79fb", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_do.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
    # retranslateUi

    def selectOutputFile(self):
        dialog = QFileDialog(None, '请选择输出路径', '', '所有pdf文件 (*.pdf *.PDF)')
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.lineEdit_out.setText(fileNames[0])

    def addFile(self):
        dialog = QFileDialog(None, '请选择PDF文件', '', '所有pdf文件 (*.pdf *.PDF)')
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.listWidget_file.addItem(fileNames[0])
    
    def deleteFile(self):
        del_item = self.listWidget_file.currentItem()
        self.listWidget_file.takeItem(self.listWidget_file.row(del_item))
        # del del_list

    def clearFiles(self):
        self.listWidget_file.clear()

    def pushUpFile(self):
        cur_item = self.listWidget_file.currentItem()
        cur_row = self.listWidget_file.row(cur_item)
        if cur_row <= 0:
            return
        else:
            txt1 = self.listWidget_file.item(cur_row - 1).text()
            txt2 = self.listWidget_file.item(cur_row).text()
            self.listWidget_file.item(cur_row - 1).setText(txt2)
            self.listWidget_file.item(cur_row).setText(txt1)
            self.listWidget_file.setCurrentRow(cur_row - 1)

    def pushDownFile(self):
        cur_item = self.listWidget_file.currentItem()
        cur_row = self.listWidget_file.row(cur_item)
        if cur_row >= self.listWidget_file.count() - 1 or cur_row < 0:
            return
        else:
            txt1 = self.listWidget_file.item(cur_row + 1).text()
            txt2 = self.listWidget_file.item(cur_row).text()
            self.listWidget_file.item(cur_row + 1).setText(txt2)
            self.listWidget_file.item(cur_row).setText(txt1)
            self.listWidget_file.setCurrentRow(cur_row + 1)

    def generatePdf(self):
        output_file = self.lineEdit_out.text()
        if not output_file:
            warn = QMessageBox()
            warn.warning(None, '提示', '请输入输出路径！')
            return
        merge_files = [self.listWidget_file.item(index).text() for index in range(self.listWidget_file.count())]
        if not merge_files:
            warn = QMessageBox()
            warn.warning(None, '提示', '请选择需要合并的pdf文件！')
            return
        pdf_file_writer = PyPDF2.PdfFileWriter()
        for merge_file in merge_files:
            merge_page(pdf_file_writer, merge_file)

        pdf_file_writer.write(open(output_file, 'wb'))
        tip = QMessageBox()
        tip.information(None, '提示', '合并完成！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
