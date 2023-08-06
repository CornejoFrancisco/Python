import random
NOMBRE_ARCHIVO = "musica.csv"


# Definición del registro Tema ...
class Tema:
    def __init__(self, titulo, genero, idioma):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma


# Función para la generación de los datos que se pasarán al archivo  ...
def carga_automatica():
    v = [None] * 100
    base_de_datos_de_titulos = 'Inconsciente colectivo', 'Los dinosaurios', 'Viernes 3 AM', \
                               'Yendo de la cama al living', 'Canción para mi muerte', 'Desarma y sangra',\
                               'Nos siguen pegando abajo',  'Pecado mortal',  'Eiti-leda',  'Kill My Mother',\
                               'Shape of You', 'Blinding Lights, Rockstar', 'Dance Monkey',  'Closer', \
                               'One Dance', 'Someone You Loved', 'Sunflower', 'Señorita', \
                               'Bad Guy', 'Thinking Out Loud', 'Perfect', 'Say You Won’t Let Go', \
                               'Believer', 'God’s Plan', 'Lucid Dreams', 'Photograph', 'Sad!', \
                               'Starboy', 'Havana', 'Deja vu', 'Gas Gas Gas', 'Running in the 90s', 'Fame', \
                               'Kamikaze', ' Never Gonna Give you Up', 'Together Forever', 'Whenever you need somebody',
    for i in range(len(v)):
        titulo = random.choice(base_de_datos_de_titulos).upper()
        genero = random.randint(0, 5)
        idioma_original = random.randint(0, 4)
        v[i] = Tema(titulo, genero, idioma_original)
    return v
