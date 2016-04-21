def calificaciones():
    ponderaciones = {"Tareas" : 0, "Examen" : 0, "Participaciones" : 0, "Conducta" : 0}
    datos_docente = {"Nombre" : "", "Grupo": "", "Materia" : ""}
    datos_alumno = {"Nombre" : "", "Tareas" : 0, "Examen" : 0, "Participaciones" : 0, "Conducta" : 0, "Calificacion" : 0}
    
    total_tareas = 0

    debugger = int(input("[0,1] : "))

    if debugger == 1:
        datos_docente["Nombre"] =  "Gustavo Rosas Martinez"
        datos_docente["Grupo"] =   "BTC02"
        datos_docente["Materia"] = "Programacion"
    
    
        ponderaciones["Tareas"] = 10
        ponderaciones["Examen"] = 60
        ponderaciones["Participaciones"] = 20
        ponderaciones["Conducta"] = 10

        total_tareas = 10
    
        datos_alumno["Nombre"] = "Noe de la Luz Seseña"
        datos_alumno["Tareas"] = 10
        datos_alumno["Examen"] = 100
        datos_alumno["Participaciones"] = 4
        conducta = "si"
        datos_alumno["Conducta"] = (0,1)[conducta=="si"]
    else:
    
        datos_docente["Nombre"] = input("Nombre docente : ")
        datos_docente["Grupo"] = input("Grupo : ")
        datos_docente["Materia"] = input("Materia: ")
        
        
        ponderaciones["Tareas"] = int(input("Porcentaje de tareas : "))
        ponderaciones["Examen"] = int(input("Porcentaje de examen : "))
        ponderaciones["Participaciones"] = int(input("Porcentaje de participaciones : "))
        ponderaciones["Conducta"] = int(input("Porcentaje de conducta : "))

        total_tareas = int(input("Total de tareas : "))
        
        datos_alumno["Nombre"] = input("Alumno : ")
        datos_alumno["Tareas"] = int(input("Tareas entregadas : "))
        datos_alumno["Examen"] = int(input("Calificacion examen [0-100]: "))
        datos_alumno["Participaciones"] = int(input("Numero de participaciones : "))
        conducta = input("¿Buena conducta? [si/no] : ")
        datos_alumno["Conducta"] = (0,1)[conducta=="si"]
    
    

##  calculos

    datos_alumno["Calificacion"] = float((datos_alumno["Tareas"] * ponderaciones["Tareas"] / total_tareas)) \
                                   + float((datos_alumno["Examen"] * ponderaciones["Examen"] / 100)) + \
                                   float((datos_alumno["Participaciones"] * ponderaciones["Participaciones"])/(float(total_tareas / 2.5))) + \
                                   float((datos_alumno["Conducta"] * ponderaciones["Conducta"]))

    
    
    
    
    
    print ("______________________________________")
    print ("Datos docente", "\n")

    print("Docente :" , datos_docente["Nombre"])
    print("Grupo : " , datos_docente["Grupo"])
    print("Materia : " , datos_docente["Materia"])

    print ("--------------------------------------")
    print ("Ponderaciones", "\n")
    for p in ponderaciones:
        print (p , " : ", ponderaciones[p])


    print ("--------------------------------------")
    print ("Datos alumno", "\n")
    print ("Nombre : " , datos_alumno["Nombre"])
    print ("Tareas entregadas : " , datos_alumno["Tareas"])
    print ("Calificacion Examen : " , datos_alumno["Examen"])
    print ("Participaciones : " , datos_alumno["Participaciones"])
    print ("¿Buena conducta? : " , datos_alumno["Conducta"])
    print ("Calificacion : ", datos_alumno["Calificacion"])
    print ("______________________________________")
calificaciones()
        
