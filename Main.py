import Juego

partida = Juego.Juego()

partida.borrar_pantalla()
print("Bienvenido")
print("1. Jugar contra un amigo.")
print("2. Jugar contra la máquina.")
opcion = input("Elija una opcion:")
match opcion:
    case "1":
        partida.jugar_1_vs_1()
    case "2":
        partida.jugar_con_IA()
