# Sistema de Gestión Bancaria Orientado a Objetos

## Descripción del Proyecto
Este repositorio contiene la arquitectura de un sistema de gestión bancaria modular programado en Python. El sistema simula las operaciones fundamentales de una institución financiera, permitiendo la administración estructurada de diferentes tipos de cuentas (Débito, Crédito, Nómina) y la gestión de la cartera de ejecutivos.

## Metodología y Arquitectura Técnica
El desarrollo del sistema se diseñó fundamentado estrictamente en los principios de la Programación Orientada a Objetos (POO):
* **Abstracción y Herencia:** Creación de una superclase abstracta (`Cuenta`) que hereda atributos y define comportamientos polimórficos obligatorios para las subclases específicas.
* **Encapsulamiento:** Protección de datos sensibles (números de cuenta, saldos, RFC) mediante el uso riguroso de atributos privados y métodos *getters/setters*.
* **Persistencia de Datos:** Implementación de controladores para la lectura y escritura automatizada en archivos `.csv`, garantizando la integridad de los datos entre sesiones.

## Tecnologías Utilizadas
* **Python** (Lógica de clases, polimorfismo, manejo de excepciones y manipulación de archivos).
