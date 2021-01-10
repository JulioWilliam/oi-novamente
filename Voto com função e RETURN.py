from datetime import date
from time import sleep


def pera():
    print("Aguarde...")
    sleep(1)


def voto():
    a2 = int(input("Ano de nascimento: ").strip())
    a1 = date.today().year - a2
    if a1 < 16:
        pera()
        return "NEGADO"
    elif a1 >= 16 and a1 < 18 or a1 >= 65:
        pera()
        return "OPCIONAL"
    elif a1 >= 18 and a1 < 65:
        pera()
        return "OBRIGATÓRIO"


print(voto())
