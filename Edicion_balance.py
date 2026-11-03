palabra_reservada = input("Reservada: ").strip().lower()
N = int(input("N: "))

validos_total = 0
invalidos_total = 0
palabras_total = 0
sustituciones_total = 0

max_palabras = -1
msg_mas_palabras = 0

for i in range(1, N + 1):
    mensaje = input(f"Mensaje {i}: ")
    
    limpio = ""
    for char in mensaje:
        if char in ".,!?":
            limpio += " "
        else:
            limpio += char
            
    tokens = limpio.split()
    
    if len(tokens) == 0:
        print(f"{i}: Inválido")
        invalidos_total += 1
    else:
        validos_total += 1
        cantidad_palabras = len(tokens)
        palabras_total += cantidad_palabras
        
        if cantidad_palabras > max_palabras:
            max_palabras = cantidad_palabras
            msg_mas_palabras = i
        
        palabras_editadas = []
        sustituciones_msg = 0
        
        for token in tokens:
            p_min = token.lower()
            if p_min == palabra_reservada:
                palabras_editadas.append("[oculto]")
                sustituciones_msg += 1
            else:
                palabras_editadas.append(p_min)
                
        sustituciones_total += sustituciones_msg
        texto_editado = " ".join(palabras_editadas)
        
        print(f'{i}: "{texto_editado}"; Palabras: {cantidad_palabras}; Sustituciones: {sustituciones_msg}')

if palabras_total > 0:
    porcentaje = (100 * sustituciones_total) / palabras_total
else:
    porcentaje = 0.00

porcentaje_str = f"{porcentaje:.2f}".replace(".", ",")

print(f"Válidos: {validos_total}; Inválidos: {invalidos_total}; Palabras: {palabras_total}; Sustituciones: {sustituciones_total}; Porcentaje: {porcentaje_str} %; Más palabras: mensaje {msg_mas_palabras}")