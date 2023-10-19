invitadosAceptados = []
invitadosRechazados = []

# Requisitos de ingreso
edad = 16
contadorAceptados = 0
contadorRechazados = 0

bienvenida = input("Bienvenido a la fiesta, ¿deseas continuar? (si/no): ")
while bienvenida.lower() == "si":
    nombreUsuario = input("Ingresa tu nombre: ")
    edadUsuario = int(input("Ingresa tu edad: "))
    vestimenta = input("¿Tu disfraz es hawaiano o tiene algún accesorio hawaiano? (Si o No): ").strip().lower()

    cumpleVestimenta = False
    if vestimenta == "si":
        vestimentaUsuario = input("Escribe cual de estas opciones llevas en tu disfraz: (camisa de flores, falda de hierba, pantaloneta hawaiana, collar de flores): ").strip().lower()
        vestimentaHawaiana = ["camisa de flores", "falda de hierba", "pantaloneta hawaiana", "collar de flores"]
        for i in vestimentaHawaiana:
            if i in vestimentaUsuario:
                cumpleVestimenta = True
                break

    arma = input("¿Portas algun tipo de arma? (Si o No): ").strip().lower()

    causaDeRechazo = []
    if edadUsuario < edad:
        causaDeRechazo.append(f"No cumples con la edad minima requerida ({edad} años) para el ingreso a la fiesta.")
    if vestimenta != "si" or not cumpleVestimenta:
        causaDeRechazo.append("Tu disfraz no es adecuado para la fiesta, por lo tanto no puedes ingresar.")
    if arma == "si":
        causaDeRechazo.append("El ingreso de armas esta prohibido en la fiesta y estas portando un arma, por lo tanto no puedes ingresar.")

    if not causaDeRechazo:
        contadorAceptados += 1
        invitadosAceptados.append({"Nombre": nombreUsuario, "Edad": edadUsuario})
        print("¡Bienvenido a la fiesta hawaiana, DISFRUTA AL MAXIMO! :D")
    else:
        contadorRechazados += 1
        invitadosRechazados.append({"Nombre": nombreUsuario, "Edad": edadUsuario, "Motivo de Rechazo": causaDeRechazo})
        print("Lo siento, no cumples con alguno de los requisitos para ingresar a la fiesta hawaiana.")

    bienvenida = input("¿Deseas continuar? (si/no): ")
    while bienvenida.lower()=="no":
        break

print("Informe de usuarios aceptados a la fiesta: ")
for invitado in invitadosAceptados:
    print(f"Nombre: {invitado['Nombre']}, Edad: {invitado['Edad']}")

print("Informe de usuarios cuyo ingreso a la fiesta ha sido rechazado: ")
for invitado in invitadosRechazados:
    print(f"Nombre: {invitado['Nombre']}, Edad: {invitado['Edad']}, Razones de Rechazo: {', '.join(invitado['Motivo de Rechazo'])}")

print("\nInforme de usuarios que no han ingresado a la fiesta:")
for invitado in invitadosRechazados:
    print(f"Nombre: {invitado['Nombre']}, Edad: {invitado['Edad']}, Razon de Rechazo: {', '.join(invitado['El motivo por el cual usted no puede ingresar a la fiesta es'])}")
