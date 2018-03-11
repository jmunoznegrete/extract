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

class yvalues(object):
    BUY =1
    SELL = 2
    STAY_ASIDE = 0

