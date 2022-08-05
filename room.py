class Room():
    ''' Contador de habitaciones, cada vez que se instancia una Room se suma 1 '''
    catidad_habitaciones = 0

    ''' Crea una room '''
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        Room.catidad_habitaciones = Room.catidad_habitaciones + 1

    ''' Propiedades get y set'''
    def set_character(self, room_character):
        self.character = room_character

    def get_character(self):
        return self.character

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    ''' Describe la habitacion '''
    def describe(self):
        print(self.description)

    ''' Relaciona las habitaciones entre si, recibe 2 parametros una habitacion y la direccion (norte, sur, este, oeste)'''
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    ''' Dice en que habitacion se encuentra y la descipcion de la misma '''
    def get_details(self):
        print("-----------------------------------------------------------------------------------")
        print("Usted se encuentra en la habitacion ----> "+self.name)
        print("-----------------------------------------------------------------------------------")
        print("Descripcion: "+ self.description)

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("La/El " + room.get_name() + " esta al " + direction)

    ''' Metodo para moverse entre las habitaciones, recibe como parametro una direccion (norte, sur, este, oeste) '''
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("No puedes ir por ese camino!")
            return self