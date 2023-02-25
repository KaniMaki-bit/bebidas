import re
import sys


def add(input_str):
    input_str = re.sub("\s", "", input_str)
    
    badInput = re.search(",[^\d]", input_str)
    badInput1 = re.search(",$", input_str)
    badInput2 = re.search(",,+", input_str)
    
    
    if badInput:
        print(f"Error de entrada despues del caracter numero {badInput.start()+1}.")
        return False
    
    if badInput1:
        print(f"Error de entrada despues del caracter numero {badInput1.start()+1}.")
        return False
    
    if badInput2:
        print(f"Error de entrada despues del caracter numero {badInput2.start()+1}.")
        return False
    
    name = re.split(",", input_str, 1)[0]
    
    if not name.isalpha():
        print("Error: El primer elemento no es un nombre de bebida valido.")
        return False
    
    if len(name) not in range(2, 16):
        print("Error: El tamano del nombre tiene que estar entre 2 y 25.")
        return False
    
    if not re.search(",", input_str):
        print("Error: Debe exisitir al menos un tamaño.")
        return False
    
    sizes = re.split(",",(re.split(",", input_str, 1)[1]))
    
    if not sizes:
        print("Error: Debe exisitir al menos un tamaño.")
        return False
    
    if not isinstance(sizes, list):
        sizes = [sizes]
    
    if len(sizes) not in range(1, 6):
        print("Error: Debe haber entre 1 y 5 tamaños.")
        return False
    
    intSizes = []
    for el in sizes:
        if re.search("[^\d]", el):
            print("Error: Todos los numeros tienen que ser enteros.")
            return False
        else:
            aux = int(el)
            if aux not in range(1, 49):
                print("Error: Los tamaños tienen que estar en un rango de 1 a 48.")
                return False
            else:
                intSizes.append(aux)
                
    originalSizes = intSizes[:]
    intSizes.sort()
    
    if originalSizes != intSizes:
        print("Error: Los tamaños tienen que estar en orden ascendente.")
        return False
    
    return True



if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])