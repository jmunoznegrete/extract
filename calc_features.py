import sys

from bot.indicadores.TimeS import SerieEscalar, TimeSerie, Barra, Tick
from bot.indicadores.iBW import iBW
from extract.auxiliares import split_path


class SerieDate(object):
    def __init__(self):
        self.listDates = []

    def addDate(self, fecha):
        if len(self.listDates)==0:
            self.listDates.append(fecha)
        else:
            self.listDates.append(self.listDates[0])
            self.listDates[0] = fecha

    def length(self):
        return len(self.listDates)

    def __getitem__(self, index):
        return(self.listDates[index])

    def toFile(self, fileOut):
        pass

class const(object):
    MIN_DATA = 40

if __name__ == "__main__":

    Precio = TimeSerie('D1')
    Fechas = SerieDate()
    SerieAC = SerieEscalar()
    SerieAC0 = SerieEscalar()

    cursorLinea=0

    bdata_path, FileIn = split_path(sys.argv[1])

    with open(bdata_path+FileIn, 'r+') as fileIn:
        for line in fileIn:
            if cursorLinea == 0:
                cursorLinea = cursorLinea + 1
                continue

            valores = line.split(',')
            val = [float(valores[i]) for i in range(1,5)]
            val.insert(0, 0.0)
            cursorLinea = cursorLinea + 1

            if cursorLinea < const.MIN_DATA:
                Precio.addBarra(Barra(val[1], val[2], val[3], val[4]))
                continue

            Fechas.addDate(valores[0])
            Precio.addBarra(Barra(val[1], val[1], val[1], val[1]))
            
            if cursorLinea == const.MIN_DATA:
                ibw = iBW(Precio)

            ibw.update()
            SerieAC0.appendValue(ibw['AC'][0])
            t1 = Tick(val[2], 0.0, "12.01.00", "EURUSD")
            Precio.setCur(t1)
            t1 = Tick(val[3], 0.0, "12.01.00", "EURUSD")
            Precio.setCur(t1)
            t1 = Tick(val[4], 0.0, "12.01.00", "EURUSD")
            Precio.setCur(t1)

            ibw.update()
            SerieAC.appendValue(ibw['AC'][0])
                
    print "Longitud: Fecha, SerieAC ", Fechas.length(), SerieAC.length()

    ListaFeatures=[]
    for i in range(Fechas.length() - const.MIN_DATA):
        cadena = Fechas[-i] + ',' + str(SerieAC0[-i]) + ',' + \
                str(SerieAC[-i-7]) + ',' +\
                str(SerieAC[-i-14]) + ',' +\
                str(SerieAC[-i-21]) + \
                '\n'

        ListaFeatures.append(cadena)

    with open(bdata_path+'features.csv', 'w') as fileOut:
        for i in range(len(ListaFeatures)):
            fileOut.write(ListaFeatures[-i-1])
    
