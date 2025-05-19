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
    for i in range (tamañoLista-1):
        if (s[i] =='a') or (s[i] =='e') or (s[i] =='i') or (s[i] =='o') or (s[i] =='u'):
            del s[i]
    return s
print(sinVocales(['h','o','l','a','a']))
