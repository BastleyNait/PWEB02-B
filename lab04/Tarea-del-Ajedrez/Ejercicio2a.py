from interpreter import draw
from chessPictures import *
#se junta caballo blanco con negro se pone encima de caballo negro con blanco juntos
draw(knight.join(knight.negative()).up(knight.negative().join(knight)))


 


