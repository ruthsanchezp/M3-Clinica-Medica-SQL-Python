# Aplicación de Consola para Clínica Médica 

Este repositorio contiene una aplicación de consola desarrollada en Python que permite gestionar la información de pacientes, médicos, habitaciones, camas y exámenes médicos en una clínica médica. Utiliza PostgreSQL como motor de base de datos para almacenar y recuperar la información necesaria.

## Caso de Aplicación

En una clínica médica, los pacientes ingresan y se les asigna una cama. Las camas están en habitaciones, y cada una de estas tiene muchas camas. Cada paciente tiene asignado un médico el cual puede tratar a muchos pacientes. El médico puede ordenar diferentes exámenes para un paciente, estos exámenes están tipificados y en la orden de examen, el médico indica un posible diagnóstico. El paciente puede cambiar de médico durante su estadía en el hospital. Cada médico puede o pudo diagnosticar una o más enfermedades a un paciente. Las enfermedades están tipificadas, sin embargo, el médico debe especificar qué exámenes de laboratorio consideró para el diagnóstico de cada enfermedad.

## Conocimientos

- Conocimientos de modelado relacional y SQL.
- Familiaridad con la programación en Python.
- Entorno de desarrollo como Miniconda con las librerías necesarias.
- PostgreSQL instalado en el sistema.

## Instrucciones de Desarrollo

1. **Modelado Relacional y Diseño de la Base de Datos**:
   - Diseñar un modelo relacional que represente las entidades y relaciones del caso de aplicación.
   - Crear la estructura de la base de datos en PostgreSQL utilizando el diseño del modelo relacional.

2. **Población de la Base de Datos**:
   - Generar un script SQL que inserte al menos 10 registros por tabla para poblar la base de datos.

3. **Implementación de la Aplicación de Consola**:
   - Desarrollar una aplicación de consola en Python que contenga un menú para acceder a las funcionalidades.
   - Funcionalidades incluidas:
     - Mostrar información de pacientes, incluyendo rut, nombre, diagnóstico, médico tratante y habitación.
     - Mostrar detalle de un paciente por rut, incluyendo información adicional como último examen realizado y cama asignada.
     - Cambiar a un paciente de cama.
     - Cambiar a un paciente de médico.
     - Crear camas y habitaciones.

