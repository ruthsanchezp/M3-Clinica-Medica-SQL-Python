INSERT INTO Habitacion (id_habitacion, numero_habitacion) VALUES
(1, 101),
(2, 102),
(3, 103),
(4, 104),
(5, 105),
(6, 106),
(7, 107),
(8, 108),
(9, 109),
(10, 110);

INSERT INTO Cama (id_cama, numero_cama, id_habitacion) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 2),
(5, 5, 3),
(6, 6, 3),
(7, 7, 4),
(8, 8, 4),
(9, 9, 5),
(10, 10, 5);

INSERT INTO Paciente (id_paciente, nombre_paciente, rut, fecha_ingreso, fecha_alta, id_cama) VALUES
(1, 'Paciente 1', '11111111-1', '2024-05-01', '2024-05-10', 1),
(2, 'Paciente 2', '11111111-2','2024-05-02', '2024-05-11', 2),
(3, 'Paciente 3', '11111111-3','2024-05-03', '2024-05-12', 3),
(4, 'Paciente 4', '11111111-3', '2024-05-04', '2024-05-13', 4),
(5, 'Paciente 5', '11111111-3', '2024-05-05', '2024-05-14', 5),
(6, 'Paciente 6', '11111111-3', '2024-05-06', '2024-05-15', 6),
(7, 'Paciente 7', '11111111-3', '2024-05-07', '2024-05-16', 7),
(8, 'Paciente 8', '11111111-3', '2024-05-08', '2024-05-17', 8),
(9, 'Paciente 9', '11111111-3', '2024-05-09', '2024-05-18', 9),
(10, 'Paciente 10', '11111111-3', '2024-05-10', '2024-05-19', 10);

INSERT INTO Medico (id_medico, nombre_medico) VALUES
(1, 'Medico 1'),
(2, 'Medico 2'),
(3, 'Medico 3'),
(4, 'Medico 4'),
(5, 'Medico 5'),
(6, 'Medico 6'),
(7, 'Medico 7'),
(8, 'Medico 8'),
(9, 'Medico 9'),
(10, 'Medico 10');

INSERT INTO Examen (id_examen, nombre_examen, tipo_examen) VALUES
(1, 'Examen 1', 'Tipo 1'),
(2, 'Examen 2', 'Tipo 2'),
(3, 'Examen 3', 'Tipo 3'),
(4, 'Examen 4', 'Tipo 4'),
(5, 'Examen 5', 'Tipo 5'),
(6, 'Examen 6', 'Tipo 6'),
(7, 'Examen 7', 'Tipo 7'),
(8, 'Examen 8', 'Tipo 8'),
(9, 'Examen 9', 'Tipo 9'),
(10, 'Examen 10', 'Tipo 10');

INSERT INTO Diagnostico (id_diagnostico, id_paciente, id_medico, comentarios_diagnostico, fecha_diagnostico) VALUES
(1, 1, 1, 'Diagnóstico 1 para Paciente 1', '2024-05-05'),
(2, 2, 2, 'Diagnóstico 2 para Paciente 2', '2024-05-06'),
(3, 3, 3, 'Diagnóstico 3 para Paciente 3', '2024-05-07'),
(4, 4, 4, 'Diagnóstico 4 para Paciente 4', '2024-05-08'),
(5, 5, 5, 'Diagnóstico 5 para Paciente 5', '2024-05-09'),
(6, 6, 6, 'Diagnóstico 6 para Paciente 6', '2024-05-10'),
(7, 7, 7, 'Diagnóstico 7 para Paciente 7', '2024-05-11'),
(8, 8, 8, 'Diagnóstico 8 para Paciente 8', '2024-05-12'),
(9, 9, 9, 'Diagnóstico 9 para Paciente 9', '2024-05-13'),
(10, 10, 10, 'Diagnóstico 10 para Paciente 10', '2024-05-14');

INSERT INTO Enfermedad (id_enfermedad, id_diagnostico, nombre_enfermedad) VALUES
(1, 1, 'Enfermedad 1'),
(2, 2, 'Enfermedad 2'),
(3, 3, 'Enfermedad 3'),
(4, 4, 'Enfermedad 4'),
(5, 5, 'Enfermedad 5'),
(6, 6, 'Enfermedad 6'),
(7, 7, 'Enfermedad 7'),
(8, 8, 'Enfermedad 8'),
(9, 9, 'Enfermedad 9'),
(10, 10, 'Enfermedad 10');

INSERT INTO Orden (id_orden, id_paciente, id_medico, id_examen, fecha_orden, comentarios_orden) VALUES
(1, 1, 1, 1, '2024-05-05', 'Orden 1 para Paciente 1'),
(2, 2, 2, 2, '2024-05-06', 'Orden 2 para Paciente 2'),
(3, 3, 3, 3, '2024-05-07', 'Orden 3 para Paciente 3'),
(4, 4, 4, 4, '2024-05-08', 'Orden 4 para Paciente 4'),
(5, 5, 5, 5, '2024-05-09', 'Orden 5 para Paciente 5'),
(6, 6, 6, 6, '2024-05-10', 'Orden 6 para Paciente 6'),
(7, 7, 7, 7, '2024-05-11', 'Orden 7 para Paciente 7'),
(8, 8, 8, 8, '2024-05-12', 'Orden 8 para Paciente 8'),
(9, 9, 9, 9, '2024-05-13', 'Orden 9 para Paciente 9'),
(10, 10, 10, 10, '2024-05-14', 'Orden 10 para Paciente 10');
