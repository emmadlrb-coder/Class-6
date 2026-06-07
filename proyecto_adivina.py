#  ════════════════════════════════════════════════════════════════════
#   PROYECTO: ADIVINA EL NÚMERO SECRETO
#   Sesión 06 · Fundamentos de Programación · UNITEC
#  ════════════════════════════════════════════════════════════════════
#
#   Vas a construir un juego: la computadora elige un número secreto y
#   el jugador intenta adivinarlo. Después de cada intento, el programa
#   da una pista ("muy alto" / "muy bajo") hasta que acierta o se le
#   acaban los intentos.
#
#   CÓMO TRABAJAR EN ESTE ARCHIVO
#   -----------------------------
#   Sigue los pasos EN ORDEN. Debajo de cada comentario "# PASO N" hay
#   un espacio en blanco: ahí escribes TU código. No borres los
#   comentarios. Cuando termines un paso, corre el programa y prueba que
#   no truene antes de seguir al siguiente.
#
#   HERRAMIENTAS QUE VAS A USAR (todo lo que ya viste)
#   --------------------------------------------------
#     · una librería (import random)
#     · constantes (MAYÚSCULAS)
#     · variables y validación de entrada
#     · funciones con return
#     · un ciclo for
#
#   Al final del archivo tienes un ejemplo de cómo debe verse el juego
#   funcionando. ¡Mucho éxito!
#  ════════════════════════════════════════════════════════════════════


# PASO 1: Importa la librería "random". La vas a necesitar para que la
#         computadora elija un número al azar. (Va siempre hasta arriba.)

import random


# PASO 2: Crea TRES constantes (nómbralas EN MAYÚSCULAS):
#           NUMERO_MIN     con valor 1
#           NUMERO_MAX     con valor 100
#           MAX_INTENTOS   con valor 7
NUM_MIN = 1
NUM_MAX = 100
MAX_INTENTOS = 7

# PASO 3: Crea una función llamada "generar_secreto" que NO reciba nada
#         y DEVUELVA (return) un número al azar entre NUMERO_MIN y
#         NUMERO_MAX.
#         Pista: random.randint(NUMERO_MIN, NUMERO_MAX)

def generar_secreto():
    return random.randint(NUM_MIN,NUM_MAX)


# PASO 4: Crea una función llamada "dar_pista" que reciba dos parámetros:
#         "secreto" y "intento". Debe devolver:
#           "muy alto"  -> si intento es MAYOR que secreto
#           "muy bajo"  -> si intento es MENOR que secreto
#           "correcto"  -> si son IGUALES
def dar_pista(secreto, intento):
    if intento > secreto:
        return "muy alto"
    elif intento < secreto:
        return "muy bajo"
    else:
        return "correcto"

# PASO 5: Llama a generar_secreto() y guarda lo que devuelve en una
#         variable llamada "secreto".
jugar_de_nuevo = True
while jugar_de_nuevo:
    secreto = generar_secreto()


# PASO 6: Da la bienvenida al jugador con print(). Dile entre qué números
#         está el secreto (usa NUMERO_MIN y NUMERO_MAX) y cuántos intentos

    print(f"\n¡Adivina el número entre {NUM_MIN} y {NUM_MAX}! "
          f"Tienes {MAX_INTENTOS} intentos.")

# PASO 7: Crea una variable llamada "adivinado" con valor False.
#         La usarás más adelante para saber si el jugador ya ganó.

    adivinado = False

# PASO 8: Escribe un ciclo "for" que se repita MAX_INTENTOS veces.
#         Pista: for intento in range(MAX_INTENTOS):
#         OJO: el código de los pasos 9, 10 y 11 va DENTRO de este for
#         (todo indentado hacia adentro).

    for intento in range(MAX_INTENTOS):


# PASO 9: (DENTRO del for) Pide un número al jugador con input(),
#         conviértelo a entero con int() y guárdalo en una variable
#         llamada "numero".
        while True:
            entrada = input("Tu numero: ")
            if entrada.lstrip("-").isdigit():
                numero = int(entrada)
                if NUM_MIN <= numero <= NUM_MAX:
                    break
                else:
                    print(f"  Ingresa un númemro entre {NUM_MIN} y {NUM_MAX}.")
            else:
                print("  Eso no es un número entero válido.")


# PASO 10: (DENTRO del for) Llama a dar_pista(secreto, numero) y guarda
#          el resultado en una variable llamada "pista".

        pista = dar_pista(secreto, numero)

# PASO 11: (DENTRO del for) Revisa la pista:
#            · Si pista es "correcto":
#                - imprime un mensaje de felicitación
#                - cambia "adivinado" a True
#                - usa  break  para salir del ciclo
#            · Si no, imprime la pista para orientar al jugador
#              (por ejemplo: "Tu número es muy alto").

        if pista == "correcto":
            intentos_usados = intento + 1
            print(f"¡Felicidades! Adivinaste en {intentos_usados} "
                  f"{'intento' if intentos_usados == 1 else 'intentos'}.")
            adivinado = True
            break
        else:
            print(f"Tu numero es {pista}.")

# PASO 12: (FUERA del for, sin indentar) Si "adivinado" sigue siendo
#          False, es que se acabaron los intentos. Imprime un mensaje
#          revelando cuál era el número secreto.

    if not adivinado:
        print(f"¡Se acabaron los intentos! El número secreto era {secreto}.")
    
    respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    jugar_de_nuevo = respuesta == "s"

print("\n¡Hasta la proxima!")


#  ════════════════════════════════════════════════════════════════════
#   EJEMPLO DE UNA PARTIDA YA FUNCIONANDO
#  --------------------------------------------------------------------
#     ¡Adivina el número entre 1 y 100! Tienes 7 intentos.
#     Tu número: 50
#     Tu número es muy alto
#     Tu número: 25
#     Tu número es muy bajo
#     Tu número: 37
#     Tu número es muy bajo
#     Tu número: 43
#     ¡Felicidades! Adivinaste en pocos intentos.
#
#   RETOS EXTRA (si terminas antes y quieres más)
#   --------------------------------------------------------------------
#     · Cuenta y muestra en cuántos intentos ganó el jugador.
#     · Valida que el número ingresado esté entre NUMERO_MIN y NUMERO_MAX.
#     · Al final, pregunta si quiere volver a jugar.
#  ════════════════════════════════════════════════════════════════════