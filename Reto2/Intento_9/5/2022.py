
informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 3,
    'primer_ingreso': True
}



def cliente(informacion: dict)-> dict:
    if informacion['edad'] > 18:
        valor = 20000
        apto = True
        if informacion['primer_ingreso'] == True:
            valor = valor - (valor*0.05)
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': apto,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': valor
            }
        else:
        
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': apto,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': valor
            }
    elif informacion['edad'] >= 15 and informacion['edad'] <= 18:
        valor = 5000
        if informacion['primer_ingreso'] == True:
            apto = True
            valor = valor - (valor*0.07)
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': apto,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': valor
            }
        else:
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': apto,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': valor
            }
    elif informacion['edad'] >= 7 and informacion['edad'] < 15:
        valor = 10000
        if informacion['primer_ingreso'] == True:
            valor = valor - (valor*0.05)
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': apto,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': valor
            }
        else:
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': apto,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': valor
            }
    else:
        if informacion['primer_ingreso'] == True:
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': False,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': 'N/A'
            }
        else:
            respuesta = {
                'nombre': informacion['nombre'],
                'edad': informacion['edad'],
                'atraccion':'X-Treme',
                'apto': False,
                'primer_ingreso': informacion['primer_ingreso'],
                'total_boleta': 'N/A'
            }
    return respuesta

print(cliente(informacion))