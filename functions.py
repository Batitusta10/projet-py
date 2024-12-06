def several_zeros():
    return [0]*10 

def several_zeros_custom(nb_zeros=10):
    return [0]*nb_zeros 

def matrix(rows, cols):
    return [[0]*cols for _ in range(rows)] 


class Matrix:
    def __init__(self, rows, cols):
        """
        Constructeur de la classe Matrix.
        Initialise une matrice de taille rows x cols avec des zéros.
        """
        self.__data = [[0 for _ in range(cols)] for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols

    def get_value(self, row, col):
        """
        Méthode pour récupérer la valeur à la position (row, col).
        """
        if 0 <= row < self.__rows and 0 <= col < self.__cols:
            return self.__data[row][col]
        else:
            raise IndexError("Index hors limites")

    def __eq__(self, other):
        """
        Méthode spéciale pour comparer deux matrices.
        Retourne True si les matrices sont égales, False sinon.
        """
        if not isinstance(other, Matrix):
            return False
        if self.__rows != other.__rows or self.__cols != other.__cols:
            return False
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__data[i][j] != other.__data[i][j]:
                    return False
        return True
    
    # self.__data, __rows et __cols sont des variables privées (attributs privés)


if __name__ == '__main__':
    # Les tests sont ici pour vérifier que le code fonctionne correctement
    print(several_zeros())
    print(several_zeros_custom(5))
    print(matrix(3, 4))
    
    mtx1 = Matrix(2, 3)
    mtx2 = Matrix(2, 3)
    print(mtx1 == mtx2)  # True
