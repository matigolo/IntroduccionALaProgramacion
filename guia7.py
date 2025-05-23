import random
#Ejercicio 1
def pertenece (s: list[int], e:int) -> bool:
    i=0
    for i in range (len(s)):
        if s[i] == e:
            return True
    return False
        
print(pertenece([1,2,3], 4))
print(pertenece([1,2,3], 2))

def divideATodos (s:list[int], e: int) -> int:
    for i in range (len(s)):
        if (s[i] % e) == 0:
            return True
    return False
print("divide a todo: ", divideATodos([2,4,6],3))

def sumaTotal (s:list[int]) -> int:
    res=0
    for i in range (len(s)):
        res = res + s[i]
    return res

print("suma total: ", sumaTotal([1,2,3,4,5]))

def maximo (s:list[int])-> int:
    maximo = 0
    for i in range (len(s)):
        if s[i] > maximo:  
            maximo = s[i]
    return maximo

print(maximo([1,2,4,2,4,3,2,22222,4,5]))
print(maximo([6,6,6]))

def minimo (s:list[int])-> int:
    minimo = s[0]
    for i in range (len(s)):
        if s[i] < minimo:  
            minimo = s[i]
    return minimo

print(minimo([1,2,4,2,4,3,2,22222,4,5]))
print(minimo([200,40,65]))

def ordenados (s:list[int]) -> bool:
    for i in range (len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True

print(ordenados([4,2,3,3,5,6]))
print(ordenados([2, 3, 3, 5, 6])) 

def posMaximo (s:list[int]) -> int:
    max = maximo(s)
    if len(s) == 0:
        return (-1)
    else:
        for i in range (len(s)):
            if s[i] == max:
                return i
            
print(posMaximo([5,3,3,3,3,2,1000]))

def posMinimo (s:list[int]) -> int:
    min = minimo(s)
    if len(s) == 0:
        return (-1)
    else:
        for i in range (len(s)):
            if s[i] == min:
                return i
            
print(posMinimo([5,3,3,3,3,2,1]))

def longMayorASiete(s:list[list[chr]]) -> bool:
    for i in range (len(s)):
        if longitudPalabra(s[i]) > 7 :
            return True
    return False


def longitudPalabra(s:list[chr]) -> int:
    return len(s) 
print("longitudpalabra ",longitudPalabra("matuas"))
print("es mayor a 7 ",longMayorASiete(["termo", "gatounodos", "tener", "jirafas"]))

def esPalindromo(s:list[chr]) -> bool:
    if len(s) <= 1:
        return True
    else:
        for i in range (len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
            
print(esPalindromo("alasda"))
print(esPalindromo("ala"))
print(esPalindromo(['r', 'a', 'c', 'e', 'c', 'a', 'r']))  # True
print(esPalindromo(['h', 'o', 'l', 'a']))  # False

def igualesConsecutivos (s: list[int]) -> bool:
    for i in range (len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return True
    return False

print("iguales consecutivos ",igualesConsecutivos([1,2,3,3,3,4,5,6]))
print("iguales consecutivos ",igualesConsecutivos([1,2,3,3,4,5,6]))

#hacer despues 1.12 y 1.13

def cantidadDigitosImpares (numeros:list[int]) -> int:
    cantidadDeImpares = 0
    for numero in numeros:  #recorro list
        for digito in str(numero):
            if (int(digito) % 2 != 0) :
                cantidadDeImpares = cantidadDeImpares + 1
    return cantidadDeImpares

print(cantidadDigitosImpares([57, 2383, 812, 246]))

#Ejercicio 2
def cerosEnPosicionesPares (s: list[int]) -> list[int]:
    for i in range (len (s)):
        if (i % 2) == 0:
            s[i] = 0
    return s

print(cerosEnPosicionesPares([1,2,3,4,5,6,7]))

#esta mal, rehacer
def sinVocales(s:list[chr]) -> list[chr]:
    tamañoLista = len(s)
    i = 0
    while i < tamañoLista:
        if s[i] in {'a','e','i','o','u'}:
            del s[i]
            tamañoLista = tamañoLista - 1
        else: 
            i = i + 1
    return s
print(sinVocales(['h','o','l','a','a','d']))

def reemplazaVocales (s:list[chr]) -> list[chr]:
    tamañoLista = len(s)
    i=0
    res=[]
    while i < tamañoLista:
        if s[i] in {'a','e','i','o','u'}:
            res.append('_')
        else:
            res.append(s[i])
        i=i+1
    return res

print(reemplazaVocales("golaaasddz"))

def darVueltaString (s:list[chr]) -> list[chr]:
    res=[]
    for i in range (len(s)):
        res.append(s[len(s)-i-1])
    return res

print(darVueltaString("holas"))

def perteneceChr (s: list[chr], e:chr) -> bool:
    i=0
    for i in range (len(s)):
        if s[i] == e:
            return True
    return False
        
print("pertenece :",perteneceChr("hola", 'z'))


def eliminar_repetidos(s: list[chr]) -> list[chr]:
    res = []
    for c in s:
        if c not in res:  # Verifica si el carácter ya está en 'res'
            res.append(c)
    return res
print(eliminar_repetidos("golafsa"))

#Ejercicio 3
def resultadoMateria (notas:list[int]) -> int:
    if todosLosElementosSonMayoresIgualACuatro(notas) == True and calcularPromedio(notas) >= 7:
        return 1
    if todosLosElementosSonMayoresIgualACuatro(notas) == True and (calcularPromedio(notas) < 7 and calcularPromedio(notas) >= 4):
        return 2
    else:
        return 3


def todosLosElementosSonMayoresIgualACuatro(s:list[int]) -> bool:
    for i in range (len(s)):
        if s[i] < 4:
            return False
    return True
print(todosLosElementosSonMayoresIgualACuatro([4.5,4,3]))

def calcularPromedio(s:list[int]) -> float:
    suma = sumaTotal(s)
    promedio = suma/(len(s))
    return promedio

print("promedio",calcularPromedio([1,2,3,4,6]))  

print(resultadoMateria([1,2,3,4,5,6]))
print(resultadoMateria([7, 8, 9, 7]))  # Output: 1
print(resultadoMateria([4, 5, 6, 5]))  # Output: 2
print(resultadoMateria([10, 3, 8, 9]))  # Output: 3
print(resultadoMateria([4, 4, 4, 3]))  # Output: 3
print(resultadoMateria([9]))  # Output: 1
print(resultadoMateria([4, 4, 4, 4]))  # Output: 2

#Ejercicio 4
#Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on.
def saldoActual (movimientos: list[(chr,int)]) -> int:
    saldo = 0
    for tupla in movimientos:
        if tupla[0] == 'I':
            saldo = saldo + tupla[1]
        else:
            saldo = saldo - tupla[1]
    return saldo

print(saldoActual([("I", 2000), ("R", 20),("R", 1000),("I", 300)]))
print(saldoActual([("I", 2000), ("I", 20),("I", 500000),("I", 3)]))
print(saldoActual([("I", 2000)]))

#3 MATRICES
def perteneceACadaUno (s:list[list[int]], e:int, res:list[bool]):
    for lista in s:
        if pertenece(lista,e) == True:
            res.append(True)
        else:
            res.append(False)
    return res

s = [[], [1], [2, 3]]
e = 1
res = []
perteneceACadaUno(s, e, res)
print(res)

def es_matriz(s: list[list[int]]) -> bool:
    if len(s) == 0 or len(s[0]) == 0:  # Condiciones 1 y 2
        return False
    columnas = len(s[0])
    for fila in s:
        if len(fila) != columnas:  # Condición 3
            return False
    return True

def filasOrdenadas (m:list[list[int]], res: list[bool]):
    for lista in m:
        if ordenados (lista) == True:
            res.append(True)
        else:
            res.append(False)
    return res

m1, m2, m3, m4 = [[1,2,3],[4,0,5],[10,20,30]], [[5],[6],[7,8]], [[3,2,1],[5,4],[9,8,7]], [[]]
res1, res2, res3, res4 = [], [], [], []
filasOrdenadas(m1, res1); filasOrdenadas(m2, res2); filasOrdenadas(m3, res3); filasOrdenadas(m4, res4)
print(f"Caso 1: {res1}\nCaso 2: {res2}\nCaso 3: {res3}\nCaso 4: {res4}")

def columna (m:list[list[int]], c: int) -> list[int]:
    res: list[int] = []
    for i in range (len(m)):
        res.append(m[i][c])
    return res

print(columna([[1,2,3],[4,5,6]],1))

def columnas_ordenadas (m:list[list[int]]) -> list[bool]:
    res: list[bool] = []
    columna = []
    cantidadColumnas = len(m[0])
    print("cantidad columnas", cantidadColumnas)
    for j in range (cantidadColumnas):
        for i in range (len(m)):
            columna.append(m[i][j])
            print("columna", columna)
        if ordenados(columna) == True:
            res.append(True)
        else:
            res.append(False)
        columna.clear()
    return res

print(columnas_ordenadas([[7,1,9],[1,2,3],[4,5,6]]))

def transponer (m:list[list[int]]) -> list[list[int]]:
    res : list[list[int]] = []
    cantidadColumnas = len(m[0])
    for j in range (cantidadColumnas):
        columna=[]
        for i in range (len(m)):
            columna.append(m[i][j])
            print("columna", columna)
        res.append(columna)

    return res

print(transponer([[7,1,9],[1,2,3],[4,5,6]]))
#HACER ESTE DEL TATETI DESPUES QUE ES IMPORTANTE
"""  def quien_gana_tateti (m:list[list[chr]]) -> int
    res : int = 0
    cantidadColumnas = len(m[0])
    for i in range (len(m)):
        for j in range(cantidadColumnas):"


def alineada (columna: list[chr], equipo: chr) -> bool:
    for i in range (len(columna)):
        if columna[i] != equipo:
            return False
    return True

print (alineada(['o','o','o'], 'o'))"""


#Ejercicio 4
def listaNombresEstudiantes () -> list[str]:
    res : list[str] = []
    seguir = True
    while seguir == True:
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre == "listo" or nombre == "":
            seguir == False
            return res
        else:
            res.append(nombre)

#print(listaNombresEstudiantes())

def historialMonederoElectronico () -> list[tuple] : 
    res : list[tuple] = []
    credito = 0
    seguir = True
    while seguir == True:
        operacion = input("Pulse 'C' si quiere cargar creditos, 'D' si quiere descontar creditos, 'X' para finalizar el programa: ")
        if operacion == "X":
            seguir = False
        else:
            monto = input("ingresar monto de la operacion: ")
            res.append((operacion, monto))
    return res

#print(historialMonederoElectronico())

def sieteYMedio () -> list[int]:
    res : list[int] = []
    primerCarta = pedirCarta()
    print("Carta: ", primerCarta)
    res.append(primerCarta)
    puntuacion = valorCarta(primerCarta)
    seguir = True
    while seguir == True and puntuacion <= 7.5:
        print("tu puntaje es: ", puntuacion)
        deseaSeguir = input("Desea pedir otra carta? (s/n): ")
        if deseaSeguir == 'n':
            seguir = False
        else:
            carta = pedirCarta()
            print("Carta: ", carta)
            res.append(carta)
            valor = valorCarta(carta)
            puntuacion = puntuacion + valor
            if puntuacion > 7.5:
                print("Has perdido")
    if puntuacion <= 7.5:
        print("Has ganado")
 
    return res


def pedirCarta () -> int :
    carta = random.randint(1,12)
    while carta in (8,9):
        carta = random.randint(1,12)
    return carta

def valorCarta(carta: int) -> float:
    res: float = 0.0
    if carta in (10,11,12):
        res = 0.5
    else:
        res = carta
    return res

#print(sieteYMedio())

def fortaleza_contraseña (contraseña: str) -> str:
    #caso contraseña roja
    if len(contraseña) < 5:
        return "ROJA"
    
    #Caso verde
    if esVerde(contraseña) == True:
        return "VERDE"
    
    #caso amarillo
    if esVerde(contraseña) == False and len(contraseña) >= 5:
        return "AMARILLO"

def esVerde (contraseña: str) -> bool:
    longitud = len(contraseña)
    tiene_mayuscula = False
    tiene_minuscula = False
    tieneDigito = False
    for i in contraseña:
        if i.islower():
            tiene_minuscula = True
        if i.isupper():
            tiene_mayuscula = True
        if i.isdigit():
            tieneDigito = True
    if longitud > 8 and tiene_mayuscula == True and tiene_minuscula == True and tieneDigito == True:
        return True
    else:
        return False

contraseña = input("ingrese la contraseña: ")
print(fortaleza_contraseña(contraseña))
