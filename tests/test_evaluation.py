import unittest

from ..evaluation import evaluate_y
from ..calc_y import day_Serie

def setUpModule():
    print ("\nInit: evaluate.py")

class evaluate_ytest(unittest.TestCase):
    def setUp(self):
        self.numdata = 20
    def test_evaluate_y_buy(self):
        yup = [ 1.0000 + i*0.001 for i in range(self.numdata)]
        ydw = [ yup[i]-0.001 for i in range(self.numdata)]
        yop = [ yup[i]-0.0005 for i in range(self.numdata)]
        ycl = [ yup[i]-0.0005 for i in range(self.numdata)]
        self.SeriePrueba = day_Serie(yop[0], yup[0], ydw[0], ycl[0])
        for i in range(1,self.numdata):
            self.SeriePrueba.addValues(yop[i], yup[i], ydw[i], ycl[i])

        y = evaluate_y(self.SeriePrueba, 0.003, 0, DEBUG=True)
        self.assertEqual(1, y)
            
        
    def test_evaluate_y_sell(self):
        yup = [ 1.0000 - i*0.001 for i in range(self.numdata)]
        ydw = [ yup[i]-0.001 for i in range(self.numdata)]
        yop = [ yup[i]-0.0005 for i in range(self.numdata)]
        ycl = [ yup[i]-0.0005 for i in range(self.numdata)]
        self.SeriePrueba = day_Serie(yop[0], yup[0], ydw[0], ycl[0])
        for i in range(1,self.numdata):
            self.SeriePrueba.addValues(yop[i], yup[i], ydw[i], ycl[i])

        y = evaluate_y(self.SeriePrueba, 0.003, 0, DEBUG=True)
        self.assertEqual(2, y)
            
    def test_evaluate_y_aside(self):
        yup = [ 1.0000 for i in range(self.numdata)]
        ydw = [ yup[i]-0.001 for i in range(self.numdata)]
        yop = [ yup[i]-0.0005 for i in range(self.numdata)]
        ycl = [ yup[i]-0.0005 for i in range(self.numdata)]
        self.SeriePrueba = day_Serie(yop[0], yup[0], ydw[0], ycl[0])
        for i in range(1,self.numdata):
            self.SeriePrueba.addValues(yop[i], yup[i], ydw[i], ycl[i])

        y = evaluate_y(self.SeriePrueba, 0.003, 0, DEBUG=True)
        self.assertEqual(0, y)
            
