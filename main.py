import time
import requests
from bs4 import BeautifulSoup

# Altera cores de textos
AMARELO = "\033[33m"
RESET = "\033[0m"

# Consulta um site de rimas
site2 = "https://pt.azrhymes.com/?q="

print("Rimas\n")

# Faz um loop principal
buscando = True
while buscando:
    rima1 = input("Digite uma palavra: ")
    print("\n")

    print(AMARELO + "Buscando rimas para", rima1 + "..." + RESET)

    time.sleep(1)

    resultado = requests.get(site2 + rima1)
    soup = BeautifulSoup(resultado.text, "html.parser")

    def mostrar_rimas():
        for rimas in soup.find_all("span", class_="result"):
            if rimas:
                print(rimas.text)
            else:
                print("Nenhuma rima encontrada.")

    print("\n")

    print(AMARELO + "Rimas encontradas:" + RESET)

    print("\n")
    mostrar_rimas()
    print("\n")
