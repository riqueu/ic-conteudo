import random


LOTACAO = 8
# Elevadores: Programação Estruturada (Tentar fazer com orientação a objetos depois)

"""
andar_elevador: int
capacidade: int
passageiros: int
direção: [-1, 0, 1]
chamadas: list/set
"""

# Condições Iniciais:
ci_elv = [('andar', 0), ('n_passageiros', 0), ('direção', 0), ('chamadas', [])]
ci_sim = [('fila', 0), ('energia', 0.0), ('viagens', 0)]


# API ELEVADOR

def embarque(andar=0):
    pos_elevadores = [e['andar'] for e in elvs]
    if andar in pos_elevadores:
        elv_i = pos_elevadores.index(andar)  # descobre o elevador está no andar
        elv = elvs[elv_i]
        n_passageiros = elv[elv]['n_passageiros']
        while n_passageiros < LOTACAO:
            n_passageiros += 1
            sim['fila'] -= 1
            if sim['fila'] == 0:
                break
        elv['n_passageiros'] = n_passageiros


def desembarque(n: int):
    pass


def chamada(n: int):
    pass


def input_int(n: int):
    pass


# Eventos:
eventos = {
    'embarque': embarque,
    'desembarque': desembarque,
    'chamada': chamada,
    'input_int': input_int,
}


def init_sim():
    # Elevadores:
    estado_e1 = dict(ci_elv)
    estado_e2 = dict(ci_elv)
    # Simulação:
    estado_sim = dict(ci_sim)
    return (estado_e1, estado_e2), estado_sim


def gera_fila():
    """ Retorna um int para acrescentar à fila no loop de evento """
    n = random.randint(1, 5)
    sim['fila'].append(n)
    if 0 not in elvs[0]['chamadas']:
        elvs[0]['chamadas'].append(0)
    if 0 not in elvs[1]['chamadas']:
        elvs[1]['chamadas'].append(0)


def mover_elevador(elevador):
    pass


def loop_de_evento(n):
    i = 0
    while True:
        gera_fila()
        if sim['fila']:
            eventos['embarque']()
            #  mover_elevador()


if __name__ == "__main__":
    elvs, sim = init_sim()
    loop_de_evento(10)
