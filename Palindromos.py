frase = input("Frase: ")

normalizado = frase.lower().replace(" ", "")

if len(normalizado) == 0:
    print("Sin letras; Palíndromo: False")
else:
    
    es_palindromo = (normalizado == normalizado[::-1])
    
    print(f'Normalizado: "{normalizado}"; Palíndromo: {es_palindromo}')