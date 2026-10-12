def dia_semana(dia):
    match dia:
        case "Domingo":
            return True
        case "Lunes":
            return True
        case "Martes":
            return False
        case "Miercoles":
            return False
        case "Jueves":
            return False
        case "Viernes":
            return False
        case "Sabado":
            return False
        case _:
            return(False)

print(dia_semana("Martes"))