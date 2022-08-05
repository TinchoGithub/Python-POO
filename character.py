class Character():

    ''' Crea un personaje '''
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    ''' Describe a este personaje '''
    def describe(self):
        print( self.name + " está aquí!" )
        print( self.description )

    ''' Establecer lo que dirá este personaje cuando se le hable '''
    def set_conversation(self, conversation):
        self.conversation = conversation

    ''' Habla con este personaje '''
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " dice]: " + self.conversation)
        else:
            print(self.name + " no quiere hablar contigo")

    ''' Pelea con este personaje '''
    def fight(self, combat_item):
        print(self.name + " no quiere pelear contigo")
        return True

class Enemy(Character):
    ''' Contador para saber cantidad de enemigos creados, suma 1 cada vez que se instancia un Enemy '''
    enemigos_derrotados = 0

    ''' Crea un Enemy'''
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.debilidad = None
        Enemy.enemigos_derrotados = Enemy.enemigos_derrotados + 1

    ''' Propiedades set y get '''
    def set_debilidad(self, debilidad):
        self.debilidad = debilidad

    def get_debilidad(self):
        return self.debilidad

    ''' Pelea con este personaje, si matas al enemigo se descuenta 1 a la cantidad de enemigos '''
    def fight(self, combat_item):
        if combat_item == self.debilidad:
            print("Enemigo asesinado ")
            Enemy.enemigos_derrotados = Enemy.enemigos_derrotados - 1
            return True
        else:
            print(self.name + " te atrapa y te destroza vivo!!")
            return False

class Friend(Character):
    ''' Crea un Friend '''
    def __int__(self, char_name, char_description):
        super().__int__(char_name, char_description)
        self.sentimiento = None
    ''' Dar un abrazo a este personaje'''
    def abrazo(self):
        print(self.name + "Te abraza!")
