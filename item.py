class Item():
    ''' Crea un Item '''
    def __int__(self):
        self.nombre = None
        self.descripcion = None

    ''' Metodos para dar valor a los atributos sin usar get y set '''
    @property
    def _nombre(self):
        return self.nombre

    @_nombre.setter
    def _nombre(self, value):
        self._nombre = value

    ''' Propiedades get y set '''
    def set_nombre(self, item_nombre):
        self.nombre = item_nombre

    def get_nombre(self):
        return self.nombre

    def set_descripcion(self, item_descripcion):
        self.descripcion = item_descripcion

    def get_descripcion(self):
        return self.descripcion

    ''' Describe el item '''
    def describe(self):
        print("Objeto en la habitacion: "+self.nombre)
        print("Descripcion del objeto: "+self.descripcion)
