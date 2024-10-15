def ingresar_puntuacion():
    """Solicita y devuelve una puntuación en una escala de 1 a 5."""
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                return point
            else:
                print('Por favor, introduzca un valor entre el 1 y 5')
        else:
            print('Por favor, introduzca la puntuación en números')

def ingresar_comentario():
    """Solicita y devuelve un comentario del usuario."""
    print('Por favor, introduzca un comentario')
    return input()

def guardar_resultado(point, comment):
    """Guarda la puntuación y el comentario en un archivo."""
    post = f'punto: {point} comentario: {comment}'
    try:
        with open("data.txt", 'a') as file_pc:
            file_pc.write(f'{post}\n')
        print("Guardado exitosamente.")
    except Exception as e:
        print(f"Error al guardar en el archivo: {e}")

def mostrar_resultados():
    """Muestra los resultados guardados en el archivo hasta la fecha."""
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            resultados = read_file.read()
            if resultados:
                print(resultados)
            else:
                print("No hay resultados hasta ahora.")
    except FileNotFoundError:
        print("No hay resultados hasta ahora.")

def seleccionar_proceso():
    """Solicita al usuario seleccionar un proceso y lo ejecuta."""
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        
        num = input("Ingrese su opción: ")
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                point = ingresar_puntuacion()
                comment = ingresar_comentario()
                guardar_resultado(point, comment)
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca un número del 1 al 3')
        else:
            print('Por favor, introduzca un número del 1 al 3')

# Ejecuta el programa
seleccionar_proceso()


