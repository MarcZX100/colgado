

#formas = ["  _______\n |/      |\n |      (_)\n |      \|/\n |       |\n |      / \\\n |\n_|___"]
formas = [["  _______"," |/      "," |      "," |      "," |       "," |      "," |","_|___"],   # Sin cuerda              0
["  _______"," |/      |"," |         "," |        "," |        "," |      "," |","_|___"],      # Sin cabeza              1
["  _______"," |/      |"," |      (_)"," |        "," |        "," |      "," |","_|___"],      # Sin cuerpo              2
["  _______"," |/      |"," |      (_)"," |       |"," |       |"," |      "," |","_|___"],      # Sin brazo izquierdo     3
["  _______"," |/      |"," |      (_)"," |      \|"," |       |"," |      "," |","_|___"],      # Sin brazo derecho       4
["  _______"," |/      |"," |      (_)"," |      \|/"," |       |"," |      "," |","_|___"],     # Sin piernas             5
["  _______"," |/      |"," |      (_)"," |      \|/"," |       |"," |        \\"," |","_|___"], # Sin pierna izquierda    6
["  _______"," |/      |"," |      (_)"," |      \|/"," |       |"," |      / \\"," |","_|___"]] # Entero                  7


def printHangman(posicion: int):
    print(f"{formas[posicion][0]}\n{formas[posicion][1]}\n{formas[posicion][2]}\n{formas[posicion][3]}\n{formas[posicion][4]}\n{formas[posicion][5]}\n{formas[posicion][6]}\n{formas[posicion][7]}")

listaLetrasProbadas = []
listaLetrasEncontradas = []
listaLetras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
listaLetrasNoUsadas = listaLetras.copy()

def comprovarRepetida(input):
    #input = "0".lower()
    if input.lower() in listaLetrasNoUsadas:
        None
    else:
        print(f"ERROR! Deberías introducir una letra que aún no hayas usado.\nPuedes usar cualquiera de la siguiente lista: {', '.join(listaLetrasNoUsadas).upper()}.")


a = input("")
comprovarRepetida(a)
def letrasCorrectas(lista, letraIntroducida, palabraResultado):
    cont = 0
    for letra in palabraResultado:
        if letra.lower() == letraIntroducida.lower():
            lista.append(cont)
        cont += 1
    return lista

#def letrasCorrectas

while True:
    a = input(" > ")
    letrasEncontradas = letrasCorrectas(listaLetrasEncontradas, a, "Holaa")
    print(letrasEncontradas)


errores = 0
palabraResultado = input("Introduce una palabra para luego buscar.\n > ")

while errores < 7:
    print(errores)
    printHangman(errores)
    input()
    errores+=1

print("Derrota")
printHangman(errores)
