from functools import reduce

def acumular(x,y):
    valor = x + y
    return valor    
def comparar(total):
    ajuste = 0
    if total < 600000:
        ajuste = total + 25000
    else:
        return total
    return ajuste
    
def ordenes(rutinaContable:list):
    #print('------------------------ Inicio Registro diario ---------------------------------')
    valores = []
    for x in rutinaContable:
        Total = []
        To = lambda x,y: x*y
        for y in x:
            if isinstance(y, tuple) == True:
                #print(To(y[1],y[2]))
                Total.append(To(y[1],y[2]))
                #Total = Total + To(y[1],y[2])
            
        valores.append(reduce(acumular, Total))
    #print(valores)
    print(list(map(comparar,valores)))
        #print(map(comparar,sum(Total)))
        #Total = comparar(Total)
        #print('La factura {} tiene un total en pesos de {}'.format(x[0],'{:,.2f}'.format(Total)))
    #print('-------------------------- Fin Registro diario ----------------------------------')
    pass


ordenes([  
        [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],  
        [1202, ("8756", 3, 115362.58),("1112",18,2354.99)], 
        [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
        [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]  
])