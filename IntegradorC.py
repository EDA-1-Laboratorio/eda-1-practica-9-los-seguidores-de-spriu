import re
def contar_palabras(texto):
    # TODO: Retornar el número total de palabras
    palabras = texto.split()
    return len(palabras)

def contar_oraciones(texto):
    # TODO: Contar oraciones (terminan en '.', '!' o '?')
    oraciones = re.split(r'[.!?]', texto)
    return len([o for o in oraciones if o.strip()])

def palabra_mas_frecuente(texto):
    # TODO: Retornar la palabra que más se repite (ignorar mayúsculas)
    # Pista: usa un diccionario para contar frecuencias
    limpio = re.sub(r'[^\w\s]', '', texto).lower()
    palabras = limpio.split()
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return max(frecuencias, key=frecuencias.get) if frecuencias else None

def palabras_unicas(texto):
    # TODO: Retornar un conjunto (set) de palabras únicas
    limpio = re.sub(r'[^\w\s]', '', texto).lower()
    return set(limpio.split())

def longitud_promedio_palabras(texto):
    # TODO: Retornar la longitud promedio de las palabras
    palabras = texto.split()
    if not palabras: return 0
    total_caracteres = sum(len(p.strip(".,!?¡¿")) for p in palabras)
    return total_caracteres / len(palabras)
def buscar_palabra(texto, palabra):

    # TODO: Retornar cuántas veces aparece la palabra en el texto
    limpio = re.sub(r'[^\w\s]', '', texto).lower()
    palabras = limpio.split()
    return palabras.count(palabra.lower())
def reemplazar_palabra(texto, vieja, nueva):

    # TODO: Retornar el texto con la palabra vieja reemplazada por la nueva
    return texto.replace(vieja, nueva)

# Texto de ejemplo para analizar
texto_ejemplo = """Python es un lenguaje de programación muy popular. Python es fácil de
aprender. Muchos programadores usan Python para ciencia de datos y para desarrollo web.
Python tiene una gran comunidad. La comunidad de Python es muy activa y amigable.
¿Te gusta programar? ¡Python es una excelente opción para empezar!"""
print("=== ANALIZADOR DE TEXTO ===")
print(f"Total de palabras: {contar_palabras(texto_ejemplo)}")
print(f"Total de oraciones: {contar_oraciones(texto_ejemplo)}")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_ejemplo)}")
print(f"Palabras únicas: {len(palabras_unicas(texto_ejemplo))}")
print(f"Longitud promedio: {longitud_promedio_palabras(texto_ejemplo):.1f}")
print(f"Veces que aparece 'Python': {buscar_palabra(texto_ejemplo, 'Python')}")

nuevo = reemplazar_palabra(texto_ejemplo, "Python", "Java")
print(f"\nTexto modificado (primeras 100 letras):\n{nuevo[:100]}...")

