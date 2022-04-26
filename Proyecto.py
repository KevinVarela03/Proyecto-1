from datetime import date
import time
import utils 
import hashlib
from agenda import usuarios_admin
from agenda import usuarios_estud
import datetime

cursos = [[(('Programacion',)) ,'4', '3', '20/11/2022', '13/03/2023', (("Lunes",)),'15:00','19:00', {'Ingenieria en Computacion'}], 
            [(('Ingles',)) ,'2', '3', '20/11/2022', '13/03/2023',  (("Martes",)), '12:00','15:00', {'Ingenieria en Computacion', 'Administracion de Empresas', 'Ingenieria en Agronomia'}]]
cursos2 = []
carreras = {'Ingenieria en Computacion', 'Administracion de Empresas', 'Ingenieria en Agronomia'}
cursos3 = set()
codigos_ansi = ("\033[94m", "\033[0;0m", chr(27) + "[2J", "\033[33m", "\033[31m", "\033[35m", "\033[32m") 
carreras_estudiante  = []
carreras2 = []
cursos_posibles = []
cursos_estudiante = []
cont3 = 0
cont4 = 0
tope = 0
tope2 = 0
actividades = {}
dias = {
        "Lunes" : [], 
        "Martes" : [], 
        "Miercoles" : [], 
        "Jueves" : [], 
        "Viernes" : [], 
        "Sabado" : [], 
        "Domingo" : []
        }
print(codigos_ansi[2])
print(codigos_ansi[0] + 
"""     
    -------------------------------
     Bienvenido al sistema del TEC
    -------------------------------
"""
    + codigos_ansi[1])
time.sleep(0.2)
print(codigos_ansi[3] + "Digite el numero de su posición académica\n"+ codigos_ansi[1])
time.sleep(0.2)
print("1) Administrativo")
time.sleep(0.2)
print("2) Estudiante")
time.sleep(0.2)
print("3) Salir\n")
time.sleep(0.2)
estudiante_o_administrativo=int(input("Su posición es: "))
time.sleep(0.3)
print(codigos_ansi[2])
while estudiante_o_administrativo != 1 or estudiante_o_administrativo != 2: ## Ingresar a un tipo de usuario, ya sea administrativo o estudiante
    condicion = True 
    if estudiante_o_administrativo == 1: ## Ingreso de usuarios administrativos
        print(codigos_ansi[3] + "Ingrese su nombre de usuario y contraseña\n" + codigos_ansi[1])
        usuario = input("Nombre de usuario: ") ## Se obtiene el nombre de usuario
        contraseña=utils.cifrar(utils.obtener_calve("Contraseña")) ## Se obtiene la contraseña cifrada
        time.sleep(1)
        print(codigos_ansi[2])
        cont = 0
        lista_gen = []
        for x in usuarios_admin:  
            for y in x['autenticacion']['usuario']: 
                for z in x['autenticacion']['tupla_contraseña']:
                    lista_gen.append(y)
                    lista_gen.append(z)
        if usuario in lista_gen: ## Se verifica que el usuario sea el correcto
            print(codigos_ansi[2])
            time.sleep(0.3)
            if contraseña in lista_gen: ## Se verifica que la contraseña sea la correcta
                condicion = True 
                while condicion == True:
                    print(codigos_ansi[3] + "Seleccione el número de la opción que desea realizar\n" + codigos_ansi[1])  ## Se solicta al usuario que seleccione una opción 
                    time.sleep(0.2)
                    print("1) Agregar un curso")
                    time.sleep(0.2)
                    print("2) Modificar un curso")
                    time.sleep(0.2)
                    print("3) Añadir una carrera")
                    time.sleep(0.2)
                    print("4) Modificar una carrera")
                    time.sleep(0.2)
                    print("5) Añadir un nuevo usuario")
                    time.sleep(0.3)
                    print("6) Salir\n")
                    time.sleep(0.2)
                    accion = int(input("Su opción es: "))
                    time.sleep(0.3)
                    print(codigos_ansi[2])
                    if accion == 1: ## Agregar un curso
                        if len(carreras) > 0:
                            cursos2 = []
                            valor_ingresado = input("Ingrese el nombre del curso: ")
                            valor_ingresado = ((valor_ingresado,))
                            time.sleep(0.3)
                            cursos2.append(valor_ingresado)
                            valor_ingresado = input ("Ingrese el número de creditos: ")
                            time.sleep(0.3)
                            cursos2.append(valor_ingresado)
                            valor_ingresado = int(input("Ingrese el número de horas lectivas diarias: "))
                            time.sleep(0.3)
                            cursos2.append(valor_ingresado)
                            fecha1 = datetime.date.fromisoformat(input("Ingrese la fecha de inicio del curso (Formato: AAAA-MM-DD): "))
                            fecha1 = fecha1.strftime('%Y/%m/%d')
                            cursos2.append(fecha1)
                            time.sleep(0.3)
                            fecha2 = datetime.date.fromisoformat(input("Ingrese la fecha de finalización del curso (Formato: AAAA-MM-DD): "))
                            fecha2 = fecha2.strftime('%Y/%m/%d')
                            if fecha1 > fecha2:
                                while fecha1 > fecha2:
                                    print(codigos_ansi[4] + 'INGRESE UNA FECHA VÁLIDA' + codigos_ansi[1])
                                    fecha2 = datetime.date.fromisoformat(input("Ingrese la fecha de finalización (Formato: AAAA-MM-DD): "))
                                    fecha2 = fecha2.strftime('%Y/%m/%d')
                            else:
                                pass
                            cursos2.append(fecha2)
                            time.sleep(0.3)
                            valor_ingresado = input("Ingrese el día de la clase: ")
                            valor_ingresado = ((valor_ingresado,))
                            cursos2.append(valor_ingresado)
                            time.sleep(0.3)
                            hora1 = datetime.time.fromisoformat(input("Ingrese la hora de inicio de la clase (Formato de 24 horas): "))
                            hora1 = hora1.strftime('%H:%M')
                            time.sleep(0.3)
                            cursos2.append(hora1)
                            hora2 = datetime.time.fromisoformat(input("Ingrese la hora de finalización de la clase (Formato de 24 horas): "))
                            hora2 = hora2.strftime('%H:%M')
                            if hora1 > hora2:
                                while hora1 > hora2:
                                    print(codigos_ansi[4] + 'INGRESE UNA HORA VÁLIDA' + codigos_ansi[1])
                                    hora2 = datetime.time.fromisoformat(input("Ingrese la hora de finalización de la clase (Formato de 24 horas): "))
                                    hora2 = hora2.strftime('%H:%M')
                            cursos2.append(hora2)
                            time.sleep(0.3)
                            carreras = list(carreras)
                            print("Ingrese el número de la carrera a la que pertenece el curso (Digite 0 cuando haya finalizado)\n")
                            time.sleep(0.3)
                            cont = 0
                            for e in carreras:
                                print('\t', cont + 1,")", carreras[cont])
                                time.sleep(0.3)
                                cont = cont + 1
                            print("")
                            valor_ingresado = int(input("Su opción es: "))
                            time.sleep(0.3)
                            cursos3.add(carreras[valor_ingresado-1])
                            while valor_ingresado != 0:
                                accion = int(input("Su opción es: "))
                                    
                                if accion != 0:
                                    cursos3.add(carreras[accion-1])
                                if accion == 0:
                                    valor_ingresado = 0
                            cursos2.append(cursos3)
                            cursos.append(cursos2)    
                            print(codigos_ansi[2])
                        else:
                            print(codigos_ansi[4] + 'PRIMERO DEBE AÑADIR UNA CARRERA' + codigos_ansi[1])
                            time.sleep(1)
                            print(codigos_ansi[2])
                        print('')
                        print(codigos_ansi[6] + '¡Curso agregado con éxito!'+ codigos_ansi[1])
                        time.sleep(0.5)
                        print(codigos_ansi[2])
                    elif accion == 2: ## Modificar un curso
                        print(codigos_ansi[3] + "Digite el número del curso a modificar\n" + codigos_ansi[1])
                        time.sleep(0.3)
                        cont = 0
                        for e in cursos:
                            for i in e:
                                for f in i:
                                    print(cont + 1,")", f)
                                    time.sleep(0.2)
                                    cont = cont + 1
                                break
                        print("")
                        valor_ingresado3 = int(input("El curso es: "))
                        nueva_lista = []
                        cursos2 = []
                        nueva_lista = cursos.pop(valor_ingresado3-1)
                        print(codigos_ansi[2])
                        time.sleep(0.2)
                        print(codigos_ansi[3] + "¿Que desea modificar?\n" + codigos_ansi[1])
                        time.sleep(0.2)
                        print("1) Nombre del curso ")
                        time.sleep(0.2)
                        print("2) Numero de creditos ")
                        time.sleep(0.2)
                        print("3) Numero de horas lectivas")
                        time.sleep(0.2)
                        print("4) Fecha de inicio")
                        time.sleep(0.2)
                        print("5) Fecha de finalizacion")
                        time.sleep(0.2)
                        print("6) Horario de clases")
                        time.sleep(0.2)
                        print("7) Agregar o borrar carrera a la cual pertenece")
                        time.sleep(0.2)
                        print("8) Eliminar curso")
                        time.sleep(0.2)
                        print("9) Salir")
                        time.sleep(0.2)
                        print("")
                        valor_ingresado2 = int(input("Su opción es: "))
                        time.sleep(0.2)
                        cont = 0
                        if valor_ingresado2 == 1: ## Modificar el nombre del curso
                            print(codigos_ansi[2])
                            valor_ingresado = input("Ingrese el nuevo nombre: ")
                            nueva_lista.pop(0)
                            valor_ingresado = ((valor_ingresado,))
                            nueva_lista.insert(0,valor_ingresado)
                            cursos.append(nueva_lista)
                            print('')
                            print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5) 
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == 2: ## Modificar la  cantidad de créditos
                            print(codigos_ansi[2])
                            valor_ingresado = input("Ingrese los nuevos creditos: ")
                            nueva_lista.pop(1)
                            nueva_lista.insert(1,valor_ingresado)
                            cursos.append(nueva_lista)
                            print('')
                            print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5) 
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == 3: ## Modificar la cantidad de horas lectivas por día
                            print(codigos_ansi[2])
                            valor_ingresado = int(input("Ingrese el número nuevo de horas lectivas: "))
                            nueva_lista.pop(2)
                            nueva_lista.insert(2,valor_ingresado)
                            cursos.append(nueva_lista)
                            print('')
                            print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5) 
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == 4:  ## Modificar la fecha de inicio del curso
                            print(codigos_ansi[2])
                            fecha1 = datetime.date.fromisoformat(input("Ingrese la nueva fecha de inicio (Formato: AAAA-MM-DD): "))
                            fecha1 = fecha1.strftime('%Y/%m/%d')
                            while fecha1 > fecha2: 
                                if fecha1 > fecha2:
                                    print( codigos_ansi[4] + "¡¡¡INGRESE UNA FECHA VÁLIDA!!!" + codigos_ansi[1])
                                    time.sleep(0.2)
                                    fecha1 = datetime.date.fromisoformat(input("Ingrese la nueva fecha de inicio (Formato: AAAA-MM-DD): "))
                                    fecha1 = fecha1.strftime('%Y/%m/%d')
                            nueva_lista.pop(3)
                            nueva_lista.insert(3,fecha1)
                            cursos.append(nueva_lista)
                            print('')
                            print(codigos_ansi[6] + 'El cambio se realizó con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5) 
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == 5: ## Modificar la fecha de finalización del curso
                            print(codigos_ansi[2])
                            fecha2 = datetime.date.fromisoformat(input("Ingrese la nueva fecha de finalizacion (Formato: AAAA-MM-DD): "))
                            fecha2 = fecha2.strftime('%Y/%m/%d')
                            while fecha1 > fecha2:
                                if fecha1 > fecha2:
                                    print( codigos_ansi[4] + "¡¡¡INGRESE UNA FECHA VÁLIDA!!!" + codigos_ansi[1])
                                    time.sleep(0.2)
                                    fecha2 = datetime.date.fromisoformat(input("Ingrese la nueva fecha de inicio (Formato: AAAA-MM-DD): "))
                                    fecha2 = fecha2.strftime('%Y/%m/%d')
                            nueva_lista.pop(4)
                            nueva_lista.insert(4,fecha2)
                            cursos.append(nueva_lista)
                            print('')
                            print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5) 
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == 6: ## Modificar el horario del curso
                            print(codigos_ansi[2])
                            print(codigos_ansi[3] + "Ingrese el número de la opción deseada\n" + codigos_ansi[1])
                            print("1) Editar el día de la clase")
                            print("2) Editar la hora de inicio de la clase")
                            print("3) Editar la hora de finalización de la clase\n")
                            valor_ingresado = input("Su opción es: ")
                            print(codigos_ansi[2])
                            if valor_ingresado  == '1': ## Modificar el día de la clase
                                valor_ingresado3 = input("Ingrese el nuevo día de la clase: ")
                                nueva_lista.pop(5)
                                valor_ingresado3 = ((valor_ingresado3,))
                                nueva_lista.insert(5, valor_ingresado3)
                                cursos.append(nueva_lista)
                                print('')
                                print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5) 
                                print(codigos_ansi[2])
                            elif valor_ingresado == '2': ## Modificar la hora de entrada de la clase
                                hora1 = datetime.time.fromisoformat(input("Ingrese la nueva hora de inicio de la clase (Formato de 24 horas): "))
                                hora1 = hora1.strftime('%H:%M')
                                nueva_lista.pop(6)
                                nueva_lista.insert(6,hora1)
                                cursos.append(nueva_lista) 
                                print('')
                                print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5) 
                                print(codigos_ansi[2])
                            elif valor_ingresado == '3': ## Modificar la hora de salida de la clase
                                hora2 = datetime.time.fromisoformat(input("Ingrese la nueva hora de finalización de la clase (Formato de 24 horas): "))
                                hora2 = hora2.strftime('%H:%M')
                                nueva_lista.pop(7)
                                nueva_lista.insert(7,hora2)
                                cursos.append(nueva_lista)
                                print('')
                                print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5) 
                                print(codigos_ansi[2])
                        elif valor_ingresado2 == 7: ## Modificar las carreras a las que pertenece el curso
                            carreras2 = []
                            print(codigos_ansi[2])
                            for x in nueva_lista[8]:
                                carreras2.append(x)
                            print(codigos_ansi[3] + "Seleccione el número de la opción que desea realizar\n" + codigos_ansi[1])
                            time.sleep(0.2)
                            print("1) Agregar carrera")
                            time.sleep(0.2)
                            print("2) Eliminar carrera\n")
                            valor_ingresado4 = input("Su opción es: ")
                            print(codigos_ansi[2])
                            if valor_ingresado4 == "1": ## Añadir el curso a una nueva carrera
                                cont = 0
                                print(codigos_ansi[3] + "Ingrese el número de la carrera\n"+ codigos_ansi[1])
                                carreras = list(carreras)
                                for e in carreras:
                                    print(cont + 1,")", carreras[cont])
                                    cont = cont + 1
                                print("")
                                valor_ingresado5 = int(input("Su opción es: "))
                                carreras2.append(carreras[valor_ingresado5-1])
                                carreras2 = set(carreras2)
                                nueva_lista.pop(8)
                                nueva_lista.append(carreras2)
                                carreras = set(carreras)
                                print('')
                                print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5) 
                                print(codigos_ansi[2])
                            elif valor_ingresado4 == "2": ## Eliminar el curso de una carrera
                                cont = 0
                                print(codigos_ansi[2])
                                print(codigos_ansi[3] + "Digite el número de la carrera\n" + codigos_ansi[1])
                                for x in carreras2:
                                    print(cont + 1,")", carreras2[cont])
                                    cont = cont + 1   
                                print("")                 
                                valor_ingresado4 = int(input("Su opción es: "))
                                carreras2.pop(valor_ingresado4-1)
                                carreras2 = set(carreras2)
                                nueva_lista.pop(8)
                                nueva_lista.append(carreras2)
                                print('')
                                print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5) 
                                print(codigos_ansi[2])
                            cursos.append(nueva_lista)
                        elif valor_ingresado2 == 8: ## Eliminar el curso
                            print(codigos_ansi[6] + '¡El cambio se realizó con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5) 
                            print(codigos_ansi[2])
                            pass
                        elif valor_ingresado2 == 9: ## Salir
                            print(codigos_ansi[2])
                            cursos.append(nueva_lista)
                            print(codigos_ansi[2])
                    elif accion == 3: ## Añadir una carrera 
                        print(codigos_ansi[2])
                        valor_ingresado = input ('Digite el nombre de la carrera que desea añadir: ')
                        carreras = set(carreras)
                        carreras.add(valor_ingresado)
                        print('')
                        print(codigos_ansi[6] + '¡Carrera agregada con éxito!'+ codigos_ansi[1])
                        time.sleep(0.5)
                        print(codigos_ansi[2])
                    elif accion == 4: ## Modificar una carrera
                        cont = 0
                        carreras = list(carreras)
                        print(codigos_ansi[3] + "Digite el número de la carrera a modificar\n" + codigos_ansi[1])
                        time.sleep(0.2)
                        for e in carreras:
                            print(cont + 1,")", carreras[cont])
                            time.sleep(0.2)
                            cont = cont + 1
                        print("")
                        valor_ingresado3 = int(input("Su opción es: "))
                        time.sleep(0.2)
                        print(codigos_ansi[2])
                        print(codigos_ansi[3] + "Digite el número de lo que desea modificar\n" + codigos_ansi[1])
                        time.sleep(0.2)
                        print("1) Nombre de la carrera ")
                        time.sleep(0.2)
                        print("2) Desvincular un curso de la carrera")
                        time.sleep(0.2)
                        print("3) Eliminar carrera")
                        time.sleep(0.2)
                        print("4) Salir")
                        time.sleep(0.2)
                        print("")
                        valor_ingresado2 = input("Su opción es: ")
                        time.sleep(0.3)
                        print(codigos_ansi[2])
                        if valor_ingresado2 == '1': ## Modificar el nombre de la carrera
                            carreras.pop(valor_ingresado3-1)
                            valor_ingresado = input("Ingrese el nuevo nombre: ")
                            carreras.append(valor_ingresado)
                            print('')
                            print(codigos_ansi[6] + '¡Cambio realizado con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5)
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == '2': ## Desvincular un curso de la carrera
                            carreras = list(carreras)
                            print(codigos_ansi[3] + 'Ingrese el numero del curso que desea desvincular\n' + codigos_ansi[1])
                            time.sleep(0.3)
                            vari1 = carreras[valor_ingresado3 - 1]
                            clase = []
                            cont = 1
                            a = 0
                            for y in cursos:
                                for z in y[8]:
                                    if carreras[valor_ingresado3 - 1] in y[8]:
                                        if a == 0:
                                            print(carreras[valor_ingresado3 - 1] + ':', '\n')
                                            a = 1
                                        clase.append(y[0])
                                        break
                            for i in clase:
                                for e in i:
                                    print(cont , ") " , e)
                                    cont = cont + 1
                            print("")
                            var = int(input("Su opción es: "))
                            print(codigos_ansi[2])
                            var1 = clase[var-1]
                            lista_nueva = []
                            carreras2 = []
                            for k in cursos:
                                for i in k:
                                    for f in i:
                                        if f in var1:
                                            cursos.remove(k)
                                            lista_nueva = k
                                            for x in lista_nueva[8]:
                                                carreras2.append(x)
                                            for b in carreras2:
                                                if vari1 == b:
                                                    lista_nueva.pop(8)
                                                    carreras2.remove(vari1)
                                                    carreras2 = set(carreras2)
                                                    lista_nueva.append(carreras2)
                                                    cursos.append(lista_nueva)
                                        else:
                                            pass
                                    break
                            print('')
                            print(codigos_ansi[6] + '¡Cambio realizado con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5)
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == '3': ## Eliminar la carrera
                            carreras.pop(valor_ingresado3-1)
                            print(codigos_ansi[6] + '¡Cambio realizado con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5)
                            print(codigos_ansi[2])
                        elif valor_ingresado2 == '4':
                            pass
                        carreras = set(carreras)
                    elif accion == 5: ## Agregar un usuario nuevo
                        print(codigos_ansi[3] + "Ingrese el número del usuario que desea agregar\n" + codigos_ansi[1])
                        time.sleep(0.2)
                        print("1) Administrativo")
                        time.sleep(0.2)
                        print("2) Estudiante")
                        time.sleep(0.2)
                        print("3) Salir\n")
                        time.sleep(0.2)
                        valor_ingresado = int(input("Su opción es: "))
                        time.sleep(0.2)
                        print(codigos_ansi[2])
                        dic_admin = {}
                        dic_estud = {}
                        lista_admin1 = ['nombre', 'apellido1', 'apellido2', 'telefono', 'autenticacion']
                        lista_admin2 = []
                        dic_autenticacion = {}
                        lista_autenticacion1 = ['usuario', 'contraseña', 'tupla_contraseña']
                        lista_autenticacion2 = []
                        clave_cifrada = 0
                        var_temp = []
                        cont = 0
                        estado = True
                        if valor_ingresado == 1: ## Agregar un usuario administrativo
                            while estado == True:
                                if valor_ingresado == 1:
                                    cont = 0
                                    estado = True
                                    nombre = input("Nombre: ")
                                    lista_admin2.append(nombre)
                                    apellido1 = input("Primer apellido: ")
                                    lista_admin2.append(apellido1)
                                    apellido2 = input("Segundo apellido: ")
                                    lista_admin2.append(apellido2)
                                    telefono = input("Número telefónico: ")
                                    lista_admin2.append(telefono)
                                    agregar_usuario = input("Nombre de usuario: ")
                                    agregar_clave = input("Contraseña: ")
                                    for x in usuarios_admin:
                                        for  y in x['autenticacion']['usuario']:
                                            var_temp.append(y)
                                    if agregar_usuario  not in var_temp:
                                        agregar_usuario = tuple((agregar_usuario,)) 
                                        lista_autenticacion2.append(agregar_usuario)
                                        clave_cifrada = hashlib.md5(agregar_clave.encode('ascii')).hexdigest()
                                        tupla_clave_cifrada = tuple((clave_cifrada,))
                                        lista_autenticacion2.append(clave_cifrada)
                                        lista_autenticacion2.append(tupla_clave_cifrada)
                                        while estado == True:
                                            for x in lista_autenticacion1:
                                                for y in lista_autenticacion2:
                                                    dic_autenticacion[x] = y
                                                    lista_autenticacion2.remove(y)
                                                    break
                                            estado = False
                                            lista_admin2.append(dic_autenticacion)
                                            estado = True
                                            while estado == True:
                                                for x in lista_admin1:
                                                    for y in lista_admin2:
                                                        dic_admin[x] = y
                                                        lista_admin2.remove(y)
                                                        break
                                                estado = False
                                                usuarios_admin.append(dic_admin)                  
                                        estado = False
                                    elif agregar_usuario in var_temp:
                                        print("ESTE USUARIO YA SE ENCUENTRA REGISTRADO")
                                        pass
                                    cont
                                print('')
                                print(codigos_ansi[6] + 'Usuario agregado con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5)
                                print(codigos_ansi[2])
                        elif valor_ingresado == 2: ## Agregar un usuario estudiante
                            lista_admin2 = []
                            var_temp = []
                            lista_autenticacion2 = []
                            dic_autenticacion = {}
                            while estado == True:
                                if valor_ingresado == 2:
                                    cont = 0
                                    estado = True
                                    nombre = input("Nombre: ")
                                    lista_admin2.append(nombre)
                                    apellido1 = input("Primer apellido: ")
                                    lista_admin2.append(apellido1)
                                    apellido2 = input("Segundo apellido: ")
                                    lista_admin2.append(apellido2)
                                    telefono = input("Número telefónico: ")
                                    lista_admin2.append(telefono)
                                    agregar_usuario = input("Nombre de usuario: ")
                                    agregar_clave = input("Contraseña: ")
                                    for x in usuarios_estud:
                                        for  y in x['autenticacion']['usuario']:
                                            var_temp.append(y)
                                    if agregar_usuario  not in var_temp:
                                        agregar_usuario = tuple((agregar_usuario,)) 
                                        lista_autenticacion2.append(agregar_usuario)
                                        clave_cifrada = hashlib.md5(agregar_clave.encode('ascii')).hexdigest()
                                        tupla_clave_cifrada = tuple((clave_cifrada,))
                                        lista_autenticacion2.append(clave_cifrada)
                                        lista_autenticacion2.append(tupla_clave_cifrada)
                                        while estado == True:
                                            for x in lista_autenticacion1:
                                                for y in lista_autenticacion2:
                                                    dic_autenticacion[x] = y
                                                    lista_autenticacion2.remove(y)
                                                    break
                                            estado = False
                                            lista_admin2.append(dic_autenticacion)
                                            estado = True
                                            while estado == True:
                                                for x in lista_admin1:
                                                    for y in lista_admin2:
                                                        dic_estud[x] = y
                                                        lista_admin2.remove(y)
                                                        break
                                                estado = False
                                                usuarios_estud.append(dic_estud)                  
                                        estado = False
                                    elif agregar_usuario in var_temp:
                                        print("ESTE USUARIO YA SE ENCUENTRA REGISTRADO")
                                        pass
                                    cont
                                print('')
                                print(codigos_ansi[6] + '¡Carrera agregada con éxito!'+ codigos_ansi[1])
                                time.sleep(0.5)
                                print(codigos_ansi[2])
                        elif valor_ingresado == 3:
                            pass
                    elif accion == 6: ## Salir del usuario administrativo
                        condicion = False
                        print(codigos_ansi[2])
                        print(codigos_ansi[0] + 
        """     
        ----------------------------------------
        Bienvenido al sistema de matrícula TEC
        ----------------------------------------
        """
                            + codigos_ansi[1])
                        time.sleep(0.2)
                        print(codigos_ansi[3] + "Digite el numero de su posición académica\n"+ codigos_ansi[1])
                        time.sleep(0.2)
                        print("1) Administrativo")
                        time.sleep(0.2)
                        print("2) Estudiante")
                        time.sleep(0.2)
                        print("3) Salir\n")
                        time.sleep(0.2)
                        estudiante_o_administrativo=int(input("Su posición es: "))
                        time.sleep(0.2)
                        print(codigos_ansi[2])
            else:
                print(codigos_ansi[4] +"¡¡¡USUARIO O CONTRASEÑA INCORRECTA!!!"+ codigos_ansi[1])
                time.sleep(3)
                print(codigos_ansi[2])
                pass
        else: 
            print(codigos_ansi[4] + "¡¡¡USUARIO O CONTRASEÑA INCORRECTA!!!" + codigos_ansi[1])
            time.sleep(3)
            print(codigos_ansi[2])
            pass  
    elif estudiante_o_administrativo == 2: ## Ingreso de usuarios estudiantes
        condicion = True
        print(codigos_ansi[3] + "Ingrese su nombre de usuario y contraseña\n" + codigos_ansi[1])
        usuario = input("Nombre de usuario: ") ## Se obtiene el nombre de usuario
        contraseña=utils.cifrar(utils.obtener_calve("Contraseña")) ## Se otiene la contraseña cifrada
        time.sleep(1)
        print(codigos_ansi[2])
        lista_gen = []
        for x in usuarios_estud:
            for y in x['autenticacion']['usuario']: 
                for z in x['autenticacion']['tupla_contraseña']:
                    lista_gen.append(y)
                    lista_gen.append(z)
        if usuario in lista_gen: ## Se verifica el nombre de usuario
            print(codigos_ansi[2])
            time.sleep(0.2)
            if contraseña in lista_gen: ## Se verifica la contraseña
                while condicion == True:
                    print (codigos_ansi[3] + 'Bienvenido estudiante. Digite el número de la opción que desea realizar\n' + codigos_ansi[1]) 
                    print("1) Matricular una carrera")
                    time.sleep(0.2)
                    print("2) Darse de baja en una carrera")
                    time.sleep(0.2)
                    print("3) Matricular un curso")
                    time.sleep(0.2)
                    print("4) Desvincular de un curso")
                    time.sleep(0.2)
                    print("5) Agregar actividades")
                    time.sleep(0.2)
                    print("6) Ver actividades")
                    time.sleep(0.2)
                    print("7) Generar reporte")
                    time.sleep(0.2)
                    print("8) Salir\n")
                    time.sleep(0.2)
                    accion = input("Su opción es: ")
                    print(codigos_ansi[2])
                    time.sleep(0.2)
                    if accion == '1': ## Matricular una carrera
                        if len(carreras_estudiante) < 1: ## Se matricula una carrera en caso de no haber matriculado una 
                            print(codigos_ansi[3] + 'Ingrese el número de la carrera que desea matricular\n' + codigos_ansi[1])
                            time.sleep(0.5)
                            cont = 1
                            for x in carreras:
                                print (cont, ')' , x)
                                time.sleep(0.2)
                                cont = cont+1
                            print("")
                            time.sleep(0.5)
                            accion = int(input("Su opción es: "))
                            time.sleep(1)
                            print(codigos_ansi[2])
                            carreras = list(carreras)
                            carreras_estudiante.append(carreras[accion-1])
                            print('')
                            print(codigos_ansi[6] + '¡Matrícula de carrera realizada con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5)
                            print(codigos_ansi[2])
                        elif len(carreras_estudiante) == 1: ## Se indica al usuario que ya hay una carrera matriculada
                            print(codigos_ansi[4] + "¡¡¡PARA MATRICULAR OTRA CARRERA DEBE DESVINCULARSE DE LA CARRERA ANTERIOR!!!" + codigos_ansi[1])
                            time.sleep(2)
                            print(codigos_ansi[2])
                            pass
                        carreras = set(carreras)
                    elif accion == '2': ## Darse de baja de una carrera
                        if len(carreras_estudiante) == 0: ## Se indica que para darse de baja debe matricular una carrera
                            print(codigos_ansi[4] + '¡¡¡DEBE MATRICULAR UNA CARRERA!!!' + codigos_ansi[1])
                            time.sleep(2)
                            print(codigos_ansi[2])
                        else: ## Se solicita la confirmación para darse de baja de la carrera matriculada
                            cont = 1
                            print(codigos_ansi[3] + "¿Realmente desea darse de baja de la carrera que está cursando actualmente? (Ingrese un 1 si su respuesta es 'Sí' o un 0 si su respuesta es 'No')\n" + codigos_ansi[1])
                            time.sleep(0.2)
                            accion = input("Su respuesta es: ")
                            time.sleep(0.5)
                            if accion == '1':
                                carreras_estudiante.clear()
                                cursos_estudiante.clear()
                                cursos_posibles.clear()
                            elif accion == '0':
                                pass
                            print(codigos_ansi[2])
                            print('')
                            print(codigos_ansi[6] + '¡Desvinculación realizada con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5)
                            print(codigos_ansi[2])
                    elif accion == '3': ## Matricular curso
                        curso_posible = []
                        cursos_posibles = []
                        if len(carreras_estudiante) > 0: ## Se seleccionan los cursos a matricular
                            print( codigos_ansi[3] + "Ingrese el número del curso a matricular (Ingrese 0 cuando haya finalizado)\n" + codigos_ansi[1])
                            time.sleep(0.2)
                            cont= 0
                            accion2 = 0
                            for a in cursos:
                                curso_posible = []
                                for b in a:
                                    if cont > 0:
                                        cont = cont+1
                                    if cont == 0:
                                        for n in a:
                                            curso_posible.append(n)
                                        cont = cont+1
                                    if  cont == 9:
                                        for d in b:
                                            if d in carreras_estudiante:
                                                if curso_posible not in cursos_posibles:
                                                    curso_posible.pop(8)
                                                    curso_posible.pop(4)
                                                    curso_posible.pop(3)
                                                    curso_posible.pop(1)
                                                    cursos_posibles.append(curso_posible)
                                                    curso_posible = []
                                                cont = 0
                                            cont = 0
                            cont2 = 1
                            for x in cursos_posibles:
                                for y in x:
                                    for k in y:
                                        print (cont2, ' )', k)
                                        time.sleep(0.2)
                                        cont2 = cont2+1
                                    break
                            print("")
                            accion = int(input("Su opción es: "))
                            time.sleep(0)
                            if accion != 0:
                                while accion != 0:
                                    if cursos_posibles[accion-1] not in cursos_estudiante:
                                        cursos_estudiante.append(cursos_posibles[accion-1])
                                        while accion != 0:
                                            accion = int(input("Su siguiente opción es: "))
                                            time.sleep(0)
                                            if accion != 0:
                                                if cursos_posibles[accion-1] not in cursos_estudiante:
                                                    cursos_estudiante.append(cursos_posibles[accion-1])
                                                else:
                                                    print('')
                                                    print(codigos_ansi[4] + "¡¡¡ESTE CURSO YA HA SIDO MATRICULADO!!!\n" + codigos_ansi[1])
                                                    accion = int(input("Su siguiente opción es: "))
                                                    time.sleep(0.3)
                                            elif accion == 0:
                                                pass
                                        print(codigos_ansi[2])
                                        print('')
                                        print(codigos_ansi[6] + '¡Cursos matriculados con éxito!'+ codigos_ansi[1])
                                        time.sleep(0.5)
                                        print(codigos_ansi[2])
                                    else:
                                        print('')
                                        print(codigos_ansi[4] + "¡¡¡ESTE CURSO YA HA SIDO MATRICULADO!!!\n" + codigos_ansi[1])
                                        accion = int(input("Su opción es: "))
                                        time.sleep(0.3)
                                        print(codigos_ansi[2])
                            elif accion == 0:
                                pass
                        elif len(cursos_posibles) == 0: ## Se indica que para matricular un curso se debe matricular una carrera
                            print(codigos_ansi[4] + "¡¡¡PARA MATRICULAR UN CURSO PRIMERO DEBE MATRICULAR UNA CARRERA¡¡¡" + codigos_ansi[1])
                            time.sleep(2)
                            print(codigos_ansi[2])
                            pass
                    elif accion == '4': ## Desvincularse de un curso
                        if len(cursos_estudiante) > 0: ## Se desvincula de un curso ya matriculado
                            cont = 1
                            print(codigos_ansi[3] + "Ingrese el número del curso del cual desea desvincularse\n" + codigos_ansi[1])
                            for x in cursos_estudiante:
                                for y in x[0]:
                                    print (cont, ')', y)
                                    time.sleep(0.2)
                                    cont = cont+1
                            print("")
                            accion = int(input('Su opción es: '))
                            cursos_estudiante.pop(accion-1)
                            print (cursos_estudiante)
                            print('')
                            print(codigos_ansi[6] + '¡Desvinculación realizada con éxito!'+ codigos_ansi[1])
                            time.sleep(0.5)
                            print(codigos_ansi[2])
                        else: ## Se indica que para desvincularse de un curso se debe matricular un curso
                            print(codigos_ansi[4] + '¡¡¡DEBE MATRICULAR COMO MÍNIMO 1 CURSO!!!')
                            time.sleep(2)
                            print(codigos_ansi[2])
                    elif accion == '5': ## Agregar actividades
                        if len(cursos_estudiante) == 0: ## Se indica que se debe matricular mínimo un curso para agregar una actividad 
                            print (codigos_ansi[4] + '¡¡¡DEBE MATRICULAR MÍNIMO 1 CURSO!!!' + codigos_ansi[1])
                            time.sleep(1)
                            print(codigos_ansi[2])
                        else: ## Si ya hay cursos matriculados, entonces se puede agregar actividades
                            if cont4 == 0:
                                for x in cursos_estudiante:
                                    for y in x[2]:
                                        for z in x[1]:
                                            z = int(z)
                                            dias[y].append(z)
                                            cont4 = cont4+1
                            actividad = input('Digite el nombre de la actividad que desea agregar: ')
                            time.sleep(0.2)
                            info_actividad = []
                            informacion = input('Añada una descripcion a su actividad: ')
                            time.sleep(0.2)
                            info_actividad.append(informacion)
                            cont = 1
                            print('Digite el número del curso al que se asocia esta actividad (en caso de no tener digite 0)')
                            for x in cursos_estudiante:
                                for y in x:
                                    for z in y:
                                        print ('\t', cont, ')', z)           
                                        cont = cont + 1
                                    break
                            informacion = int(input('Su opción es: '))
                            if informacion == 0:
                                info_actividad.append('Sin curso asociado')
                            else:
                                info_actividad.append(cursos_estudiante[informacion-1][0])
                            fecha1 = datetime.date.fromisoformat(input("Ingrese la fecha de inicio (Formato: AAAA-MM-DD): ")) 
                            fecha1 = fecha1.strftime('%Y/%m/%d')
                            fecha2 = datetime.date.fromisoformat(input("Ingrese la fecha de finalización (Formato: AAAA-MM-DD): "))
                            fecha2 = fecha2.strftime('%Y/%m/%d')
                            if fecha1 > fecha2:
                                while fecha1 > fecha2:
                                    print(codigos_ansi[4] + 'INGRESE UNA FECHA VÁLIDA' + codigos_ansi[1])
                                    fecha2 = datetime.date.fromisoformat(input("Ingrese la fecha de finalización (Formato: AAAA-MM-DD): "))
                                    fecha2 = fecha2.strftime('%Y/%m/%d')
                            info_actividad.append(fecha1)
                            info_actividad.append(fecha2)
                            palabras2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
                            cont= 1
                            print('Ingrese el número del día que desea ejercer esta actividad')
                            for x in palabras2:
                                print ("\t", cont, ')', x)
                                time.sleep(0.2)
                                cont = cont+1
                            informacion = int(input('Su opción es: '))
                            dia = palabras2[informacion-1]
                            info_actividad.append(dia)
                            informacion = int(input('Digite el numero de horas que desea invertir: '))
                            dias[dia].append(informacion)
                            tope2 = tope2+informacion
                            info_actividad.append(informacion) 
                            info_actividad.append('En proceso')
                            for x in dias.get(dia):
                                tope = tope + x
                            if cont3 == 0:
                                if tope > 12:
                                    print(codigos_ansi[2])
                                    print(codigos_ansi[4] + '¡¡¡LÍMITE DE HORAS DIARIAS ALCANZADA. LA ACTIVIDAD NO HA SIDO AÑADIDA!!!' + codigos_ansi[1])
                                    time.sleep(2)
                                    print(codigos_ansi[2])
                                    dias[dia].pop(-1)
                                    tope = 0
                                elif tope2 > 74:
                                    print(codigos_ansi[2])
                                    print(codigos_ansi[4] + '¡¡¡LÍMITE DE HORAS SEMANALES ALCANZADA. LA ACTIVIDAD NO HA SIDO AÑADIDA!!!' + codigos_ansi[1])
                                    time.sleep(2)
                                    print(codigos_ansi[2])
                                    dias[dia].pop(-1)
                                    tope2 = tope2-informacion
                                    tope = 0
                                else:
                                    actividades = {actividad:info_actividad}
                                    print('')
                                    print (codigos_ansi[6] + '¡Actividad agregada correctamente!' + codigos_ansi[1])
                                    time.sleep(1)
                                    print(codigos_ansi[2])
                                    cont3 = 1
                                    tope = 0
                            else:
                                if tope > 12:
                                    print(codigos_ansi[2])
                                    print(codigos_ansi[4] + '¡¡¡LÍMITE DE HORAS DIARIAS ALCANZADA. LA ACTIVIDAD NO HA SIDO AÑADIDA!!!' + codigos_ansi[1])
                                    time.sleep(2)
                                    print(codigos_ansi[2])
                                    dias[dia].pop(-1)
                                    tope = 0
                                elif tope2 > 74:
                                    print(codigos_ansi[2])
                                    print(codigos_ansi[4] + '¡¡¡LÍMITE DE HORAS SEMANALES ALCANZADA. LA ACTIVIDAD NO HA SIDO AÑADIDA!!!' + codigos_ansi[1])
                                    time.sleep(2)
                                    print(codigos_ansi[2])
                                    tope2 = tope2-informacion
                                    dias[dia].pop(-1)
                                    tope = 0
                                else: 
                                    actividades[actividad] = info_actividad
                                    print('')
                                    print (codigos_ansi[6] + '¡Actividad agregada correctamente!' + codigos_ansi[1])
                                    time.sleep(1)
                                    print(codigos_ansi[2])
                                    tope = 0
                    elif accion == '6': ## Ver actividades que ha agregado el usuario
                        palabras = ['Descripción:', 'Curso asociado:', 'Fecha de inicio:', 'Fecha de finalización:','Día:', 'Horas dedicadas:', 'Estado:']
                        if actividades == {}: ## Se indica que no posee actividades
                            print(codigos_ansi[4] + '¡¡¡NO POSEE ACTIVIDADES REGISTRADAS!!!')
                        else: ## Se logran visualizar todas las actividades actividades
                            print(codigos_ansi[5] + "ACTIVIDADES" + codigos_ansi[1])
                            actividades_nombre = []
                            cont = 0
                            valor = actividades.values()
                            key = actividades.keys()
                            for x in key:                                  
                                actividades_nombre.append(x)
                            cont2 = 0
                            for x in valor:
                                print("-------------------------------------------------------------")
                                print(cont2 + 1, ')', actividades_nombre[cont2])
                                cont = 0
                                for y in x:
                                    print('\t', palabras[cont], y )
                                    cont = cont+ 1
                                print("-------------------------------------------------------------") 
                                cont2 = cont2+1
                            accion = input('Ingrese la actividad que quiere marcar como ejecutada (tenga en cuenta las mayúsculas). Digite "0" si desea salir: ')
                            cont = 0
                            lista_temporal = []
                            Estado = False
                            for x in actividades:
                                if x == accion:
                                    for x in actividades.get(accion):
                                        lista_temporal.append(x)
                                        cont = cont+1
                                        if cont == 6:
                                            lista_temporal.append('Ejecutada')
                                            actividades[accion] = lista_temporal
                                            print('')
                                            print(codigos_ansi[6] + '¡Actividad marcada como ejecutada!' + codigos_ansi[1])
                                            time.sleep(1)
                                            print(codigos_ansi[2])
                                            Estado = True
                                            break
                            if Estado == False:
                                print(codigos_ansi[4] + '¡¡¡ACTIVIDAD NO ENCONTRADA!!!' + codigos_ansi[1])
                                time.sleep(2)
                                print(codigos_ansi[2])
                    elif accion == '7': ## Generar reporte
                        print(codigos_ansi[3] + "Ingrese el número de la opción deseada\n" + codigos_ansi[1])
                        time.sleep(0.2)
                        print('1) Reporte de actividades')
                        time.sleep(0.2)
                        print('12) Reporte de porcentaje de tiempo ejecutado')
                        time.sleep(0.2)
                        print('1) Reporte de tiempo disponible\n')
                        time.sleep(0.2)
                        valor_ingresado4 = input("Su opción es: ")
                        time.sleep(0.2)
                        print(codigos_ansi[2])
                        if valor_ingresado4 == '1': ## Se genera un reporte de las actividades 
                            dia_clases = ['Materia: ', 'Horas: ', 'Día: ', 'Hora de inicio: ', 'Hora de finalización :']
                            palabras2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
                            acts = []
                            dict_report = {}
                            cont = 0
                            cont2 = 0
                            print(codigos_ansi[3] + 'Ingrese el número del día del cual desea generar un reporte \n' + codigos_ansi[1])
                            for x in palabras2:
                                print(cont + 1, ')', x )
                                cont = cont + 1
                            valor_ingresado = int(input('Su opción es: '))
                            print(codigos_ansi[2])
                            print(codigos_ansi[3] + 'Actividades del '+ palabras2[valor_ingresado-1] + codigos_ansi[1])
                            print('-------------------------------------')
                            print(codigos_ansi[5] + 'Clases\n' + codigos_ansi[1])
                            for x in cursos_estudiante:
                                cond = True
                                for y in x[2]:
                                    if y == palabras2[valor_ingresado-1]:                                        
                                        for i in x:
                                            acts.append(i)
                                        for p in dia_clases:
                                            for l in acts:
                                                dict_report[p] = l
                                                acts.remove(l)
                                                break
                                        time.sleep(0.3)
                                        for clave, valor in dict_report.items():
                                            print('{} {}'.format(clave, valor))
                                        print('-------------------------------------')
                            for key in actividades:
                                valor_ingresado5 = actividades[key]
                                cont2 = 0
                                palabras = ['Descripcion:', 'Curso asociado:', 'Fecha de inicio:', 'Fecha de Finalizacion:','Dia:', 'Horas dedicadas:', 'Estado:']
                                if palabras2[valor_ingresado-1] in valor_ingresado5:
                                    if valor_ingresado5[1] != 'Sin curso asociado':
                                        print('-------------------------------------')
                                        print(codigos_ansi[5] + 'Actividades académicas\n' + codigos_ansi[1])
                                        print('Nombre: ', key)
                                        cont = 0
                                        for x in valor_ingresado5:
                                            print(palabras[cont], x )
                                            cont = cont+ 1
                                        print('-------------------------------------')
                            for key in actividades:
                                valor_ingresado5 = actividades[key]
                                cont2 = 0
                                palabras = ['Descripcion:', 'Curso asociado:', 'Fecha de inicio:', 'Fecha de Finalizacion:','Dia:', 'Horas dedicadas:', 'Estado:']
                                if palabras2[valor_ingresado-1] in valor_ingresado5:
                                    if valor_ingresado5[1] == 'Sin curso asociado':
                                        print('-------------------------------------')
                                        print(codigos_ansi[5] + 'Actividades recreativas\n' + codigos_ansi[1])
                                        print('Nombre: ', key)
                                        cont = 0
                                        for x in valor_ingresado5:
                                            print(palabras[cont], x )
                                            cont = cont+ 1
                                        print('-------------------------------------')
                            time.sleep(10)
                            print(codigos_ansi[2])
                        elif valor_ingresado4 == '2': ## Se genera un reporte que indique el porcentaje actividades realizadas y las que faltan por realizar
                            palabras2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
                            cont = 1
                            print('Ingrese el número del día del cual desea generar un reporte \n')
                            for x in palabras2:
                                print("\t", cont, ')', x)
                                time.sleep(0.2)
                                cont = cont+1
                            print ('\t', '8 ) Toda la semana\n')
                            accion = int(input('Su opción es: '))
                            time.sleep(0.2)
                            print(codigos_ansi[2])
                            if accion == 8:
                                accion == 'Toda la semana'
                            else:
                                accion = palabras2[accion-1] 
                            actividades_ejecutadas = 0
                            actividades_en_proceso = 0
                            condicion3 = False
                            condicion2 = False
                            if accion == 8:
                                condicion2 = True
                            for x in actividades.values():
                                for y in x:
                                    if y == accion:
                                        condicion3 = True
                                    if y == 'En proceso' and condicion3 == True or y == 'En proceso' and condicion2 == True:
                                        actividades_en_proceso = actividades_en_proceso+1
                                        condicion3 = False
                                    if y == 'Ejecutada' and condicion3 == True or y == 'Ejecutada' and condicion2 == True:
                                        actividades_ejecutadas = actividades_ejecutadas+1
                                        condicion3 = False
                            total_actividades = actividades_en_proceso + actividades_ejecutadas
                            if total_actividades == 0:
                                print('No tiene actividades ese día')
                            else:
                                print ('Total de actividades:', total_actividades)
                                print ('Activdades ejecutadas:', round((actividades_ejecutadas/total_actividades)*100),'%')
                                print ('Actividades en proceso:', round((actividades_en_proceso/total_actividades)*100),'%')
                        elif valor_ingresado4 == '3': ## Se genera un reporte un de las horas disponibles para realizar actividades 
                            palabras2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
                            cont = 1
                            total = 0
                            print('Ingrese el número del día del cual desea generar un reporte \n')
                            for x in palabras2:
                                print('\t', cont, ')', x)
                                cont = cont+1
                            print('\t', '8 ) Toda la semana\n')
                            accion = int(input('Su opción es: '))
                            print()
                            print()
                            if accion == 8:
                                total = 0
                                for x in (dias.values()):
                                    for y in x:
                                        total = total+y
                                print('Le quedan', 74-total,'horas disponibles en la semana!')
                            else:
                                dia = palabras2[accion-1]
                                total = 0
                                for x in (dias[dia]):
                                    total = total+x
                                print ('Le quedan',12-total, 'horas disponibles el día', dia)
                    elif accion == '8': ## Salir del usuario estudiante
                        condicion = False          
                        print(codigos_ansi[2])
                        print(codigos_ansi[0] + 
    """     
    ----------------------------------------
    Bienvenido al sistema de matrícula TEC
    ----------------------------------------
    """
                        + codigos_ansi[1])
                        time.sleep(0.5)
                        print(codigos_ansi[3] + "Digite el numero de su posición académica\n"+ codigos_ansi[1])
                        time.sleep(0.5)
                        print("1) Administrativo")
                        time.sleep(0.5)
                        print("2) Estudiante")
                        time.sleep(0.5)
                        print("3) Salir\n")
                        time.sleep(0.5)
                        estudiante_o_administrativo=int(input("Su posición es: "))
                        time.sleep(0.3)
                        print(codigos_ansi[2])
            else:
                print(codigos_ansi[4] +"¡¡¡USUARIO O CONTRASEÑA INCORRECTA!!!"+ codigos_ansi[1])
                time.sleep(3)
                print(codigos_ansi[2])
                pass
        else: 
            print(codigos_ansi[4] + "¡¡¡USUARIO O CONTRASEÑA INCORRECTA!!!" + codigos_ansi[1])
            time.sleep(3)
            print(codigos_ansi[2])
            pass
    elif estudiante_o_administrativo == 3: ## Salir de la aplicación
        break