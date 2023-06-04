from interpreter import draw
from chessPictures import *
"""PRUEBAS"""
# squareN = square.negative().join(square)
# squareB = square.join(square.negative())

# blanco = squareB.join(squareB.join(squareB.join(squareB)))
# negro = squareN.join(squareN.join(squareN.join(squareN)))

# draw(blanco.up(negro).verticalRepeat(4))

# draw(knight.negative().under(square.negative()))

# draw(knight.horizontalRepeat(6))
"""FILA PEONES"""
# doble peon blanco sobre tablero blanco y negro x 6
peonx2B = (pawn.under(square).join(pawn.under(square.negative()))).horizontalRepeat(4)
# doble peon negro sobre tablero negro y blanco x 6
peonx2N = (pawn.negative().under(square.negative()).join(pawn.negative().under(square))).horizontalRepeat(4)
"""TABLERO DEL MEDIO"""
# tablero 2 x 2 
tab2x2 = ((square.join(square.negative())).up(square.negative().join(square)))
# tablero 8 x 4 
tab8x4 = (tab2x2.horizontalRepeat(4)).verticalRepeat(2)
# Haciendo fichas con sus coleres de tableros
"""TORRE"""
# torre negra tablero blanco
rockNtB = rock.negative().under(square)
# torre negra tablero negro
rockNtN = rock.negative().under(square.negative())
# torre blanca tablero negro
rockBtN = rock.under(square.negative())
# torre blanca tablero blanco
rockBtB = rock.under(square)
"""CABALLO"""
# torre negra tablero blanco
knightNtB = knight.negative().under(square)
# torre negra tablero negro
knightNtN = knight.negative().under(square.negative())
# torre blanca tablero negro
knightBtN = knight.under(square.negative())
# torre blanca tablero blanco
knightBtB = knight.under(square)
"""ALFIL"""
# torre negra tablero blanco
bishopNtB = bishop.negative().under(square)
# torre negra tablero negro
bishopNtN = bishop.negative().under(square.negative())
# torre blanca tablero negro
bishopBtN = bishop.under(square.negative())
# torre blanca tablero blanco
bishopBtB = bishop.under(square)
"""REINA"""
# torre negra tablero blanco
queenNtB = queen.negative().under(square)
# torre negra tablero negro
queenNtN = queen.negative().under(square.negative())
# torre blanca tablero negro
queenBtN = queen.under(square.negative())
# torre blanca tablero blanco
queenBtB = queen.under(square)

"""REY"""
# torre negra tablero blanco
kingNtB = king.negative().under(square)
# torre negra tablero negro
kingNtN = king.negative().under(square.negative())
# torre blanca tablero negro
kingBtN = king.under(square.negative())
# torre blanca tablero blanco
kingBtB = king.under(square)

"""CADENA NEGRO"""
cadenaN = rockNtB.join(knightNtN.join(bishopNtB.join(queenNtN.join(kingNtB.join(bishopNtN.join(knightNtB.join(rockNtN)))))))

"""CADENA BLANCO"""
cadenaB = rockBtB.join(knightBtN.join(bishopBtB.join(queenBtN.join(kingBtB.join(bishopBtN.join(knightBtB.join(rockBtN)))))))

"""DIBUJANDO TABLERO COMPLETO"""
draw(((cadenaN.up(peonx2N)).up(tab8x4)).up(peonx2B.up(cadenaB)))




