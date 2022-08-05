class RPGInfo():
    ''' Esta clase se utiliza para dar la bienvenida al juego y los creditos'''

    ''' declaro variable con nombre de autor '''
    autor = "< Martin Perez >"

    ''' Crea una RPGInfo'''
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print(self.title)

    ''' Metodo estatico para dar la bienvenida al juego '''
    @staticmethod
    def info():
        print("Bienvenido al juego de texto")
        print("Metodologia de Programacion : POO")

    ''' Class metodo para mostrar los creditos del juego '''
    @classmethod
    def creditos(cls):
        print("Gracias por jugar")
        print("Creado por "+ cls.autor)