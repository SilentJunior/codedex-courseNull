""" 
main para probrar el ejercicio
"""
import ejerciciopractico

empleadofulltime: ejerciciopractico.EmpleadoTiempoCompleto = ejerciciopractico.EmpleadoTiempoCompleto(
    "Luis", 5000)
empleadoparttime: ejerciciopractico.EmpleadoTiempoParcial = ejerciciopractico.EmpleadoTiempoParcial(
    "Juan", 2500, 80)

empleadofulltime.mostrar_detalles()
print("--------------------")
empleadoparttime.mostrar_detalles()
