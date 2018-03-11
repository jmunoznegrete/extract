## importo funciones necesarias
from datetime import date, datetime, time, timedelta
from time import gmtime, strftime, strptime
from evaluation import evaluate_y

## leo fichero de configuracion con:
class cfg(object):
    SPREAD = 0.00015                ## in pips / 10000
    DELAY_INI_ORDER = 780   ## Max number fo M1 bars (from 23:00 to 12:00 am)
    EXPIRE_ORDER_TIME = 480     ## Maximum time to expire the order (M1 bars)
    EXPECTED_MOVEMENT = 0.0030      ## in pips / 10000

## Defino estados:
##  * Leyendo lista para las compras (a partir de las 23:00).
##  * finalizada lectura y captando nueva fecha

class status(object):
    def __init__(self):
        self.CAPTURING_FIRST_BAR = True
        a=strptime("01 Jan 2000 11:00", "%d %b %Y %H:%M")
        self.dateFirstBar = datetime(a[0], a[1], a[2], a[3], a[4])
        self.oldBar = datetime(a[0], a[1], a[2], a[3], a[4])

##---------------------------------------------
## y_result is the class to be stored as a result of the selected criteria
## with this algorithm y is a list of values between 0 and 2
## the date associated to that value is stored in another list with the
## same index value to identify the result

class y_result(object):
    def __init__(self, name):
        self.date_result = []
        self.y = []
        self.filename = name
    def app(self, date_insert, y_value):
        self.date_result.append(date_insert)
        self.y.append(y_value)
    def get_value(self, i):
        return self.date_result[i], self.y[i]
    def toFile(self):
        pass

class day_Serie(object):
    def __init__(self,ValueOpen, ValueHigh, ValueLow, ValueClose):
        self.Open=[]
        self.High=[]
        self.Low=[]
        self.Close=[]
        self.addValues(ValueOpen, ValueHigh, ValueLow, ValueClose)
    def addValues(self, ValueOpen, ValueHigh, ValueLow, ValueClose):
        self.Open.append(float(ValueOpen))
        self.High.append(float(ValueHigh))
        self.Low.append(float(ValueLow))
        self.Close.append(float(ValueClose))
    def len(self):
        return len(self.Open)
    def toFile(self):
        print "printing DaySerie..."
        for i in range(len(self.Open)):
            print "i=",self.Open[i]
## --------------------------------------------------------------
    ## 
if __name__ == "__main__":
    vector_y = y_result('rawData/yVector')
    
    with open('rawData/EURUSDM1.csv', 'r+') as fin:
        status_eur = status()
        i = 0
        for line in fin:
            if i==0:
                i = i + 1
                continue
            valores = line.split(',')    
            if status_eur.CAPTURING_FIRST_BAR:
                ## capturing the first bar of the day and skipping if not
                ## something like 23:xx
                if not (valores[0][11:13] == '23'):
                    continue
                tmp_date = strptime(valores[0],"%d.%m.%Y %H:%M:%S")
                current_date = datetime(tmp_date[0], tmp_date[1], tmp_date[2],
                                        tmp_date[3], tmp_date[4], tmp_date[5])
    
                ## if Friday or Saturday skip these values
                if current_date.weekday() == 5 or \
                    current_date.weekday() ==6:
                    continue
                
                ## date of first bar is already stored in current_date
                ## and values OHLC stored as first values
                status_eur.CAPTURING_FIRST_BAR = False
                tmpDaySerie = day_Serie(valores[1], valores[2], 
                                        valores[3], valores[4])
    
            else:
                ## date of first bar is already stored in current_date
                ## now we are going to store the follwing bar values in a list
                ## and decide de value for y
                tmp_date = strptime(valores[0],"%d.%m.%Y %H:%M:%S")
                current_time = datetime(tmp_date[0], tmp_date[1], tmp_date[2],
                                        tmp_date[3], tmp_date[4], tmp_date[5])
    
                if (current_time < 
                        current_date + timedelta(minutes=cfg.EXPIRE_ORDER_TIME)):
                    tmpDaySerie.addValues(valores[1], valores[2],
                                            valores[3], valores[4])    
    
                else:
                    y = evaluate_y(tmpDaySerie, 
                                    cfg.EXPECTED_MOVEMENT,
                                    cfg.SPREAD)
                    print "Resultado = ", y
                    vector_y.app(valores[0], y)
                    status_eur.CAPTURING_FIRST_BAR = True
                    break
    
    ##tmpDaySerie.toFile()
    ##vector_y.toFile()
                
    
    ## Iteracion hasta final de fichero:
    ##  * leo fecha
    ##  * busco hora de compra 23:00 + D [+ 5 min]: hay veces que a las 23:00 vol=0
    ##  * completo la lista dede Hora de compra hasta F.
    ##  * comparo y escribo las etiquetas en el fichero Y
    ##  * chequeo errores: si hay alguno que no se compra o algun dia que falta
    ##    para revisarlo.
