from colors import *


class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        return Picture(None)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        invertido = []
        for elem in self.img:
            aux = elem.replace("_", "=").replace(".", "@").replace("_", "=")
            invertido.append(aux)
        return Picture(invertido)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        lista_combinada = [x + y for x, y in zip(self.img, p.img)]
        return Picture(lista_combinada)

    def up(self, p):
        return Picture(self.img + p.img)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        superpuesto=[]
        if "_" in p.img[0]:
            for elem in self.img:
                aux = elem.replace(" ", "_")
                superpuesto.append(aux)
        else:
            for elem in self.img:
                aux = elem.replace(" ", "=")
                superpuesto.append(aux)
        return Picture(superpuesto)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        return Picture(None)

    def verticalRepeat(self, n):
        repeted = self.img * n
        return Picture(repeted)

    # Extra: Sólo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""
        return Picture(None)
