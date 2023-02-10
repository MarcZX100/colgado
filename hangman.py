

#formas = ["  _______\n |/      |\n |      (_)\n |      \|/\n |       |\n |      / \\\n |\n_|___"]
formas = [["  _______"," |/      "," |      "," |      "," |       "," |      "," |","_|___"], # Sin cuerda
["  _______"," |/      |"," |         "," |        "," |        "," |      "," |","_|___"], # Sin cabeza
["  _______"," |/      |"," |      (_)"," |        "," |        "," |      "," |","_|___"], # Sin cuerpo
["  _______"," |/      |"," |      (_)"," |       |"," |       |"," |      "," |","_|___"], # Sin brazo izquierdo
["  _______"," |/      |"," |      (_)"," |      \|"," |       |"," |      "," |","_|___"], # Sin brazo derecho
["  _______"," |/      |"," |      (_)"," |      \|/"," |       |"," |      "," |","_|___"], # Sin piernas
["  _______"," |/      |"," |      (_)"," |      \|/"," |       |"," |        \\"," |","_|___"], # Sin pierna izquierda
["  _______"," |/      |"," |      (_)"," |      \|/"," |       |"," |      / \\"," |","_|___"]] # Entero


"""cont = 0
for i in formas:
    print(f"{formas[cont][0]}\n{formas[cont][1]}\n{formas[cont][2]}\n{formas[cont][3]}\n{formas[cont][4]}\n{formas[cont][5]}\n{formas[cont][6]}\n{formas[cont][7]}")
    cont += 1"""

def printHangman(posicion: int):
    print(f"{formas[posicion][0]}\n{formas[posicion][1]}\n{formas[posicion][2]}\n{formas[posicion][3]}\n{formas[posicion][4]}\n{formas[posicion][5]}\n{formas[posicion][6]}\n{formas[posicion][7]}")

while True:
    num = input("ooomagat\n > ")
    printHangman(int(num))