#!/usr/bin/python3

import sys
from sys import argv

def suma (op1, op2):
    return op1 + op2
def resta (op1, op2):
    return op1 - op2
def mult (op1, op2):
    return op1 * op2
def div (op1, op2):
    return op1 / op2

funciones = {"suma" : suma,
            "resta" : resta,
            "multiplica" : mult,
            "divide" : div,
}

if __name__ == "__main__":

    try:
        operacion = argv[1]
        op1 = float((argv[2]))
        op2 = float((argv[3]))
        print(str(funciones[operacion](op1,op2)))
    except IndexError:
        sys.exit("Número de argumentos inválido.")
    except ValueError:
        sys.exit("Tipo de operando inválido, solo es posible int o float.")
    except KeyError:
        sys.exit('Esta operación no está contemplada.')
