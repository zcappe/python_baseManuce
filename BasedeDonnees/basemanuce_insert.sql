PRAGMA encoding = 'UTF-8';

INSERT INTO printer(id, name, birthyear, deathyear) 
	VALUES 
	(1, "Aldo Manuzio", 1450, 1515), 
	(2, "Paul Manuce", 1512, 1574),
	(3, "Aldo Manuzio", 1547, 1597),
	(4, "Andrea Torresano", 1451, 1529);


INSERT INTO institution(id, country, city, 
	institution_name) 
	VALUES 
	(1, "France", "Paris", "Bibliothèque de l'Ecole des chartes"), 
	(2, "France", "Paris", "Bibliothèque Mazarine"),
	(3, "Danemark", "Copenhague", "Bibliothèque royale");


INSERT INTO books (id, title, printdate, format, 
	language, identifier, printer_id, institution_id) 
	VALUES 
	(1, "Discorsi della penitenza, sopra i sette salmi penitentiali di David di M. Nicolo Vito di Grozze", 1589, "in-8", "italien", "8R23", 3, 1),
	(2, "Ovidii Metamorphoseon libri XV", 1502, "in-12", "latin", "8R24", 1, 1),
	(3, "Urbani Bolzanii bellunensis grammaticae institutiones ad greacam linguam...", 1557, "in-8", "latin; grec moderne", "8R25", 2, 1),
	(4, "M. Tullii Ciceronis orationum pars II. Cum correctionibus Pauli Manutij", 1565, "in-12", "latin", "8R171", 2, 1),
	(5, "Pauli Manutii Praefationes quibus...", 1571, "in-8", "latin", "8R173", 2, 1),
	(6, "Hoc volumine continentur Commentariorum de bello Gallico libri VIII...", 1559, "in-8", "latin", "8R174", 2, 1),
	(7, "Asconii Paediani expositio in IIII orationes M. Tullii Cic. Contra C. Verrem...", 1522, "in-8", "latin", "8R175", 4, 1),
	(8, "Commentarius Pauli Manutii in epistolas Ciceronis ad Atticum. Index rerum, & verborum", 1561, "in-8", "latin", "8R176", 2, 1),
	(9, "In hoc volumine haec continentur...", 1521, "in-4", "latin", "8R178", 4, 1),
	(10, "Polybii historiarum libri quinque in latiam conversi linguam, Nicolao Perotto interprete", 1521, "in-8", "latin", "8R179", 4, 1),
	(11, "Giocasta, tragedia di m. lodovico dolce", 1549, "in-8", "italien", "8R180", 2, 1),
	(12, "Francisci Luisini utinensis in librum Q. Horatii Flacci De arte poetica commentarius", 1554, "in-4", "latin", "8R183", 2, 1),
	(13, "Ex Plautii comoediis 20 quarum carmina magna ex parte in mensum suum restituta sunt 1522...", 1522, "in-4", "latin", "4° 10495", 4, 2),
	(14, "Delle lettere: facete et piacevoli di diversi grandi huomini et chiari ingegni...", 1582, "in-8", "italien", "8° 45541-1", 3, 2),
	(15, "In hoc libro haec habentur Constantini Lascaris Byzantini de octo partibus orationis lib. I ...", 1512, NULL, "latin", "72, 155", 1, 3),
	(16, "De Literis Graecis ac Diphtonhis et quemadmodum ad nos veniant...", 1512, NULL, "latin", "72, 163", 1, 3);