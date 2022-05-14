def cliente(informacion: dict) -> dict:
    
    xTreme = 20000
    carros_chocones = 5000
    sillas_voladoras = 10000
    valor_entrada = 0

    apto = True
    atraccion = 'Libre'

    edad= informacion['edad']
    primera_vez= informacion['primer_ingreso']

    if edad >= 7:
        apto= True
    else:
        apto= False
        atraccion= 'N/A'
        valor_entrada= str('N/A')

    if primera_vez == True and apto == True:
        if edad >= 7 and edad < 15:
            atraccion= 'Sillas Voladoras'
            valor_entrada= 10000 - (10000*0.05)
        elif edad >= 15 and edad <= 18:
            atraccion= 'Carros Chocones'
            valor_entrada= 5000 - (5000*0.07)
        elif edad > 18:
            atraccion= 'X-Treme'
            valor_entrada= 20000 - (20000*0.05)

    if primera_vez == False and apto == True:
        if edad >= 7 and edad < 15:
            atraccion= 'Sillas Voladoras'
            valor_entrada= 10000
        elif edad >= 15 and edad <= 18:
            atraccion= 'Carros Chocones'
            valor_entrada= 5000
        elif edad > 18:
            atraccion= 'X-Treme'
            valor_entrada= 20000
    
    database = {
        'nombre': str(informacion['nombre']),
        'edad': str(informacion['edad']),
        'atraccion': str(atraccion),
        'apto': bool(apto),
        'primer_ingreso': bool(informacion['primer_ingreso']),
        'total_boleta': valor_entrada
    }

    return database

def run():
    informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': False
    }

    info=cliente(informacion)
    print(info)

if __name__ == '__main__':
    run()