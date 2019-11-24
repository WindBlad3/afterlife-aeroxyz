#Venta de pasajes aerolinea xyz

 #Clases para guardar datos
class Asiento:
   numeroAsiento=0
   estadoAsiento = ""
   tipoAsiento=""
   precioAsiento=0

class Pasaje:
   asiento = Asiento()

class Pasajero:
   rutPasajero=0
   pasaje = []
   precioTotalPasajes=0

class Avion:
   asientosTotales = []
   pasajerosTotales = []
   cantidadAsientosTotal=198+1

# Inicializar variables principales #
avion = Avion()
seleccionMenu=0

# Inicializamos el avion con cantidad de asientos diferentes #
for index in range(1,avion.cantidadAsientosTotal):

   # asientos no reclinables #
   if index <= 12:
      asiento = Asiento()
      asiento.numeroAsiento = index
      asiento.estadoAsiento = ""
      asiento.tipoAsiento = "No Reclinable"
      asiento.precioAsiento = 50000
      avion.asientosTotales.append(asiento)

   # asientos reclinables #
   elif index > 12 and index <= 48:
      asiento = Asiento()
      asiento.numeroAsiento = index
      asiento.estadoAsiento = ""
      asiento.tipoAsiento = "Reclinable"
      asiento.precioAsiento = 80000
      avion.asientosTotales.append(asiento)

   # asientos comunes #
   elif index > 48 and index <= 198 :
      asiento = Asiento()
      asiento.numeroAsiento = index
      asiento.estadoAsiento = ""
      asiento.precioAsiento = 60000
      asiento.tipoAsiento = "Comun"
      avion.asientosTotales.append(asiento)


# Seleccion de menu #
while seleccionMenu != 7:
   print(" ")
   print("*********** Bienvenido a la pagina online de aerolineas XYZ Boeing 717 *********** \n ")
   print("Menu:")
   print("1. Comprar pasaje")
   print("2. Mostrar ubicaciones disponibles")
   print("3. Ver listado de pasajeros")
   print("4. Buscar pasajero")
   print("5. Reasignar asiento")
   print("6. Mostrar ganancias totales")
   print("7. Salir!")

   seleccionMenu = int(input("\n Porfavor, seleccione una opcion: \n"))
   
   try:
      
      #  Seleccion salir de menu #
      if seleccionMenu == 7:
         print("Ha salido del sistema, muchas gracias!")
         exit()

      #  Opcion Comprar pasaje de menu #
      if seleccionMenu == 1:
         print("---------------------------= Ha seleccionado Comprar pasaje =---------------------------")      
         print("ATENCION!, Los asientos con X ya se encuentran reservados y no se podran reservar.")
         print("----------------------------------------------------------------------------------------") 
        
         rutPasajero = ""
         rutPasajero = input("Porfavor, ingrese el rut (Por tema de formato ingreselo con puntos y guion, de todas maneras se guardara sin estos): \n")
         rutPasajero = rutPasajero.replace(".","",-1)
         rutPasajero = rutPasajero.replace("-","",-1)
         rutPasajero = rutPasajero[0 : len(rutPasajero) -1]
         rutPasajero = int(rutPasajero)

         cantidadPasajes = int(input("> Cuantos pasajes desea comprar? \n"))
         pasajero = Pasajero()
         pasajero.rutPasajero = rutPasajero
         pasajero.pasaje = []

         for index in range(0,cantidadPasajes):
               print(" ")  
               print("-= Pasajero [" + str(index+1) + "]")    
               print("                            -= TIPOS DE ASIENTOS =-                          ")      
               print("---------------------------------------------------------------------------- ")   
               print("1.- Comun")
               print("2.- Reclinable")
               print("3.- No Reclinable")
               tipoAsientoRequerido = int(input("> Escriba el tipo de asiento desea: \n"))

               nombreTipoAsientoRequerido = ""
               if tipoAsientoRequerido == 1 :
                  nombreTipoAsientoRequerido= "Comun"
               if tipoAsientoRequerido == 2 :
                  nombreTipoAsientoRequerido= "Reclinable"
               if tipoAsientoRequerido == 3 :
                  nombreTipoAsientoRequerido= "No Reclinable"

               cantidadFilasMostradas = 0
               filasConcadenadas=""

               for asientoAvion in avion.asientosTotales:
                  # Asientos que desea ver el cliente #
                  if asientoAvion.tipoAsiento == nombreTipoAsientoRequerido :
                     cantidadFilasMostradas+=1
                     if asientoAvion.estadoAsiento == "X" and  cantidadFilasMostradas <=5:
                        filasConcadenadas+="[Asiento "+ str(asientoAvion.numeroAsiento) + " - "+ asientoAvion.estadoAsiento +"]"
                     if asientoAvion.estadoAsiento == "" and  cantidadFilasMostradas <=5:
                        filasConcadenadas+="[Asiento "+ str(asientoAvion.numeroAsiento) +"]"
                     if cantidadFilasMostradas == 5 :
                        filasConcadenadas += "\n"
                        cantidadFilasMostradas=0
               print("                              -= ASIENTOS "+ nombreTipoAsientoRequerido.upper() +" =-                                 ")   
               print("----------------------------------------------------------------------------------------------- ")     
               print(filasConcadenadas)
               print(" ")  
               seleccionAsiento = int(input("Porfavor, seleccione el asiento que desea: \n"))

               if( avion.asientosTotales[seleccionAsiento - 1].estadoAsiento == "X"):
                  print("ERROR: El asiento"+ seleccionAsiento - 1 +" ya se encuentra reservado, intente nuevamente con otro!")
               else:
                  #Se deja asiento como no disponible
                  avion.asientosTotales[seleccionAsiento - 1].estadoAsiento="X"
                  #Se asigna al pasaje el asiento seleccionado
                  pasaje = Pasaje()
                  pasaje.asiento = avion.asientosTotales[seleccionAsiento - 1]
                  #Al pasajero se le asigna el rut y el pasaje
                  pasajero.precioTotalPasajes+=avion.asientosTotales[seleccionAsiento - 1].precioAsiento
                  pasajero.pasaje.append(pasaje)
         
         #Al avion le anadimos el pasajero y el total sumado de todos los pasajeros
         avion.pasajerosTotales.append(pasajero)
         
         print("---------------------------= Gracias por su compra =---------------------------")
         print("---------------------------= Fin Comprar pasaje =---------------------------")      

      #  Opcion Mostrar ubicaciones disponibles de menu #
      if seleccionMenu == 2:
         print("---------------------------= Ha seleccionado Mostrar ubicaciones disponibles =---------------------------") 
         print("---------------------------------------------------------------------------------------------------------")  
         
         cantidadFilasMostradas = 0
         filasConcadenadas=""
        
         for asientoAvion in avion.asientosTotales:
            
            cantidadFilasMostradas+=1
            
            if asientoAvion.estadoAsiento != "X" and cantidadFilasMostradas <=3:
               filasConcadenadas+="[Asiento "+ str(asientoAvion.numeroAsiento) + " - Tipo de asiento: "+ asientoAvion.tipoAsiento +"]"
            
            if cantidadFilasMostradas == 3 :
               filasConcadenadas += "\n"
               cantidadFilasMostradas=0
         
         print("                              -= ASIENTOS DISPONIBLES =-                     ")   
         print("-------------------------------------------------------------------------------------------- ") 
         print(filasConcadenadas)
         print(" ")
         input("Presione enter para volver al menu...")
         print("---------------------------= Fin Mostrar ubicaciones disponibles =---------------------------")   
      
      #  Opcion Ver listado de pasajeros de menu #
      if seleccionMenu == 3:
         print("-= Ha seleccionado Ver listado de pasajeros =-")
         print("---------------------------------------------")  
         
         if not avion.pasajerosTotales :
            print("No hay pasajeros agregados en el avion para listar") 
         else:
            rutsPasajerosOrdenados = []
            
            for pasajero in avion.pasajerosTotales:
               rutsPasajerosOrdenados.append(pasajero.rutPasajero)
            
            rutsPasajerosOrdenados.sort()
            for rutPasajero in rutsPasajerosOrdenados:
               print(str(rutPasajero))
         
         print(" ")
         input("Presione enter para volver al menu...")
         print("---------------------------= Fin Ver listado de pasajeros =---------------------------") 

      #  Opcion Buscar pasajero de menu #
      if seleccionMenu == 4:
         print("-=Ha seleccionado Buscar pasajero=-")
         print("---------------------------------------------")
         
         if not avion.pasajerosTotales :
             print("No hay pasajeros agregados en el avion para buscar") 
         else:
            rutPasajeroABuscar = int(input("Ingrese el rut del pasajero que desea buscar: \n"))
            print(" ")
            print("Pasajes comprados por el pasajero;")
            contadorPasajes=0
            existePasajero=False
            for pasajero in avion.pasajerosTotales:
               if pasajero.rutPasajero == rutPasajeroABuscar :
                  existePasajero = True
                  for pasaje in pasajero.pasaje:
                     contadorPasajes+=1
                     print(" -=Pasaje N° "+ str(contadorPasajes) +" del Rut "+ str(rutPasajeroABuscar))
                     print("   Numero de asiento: "+ str(pasaje.asiento.numeroAsiento))
                     print("   Estado de asiento: "+pasaje.asiento.estadoAsiento)
                     print("   Precio de asiento: "+ str(pasaje.asiento.precioAsiento))
                     print("   Tipo de asiento: " + pasaje.asiento.tipoAsiento)
                     print(" ")  
            
            if existePasajero == False :
               print("No se ha encontrado el rut indicado en los pasajeros")
         
         print(" ")
         input("Presione enter para volver al menu...")
         print("---------------------------= Fin Buscar pasajero =---------------------------")   

      #  Opcion Reasignar asiento de menu #
      if seleccionMenu == 5:
         print("-=Ha seleccionado Reasignar asiento=-")
         print("---------------------------------------------") 
         
         numeroAsiento = int(input("Indique su numero de asiento: \n"))
         rutPasajeroABuscar = int(input("Ingrese el rut del pasajero que desea buscar y cambiar su asiento (solo numerico): \n"))
         contadorPasajes=0
         existePasajero=False
         
         print(" ")
        
         for pasajero in avion.pasajerosTotales:
               if pasajero.rutPasajero == rutPasajeroABuscar :

                  existePasajero = True

                  for pasaje in pasajero.pasaje:
                     contadorPasajes+=1

                  if contadorPasajes > 1 :
                     indexPasajeACambiar = int(input("El pasajero indicado tiene "+ str(contadorPasajes) +" pasajes, > A cual desea cambiar su asiento?\n"))

                     #Se obtiene el asiento antiguo del pasajero
                     asientoAntiguo = pasajero.pasaje[indexPasajeACambiar - 1 ].asiento

                     #Se obtiene el numero de asiento antiguo
                     numeroAsientoAntiguo = asientoAntiguo.numeroAsiento

                     #Se modifica el estado del asiento antiguo como disponible
                     avion.asientosTotales[numeroAsientoAntiguo - 1 ].estadoAsiento = ""

                     #Se le entrega el nuevo asiento al pasajero indicado con el rut
                     avion.asientosTotales[numeroAsiento - 1].estadoAsiento = "X"
                     pasajero.pasaje[indexPasajeACambiar - 1].asiento = avion.asientosTotales[numeroAsiento - 1]
                     break
                  else:

                     #Se obtiene el asiento antiguo del pasajero
                     asientoAntiguo = pasajero.pasaje[0].asiento

                     #Se obtiene el numero de asiento antiguo
                     numeroAsientoAntiguo = asientoAntiguo.numeroAsiento

                     #Se modifica el estado del asiento antiguo como disponible
                     avion.asientosTotales[numeroAsientoAntiguo - 1].estadoAsiento = ""

                     #Se le entrega el nuevo asiento al pasajero indicado con el rut
                     avion.asientosTotales[numeroAsiento - 1].estadoAsiento = "X"
                     pasajero.pasaje[0].asiento = avion.asientosTotales[numeroAsiento - 1]
                     break

         if existePasajero == False :
            print("No se ha encontrado el rut indicado en los pasajeros")

         print(" ")
         input("Presione enter para volver al menu...")
         print("---------------------------= Fin Reasignar asiento =---------------------------")   

      #  Opcion Mostrar ganancias totales de menu #
      if seleccionMenu == 6:
         print("-=Ha seleccionado Mostrar ganancias totales=-")
         print("---------------------------------------------") 
         
         if not avion.pasajerosTotales :
             print("No hay pasajeros agregados en el avion para mostrar ganacias totales") 
         else:
            totalAsientoComun = 0
            contadorAsientoComun =0
            for pasajero in avion.pasajerosTotales:
               for pasaje in pasajero.pasaje:
                  if pasaje.asiento.tipoAsiento == "Comun" :
                     totalAsientoComun += pasaje.asiento.precioAsiento
                     contadorAsientoComun +=1

            totalAsientoReclinable = 0
            contadorAsientoReclinable =0
            for pasajero in avion.pasajerosTotales:
               for pasaje in pasajero.pasaje:
                  if pasaje.asiento.tipoAsiento == "Reclinable" :
                     totalAsientoReclinable += pasaje.asiento.precioAsiento
                     contadorAsientoReclinable +=1

            totalAsientoNoReclinable = 0
            contadorAsientoNoReclinable =0
            for pasajero in avion.pasajerosTotales:
               for pasaje in pasajero.pasaje:
                  if pasaje.asiento.tipoAsiento == "No Reclinable" :
                     totalAsientoNoReclinable += pasaje.asiento.precioAsiento
                     contadorAsientoNoReclinable +=1
           
            print("Tipo de asiento        |           Cantidad           |          Total")
            print("----------------------------------------------------------------------")   
            print("Asiento comun          |              "+ str(contadorAsientoComun)+"                |       CLP $ "+ str(totalAsientoComun))
            print("Espacio para piernas   |              "+ str(contadorAsientoReclinable)+ "                |       CLP $ "+ str(totalAsientoReclinable))
            print("No reclina             |              "+ str(contadorAsientoNoReclinable)+"                |       CLP $ "+ str(totalAsientoNoReclinable))
            print("----------------------------------------------------------------------")   
            print("El total es:           |              "+ str(contadorAsientoNoReclinable + contadorAsientoComun +contadorAsientoReclinable )+"                |  CLP $ " + str(totalAsientoComun + totalAsientoReclinable +totalAsientoNoReclinable))
            print(" ")
            input("Presione enter para volver al menu...")
            print("---------------------------= Fin Mostrar ganancias totales =---------------------------")   
   except:
      if seleccionMenu !=7 :
         print("")
         print("Oops!","Un error ocurrio.")
         print("Intentalo denuevo!.")
         print("")