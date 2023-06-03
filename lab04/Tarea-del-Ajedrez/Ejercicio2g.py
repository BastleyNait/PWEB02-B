from interpreter import draw
from chessPictures import *
# squareN = square.negative().join(square)
# squareB = square.join(square.negative())

# blanco = squareB.join(squareB.join(squareB.join(squareB)))
# negro = squareN.join(squareN.join(squareN.join(squareN)))

# draw(blanco.up(negro).verticalRepeat(4))

draw(knight.negative().under(square.negative()))
