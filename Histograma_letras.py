texto = input("Texto: ")

texto_limpio = texto.lower().replace(" ", "")

if len(texto_limpio) == 0:
    print("Total: 0; Distintas: 0; Más frecuente: ninguna")
else:
    letras_ordenadas = []
    frecuencias = {}

    for letra in texto_limpio:
        if letra not in frecuencias:
            letras_ordenadas.append(letra)
            frecuencias[letra] = 1
        else:
            frecuencias[letra] += 1

    total_letras = len(texto_limpio)
    distintas = len(letras_ordenadas)
    mas_frecuente = letras_ordenadas[0]
    max_frecuencia = frecuencias[mas_frecuente]

    for letra in letras_ordenadas:
        cant = frecuencias[letra]
        barra = "*" * cant
        print(f"{letra}: {cant} {barra}")
        
        if cant > max_frecuencia:
            max_frecuencia = cant
            mas_frecuente = letra
    print(f"Total: {total_letras}; Distintas: {distintas}; Más frecuente: {mas_frecuente}")