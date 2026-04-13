
ARCHIVOS_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de pedidos:")
        with open(ARCHIVOS_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(str(i) + ". " + pedido.strip())
    except FileNotFoundError:
        print("\n No se a creado un historial de pedidos.")