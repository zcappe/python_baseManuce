BEGIN TRANSACTION;

DROP TABLE IF EXISTS `printers`;
CREATE TABLE IF NOT EXISTS `printers` (
	`id` 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`		TEXT NOT NULL,
	`birthyear`	INTEGER,
	`deathyear`	INTEGER
);

DROP TABLE IF EXISTS `institutions`;
CREATE TABLE `institutions` (
	`id` 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`country` 	TEXT NOT NULL,
	`city`		TEXT NOT NULL,
	`institution_name`	TEXT NOT NULL
);

DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
	`id` 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`title`		TEXT,
	`printdate`	INTEGER,
	`format`	TEXT,
	`language`	TEXT,
	`identifier`	TEXT NOT NULL,
	`printer_id` INTEGER NOT NULL,
	`institution_id` INTEGER NOT NULL,
	FOREIGN KEY(printer_id) REFERENCES printers(id),
	FOREIGN KEY(institution_id) REFERENCES institutions(id)
);
COMMIT;

BEGIN TRANSACTION;

INSERT INTO `printers` (`id`, `name`, `birthyear`, `deathyear`) 
	VALUES 
	(0, "Aldo Manuzio", 1450, 1515), 
	(1, "Paul Manuce", 1512, 1574),
	(2, "Aldo Manuzio", 1547, 1597),
	(3, "Andrea Torresano", 1451, 1529);


INSERT INTO `institutions`(`id`, `country`, `city`, 
	`institution_name`) 
	VALUES 
	(0, "France", "Paris", "Bibliothèque de l Ecole des chartes"), 
	(1, "France", "Paris", "Bibliothèque Mazarine"),
	(2, "Danemark", "Copenhague", "Bibliothèque royale"),
	(3, "France", "Paris", "Bibliothèque Sainte-Geneviève");


INSERT INTO `books` (`id`, `title`, `printdate`, `format`, 
	`language`, `identifier`, `printer_id`, `institution_id`) 
	VALUES 
	(0, "Discorsi della penitenza, sopra i sette salmi penitentiali di David di M. Nicolo Vito di Grozze", 1589, "in-8", "italien", "8R23", 2, 0),
	(1, "Ovidii Metamorphoseon libri XV", 1502, "in-12", "latin", "8R24", 0, 0),
	(2, "Urbani Bolzanii bellunensis grammaticae institutiones ad greacam linguam...", 1557, "in-8", "latin; grec moderne", "8R25", 1, 0),
	(3, "M. Tullii Ciceronis orationum pars II. Cum correctionibus Pauli Manutij", 1565, "in-12", "latin", "8R171", 1, 0),
	(4, "Pauli Manutii Praefationes quibus...", 1571, "in-8", "latin", "8R173", 1, 0),
	(5, "Hoc volumine continentur Commentariorum de bello Gallico libri VIII...", 1559, "in-8", "latin", "8R174", 1, 0),
	(6, "Asconii Paediani expositio in IIII orationes M. Tullii Cic. Contra C. Verrem...", 1522, "in-8", "latin", "8R175", 3, 0),
	(7, "Commentarius Pauli Manutii in epistolas Ciceronis ad Atticum. Index rerum, & verborum", 1561, "in-8", "latin", "8R176", 1, 0),
	(8, "In hoc volumine haec continentur...", 1521, "in-4", "latin", "8R178", 3, 0),
	(9, "Polybii historiarum libri quinque in latiam conversi linguam, Nicolao Perotto interprete", 1521, "in-8", "latin", "8R179", 3, 0),
	(10, "Giocasta, tragedia di m. lodovico dolce", 1549, "in-8", "italien", "8R180", 1, 0),
	(11, "Francisci Luisini utinensis in librum Q. Horatii Flacci De arte poetica commentarius", 1554, "in-4", "latin", "8R183", 1, 0),
	(12, "Ex Plautii comoediis 20 quarum carmina magna ex parte in mensum suum restituta sunt 1522...", 1522, "in-4", "latin", "4° 10495", 3, 1),
	(13, "Delle lettere: facete et piacevoli di diversi grandi huomini et chiari ingegni...", 1582, "in-8", "italien", "8° 45541-1", 2, 1),
	(14, "In hoc libro haec habentur Constantini Lascaris Byzantini de octo partibus orationis lib. I ...", 1512, NULL, "latin", "72, 155", 0, 2),
	(15, "De Literis Graecis ac Diphtonhis et quemadmodum ad nos veniant...", 1512, NULL, "latin", "72, 163", 0, 2),
	(16, "De die natali liber ad Q; Caerellium, ab Aldo Manuccio, Pauli filii Aldi n. emendatus et notis illustratus", 1581, "in-8", "latin", "8 OEA 185 INV 454 RES", 2, 3),
	(17, "Omnia Platonis opera", 1513, "in-fol", "grec", "OEA 26 INV 41 RES", 0, 3),
	(18, "Accipite studiosi omnes obviis ut aiunt manibus...", 1508, "in-4", "latin", "4 I 360 INV 471 RES (P.2)", 0, 3),
	(19, "Antiquitatum Romanarum Paulli. Mannucci liber ...", 1581, "in-4", "latin", "4 OEA 95 INV 206 RES", 2, 3);

	COMMIT;