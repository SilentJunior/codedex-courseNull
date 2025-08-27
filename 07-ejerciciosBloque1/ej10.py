""" 
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
            y sacar por pantalla cuantos han aprobado y cuantos han suspendido.
"""

contador = 1
aprobados = 0
suspendidos = 0
while contador <= 15:
    notaAlumno = int(input(f"Alumno {contador}, nota final: "))
    if notaAlumno > 15:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1

print(f"\nAprobados= {aprobados}\nSuspendidos= {suspendidos}")
