import  random
import os

listResultados = []

def ImprimirResultados():
    print("--------------- True Results ----------------")
    print(f"{listResultados}")

def main():
    while True:
        try:
            ImprimirResultados()
            print("--------------- Ask ----------------")
            n1 = random.randrange(0, 12)
            n2 = random.randrange(0, 12)
            resultado = int(input(f"{n1} * {n2}"))
            if resultado == n1 * n2:
                listResultados.append(resultado)
            else:
                print("INCORRECT")
            os.system("cls")
        except ValueError:
            print("pleas dont do that")
            os.system("cls")
if __name__ == "__main__":
    main()