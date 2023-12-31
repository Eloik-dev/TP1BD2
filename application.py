# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 942)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 141, 68))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.book = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.book.setContentsMargins(0, 0, 0, 0)
        self.book.setSpacing(4)
        self.book.setObjectName("book")
        self.book_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.book_label.setFont(font)
        self.book_label.setObjectName("book_label")
        self.book.addWidget(self.book_label)
        self.books_dropdown = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.books_dropdown.setObjectName("books_dropdown")
        self.book.addWidget(self.books_dropdown)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(460, 10, 481, 641))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.chapter = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.chapter.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.chapter.setContentsMargins(0, 0, 0, 0)
        self.chapter.setObjectName("chapter")
        self.chapter_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.chapter_label.setFont(font)
        self.chapter_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chapter_label.setObjectName("chapter_label")
        self.chapter.addWidget(self.chapter_label, 0, QtCore.Qt.AlignHCenter)
        self.chapter_text = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.chapter_text.setReadOnly(True)
        self.chapter_text.setObjectName("chapter_text")
        self.chapter.addWidget(self.chapter_text)
        self.chapter_dropdown = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.chapter_dropdown.setMinimumSize(QtCore.QSize(150, 0))
        self.chapter_dropdown.setMaximumSize(QtCore.QSize(100, 16777215))
        self.chapter_dropdown.setEditable(False)
        self.chapter_dropdown.setCurrentText("")
        self.chapter_dropdown.setObjectName("chapter_dropdown")
        self.chapter.addWidget(self.chapter_dropdown, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 90, 371, 765))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.fiche_aventure = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.fiche_aventure.setContentsMargins(0, 0, 0, 0)
        self.fiche_aventure.setSpacing(25)
        self.fiche_aventure.setObjectName("fiche_aventure")
        self.disciplines_armes = QtWidgets.QHBoxLayout()
        self.disciplines_armes.setObjectName("disciplines_armes")
        self.disciplines = QtWidgets.QVBoxLayout()
        self.disciplines.setContentsMargins(-1, -1, -1, 0)
        self.disciplines.setSpacing(4)
        self.disciplines.setObjectName("disciplines")
        self.disciplines_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disciplines_label.sizePolicy().hasHeightForWidth())
        self.disciplines_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.disciplines_label.setFont(font)
        self.disciplines_label.setObjectName("disciplines_label")
        self.disciplines.addWidget(self.disciplines_label)
        self.disciplines_list = QtWidgets.QListWidget(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disciplines_list.sizePolicy().hasHeightForWidth())
        self.disciplines_list.setSizePolicy(sizePolicy)
        self.disciplines_list.setMaximumSize(QtCore.QSize(16777215, 95))
        self.disciplines_list.setObjectName("disciplines_list")
        item = QtWidgets.QListWidgetItem()
        self.disciplines_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.disciplines_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.disciplines_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.disciplines_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.disciplines_list.addItem(item)
        self.disciplines.addWidget(self.disciplines_list)
        self.disciplines_actions = QtWidgets.QVBoxLayout()
        self.disciplines_actions.setContentsMargins(25, -1, 25, -1)
        self.disciplines_actions.setSpacing(6)
        self.disciplines_actions.setObjectName("disciplines_actions")
        self.disciplines_dropdown = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.disciplines_dropdown.setEditable(False)
        self.disciplines_dropdown.setCurrentText("")
        self.disciplines_dropdown.setObjectName("disciplines_dropdown")
        self.disciplines_actions.addWidget(self.disciplines_dropdown)
        self.disciplines_suppr_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.disciplines_suppr_btn.setObjectName("disciplines_suppr_btn")
        self.disciplines_actions.addWidget(self.disciplines_suppr_btn)
        self.disciplines.addLayout(self.disciplines_actions)
        self.disciplines_armes.addLayout(self.disciplines)
        self.armes = QtWidgets.QVBoxLayout()
        self.armes.setSpacing(4)
        self.armes.setObjectName("armes")
        self.armes_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.armes_label.sizePolicy().hasHeightForWidth())
        self.armes_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.armes_label.setFont(font)
        self.armes_label.setObjectName("armes_label")
        self.armes.addWidget(self.armes_label)
        self.armes_list = QtWidgets.QListWidget(self.verticalLayoutWidget_5)
        self.armes_list.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.armes_list.sizePolicy().hasHeightForWidth())
        self.armes_list.setSizePolicy(sizePolicy)
        self.armes_list.setMaximumSize(QtCore.QSize(30012, 95))
        self.armes_list.setObjectName("armes_list")
        item = QtWidgets.QListWidgetItem()
        self.armes_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.armes_list.addItem(item)
        self.armes.addWidget(self.armes_list)
        self.armes_actions = QtWidgets.QVBoxLayout()
        self.armes_actions.setContentsMargins(25, -1, 25, -1)
        self.armes_actions.setSpacing(6)
        self.armes_actions.setObjectName("armes_actions")
        self.armes_dropdown = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.armes_dropdown.setEditable(False)
        self.armes_dropdown.setCurrentText("")
        self.armes_dropdown.setObjectName("armes_dropdown")
        self.armes_actions.addWidget(self.armes_dropdown)
        self.armes_suppr_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.armes_suppr_btn.setObjectName("armes_suppr_btn")
        self.armes_actions.addWidget(self.armes_suppr_btn)
        self.armes.addLayout(self.armes_actions)
        self.disciplines_armes.addLayout(self.armes)
        self.fiche_aventure.addLayout(self.disciplines_armes)
        self.divers = QtWidgets.QVBoxLayout()
        self.divers.setContentsMargins(-1, -1, -1, 0)
        self.divers.setSpacing(4)
        self.divers.setObjectName("divers")
        self.divers_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.divers_label.setFont(font)
        self.divers_label.setObjectName("divers_label")
        self.divers.addWidget(self.divers_label)
        self.divers_table = QtWidgets.QTableWidget(self.verticalLayoutWidget_5)
        self.divers_table.setMaximumSize(QtCore.QSize(452, 16777215))
        self.divers_table.setObjectName("divers_table")
        self.divers_table.setColumnCount(3)
        self.divers_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.divers_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.divers_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.divers_table.setHorizontalHeaderItem(2, item)
        self.divers_table.horizontalHeader().setVisible(True)
        self.divers_table.horizontalHeader().setCascadingSectionResizes(False)
        self.divers_table.horizontalHeader().setDefaultSectionSize(100)
        self.divers_table.horizontalHeader().setHighlightSections(True)
        self.divers_table.horizontalHeader().setMinimumSectionSize(39)
        self.divers_table.horizontalHeader().setStretchLastSection(True)
        self.divers_table.verticalHeader().setStretchLastSection(False)
        self.divers.addWidget(self.divers_table)
        self.divers_actions = QtWidgets.QHBoxLayout()
        self.divers_actions.setObjectName("divers_actions")
        self.divers_combo = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.divers_combo.setObjectName("divers_combo")
        self.divers_combo.addItem("")
        self.divers_combo.addItem("")
        self.divers_combo.addItem("")
        self.divers_actions.addWidget(self.divers_combo)
        self.divers_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.divers_input.setObjectName("divers_input")
        self.divers_actions.addWidget(self.divers_input)
        self.divers_btns = QtWidgets.QVBoxLayout()
        self.divers_btns.setObjectName("divers_btns")
        self.divers_insert_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.divers_insert_btn.setObjectName("divers_insert_btn")
        self.divers_btns.addWidget(self.divers_insert_btn)
        self.divers_suppr_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.divers_suppr_btn.setObjectName("divers_suppr_btn")
        self.divers_btns.addWidget(self.divers_suppr_btn)
        self.divers_actions.addLayout(self.divers_btns)
        self.divers_actions.setStretch(0, 1)
        self.divers_actions.setStretch(1, 2)
        self.divers_actions.setStretch(2, 1)
        self.divers.addLayout(self.divers_actions)
        self.fiche_aventure.addLayout(self.divers)
        self.quantifiables = QtWidgets.QVBoxLayout()
        self.quantifiables.setSpacing(15)
        self.quantifiables.setObjectName("quantifiables")
        self.quantifiables_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.quantifiables_label.setFont(font)
        self.quantifiables_label.setObjectName("quantifiables_label")
        self.quantifiables.addWidget(self.quantifiables_label)
        self.compteurs = QtWidgets.QHBoxLayout()
        self.compteurs.setObjectName("compteurs")
        self.habilete = QtWidgets.QVBoxLayout()
        self.habilete.setSpacing(4)
        self.habilete.setObjectName("habilete")
        self.habilete_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.habilete_label.setFont(font)
        self.habilete_label.setObjectName("habilete_label")
        self.habilete.addWidget(self.habilete_label)
        self.habilete_counter = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.habilete_counter.setObjectName("habilete_counter")
        self.habilete.addWidget(self.habilete_counter)
        self.compteurs.addLayout(self.habilete)
        self.bourse = QtWidgets.QVBoxLayout()
        self.bourse.setSpacing(4)
        self.bourse.setObjectName("bourse")
        self.bourse_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.bourse_label.setFont(font)
        self.bourse_label.setObjectName("bourse_label")
        self.bourse.addWidget(self.bourse_label)
        self.bourse_counter = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.bourse_counter.setObjectName("bourse_counter")
        self.bourse.addWidget(self.bourse_counter)
        self.compteurs.addLayout(self.bourse)
        self.endurance = QtWidgets.QVBoxLayout()
        self.endurance.setSpacing(4)
        self.endurance.setObjectName("endurance")
        self.endurance_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.endurance_label.setFont(font)
        self.endurance_label.setObjectName("endurance_label")
        self.endurance.addWidget(self.endurance_label)
        self.endurance_counter = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.endurance_counter.setObjectName("endurance_counter")
        self.endurance.addWidget(self.endurance_counter)
        self.compteurs.addLayout(self.endurance)
        self.quantifiables.addLayout(self.compteurs)
        self.fiche_aventure.addLayout(self.quantifiables)
        self.sauvegarde = QtWidgets.QVBoxLayout()
        self.sauvegarde.setSpacing(10)
        self.sauvegarde.setObjectName("sauvegarde")
        self.sauvegarde_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.sauvegarde_label.setFont(font)
        self.sauvegarde_label.setObjectName("sauvegarde_label")
        self.sauvegarde.addWidget(self.sauvegarde_label)
        self.sauvegarde_new_actions = QtWidgets.QVBoxLayout()
        self.sauvegarde_new_actions.setSpacing(4)
        self.sauvegarde_new_actions.setObjectName("sauvegarde_new_actions")
        self.sauvegarde_actions_middle = QtWidgets.QHBoxLayout()
        self.sauvegarde_actions_middle.setSpacing(25)
        self.sauvegarde_actions_middle.setObjectName("sauvegarde_actions_middle")
        self.sauvegarde_dropdown = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.sauvegarde_dropdown.setObjectName("sauvegarde_dropdown")
        self.sauvegarde_dropdown.addItem("")
        self.sauvegarde_dropdown.addItem("")
        self.sauvegarde_dropdown.addItem("")
        self.sauvegarde_dropdown.addItem("")
        self.sauvegarde_actions_middle.addWidget(self.sauvegarde_dropdown)
        self.sauvegarde_field_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.sauvegarde_field_input.setObjectName("sauvegarde_field_input")
        self.sauvegarde_actions_middle.addWidget(self.sauvegarde_field_input)
        self.sauvegarde_actions_middle.setStretch(0, 1)
        self.sauvegarde_actions_middle.setStretch(1, 1)
        self.sauvegarde_new_actions.addLayout(self.sauvegarde_actions_middle)
        self.sauvegarde_actions_bottom = QtWidgets.QHBoxLayout()
        self.sauvegarde_actions_bottom.setSpacing(25)
        self.sauvegarde_actions_bottom.setObjectName("sauvegarde_actions_bottom")
        self.sauvegarde_suppr_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.sauvegarde_suppr_btn.setObjectName("sauvegarde_suppr_btn")
        self.sauvegarde_actions_bottom.addWidget(self.sauvegarde_suppr_btn)
        self.sauvegarde_create_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.sauvegarde_create_btn.setObjectName("sauvegarde_create_btn")
        self.sauvegarde_actions_bottom.addWidget(self.sauvegarde_create_btn)
        self.sauvegarde_actions_bottom.setStretch(0, 1)
        self.sauvegarde_actions_bottom.setStretch(1, 1)
        self.sauvegarde_new_actions.addLayout(self.sauvegarde_actions_bottom)
        self.sauvegarde.addLayout(self.sauvegarde_new_actions)
        self.sauvegarde_actions = QtWidgets.QHBoxLayout()
        self.sauvegarde_actions.setObjectName("sauvegarde_actions")
        self.sauvegarde_choix = QtWidgets.QVBoxLayout()
        self.sauvegarde_choix.setObjectName("sauvegarde_choix")
        self.sauvegarde_actions.addLayout(self.sauvegarde_choix)
        self.sauvegarde_field = QtWidgets.QVBoxLayout()
        self.sauvegarde_field.setSpacing(6)
        self.sauvegarde_field.setObjectName("sauvegarde_field")
        self.sauvegarde_actions.addLayout(self.sauvegarde_field)
        self.sauvegarde.addLayout(self.sauvegarde_actions)
        self.fiche_aventure.addLayout(self.sauvegarde)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.book_label.setText(_translate("MainWindow", "Livre"))
        self.chapter_label.setText(_translate("MainWindow", "Chapitre 84923"))
        self.chapter_dropdown.setPlaceholderText(_translate("MainWindow", "Aller vers un chapitre"))
        self.disciplines_label.setText(_translate("MainWindow", "Disciplines"))
        __sortingEnabled = self.disciplines_list.isSortingEnabled()
        self.disciplines_list.setSortingEnabled(False)
        item = self.disciplines_list.item(0)
        item.setText(_translate("MainWindow", "Camouflage"))
        item = self.disciplines_list.item(1)
        item.setText(_translate("MainWindow", "Chasse"))
        item = self.disciplines_list.item(2)
        item.setText(_translate("MainWindow", "Sixième sens"))
        item = self.disciplines_list.item(3)
        item.setText(_translate("MainWindow", "Orientation"))
        item = self.disciplines_list.item(4)
        item.setText(_translate("MainWindow", "Guérison"))
        self.disciplines_list.setSortingEnabled(__sortingEnabled)
        self.disciplines_dropdown.setPlaceholderText(_translate("MainWindow", "Ajouter"))
        self.disciplines_suppr_btn.setText(_translate("MainWindow", "Supprimer"))
        self.armes_label.setText(_translate("MainWindow", "Armes"))
        __sortingEnabled = self.armes_list.isSortingEnabled()
        self.armes_list.setSortingEnabled(False)
        item = self.armes_list.item(0)
        item.setText(_translate("MainWindow", "Lance"))
        item = self.armes_list.item(1)
        item.setText(_translate("MainWindow", "Masse d\'arme"))
        self.armes_list.setSortingEnabled(__sortingEnabled)
        self.armes_dropdown.setPlaceholderText(_translate("MainWindow", "Ajouter", "Ajouter"))
        self.armes_suppr_btn.setText(_translate("MainWindow", "Supprimer"))
        self.divers_label.setText(_translate("MainWindow", "Divers"))
        self.divers_table.setSortingEnabled(False)
        item = self.divers_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Objets"))
        item = self.divers_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Objets spéciaux"))
        item = self.divers_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Repas"))
        self.divers_combo.setItemText(0, _translate("MainWindow", "Objets"))
        self.divers_combo.setItemText(1, _translate("MainWindow", "Objets spéciaux"))
        self.divers_combo.setItemText(2, _translate("MainWindow", "Repas"))
        self.divers_insert_btn.setText(_translate("MainWindow", "Insérer"))
        self.divers_suppr_btn.setText(_translate("MainWindow", "Supprimer"))
        self.quantifiables_label.setText(_translate("MainWindow", "Quantifiables"))
        self.habilete_label.setText(_translate("MainWindow", "Habileté"))
        self.bourse_label.setText(_translate("MainWindow", "Bourse"))
        self.endurance_label.setText(_translate("MainWindow", "Endurance"))
        self.sauvegarde_label.setText(_translate("MainWindow", "Sauvegarde"))
        self.sauvegarde_dropdown.setItemText(0, _translate("MainWindow", "Objets"))
        self.sauvegarde_dropdown.setItemText(1, _translate("MainWindow", "Objets spéciaux"))
        self.sauvegarde_dropdown.setItemText(2, _translate("MainWindow", "Repas"))
        self.sauvegarde_dropdown.setItemText(3, _translate("MainWindow", "Bourse"))
        self.sauvegarde_suppr_btn.setText(_translate("MainWindow", "Supprimer"))
        self.sauvegarde_create_btn.setText(_translate("MainWindow", "Enregistrer"))
