from bot.indicadores.TimeS import SerieEscalar, TimeSerie, Barra, Tick
from bot.indicadores.iBW import iBW


class SerieDate(object):
    def __init__(self):
        self.listDates = []

    def insert_date(self, fecha):
        if len(self.listDates)==0:
            self.listDates.append(fecha)
        else:
            self.listDates.append(self.listDates[0])
            self.listDates[0] = fecha

    def toFile(self, fileOut):
        pass

class const(object):
    MIN_DATA = 40

if __name__ == "main":
    
    Precio = TimeSerie('D1')
    Fechas = SerieDate()
    SerieAC = SerieEscalar()
    SerieAC0 = SerieEscalar()

    cursorLinea=0

    with open('rawData/EURUSDM1.csv', 'r+') as fileIn:
        for line in fileIn:
            if cursorLinea == 0:
                cursorLinea = cursorLinea + 1
                continue

            valores = line.split(',')
            val = [float(valores[i]) for i in range(1,5)]

            if cursorLinea < const.MIN_DATA:
                Precio.append(Barra(val[1], val[2], val[3], val[4]))
                continue

            Fechas.append(valores[0])
            Precio.append(Barra(val[1], val[1], val[1], val[1]))
            
            if cursorLinea == const.MIN_DATA:
                ibw = iBW(Precio)

            SerieAC0.append(ibw['AC'][0])
            t1 = Tick(val[2], 0.0, "12.01.00", "EURUSD")
            Precio.setCur(t1)
            t1 = Tick(val[3], 0.0, "12.01.00", "EURUSD")
            Precio.setCur(t1)
            t1 = Tick(val[4], 0.0, "12.01.00", "EURUSD")
            Precio.setCur(t1)

            ibw.update()
            SerieAC.append(ibw['AC'][0])
                

    with open('rawData/features.csv', 'w') as fileOut:
        for i in range(len(Fechas)):
            cadena = Fechas[-i] + ',' + str(SerieAC0[i]) + ',' + \
                    str(SerieAC[i]) + '\n'

            fileOut.write(cadena)
    
