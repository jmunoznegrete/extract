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
    def len(self):
        return len(self.y)
    def toFile(self):
        with open(self.filename,'w') as fout:
            print "printing y..."
            for i in range(len(self.y)):
                fout.write(self.date_result[i]+','+str(self.y[i])+'\n')


class yvalues(object):
    BUY =1
    SELL = 2
    STAY_ASIDE = 0

