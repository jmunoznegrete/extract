import matplotlib.pyplot as plt
from y_result import yvalues

def evaluate_y(DaySerie, movement, spread, DEBUG = False):
    upper_limit = DaySerie.Open[0] + movement + spread
    upper_limit_serie=[upper_limit for i in range(DaySerie.len())]
    down_limit = DaySerie.Open[0] - movement
    down_limit_serie=[down_limit for i in range(DaySerie.len())]

    upper_comparison = \
        [upper_limit_serie[i] < DaySerie.Low[i] for i in range(DaySerie.len())]
    down_comparison = \
        [down_limit_serie[i] > DaySerie.High[i] for i in range(DaySerie.len())]

    if DEBUG:
        x = [i for i in range(DaySerie.len())]
    
        plt.plot(x, DaySerie.High)
        plt.plot(x, DaySerie.Low)
        plt.plot(x, upper_limit_serie)
        plt.plot(x, down_limit_serie)
        plt.show()

    if upper_comparison > down_comparison:
        #print "BUY SIGNAL"
        return(yvalues.BUY)
    if upper_comparison < down_comparison:
        #print "SELL SIGNAL"
        return(yvalues.SELL)

    #print "STAY ASIDE"
    return(yvalues.STAY_ASIDE)
