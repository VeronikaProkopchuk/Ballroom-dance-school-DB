BEGIN TRANSACTION;
INSERT INTO SALAS VALUES ('Sala London',20);
INSERT INTO SALAS VALUES ('Sala Madrid',40);
INSERT INTO SALAS VALUES ('Sala Nueva York',65);
INSERT INTO ENTRENADORES VALUES ('09267845A','Lua','Perez','+34628495869','1980-09-09','S');
INSERT INTO ENTRENADORES VALUES ('24375849A','Francisco','Rodriguez','+34456823765','1999-08-30','A');
INSERT INTO ENTRENADORES VALUES ('85638574B','Anna','Martinez','+34784553667','1997-02-21','S');
INSERT INTO DEPORTISTAS VALUES ('09574638A','Laura','Lopez','+34224668574','2004-02-03','C');
INSERT INTO DEPORTISTAS VALUES ('09894638A','Rafael','Alonso Romero','+34987994003','2005-01-11','D');
INSERT INTO DEPORTISTAS VALUES ('09574638C','David','Ulloa Martínez','+34893465734','2004-04-28','D');
INSERT INTO DEPORTISTAS VALUES ('09573438A','Lorenzo','Pérez Martín','+34347534876',NULL,'C');
INSERT INTO DEPORTISTAS VALUES ('09574638D','Juan','Gomez','+34894567384','2005-10-01','D');
INSERT INTO DEPORTISTAS VALUES ('09574638F','Daniel','Fernandes Romero','+34095673845','2003-12-24','D');
INSERT INTO DEPORTISTAS VALUES ('09574667C','Alisia',NULL,'+34983654784','2004-10-17','D');
INSERT INTO DEPORTISTAS VALUES ('09574836A','Roman','Gonzalez','+34097367946','2004-05-07','C');
INSERT INTO DEPORTISTAS VALUES ('09578740D','Harry','Potter','+34983647938','2007-04-05','E');
INSERT INTO DEPORTISTAS VALUES ('09574638E','Draco','Malfoy','+34983765808','2006-10-02','E');
INSERT INTO LECCIONES VALUES ('Latino','01:45','09267845A');
INSERT INTO LECCIONES VALUES ('Estandart','01:45','85638574B');
INSERT INTO LECCIONES VALUES ('Practica Latino','00:45','09267845A');
INSERT INTO LECCIONES VALUES ('Practica Estandart','00:45','24375849A');
INSERT INTO PARTICIPACION VALUES ('Practica Estandart','09574638A');
INSERT INTO PARTICIPACION VALUES ('Practica Estandart','09574638E');
INSERT INTO PARTICIPACION VALUES ('Practica Estandart','09574638F');
INSERT INTO PARTICIPACION VALUES ('Practica Estandart','09574638C');
INSERT INTO PARTICIPACION VALUES ('Practica Latino','09574638A');
INSERT INTO PARTICIPACION VALUES ('Practica Latino','09574638C');
INSERT INTO PARTICIPACION VALUES ('Practica Latino','09574638E');
INSERT INTO PARTICIPACION VALUES ('Practica Latino','09574638D');
INSERT INTO PARTICIPACION VALUES ('Latino','09574638A');
INSERT INTO PARTICIPACION VALUES ('Latino','09574638C');
INSERT INTO PARTICIPACION VALUES ('Latino','09574638D');
INSERT INTO PARTICIPACION VALUES ('Estandart','09574638A');
INSERT INTO PARTICIPACION VALUES ('Estandart','09574638F');
INSERT INTO PARTICIPACION VALUES ('Estandart','09574638C');
INSERT INTO PARTICIPACION VALUES ('Estandart','09574638D');
INSERT INTO PARTICIPACION VALUES ('Estandart','09574638E');
INSERT INTO REALIZACIONES VALUES ('Sala London','Latino','Jueves','19:30');
INSERT INTO REALIZACIONES VALUES ('Sala Madrid','Practica Estandart','Martes','19:30');
INSERT INTO REALIZACIONES VALUES ('Sala Nueva York','Practica Latino','Martes','20:15');
INSERT INTO REALIZACIONES VALUES ('Sala Nueva York','Estandart','Viernes','19:30');
COMMIT;