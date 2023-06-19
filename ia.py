import time
from copy import deepcopy



def minimax(tablero, depth, max_player, juego):
    if depth == 0 or tablero.ganar() != None:
        return tablero.evaluate(), tablero
    
    if max_player:
        maxEval = float('-inf')
        mejorMovimiento = None
        for movimiento in getMovimientosBlancas(tablero, juego):
            evaluation = minimax(movimiento, depth-1, False, juego)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                mejorMovimiento = movimiento
        
        return maxEval, mejorMovimiento
    else:
        minEval = float('inf')
        mejorMovimiento = None
        for movimiento in getMovimientosNegras(tablero, juego):
            evaluation = minimax(movimiento, depth-1, True, juego)[0] 
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                mejorMovimiento = movimiento
        
        return minEval, mejorMovimiento


def simularMov(pieza, movimiento, tablero, juego, skip):
    tablero.moverPieza(movimiento[0], movimiento[1],pieza)
    if skip:
        tablero.delete(skip)

    return tablero


def getMovimientosBlancas(tablero, juego):
    movimientos = []

    for pieza in tablero.getPiezasBlancas():
        movimientosValidos = tablero.getMovimientosV(pieza)
        for movimiento, skip in movimientosValidos.items():
            temp_tablero = deepcopy(tablero)
            temp_pieza = temp_tablero.getPieza(pieza.i, pieza.j)
            new_tablero = simularMov(temp_pieza, movimiento, temp_tablero, juego, skip)
            movimientos.append(new_tablero)
    
    return movimientos

def getMovimientosNegras(tablero, juego):
    movimientos = []

    for pieza in tablero.getPiezasNegras():
        movimientosValidos = tablero.getMovimientosV(pieza)
        for movimiento, skip in movimientosValidos.items():
            temp_tablero = deepcopy(tablero)
            temp_pieza = temp_tablero.getPieza(pieza.i, pieza.j)
            new_tablero = simularMov(temp_pieza, movimiento, temp_tablero, juego, skip)
            movimientos.append(new_tablero)
    
    return movimientos
