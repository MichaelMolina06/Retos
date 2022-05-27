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