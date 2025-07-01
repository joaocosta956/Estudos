"""Modulo de Exemplo


    Mais de uma linha
"""

variavel_1 = 1

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma de X e Y
    """

def multi(x: int | float, 
          y: int | float,
          z: int| float | None = None) -> int | float:
    
    """Função de Multiplicação
    
        Z é opicional
    """
    if z is None:
        return x*y
    return x*y*z
    

variavel_2 = 2
variavel_3 = 3