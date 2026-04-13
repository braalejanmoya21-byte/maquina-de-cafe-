
ARCHIVOS_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n elige el cafe que prefieras")
    print("1. espresso ")
    print("2. americano")
    print("3. capuchino")
    print("4. latte")
    
    opcion = input("selecciona una opcion: ")

    cafe = {
        "1": "espresso",
        "2": "americano",
        "3": "capuchino",
        "4": "latte"
    }
    if opcion in cafe:
        cafe_elegido = cafe[opcion]
        print("has elegido un "+ cafe_elegido + " preparando tu cafe")
        
        with open(ARCHIVOS_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
            
    else:
        print("\n opcion no es valida, por favor vuelva a elegir")