import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
# Importer la classe Ui_MainWindow du fichier demo.py
from application import Ui_MainWindow

cnx = mysql.connector.connect(
    user='utilisateur', 
    password='motdepassepuissant',
    host='127.0.0.1',
    database='RousseauEloik_Livre')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.livre_id = 1
        self.chapitre_id = 1
        self.fiche_personnage = None

        self.initialisation()
        self.initConnexions()
    
    def initConnexions(self):
        self.chapter_dropdown.activated.connect(self.changerChapitre)

        self.disciplines_dropdown.activated.connect(self.ajouterDiscipline)
        self.disciplines_suppr_btn.clicked.connect(self.supprimerDiscipline)

        self.armes_dropdown.activated.connect(self.ajouterArme)
        self.armes_suppr_btn.clicked.connect(self.supprimerArme)

        self.divers_insert_btn.clicked.connect(self._ajouter_item_table)
        self.divers_suppr_btn.clicked.connect(self.supprimerTableItem)

        self.sauvegarde_create_btn.clicked.connect(self.sauvegarder)
        self.sauvegarde_dropdown.activated.connect(self.changerSauvegarde)
        self.sauvegarde_suppr_btn.clicked.connect(self.supprimerSauvegarde)

    def initialisation(self):
        self.initLivre()
        self.initDisciplines()
        self.initArmes()
        self.initDivers()
        self.initQuantifiables()
        self.initChapitre()
        self.initSauvegarde()
    
    def initLivre(self):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `livre`;')
        self.books_dropdown.clear()

        for livre in cursor:
            self.books_dropdown.addItem(livre['titre'])

        self.books_dropdown.setCurrentIndex(0)
        self.livre_id = 1
    
    def initDisciplines(self):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `discipline`;')
        self.disciplines_dropdown.clear()
        self.disciplines_list.clear()

        self.disciplines_dropdown.insertItem(-1, 'Ajouter une discipline')
        self.disciplines_dropdown.setCurrentIndex(0)

        disciplines = []

        for discipline in cursor:
            disciplines.append(discipline)
            self.disciplines_dropdown.addItem(discipline['nom'])

        # Utiliser une sauvegarde
        if self.fiche_personnage == None: return

        cnx.reconnect()

        cursor.execute('SELECT * FROM `discipline_fiche_personnage` WHERE `fiche_personnage_id` = {0};'.format(self.fiche_personnage['id']))

        for discipline_fiche_personnage in cursor:
            for discipline in disciplines:
                if discipline['id'] == discipline_fiche_personnage['discipline_id']:
                    self.disciplines_list.addItem(discipline['nom'])

    def initArmes(self):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `arme`;')
        self.armes_dropdown.clear()
        self.armes_list.clear()

        self.armes_dropdown.insertItem(-1, 'Ajouter une arme')
        self.armes_dropdown.setCurrentIndex(0)

        armes = []

        for arme in cursor:
            armes.append(arme)
            self.armes_dropdown.addItem(arme['nom'])

        # Utiliser une sauvegarde
        if self.fiche_personnage == None: return

        cnx.reconnect()

        cursor.execute('SELECT * FROM `arme_fiche_personnage` WHERE `fiche_personnage_id` = {0};'.format(self.fiche_personnage['id']))

        for arme_fiche_personnage in cursor:
            for arme in armes:
                if arme['id'] == arme_fiche_personnage['arme_id']:
                    self.armes_list.addItem(arme['nom'])

    def initDivers(self):
        self.divers_table.clear()
        self.divers_table.reset()
        self.divers_table.setRowCount(0)
        self.divers_table.setColumnCount(0)

        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `divers`;')

        colonnes_divers = cursor.fetchall()
        nouvelles_colonnes_table = []

        for divers in colonnes_divers:
            nouvelles_colonnes_table.append(divers['nom'])

        self.divers_table.setColumnCount(len(nouvelles_colonnes_table))
        self.divers_table.setHorizontalHeaderLabels(nouvelles_colonnes_table)
        
        if self.fiche_personnage == None: return
        
        for nouveau_divers in colonnes_divers:
            cursor.execute('SELECT * FROM `divers_fiche_personnage` WHERE `fiche_personnage_id` = {0} AND `divers_id` = {1};'.format(self.fiche_personnage['id'], nouveau_divers['id']))
            rows = cursor.fetchall()
            for rangee in rows:
                if rangee['valeur']:
                    self.ajouterTableItem(nouveau_divers['id'] - 1 if nouveau_divers['id'] > 0 else nouveau_divers['id'], rangee['valeur'])

    def initQuantifiables(self):
        self.habilete_counter.setValue(self.fiche_personnage['habilete'] if self.fiche_personnage else 0)
        self.bourse_counter.setValue(self.fiche_personnage['bourse'] if self.fiche_personnage else 0)
        self.endurance_counter.setValue(self.fiche_personnage['endurance'] if self.fiche_personnage else 0)

    def initChapitre(self):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `chapitre` WHERE `id` = {0} AND `livre_id` = {1} LIMIT 1;'.format(self.chapitre_id, self.livre_id))

        for chapitre in cursor:
            if chapitre['no_chapitre'].isdigit():
                self.chapter_label.setText('Chapitre ' + chapitre['no_chapitre'])
            else:
                self.chapter_label.setText(chapitre['no_chapitre'])
                
            self.chapter_text.setText(chapitre['texte'])

        self.initLienChapitre()

    def initLienChapitre(self):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('CALL trouverChapitres({0}, {1});'.format(self.livre_id, self.chapitre_id - 1 if self.chapitre_id > 1 else self.chapitre_id))

        self.chapter_dropdown.clear()
        self.chapter_dropdown.insertItem(-1, 'Aller vers un chapitre')
        self.chapter_dropdown.setCurrentIndex(0)

        for lien_chapitre in cursor:
            self.chapter_dropdown.addItem(str(lien_chapitre['no_chapitre_destination']))
        
        cnx.reconnect()

    def initSauvegarde(self):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `fiche_personnage` WHERE `livre_id` = {0};' . format(self.livre_id))

        self.sauvegarde_dropdown.clear()
        self.sauvegarde_dropdown.insertItem(-1, 'Choisir une sauvegarde')
        self.sauvegarde_dropdown.setCurrentIndex(0)

        for fiche_personnage in cursor:
            self.sauvegarde_dropdown.addItem(fiche_personnage['nom'])

    def changerChapitre(self, value):
        if value == 0:
            return
        
        no_chapitre = self.chapter_dropdown.itemText(value)
        
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `chapitre` WHERE `livre_id` = {0} AND `no_chapitre` = {1} LIMIT 1;'.format(self.livre_id, no_chapitre))

        for chapitre in cursor:
            self.chapitre_id = int(chapitre['no_chapitre']) + 1

        self.initChapitre()

    def ajouterDiscipline(self, value):
        if value == 0: return

        if self.disciplines_list.count() < 5:
            discipline = self.disciplines_dropdown.itemText(value)
            self.disciplines_list.addItem(discipline)

        self.disciplines_dropdown.setCurrentIndex(0)

    def supprimerDiscipline(self):
        self.disciplines_list.takeItem(self.disciplines_list.currentRow())
    
    def ajouterArme(self, value):
        if value == 0: return

        if self.armes_list.count() < 2:
            discipline = self.armes_dropdown.itemText(value)
            self.armes_list.addItem(discipline)

        self.armes_dropdown.setCurrentIndex(0)

    def supprimerArme(self):
        self.armes_list.takeItem(self.armes_list.currentRow())

    def _ajouter_item_table(self):
        self.ajouterTableItem()
    
    def ajouterTableItem(self, colonneIdx = None, valeur = ''):
        colonneIdx = colonneIdx or self.trouverIndexColonne(self.divers_combo.currentText())
        rangeeIdx = self.trouverCaseVide(colonneIdx)

        self.divers_table.setItem(rangeeIdx, colonneIdx, QTableWidgetItem(valeur or self.divers_input.text()))

    def trouverCaseVide(self, colonne):
        rowCount = self.divers_table.rowCount()

        if rowCount == 0:
            self.divers_table.setRowCount(1)
            return 0

        for row in range(rowCount):
            item = self.divers_table.item(row, colonne)
            if item is None:
                if row == -1:
                    self.divers_table.setRowCount(rowCount + 1)
                    continue
                return row
        
        self.divers_table.setRowCount(self.divers_table.rowCount() + 1)
        return self.trouverCaseVide(colonne)

    def trouverIndexColonne(self, nom_colonne):
        for i in range(self.divers_table.columnCount()):
            print(i)
            colonne = self.divers_table.horizontalHeaderItem(i)
            if colonne is not None and colonne.text() == nom_colonne:
                return i
        return -1
    
    def supprimerTableItem(self):
        self.divers_table.takeItem(self.divers_table.currentRow(), self.divers_table.currentColumn())

        if self.supprimerRangeesVides():
            self.divers_table.setRowCount(self.divers_table.rowCount() - 1)

    def supprimerRangeesVides(self):
        row_count = self.divers_table.rowCount()
        for row in range(row_count - 1, -1, -1):
            est_vide = True
            for column in range(self.divers_table.columnCount()):
                item = self.divers_table.item(row, column)
                if item is not None:
                    est_vide = False
                    break
            if est_vide:
                self.divers_table.removeRow(row)

    def trouverSauvegarde(self, nom_sauvegarde):
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM `fiche_personnage` WHERE `nom` = "{0}" AND `livre_id` = {1} LIMIT 1;'.format(nom_sauvegarde, self.livre_id))
        return cursor.fetchone()
    
    def changerSauvegarde(self, value):
        if value == 0: return

        fiche_personnage = self.trouverSauvegarde(self.sauvegarde_dropdown.itemText(value))
        self.fiche_personnage = fiche_personnage
        
        self.chapitre_id = self.fiche_personnage['chapitre_id']

        self.initialisation()
        self.sauvegarde_dropdown.setCurrentIndex(value)
        self.sauvegarde_field_input.setText(self.sauvegarde_dropdown.itemText(self.sauvegarde_dropdown.currentIndex()))
    
    def supprimerSauvegarde(self):
        if self.fiche_personnage is None: return

        cursor = cnx.cursor(dictionary=True)
        cursor.execute('DELETE FROM `fiche_personnage` WHERE `id` = "{0}"'.format(self.fiche_personnage['id']))

        cnx.commit()

        self.initialisation()
        self.changerSauvegarde(self.sauvegarde_dropdown.count() - 1)
    
    def sauvegarder(self):
        nom_fiche_personnage = self.sauvegarde_field_input.text()

        if not nom_fiche_personnage: return

        # Valeurs à sauvegarder
        habilete = self.habilete_counter.value()
        bourse = self.bourse_counter.value()
        endurance = self.endurance_counter.value()

        # Modifier ou créer une sauvegarde
        cursor = cnx.cursor(dictionary=True)
        fiche_personnage = self.trouverSauvegarde(nom_fiche_personnage)

        if fiche_personnage:
            cursor.execute('UPDATE `fiche_personnage` SET `nom` = "{0}", `habilete` = {1}, `bourse` = {2}, `endurance` = {3}, `chapitre_id` = {4} WHERE `nom` = "{5}" AND `livre_id` = {6};'.format(nom_fiche_personnage, habilete, bourse, endurance, self.chapitre_id, nom_fiche_personnage, self.livre_id))
        else:
            cursor.execute('INSERT INTO `fiche_personnage` (`nom`, `habilete`, `bourse`, `endurance`, `chapitre_id`, `livre_id`) VALUES ("{0}", {1}, {2}, {3}, {4}, {5});'.format(nom_fiche_personnage, habilete, bourse, endurance, self.chapitre_id, self.livre_id))

        fiche_personnage = self.trouverSauvegarde(nom_fiche_personnage)

        # Sauvegarder les disciplines
        cursor.execute('DELETE FROM `discipline_fiche_personnage` WHERE `fiche_personnage_id` = {0};'.format(fiche_personnage['id']))
        for i in range(self.disciplines_list.count()):
            item = self.disciplines_list.item(i)

            cursor.execute('SELECT * FROM `discipline` WHERE `nom` = "{0}" AND `livre_id` = {1} LIMIT 1;'.format(item.text(), self.livre_id))
            discipline = cursor.fetchone()

            if discipline:
                cursor.execute('INSERT INTO `discipline_fiche_personnage` (`fiche_personnage_id`, `discipline_id`) VALUES ({0}, {1});'.format(fiche_personnage['id'], discipline['id']))

        # Sauvegarder les armes
        cursor.execute('DELETE FROM `arme_fiche_personnage` WHERE `fiche_personnage_id` = {0};'.format(fiche_personnage['id']))
        for i in range(self.armes_list.count()):
            item = self.armes_list.item(i)

            cursor.execute('SELECT * FROM `arme` WHERE `nom` = "{0}" LIMIT 1;'.format(item.text()))
            arme = cursor.fetchone()

            if arme:
                cursor.execute('INSERT INTO `arme_fiche_personnage` (`fiche_personnage_id`, `arme_id`) VALUES ({0}, {1});'.format(fiche_personnage['id'], arme['id']))

        # Mettre à jour les valeurs de la table
        cursor.execute('DELETE FROM `divers_fiche_personnage` WHERE `fiche_personnage_id` = {0};'.format(fiche_personnage['id']))
        for i in range(self.divers_table.columnCount()):
            colonne = self.divers_table.horizontalHeaderItem(i)
            
            cursor.execute('SELECT * FROM `divers` WHERE `nom` = "{0}" AND `livre_id` = {1} LIMIT 1;'.format(colonne.text(), self.livre_id))
            divers = cursor.fetchone()

            if divers is None: continue

            for row in range(self.divers_table.rowCount()):
                item = self.divers_table.item(row, i)
                if item is not None:
                    cursor.execute('INSERT INTO `divers_fiche_personnage` (`valeur`, `fiche_personnage_id`, `divers_id`) VALUES ("{0}", {1}, {2});'.format(item.text(), fiche_personnage['id'], divers['id']))

        nomSauvegarde = self.sauvegarde_field_input.text()

        # Commit et réinitialiser les valeurs de la section sauvegarde
        cnx.commit()
        self.initialisation()

        if nomSauvegarde != None:
            self.sauvegarde_dropdown.setCurrentText(nomSauvegarde)
            self.changerSauvegarde(self.sauvegarde_dropdown.currentIndex())

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
