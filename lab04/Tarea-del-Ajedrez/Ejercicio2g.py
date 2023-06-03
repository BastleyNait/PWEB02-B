from interpreter import draw
from chessPictures import *
# squareN = square.negative().join(square)
# squareB = square.join(square.negative())

# blanco = squareB.join(squareB.join(squareB.join(squareB)))
# negro = squareN.join(squareN.join(squareN.join(squareN)))

# draw(blanco.up(negro).verticalRepeat(4))

# draw(knight.negative().under(square.negative()))

# draw(knight.horizontalRepeat(6))

# doble peon blanco sobre tablero blanco y negro
peonx2B = pawn.under(square).join(pawn.under(square.negative()))
# doble peon negro sobre tablero negro y blanco
peonx2N = pawn.negative().under(square.negative()).join(pawn.negative().under(square))
# tablero 8 x 4 
tab1x8 = ((square.join(square.negative())).horizontalRepeat(4))
tab4x8 = tab1x8.verticalRepeat(4)
draw(tab4x8)




