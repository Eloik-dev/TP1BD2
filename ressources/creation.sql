DROP DATABASE IF EXISTS `RousseauEloik_Livre`;
CREATE DATABASE `RousseauEloik_Livre`;
USE `RousseauEloik_Livre`;

-- Création des tables
CREATE TABLE `livre` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `titre` VARCHAR(255) NOT NULL
);

CREATE TABLE `chapitre` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `livre_id` INT DEFAULT 1 NOT NULL,
    `no_chapitre` VARCHAR(255) NOT NULL,
    `texte` TEXT NOT NULL,
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE `lien_chapitre` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `no_chapitre_origine` INT NOT NULL,
    `no_chapitre_destination` INT NOT NULL,
    FOREIGN KEY (`no_chapitre_origine`) REFERENCES `chapitre`(`id`),
    FOREIGN KEY (`no_chapitre_destination`) REFERENCES `chapitre`(`id`)
);

CREATE TABLE `fiche_personnage` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(64) NOT NULL,
    `bourse` INT DEFAULT 0,
    `habilete` INT DEFAULT 0,
    `endurance` INT DEFAULT 0,
    `chapitre_id` INT NOT NULL,
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`chapitre_id`) REFERENCES `chapitre`(`id`),
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`) ON DELETE CASCADE
);

CREATE TABLE `discipline` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(64),
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE `discipline_fiche_personnage` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `fiche_personnage_id` INT NOT NULL,
	`discipline_id` INT NOT NULL,
	FOREIGN KEY (`fiche_personnage_id`) REFERENCES `fiche_personnage`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`discipline_id`) REFERENCES `discipline`(`id`) ON DELETE CASCADE
);

CREATE TABLE `divers` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(255),
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE `divers_fiche_personnage` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `valeur` TEXT NOT NULL,
    `fiche_personnage_id` INT NOT NULL,
	`divers_id` INT NOT NULL,
	FOREIGN KEY (`fiche_personnage_id`) REFERENCES `fiche_personnage`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`divers_id`) REFERENCES `divers`(`id`) ON DELETE CASCADE
);

CREATE TABLE `arme` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(64),
    `livre_id` INT DEFAULT 1 NOT NULL,
    FOREIGN KEY (`livre_id`) REFERENCES `livre`(`id`)
);

CREATE TABLE `arme_fiche_personnage` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
    `fiche_personnage_id` INT NOT NULL,
	`arme_id` INT NOT NULL,
	FOREIGN KEY (`fiche_personnage_id`) REFERENCES `fiche_personnage`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`arme_id`) REFERENCES `arme`(`id`) ON DELETE CASCADE
);

-- Procédure pour obtenir les chapitres possibles d'un chapitre
DELIMITER $$
CREATE PROCEDURE `trouverChapitres`(IN `_livre_id` INT, IN `_no_chapitre` INT) 
BEGIN
    SELECT * FROM `lien_chapitre` `lc`
        INNER JOIN `chapitre` `c` ON `c`.`id` = `lc`.`no_chapitre_origine`
        INNER JOIN `livre` `l` ON `l`.`id` = `_livre_id`
        WHERE `no_chapitre_origine` = `_no_chapitre`;
END $$

-- Procédure pour obtenir toutes les armes
CREATE PROCEDURE `prendreArmes`() 
BEGIN
    SELECT * FROM `arme`;
END $$
DELIMITER ;

-- Création de l'utilisateur
DROP USER IF EXISTS `utilisateur`@`localhost`;
CREATE USER 'utilisateur'@'localhost' IDENTIFIED BY 'motdepassepuissant';
GRANT EXECUTE ON PROCEDURE `trouverChapitres` TO 'utilisateur'@'localhost';
GRANT SELECT ON *.* TO 'utilisateur'@'localhost';
GRANT INSERT, DELETE, UPDATE ON `fiche_personnage` TO 'utilisateur'@'localhost';
GRANT INSERT, DELETE ON `discipline_fiche_personnage` TO 'utilisateur'@'localhost';
GRANT INSERT, DELETE ON `divers_fiche_personnage` TO 'utilisateur'@'localhost';
GRANT INSERT, DELETE ON `arme_fiche_personnage` TO 'utilisateur'@'localhost';

-- Insertion par défaut
INSERT INTO `livre` (`titre`) VALUES ('Les Maîtres des Ténèbres');

INSERT INTO `discipline` (`nom`) VALUES
	('Le camouflage'),
    ('La Chasse'),
    ('Le Sixième Sens'),
    ('L\'Orientation'),
    ('La Guérison'),
    ('La Maîtrise des armes');
    
INSERT INTO `arme` (`nom`) VALUES
	('Le poignard'),
    ('La lance'),
    ('La masse d\'armes'),
    ('Le sabre'),
    ('Le marteau de guerre'),
    ('L\'épée'),
    ('La hache'),
    ('L\'épee'),
    ('Le baton'),
    ('Le glaive');

INSERT INTO `divers` (`nom`) VALUES
	('Objets'),
    ('Objets spéciaux'),
    ('Repas');