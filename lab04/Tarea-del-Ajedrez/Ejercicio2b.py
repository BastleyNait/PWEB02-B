from interpreter import draw
from chessPictures import *
#Knight inverted
knightI = Picture(knight.verticalMirror())
draw(knight.join(knight.negative()).up(knightI.negative().join(knightI)))
