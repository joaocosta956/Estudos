# Dunder 

class Pontos:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        # self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        # class_name = type(self).__name__
        print(f'{class_name}(x={self.x!r}, y={self.y!r}')

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y

        return Pontos(novo_x, novo_y)
    
    def __gt__(self, other):
        novo_self = self.x + self.y
        novo_other = other.x + other.y

        return novo_self > novo_other
    
    def __lt__(self, other):
        novo_self = self.x + self.y
        novo_other = other.x + other.y

        return novo_self < novo_other

if __name__ == '__main__':
    p1 = Pontos(6,8)
    p2 = Pontos(8,9)
    p3 = p1 + p2
    print(p3)
    print('P2 é maior que P1', p2 > p1)
    print('P2 é mmenor que P1', p2 < p1)
