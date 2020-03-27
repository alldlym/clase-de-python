def menu():
    print ("Calculadora en python:\n","-1 Para sumar:\n","-2 Para restar:\n","-3 para multiplicar:\n","-4 para dividir:\n","-Otro numero para salir:\n")
    
def calculadora():
    menu()

    M = int(input("Selecione Opcion\n"))

    while (M >0 and M <5):

        a = int(input("Primer numero\n"))

        b = int(input("Segundo numero\n"))

        if (M==1):

            print ("La Suma es:", a+b)

            M = int(input("Selecione Opcion\n"))

        elif(M==2):

            print ("La Resta es:",a-b)

            M = int(input("Selecione Opcion\n"))

        elif(M==3):

            print ("La Multiplicacion es:",a*b)

            M = int(input("Selecione Opcion\n"))

        elif(M==4):

            try:

              print ("La Division es:", a/b)

              M = int(input("Selecione Opcion\n"))

            except ZeroDivisionError:

              print ("Jaja no.")

              M = int(input("Selecione Opcion\n"))

calculadora()
