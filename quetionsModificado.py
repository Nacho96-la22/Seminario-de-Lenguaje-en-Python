import random
# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?",
             "¿Cuál de las siguientes opciones es un número entero en Python?",
             "¿Cómo se solicita entrada del usuario en Python?",
             "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
             "¿Cuál es el operador de comparación para verificar si dos valores son iguales?"]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [("size()", "len()", "length()", "count()"),
           ("3.14", "'42'", "10", "True"),
           ("input()", "scan()", "read()", "ask()"),
           ("// Esto es un comentario","/* Esto es un comentario */",
            "-- Esto es un comentario","# Esto es un comentario",),
            ("=", "==", "!=", "==="),]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Puntaje del jugador por pedido 7.2
puntaje = 0.0

# He modificado por pedido 7.3 y 7.4
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for pregunta,opcion,correcto in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(pregunta)

    for i, answer in enumerate(opcion):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es correcta
        # He modificado por pedido el 7.1 y 7.2
        if user_answer.isdigit(): # se transforma un string a un entero para pueda comparar la condicion.
            user_num = int(user_answer)
            if ((user_num - 1) == correcto):
                print("¡Correcto!")
                puntaje += 1.0
                break
            else: 
                print("Respuesta no valida")
                puntaje -= 0.5
        else:
            exit(1) # Sino se cierra el programa por error no es valida un string.
    else:
        # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(opcion[correcto])
    # Se imprime un blanco al final de la pregunta
    print()

# Mostrar el puntaje final
print(f"El final de la partida, tu puntaje es {puntaje}")