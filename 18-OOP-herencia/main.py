""" 
Main.py -> herencia
"""
import clases

perso: clases.Persona = clases.Persona("Jose", "Garcia", 167, 27)
# perso.setnombre("Jose")
# perso.setapellidos("Garcia")
# perso.setaltura(167)
# perso.setedad(27)

print(
    f"La persona es {perso.getnombre()} {perso.getapellidos()} y tiene {perso.getedad()} años")
print(perso.hablar())
print(perso.dormir())
print("--------------------------------------------------")
inform: clases.Informatico = clases.Informatico(
    "JJ", "GN", 167, 27, "Python, Java", 3)
print(
    f"El informatico es {inform.getnombre()} {inform.getapellidos()}, es informatico")
print(
    f"Tiene {inform.getexperiencia()} años programando en {inform.getlenguajes()}")
print(inform.programar())
print(inform.repararpc())
