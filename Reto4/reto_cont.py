from functools import reduce
import functools
    
def ordenes(rutinaContable: list):
    print('------------------------ Inicio Registro diario ---------------------------------')
    for ix in rutinaContable:
        tupleValue=list()
        for iy in ix:
            if isinstance(iy,tuple)==True:
                # To = lambda x,y: x*y
                # tupleValue.append(To(y[1],y[2]))
                tupleValue.append(functools.reduce(lambda x,y: x*y,(iy[1],iy[2])))
        sumTupleValue=[(functools.reduce(lambda a,c: a+c, tupleValue))]
        totalValue=list(map(lambda x: x + 25000 if x < 600000 else x, sumTupleValue))
        list(map(lambda x:[print("La factura {} tiene un total en pesos de {:,.2f}".format(ix[0],i)) for i in totalValue],totalValue))
    print('-------------------------- Fin Registro diario ----------------------------------')
    return

def run():
    ordenes([  
        [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],  
        [1202, ("8756", 3, 115362.58),("1112",18,2354.99)], 
        [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
        [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]  
        ])

if __name__ == '__main__':
    run()