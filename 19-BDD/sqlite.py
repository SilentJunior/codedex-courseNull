""" 
SQLite

SQLite es un sistema de gestión de bases de datos relacional ligero,
independiente y de código abierto, que se almacena en un solo archivo.
Fue diseñado para ser eficiente y rápido, funcionando sin necesidad de
un servidor separado, ya que se integra dentro de la aplicación que lo 
usa. Es compatible con la mayoría del estándar SQL y soporta 
transacciones ACID, lo que garantiza la integridad y confiabilidad de los datos.

Entre sus características principales destacan que es small footprint 
(menos de 300KB), autocontenida (no requiere dependencias externas),
multiplataforma y muy utilizada en dispositivos móviles y aplicaciones
de escritorio. SQLite almacena toda la base de datos en un archivo 
estándar del sistema y permite accesos simultáneos en lectura, aunque 
la escritura es serie para evitar conflictos. Además, es una herramienta 
ideal para desarrollos con Python por su fácil integración y uso sin 
configuración compleja.
"""
import sqlite3

# Conexión
conn = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conn.cursor()

# Crear tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
    id integer primary key autoincrement not null,
    titulo varchar(255),
    descripcion text,
    precio int(255)
    );
    ''')

# Guardar cambios
conn.commit()

# # Insertar datos
# cursor.execute("""INSERT INTO productos VALUES(
#     null,
#     "Jabón",
#     "Jabón para las manos, quita 99% las bacterias",
#     2.5
#     );
#     """)
# conn.commit()

# Listar datos
cursor.execute("select * from productos;")
productos = cursor.fetchall()

for i in productos:
    print(i)

# Cerrar Conexión
conn.close()
