# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 573)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_ingresarProcesos = QGroupBox(self.tab)
        self.groupBox_ingresarProcesos.setObjectName(u"groupBox_ingresarProcesos")
        self.formLayout = QFormLayout(self.groupBox_ingresarProcesos)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_ingresarProcesos)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinBox_numeroProcesos = QSpinBox(self.groupBox_ingresarProcesos)
        self.spinBox_numeroProcesos.setObjectName(u"spinBox_numeroProcesos")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox_numeroProcesos)

        self.pushButton_agregarProcesos = QPushButton(self.groupBox_ingresarProcesos)
        self.pushButton_agregarProcesos.setObjectName(u"pushButton_agregarProcesos")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton_agregarProcesos)


        self.gridLayout_5.addWidget(self.groupBox_ingresarProcesos, 0, 0, 1, 1)

        self.groupBox_listaProcesos = QGroupBox(self.tab)
        self.groupBox_listaProcesos.setObjectName(u"groupBox_listaProcesos")
        self.horizontalLayout = QHBoxLayout(self.groupBox_listaProcesos)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit_listaProcesos = QPlainTextEdit(self.groupBox_listaProcesos)
        self.plainTextEdit_listaProcesos.setObjectName(u"plainTextEdit_listaProcesos")

        self.horizontalLayout.addWidget(self.plainTextEdit_listaProcesos)


        self.gridLayout_5.addWidget(self.groupBox_listaProcesos, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lineEdit_lotesPendientes = QLineEdit(self.groupBox_2)
        self.lineEdit_lotesPendientes.setObjectName(u"lineEdit_lotesPendientes")
        self.lineEdit_lotesPendientes.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_lotesPendientes, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 1, 0, 1, 1)

        self.pushButton_iniciar = QPushButton(self.groupBox_2)
        self.pushButton_iniciar.setObjectName(u"pushButton_iniciar")

        self.gridLayout_6.addWidget(self.pushButton_iniciar, 2, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.lcdNumber = QLCDNumber(self.groupBox_2)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.gridLayout_6.addWidget(self.lcdNumber, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableWidget_procesoEjecucion = QTableWidget(self.groupBox_4)
        if (self.tableWidget_procesoEjecucion.columnCount() < 1):
            self.tableWidget_procesoEjecucion.setColumnCount(1)
        if (self.tableWidget_procesoEjecucion.rowCount() < 5):
            self.tableWidget_procesoEjecucion.setRowCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_procesoEjecucion.setVerticalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_procesoEjecucion.setObjectName(u"tableWidget_procesoEjecucion")
        self.tableWidget_procesoEjecucion.setRowCount(5)
        self.tableWidget_procesoEjecucion.setColumnCount(1)

        self.gridLayout_2.addWidget(self.tableWidget_procesoEjecucion, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 2, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_3 = QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_procesosTerminados = QTableWidget(self.groupBox_5)
        if (self.tableWidget_procesosTerminados.columnCount() < 5):
            self.tableWidget_procesosTerminados.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_procesosTerminados.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tableWidget_procesosTerminados.setObjectName(u"tableWidget_procesosTerminados")
        self.tableWidget_procesosTerminados.setColumnCount(5)

        self.gridLayout_3.addWidget(self.tableWidget_procesosTerminados, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_5, 2, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget_loteEjecucion = QTableWidget(self.groupBox_3)
        if (self.tableWidget_loteEjecucion.columnCount() < 2):
            self.tableWidget_loteEjecucion.setColumnCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_loteEjecucion.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_loteEjecucion.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        self.tableWidget_loteEjecucion.setObjectName(u"tableWidget_loteEjecucion")
        self.tableWidget_loteEjecucion.setRowCount(0)
        self.tableWidget_loteEjecucion.setColumnCount(2)

        self.gridLayout.addWidget(self.tableWidget_loteEjecucion, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 624, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton_agregarProcesos, self.lineEdit_lotesPendientes)
        QWidget.setTabOrder(self.lineEdit_lotesPendientes, self.tableWidget_loteEjecucion)
        QWidget.setTabOrder(self.tableWidget_loteEjecucion, self.tableWidget_procesoEjecucion)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_ingresarProcesos.setTitle(QCoreApplication.translate("MainWindow", u"Ingresar Procesos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Numero de Procesos", None))
        self.pushButton_agregarProcesos.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_listaProcesos.setTitle(QCoreApplication.translate("MainWindow", u"Lista de Procesos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Lotes Pendientes", None))
        self.pushButton_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contador Global", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Proceso en ejecuci\u00f3n", None))
        ___qtablewidgetitem = self.tableWidget_procesoEjecucion.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem1 = self.tableWidget_procesoEjecucion.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem2 = self.tableWidget_procesoEjecucion.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tiempo Estimado", None));
        ___qtablewidgetitem3 = self.tableWidget_procesoEjecucion.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tiempo Transcurrido", None));
        ___qtablewidgetitem4 = self.tableWidget_procesoEjecucion.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tiempo Restante", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Procesos terminados", None))
        ___qtablewidgetitem5 = self.tableWidget_procesosTerminados.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem6 = self.tableWidget_procesosTerminados.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Primer Dato", None));
        ___qtablewidgetitem7 = self.tableWidget_procesosTerminados.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem8 = self.tableWidget_procesosTerminados.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Segundo Dato", None));
        ___qtablewidgetitem9 = self.tableWidget_procesosTerminados.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Lote en ejecuci\u00f3n", None))
        ___qtablewidgetitem10 = self.tableWidget_loteEjecucion.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Programa", None));
        ___qtablewidgetitem11 = self.tableWidget_loteEjecucion.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Tiempo Estimado", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Procesos", None))
    # retranslateUi

