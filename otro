-- Primero, crea la tabla que no tiene dependencias
CREATE TABLE Habitacion (
    id_habitacion INT PRIMARY KEY,
    numero_habitacion INT
);

-- Luego crea Cama, que depende de Habitacion
CREATE TABLE Cama (
    id_cama INT PRIMARY KEY,
    numero_cama INT,
    id_habitacion INT,
    FOREIGN KEY (id_habitacion) REFERENCES Habitacion(id_habitacion)
);

-- Ahora, puedes crear Paciente que depende de Cama
CREATE TABLE Paciente (
    id_paciente INT PRIMARY KEY,
    nombre_paciente VARCHAR(255),
    fecha_ingreso DATE,
    fecha_alta DATE,
    id_cama INT,
    FOREIGN KEY (id_cama) REFERENCES Cama(id_cama)
);

CREATE TABLE Medico (
    id_medico INT PRIMARY KEY,
    nombre_medico VARCHAR(255)
);

CREATE TABLE Examen (
    id_examen INT PRIMARY KEY,
    nombre_examen VARCHAR(255),
    tipo_examen VARCHAR(255)
);

CREATE TABLE Enfermedad (
    id_enfermedad INT PRIMARY KEY,
    nombre_enfermedad VARCHAR(255)
);

CREATE TABLE Diagnostico (
    id_diagnostico INT PRIMARY KEY,
    detalle_diagnostico TEXT,
    fecha_diagnostico DATE
);

CREATE TABLE RegistroAtencionMedico (
    id_registro_atencion INT PRIMARY KEY,
    id_medico INT,
    id_paciente INT,
    fecha_atencion DATE,
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);
CREATE TABLE RegistroDiagnosticoExamen (
    id_registro_diagnostico_examen INT PRIMARY KEY,
    id_diagnostico INT,
    id_examen INT,
    FOREIGN KEY (id_diagnostico) REFERENCES Diagnostico(id_diagnostico),
    FOREIGN KEY (id_examen) REFERENCES Examen(id_examen)
);

CREATE TABLE Orden (
    id_orden INT PRIMARY KEY,
    id_paciente INT,
    id_medico INT,
    id_examen INT,
    fecha_orden DATE,
    detalle_orden TEXT,
    id_registro_diagnostico_examen INT,
    FOREIGN KEY (id_registro_diagnostico_examen) REFERENCES RegistroDiagnosticoExamen(id_registro_diagnostico_examen),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico),
    FOREIGN KEY (id_examen) REFERENCES Examen(id_examen)
);

CREATE TABLE DiagnosticoEnfermedad (
    id_diagnostico_enfermedad INT PRIMARY KEY,
    id_diagnostico INT,
    id_enfermedad INT,
    FOREIGN KEY (id_diagnostico) REFERENCES Diagnostico(id_diagnostico),
    FOREIGN KEY (id_enfermedad) REFERENCES Enfermedad(id_enfermedad)
);


-- Inserción de datos en la tabla Habitacion
INSERT INTO Habitacion (id_habitacion, numero_habitacion) VALUES
(1, 101), (2, 102), (3, 103), (4, 104), (5, 105), 
(6, 106), (7, 107), (8, 108), (9, 109), (10, 110);

-- Inserción de datos en la tabla cama
INSERT INTO cama (id_cama, numero_cama, id_habitacion) VALUES
(1, 01, 1 ), (2, 02, 1), (3, 03, 1), (4, 01, 2), (5, 02, 2),
(6, 03, 2), (7, 01, 3), (8, 02, 3), (9, 03, 3), (10, 01, 4);

INSERT INTO Paciente (id_paciente, nombre_paciente, fecha_ingreso, fecha_alta, id_cama)
VALUES 
(1, 'Pedro', '2024-04-01', '2024-04-02', 1), 
(2, 'Rodrigo', '2024-04-03', '2024-04-04', 2),
(3, 'Javiera', '2024-03-18', '2024-04-04', 3),
(4, 'Pia', '2024-01-09', '2024-02-14', 4),
(5, 'Camilo', '2024-02-05', '2024-03-15', 5),
(6, 'Manuel', '2024-01-10', '2024-04-12', 6),
(7, 'Paula', '2023-03-04', '2024-04-19', 7),
(8, 'Camila', '2024-04-10', '2024-04-15', 8),
(9, 'Andres', '2024-04-10', '2024-04-15', 9),
(10, 'Daniela', '2024-04-10', '2024-04-15', 10);


INSERT INTO medico (id_medico, nombre_medico) VALUES
(1, 'DRA Salgado'), (2, 'DR Martines'), (3, 'DR Manriquez'),
(4, 'DR Pedreros'), (5, 'DR Sanchez'), (6, 'DR Urrutia'),
(7, 'DR Contreras'), (8, 'DR Rojas'), (9, 'DRA Arrigada'),
(10, 'DRA Venegas');

INSERT INTO examen (id_examen, nombre_examen, tipo_examen) VALUES
(1, 'Resonancia', 'Imagenologico'), (2, 'Densitometria', 'Imagenologico'), (3, 'Petct', 'Imagenologico'),
(4, 'Scanner', 'Imagenologico'), (5, 'Ecografia', 'Imagenologico'), (6, 'Octavo Par', 'Fonoaudiologia'),
(7, 'VHS', 'Laboratorio' ), (8, 'VDRL', 'Laboratorio'), (9, 'Perfil Lipidico', 'Laboratorio'),
(10, 'Glucosa', 'Laboratorio');

INSERT INTO enfermedad (id_enfermedad, nombre_enfermedad) VALUES
(1, 'Diabetes'), (2, 'Gastritis'), (3, 'Covid'),  (4, 'Gripe'), (5, 'Conjuntivitis'),
(6, 'Gastroenteritis'), (7, 'Arritmia'), (8, 'Osteoporosis'),  (9, 'Faringitis'),  
(10, 'Insuficiencia Renal');

INSERT INTO diagnostico (id_diagnostico, detalle_diagnostico, fecha_diagnostico) 
VALUES
(1, 'Dolor abdominal en la parte superior', '2023-11-17'), 
(2, 'Dolor de cabeza y mareo', '2023-11-19'), 
(3, 'Resfriado común', '2024-11-01'), 
(4, 'Líquido en la rodilla', '2024-05-01'), 
(5, 'Esguince de pie', '2024-04-01'), 
(6, 'Migraña crónica', '2024-05-01'),
(7, 'Problema cardíaco', '2022-05-01'),
(8, 'Infección gastro', '2023-07-01'),
(9, 'Problema mental', '2025-03-01'),
(10, 'Problema neurológico', '2022-08-01');

INSERT INTO RegistroAtencionMedico (id_registro_atencion, id_medico, id_paciente, fecha_atencion) 
VALUES
(1, 1, 1, '2021-02-21'),
(2, 1, 1, '2023-03-04'),
(3, 3, 1, '2022-04-14'),
(4, 4, 1, '2023-05-13'),
(5, 5, 1, '2024-06-12'),
(6, 4, 1, '2023-02-02'),
(7, 5, 1, '2024-04-03'),
(8, 6, 1, '2023-05-05'),
(9, 8, 1, '2024-03-03'),
(10, 9, 1,'2024-04-21');

-- Insert para RegistroDiagnosticoExamen
INSERT INTO RegistroDiagnosticoExamen (id_registro_diagnostico_examen, id_diagnostico, id_examen) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- Insert para DiagnosticoEnfermedad
INSERT INTO DiagnosticoEnfermedad (id_diagnostico_enfermedad, id_diagnostico, id_enfermedad) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);
