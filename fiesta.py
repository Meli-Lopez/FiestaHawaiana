invitadosAceptados = []
invitadosRechazados = []

# Requisitos de ingreso
edad = 16
vestimentaHawaiana = True
porteArmas = False


nombreUsuario = input("Ingresa tu nombre: ")
edadUsuario = int(input("Ingresa tu edad: "))
vestimenta = input("¿Tu disfraz es hawaiano o tiene algun accesorio hawaiano? (Si o No): ").strip().lower()
vestimentaUsuario = input("Escribe cual de estas opciones llevas en tu disfraz: (camisa de flores, falda de hierbas, pantaloneta hawaiana, collar de flores): ").strip().lower()
arma = input("¿Portas algun tipo de arma? (Si o No): ").strip().lower()

cumpleVestimenta = False
vestimentaHawaiana = ["camisa de flores", "falda de hierba", "pantaloneta hawaiana", "collar de flores"]

for i in vestimentaHawaiana:
    if i in vestimentaUsuario:
        cumpleVestimenta = True
        break

if edadUsuario >= edad and vestimenta == "si" and arma == "no" and cumpleVestimenta:
    invitadosAceptados.append({"Nombre": nombreUsuario, "Edad": edadUsuario})
    print("¡Bienvenido a la fiesta hawaiana, DISFRUTA AL MAXIMO :D!")
else:
    causaDeRechazo = []
    if edadUsuario < edad:
        causaDeRechazo.append("No cumple con la edad minima para el ingreso a la fiesta segun los requisitos.")
    if vestimenta != "si":
        causaDeRechazo.append("Su disfraz no es adecuado para la fiesta, por lo tanto no puede ingresar.")
    if arma != "no":
        causaDeRechazo.append("El ingreso de armas es prohibido en la fiesta y usted porta un arma, por lo tanto no puede ingresar.")
    else:
        print("No puede ingresar a la fiesta")

'''
invitadosRechazados.append({"Nombre": nombreUsuario, "Edad": edadUsuario, "El motivo por el cual usted no puede ingresar a la fiesta es": causaDeRechazo})    
print("Lo siento, no cumples con alguno de los requisitos para ingresar a la fiesta hawaiana.")


print("\nInforme de usuarios que han ingresado a la fiesta:")
for invitado in invitadosAceptados:
    print(f"Nombre: {invitado['Nombre']}, Edad: {invitado['Edad']}")

print("\nInforme de usuarios que no han ingresado a la fiesta:")
for invitado in invitadosRechazados:
    print(f"Nombre: {invitado['Nombre']}, Edad: {invitado['Edad']}, Razon de Rechazo: {', '.join(invitado['El motivo por el cual usted no puede ingresar a la fiesta es'])}")
'''