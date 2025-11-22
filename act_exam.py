num_estudiantes = int(input("¿Cuántos estudiantes hay? "))
num_materias = int(input("¿Cuántas materias tienen? "))

matriz = []

print("\n--- Captura de calificaciones ---")
for i in range(num_estudiantes):
    fila = []
    print(f"\nEstudiante {i+1}:")
    for j in range(num_materias):
        cal = float(input(f"  Calificación de la materia {j+1}: "))
        fila.append(cal)
    matriz.append(fila)

promedio_estudiantes = []
for fila in matriz:
    promedio_estudiantes.append(sum(fila) / num_materias)

promedio_materias = []
for j in range(num_materias):
    suma = 0
    for i in range(num_estudiantes):
        suma += matriz[i][j]
    promedio_materias.append(suma / num_estudiantes)

mayor = max(max(fila) for fila in matriz)
menor = min(min(fila) for fila in matriz)

print("\n\n--- RESULTADOS ---")

print("\nPromedio de cada estudiante:")
for i, p in enumerate(promedio_estudiantes):
    print(f"  Estudiante {i+1}: {p:.2f}")

print("\nPromedio de cada materia:")
for j, p in enumerate(promedio_materias):
    print(f"  Materia {j+1}: {p:.2f}")

print(f"\nCalificación más ALTA: {mayor}")
print(f"Calificación más BAJA: {menor}")
