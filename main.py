''' Importo las clases '''
from room import Room
from character import Enemy, Friend
from rpgInfo import RPGInfo
from item import Item

''' Funcion para imprimir el menu de opciones '''
def menu():
    print("\n")
    print("-----------------------------------------------------")
    print("|              - Menu del Juego -                   |")
    print("|---------------------------------------------------|")
    print("| - Opciones                                        |")
    print("|---------------------------------------------------|")
    print("| > norte                                           |")
    print("| > sur                                             |")
    print("| > este                                            |")
    print("| > oeste                                           |")
    print("| > pelear                                          |")
    print("| > abrazo                                          |")
    print("| > mapa                                            |")
    print("| > recoger                                         |")
    print("| > hablar                                          |")
    print("| > salir                                           |")
    print("-----------------------------------------------------")
    print("|Ingrese una opcion:                                |")

''' Funcion para imprimir el mapa del juego '''
def mapa():
    print("Mapa de juego")
    print("\n")
    print('-----------------------------------------------')
    print('|                                             |')
    print('|                 Terraza                     |')
    print('|                                             |')
    print('--------------------------------------------------------------')
    print('|              |              |               |              |')
    print('| Dormitorio1  | Dormitorio2  |  BañoArriba   |      P       |')
    print('|              |              |               |      a       |')
    print('-----------------------------------------------      t       |')
    print('|              |              |               |      i       |')
    print('|   Living     |    cocina    |   BañoAbajo   |      o       |')
    print('|              |              |               |              |')
    print('-------------------------------------------------------------|')
    print('|              |              |               |')
    print('| SalondeBaile |   Comedor    |    Sotano     |')
    print('|              |              |               |')
    print('----------------------------------------------|')


''' Instancio las habitaciones '''

terraza = Room("Terraza")
terraza.set_description("terraza al aire libre con muchas velas encendidas y un cadaver mutilado en descomposicion ")

dormitorio_1 = Room("Dormitorio_1")
dormitorio_1.set_description("Valijas armadas como si alguien quisiera irse de pronto, ropa desparramada por todos lados..")

dormitorio_2 = Room("Dormitorio_2")
dormitorio_2.set_description("Cuarto de una niña con adornos de princesas y muchos juguetes desparramados")

baño_arriba = Room("Baño_arriba")
baño_arriba.set_description("baño lujoso con muchos espejos")

living = Room("Living")
living.set_description("Salon amplio con tv de 50pulgadas y un gran juego de sillones ")

cocina = Room("Cocina")
cocina.set_description("Una habitación húmeda y sucia llena de moscas.")

baño_abajo = Room("Baño_abajo")
baño_abajo.set_description("no se aguanta el olor nauseabundo")

comedor = Room("Comedor")
comedor.set_description("Una gran sala con adornos dorados en cada pared..")

salon_de_baile = Room("Salon de Baile")
salon_de_baile.set_description("Una amplia habitación con un piso de madera brillante. Enormes candelabros custodian la entrada.")

sotano = Room("Sotano")
sotano.set_description("habitacion inundada de agua, humedad por las paredes y ratas por doquier")

patio = Room("Patio")
patio.set_description("patio con piscina, palmeras, parrilla y una barra de tragos")

''' Relaciono las habitaciones '''

terraza.link_room(dormitorio_1, "sur")
terraza.link_room(dormitorio_2, "sur")
terraza.link_room(baño_arriba, "sur")
dormitorio_1.link_room(dormitorio_2, "oeste")
dormitorio_2.link_room(dormitorio_1, "este")
baño_arriba.link_room(dormitorio_2, "este")
living.link_room(cocina, "este")
cocina.link_room(living, "oeste")
cocina.link_room(comedor, "sur")
baño_abajo.link_room(baño_arriba, "sur")
baño_abajo.link_room(sotano, "norte")
patio.link_room(baño_abajo, "oeste")
patio.link_room(baño_arriba, "oeste")
comedor.link_room(sotano, "este")
comedor.link_room(cocina, "norte")
comedor.link_room(salon_de_baile, "oeste")
salon_de_baile.link_room(comedor, "este")
salon_de_baile.link_room(living, "norte")

''' Instancio personajes Enemigos y los asigno a una habitacion '''

rata_mutante = Enemy("Rata mutante", "una rata enorme con tres ojos y hambrienta..Quiere devorarte")
rata_mutante.set_debilidad("queso")
rata_mutante.set_conversation("ggrrrrrrgggg!!!")
sotano.set_character(rata_mutante)

zombie = Enemy("Zombie", "el zombie maloliente esta hambriento")
zombie.debilidad="escopeta"
zombie.set_conversation("Whargh! Whargh! ceEEErrreEEEEEbrooOOOOOOOO")
comedor.set_character(zombie)

forky = Enemy("Forky", "un muñeco poseido")
forky.set_debilidad("agua bendita")
forky.set_conversation("voy a arrastrarte al infierno malditooo..")
living.set_character(forky)

chica_poseida = Enemy("chica poseida", "joven poseida por demonio..debe realizarse exorcismo!!")
chica_poseida.set_debilidad("libro de exorcismos")
chica_poseida.set_conversation("asbfkgjyvdcbhsdgcjsasdgychascbvsdcvvsdgchbs!!!!!!!!")
dormitorio_2.set_character(chica_poseida)

bruja = Enemy("Bruja", "bruja realizando ritual con velas y un cadaver mutilado..Poor DIIIOOOS!!!")
bruja.set_debilidad("estaca")
bruja.set_conversation("ven pequeño..veeeen...puedo darte lo que mas anelaaas...uauajajajajaa...(risa orripilante)")
terraza.set_character(bruja)

''' Instancio personajes amigables y los asigno a una habitacion '''

fantasmita = Friend("Fantasmita", "amigable y simpatico")
fantasmita.set_conversation("Se que huele mal...pero toma el queso que te podria ser util mas adelante...")
cocina.set_character(fantasmita)

spinky = Friend("spinky", "un esqueleto amigable")
spinky.set_conversation("Hola amigo toma esta katana...con su filo puede decapitar facilmente a alguien..")
salon_de_baile.set_character(spinky)

roco = Friend("Roco", "un perro hablador..")
roco.set_conversation("hola mi buen amigo..esta casa embrujada es muy peligrosa..toma esta estaca te va a ser util..creemelo!!!")
baño_arriba.set_character(roco)

''' Instacio Items y los asigno a una habitacion '''

item_1 = Item()
item_1.nombre = "espada"
item_1.descripcion = "Una Katana antigua con mucho filo.."
salon_de_baile.set_item(item_1)

item_2 = Item()
item_2.nombre = "queso"
item_2.descripcion = "Un roquefort en la estado y oloriento"
cocina.set_item(item_2)

item_3 = Item()
item_3.nombre = "banana"
item_3.descripcion = "una fruta fresca"
comedor.set_item(item_3)

item_4 = Item()
item_4.nombre = "agua bendita"
item_4.descripcion = "pote de agua bendita"
patio.set_item(item_4)

item_5 = Item()
item_5.nombre = "libro de exorcismos"
item_5.descripcion = "libro antiguo con instrucciones para realizar exorcismos"
dormitorio_1.set_item(item_5)

item_6 = Item()
item_6.nombre = "estaca"
item_6.descripcion = "estaca puntiaguda, ideal para atravezar un corazon!"
baño_arriba.set_item(item_6)

''' ------------------------------------ MAIN ------------------------------------'''

''' Declaro la posicion actual al comenzar el juego'''
habitacion_actual = cocina
''' Creo una lista llamada mochila para alojar los items '''
mochila = []
''' Bienvenida '''
mi_juego = RPGInfo("                    -------- La Mansion Embrujada ---------- ")
print("-----------------------------------------------------------------------------------")
mi_juego.welcome()
print("-----------------------------------------------------------------------------------")
RPGInfo.info()
print("Hay " + str(Room.catidad_habitaciones) + " habitaciones por explorar!!!")
print("Total de enemigos en el juego: " + str(Enemy.enemigos_derrotados))

''' Bucle para simular el juego'''
muerto = False
while muerto == False:
    print("\n")
    habitacion_actual.get_details()
    print("-----------------------------------------------------------------------------------")
    habit = habitacion_actual.get_character()
    if habit is not None:
        habit.describe()
    item = habitacion_actual.get_item()
    if item is not None:
        print("-----------------------------------------------------------------------------------")
        print("Items en la habitacion")
        print("----------------------")
        item.describe()
        print("-----------------------------------------------------------------------------------")
    menu()
    opcion = input("> ")
    if opcion in ["norte", "sur", "este", "oeste"]:
        habitacion_actual = habitacion_actual.move(opcion)
    elif opcion == "hablar":
        if habit is not None:
            habit.talk()
    elif opcion == "pelear":
        if habit is not None and isinstance(habit, Enemy):
            print("Que item usaras para pelear?")
            pelear_item = input("> ")
            if pelear_item in mochila:
                if habit.fight(pelear_item) == True:
                    print("Felicidades has matado al enemigo!")
                    habitacion_actual.set_character(None)
                    if Enemy.enemigos_derrotados == 0:
                        print("Felicitaciones has derrotado la horda de enemigos!")
                        muerto = True

                else:
                    print("Has sido Asesinado")
                    print("GAME OVER")
                    muerto = True
            else:
                print("Usted no pocee "+ pelear_item)
        else:
            print("Aqui no hay nadie con quien pelear")
    elif opcion == "abrazo":
        if habit is not None:
            if isinstance(habit, Enemy):
                print("Yo no haria eso si fuera tu...")
            else:
                habit.abrazo()
        else:
            print("Aqui no hay nadie a quien abrazar! :(")
    elif opcion == "mapa":
        mapa()
    elif opcion == "recoger":
        if item is not None:
            print("Pones el "+item.get_nombre()+ " en tu mochila")
            mochila.append(item.get_nombre())
            habitacion_actual.set_item(None)
            for i in mochila:
                print(i)
    elif opcion == "salir":
        print("Cerrando juego...\n")
        break

RPGInfo.creditos()







