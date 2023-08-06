
from registro import*
import random

class Medicamento:
    def __init__(self, identificacion, nombre_del_medicamento, tipo_de_medicamento, modo_de_almacenamiento, costo_de_fabricacion):
        self.identificacion = identificacion
        self.nombre_del_medicamento = nombre_del_medicamento
        self.tipo_de_medicamento = tipo_de_medicamento
        self.modo_de_almacenamiento = modo_de_almacenamiento
        self.costo_de_fabricacion = costo_de_fabricacion


def carga_automatica():
    vector = []
    nombre_de_medicamento = 'Abacavir', 'ZIAGEN', 'Abaloparatida', 'TYMLOS'\
        , 'Abatacept', 'ORENCIA', 'Abciximab', 'REOPRO', 'Acamprosate', 'Acarbosa'\
        , 'PRECOSE', 'Acebutolol', 'SECTRAL', 'Acetazolamida', 'DIAMOX', 'Acetohydroxamic acid'\
        , 'LITHOSTAT', 'Acetilcisteína', 'ACETADOTE', 'Acetilprocainamida', 'Acitretin', 'SORIATANE'\
        , 'Aclidinium', 'TUDORZA PRESSAIR', 'Aciclovir', 'ZOVIRAX', 'Adalimumab', 'HUMIRA',  'Adapaleno'\
        , 'DIFFERIN', 'Adefovir', 'HEPSERA', 'Adenosina', 'ADENOCARD', 'Aflibercept', 'Ojos', 'Agalsidase beta'\
        , 'FABRAZYME', 'Albendazol', 'ALBENZA',
    
    for i in range(1000):
        identificacion = random.randint(0, 100000000)
        nombre_del_medicamento = random.choice(nombre_de_medicamento)
        tipo_de_medicamento = random.randint(1, 40)
        modo_de_almacenamiento = random.randint(0, 9)
        costo_de_fabricacion = round(random.uniform(1000, 2000), 2)
        medicamento = Medicamento(identificacion, nombre_del_medicamento, tipo_de_medicamento, modo_de_almacenamiento, costo_de_fabricacion)
        if i > 2:
            add_in_order(vector, medicamento)
    print("=" * 60)
    print("Medicamento cargado...")
    return vector

def add_in_order(v, x):
    n = len(v)
    pos = izq = 0
    der = n - 1
    while izq <= der:
        c = (izq + der) // 2

        if v[c].identificacion == x.identificacion:
            pos = c
            break

        elif x.identificacion > v[c].identificacion:
            izq = c+1
        else:
            der = c-1

    if izq > der:
        pos = izq

    v[pos:pos] = [x]

