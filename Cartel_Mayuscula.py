frase = input("Frase: ")

frase_mayusculas = frase.upper()

vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"

contador_vocales = 0

for caracter in frase:
    if caracter in vocales:
        contador_vocales += 1

print(f'Mayúsculas: "{frase_mayusculas}"; Vocales: {contador_vocales}')