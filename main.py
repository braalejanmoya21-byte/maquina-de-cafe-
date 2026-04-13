from pedidos import pedir_cafe
from menu import mostrar_menu
from historial import ver_historial

def main ():
    while True:
        mostrar_menu()

        opcion = input ("selecciones una opcion: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
              ver_historial()
        elif opcion == "3":
            print("\n Muchas Gracias por usar la maquina de cafe, vuelva pronto")
            break
        else:
            print("\n opcion invalida, por favor vuelva a elejir")

if  __name__=="__main__":
    main()