def mostrar_menu():
    print("1. CastilloVera")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Mendoza, Ruiz, Zurita ")
    print("5. Opción 5")
    print("6. Opción 6")
    print("7. Opción 7")
    print("8. Opción 8")
    print("9. Opción 9")
    print("10. Opción 10")
    print("11. Opción 11")
    print("12. Opción 12")
    print("13. Opción 13")
    print("14. Opción 14")
    print("15. Opción 15")
    print("16. Navarrete_Toapanta")
    print("17. Opción 17")
    print("18. Opción 18")
    print("19. Opción 19")
    print("20. Bacuy, Cunalata, Bustos")
    print("21. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Ejecutando opción 1")
        def CastilloVera():
            while True:
                try:
                    num=int(input("Ingrese entero positivo: "))
                    if num>0:
                        return num
                    else:
                        print("Ingresar entero positivo nuevamente")
                except ValueError:
                        print("Ingrese un numero valido")
                        
        def multiplo (num1,num2):
            return num1%num2==0 or num2%num1==0
        def main():
            num1=CastilloVera()
            num2=CastilloVera()
            if multiplo (num1,num2):
                print("1 Son multiplos")
            else:
                print("0 No son multiplos")
        if __name__ == "__main__":
            main()
    elif opcion == 2:
        print("Ejecutando opción 2")
        # Agregar código para la opción 2
    elif opcion == 3:
        print("Ejecutando opción 3")
        # Agregar código para la opción 3
    elif opcion == 4:
        print("Ejecutando Mendoza, Ruiz, Zurita")
        def Mendoza_Ruiz_Zurita():
            while True:
                try:
                    n1 = int(input("Ingrese el primer número: "))
                    n2 = int(input("Ingrese el segundo número: "))
                    if n1 > 0 and n2 > 0:
                        break
                    else:
                        print("Por favor, ingrese números positivos.")
                except ValueError:
                    print("Dato incorrecto")
            if n1 == 0 or n2 == 0:
                return 0
            elif n1 % n2 == 0 or n2 % n1 == 0:
                return 1
            else:
                return 0
        if __name__ == "__main__":
            if Mendoza_Ruiz_Zurita():
                print("1")
            else:
                print("0")
    elif opcion == 5:
        print("Ejecutando opción 5")
        # Agregar código para la opción 5
    elif opcion == 6:
        print("Ejecutando opción 6")
        # Agregar código para la opción 6
    elif opcion == 7:
        print("Ejecutando opción 7")
        # Agregar código para la opción 7
    elif opcion == 8:
        print("Ejecutando opción 8")
        # Agregar código para la opción 8
    elif opcion == 9:
        print("Ejecutando opción 9")
        # Agregar código para la opción 9
    elif opcion == 10:
        print("Ejecutando opción 10")
        # Agregar código para la opción 10
    elif opcion == 11:
        print("Ejecutando opción 11")
        #Agregar código para la opción 11
    elif opcion == 12:
        print("Ejecutando opción 12")
        # Agregar código para la opción 12
    elif opcion == 13:
        print("Ejecutando opción 13")
        # Agregar código para la opción 13
    elif opcion == 14:
        print("Ejecutando opción 14")
        # Agregar código para la opción 14
    elif opcion == 15:
        print("Ejecutando opción 15")
        # Agregar código para la opción 15
    elif opcion == 16:
        print("Ejecutando opción 16")
        def Navarrete_Toapanta():
            while True:
                try:
                    num = int(input("Ingrese un número entero positivo: "))
                    if num > 0:
                        return num
                    else:
                        print("Inténtelo de nuevo.")
                except ValueError:
                    print("Ingrese de nuevo un número entero positivo")

        def Multiplo():
            n = Navarrete_Toapanta()
            x = Navarrete_Toapanta()
            if n % x == 0 or x % n == 0:
                print(1, "Es múltiplo")
            else:
                print(0, "No es múltiplo")  

        Multiplo()



    elif opcion == 17:
        print("Ejecutando opción 17")
        # Agregar código para la opción 17
    elif opcion == 18:
        print("Ejecutando opción 18")
        # Agregar código para la opción 18
    elif opcion == 19:
        def MorenoGusqui():
    while True:
        try:
            num1 = int(input("Ingrese el primer número positivo: "))
            if num1 > 0:
                break
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    while True:
        try:
            num2 = int(input("Ingrese el segundo número positivo: "))
            if num2 > 0:
                break
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    if num1 % num2 == 0 or num2 % num1 == 0:
        print(1)
    else:
        print(0)

def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")

def ejecutar_opcion(opcion):
    if opcion == 19:
        MorenoGusqui()

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
       
    elif opcion == 20:
        def Bacuy_Bustos_Cunalata():
        try:
                a = int(input("Ingrese el primer número entero positivo: "))
                b = int(input("Ingrese el segundo número entero positivo: "))
                if a > 0 and b > 0:
                    if (a % b) == 0 or (b % a) == 0:
                        print("1")
                    else:
                        print("0")
                else:
                    print("Ambos números deben ser enteros positivos.")
            except ValueError:
                print("Ingrese un valor válido (número entero positivo).")

        def main():
            while True:
                try:
                    Bacuy_Bustos_Cunalata()
                    respuesta = input("¿Desea verificar otros números? (s/n): ")
                    if respuesta.lower() != "s":
                        break
                except KeyboardInterrupt:
                    print("\n¡Hasta luego!")
        if __name__ == "__main__":
            main()
    elif opcion == 21:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción no válida")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
