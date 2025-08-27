""" 
BDD

La base de datos (BDD) es un sistema organizado para almacenar, gestionar y recuperar datos 
de manera eficiente. Se estructuran en tablas que contienen filas (registros) y columnas (campos),
permitiendo representar información de forma lógica y accesible.

Conceptos clave de BDD

Modelo relacional: Es el modelo más común, donde los datos se organizan en tablas con relaciones 
entre ellas, usando claves primarias y foráneas para mantener la integridad.

SQL (Structured Query Language): Lenguaje estándar para interactuar con bases de datos relacionales, 
permite consultas, inserciones, actualizaciones, y eliminación de datos.

Transacciones: Permiten agrupar varias operaciones para que todas se ejecuten 
correctamente o ninguna, garantizando la consistencia de la base de datos.

Normalización: Proceso de diseño para eliminar redundancias y dependencias indeseadas,
mejorando la eficiencia y la integridad.

Sistemas de gestión de bases de datos (SGBD): Software que facilita la creación, mantenimiento 
y uso de bases de datos, como MySQL, PostgreSQL, SQLite.

El conocimiento de BDD es fundamental para desarrollar aplicaciones y sitios web que 
manejan datos de manera robusta y eficiente, especialmente con Python que ofrece herramientas 
como SQLite integradas y librerías para conectar con diversos SGBD.

ELEMENTOS

Los elementos que conforman una base de datos (BDD) son principalmente:

Tablas: Son el componente principal y almacenan los datos en filas (registros) y 
columnas (campos o atributos), representando entidades específicas como clientes, productos, etc.

Registros: Cada fila de una tabla representa un registro, que es una instancia 
concreta de la entidad, con valores específicos para cada campo.

Campos (columnas): Son las unidades verticales de una tabla, cada uno con un tipo 
y nombre específico, que almacenan una categoría de información (por ejemplo, nombre, 
edad, dirección).

Claves: Son campos especiales que identifican de forma única cada registro, como 
la clave primaria, y permiten establecer relaciones entre tablas mediante claves foráneas.

Consultas: Son comandos o instrucciones para acceder, modificar, eliminar o agregar 
datos en las tablas.

Índices: Estructuras que permiten acelerar la búsqueda y acceso a los datos.

Relaciones: Enlaces entre tablas que establecen cómo se conectan los datos, típicamente 
representados por las claves foráneas.

Estos elementos permiten organizar, manipular y asegurar la integridad y consistencia 
de los datos en una base relacional de manera eficiente y estructurada.

"""
