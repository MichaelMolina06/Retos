informacion = {
    'id_cliente': 1,
    'nombre': 'Gloria Suarez',
    'edad': 20,
    'primer_ingreso': False
}

def cliente(informacion: dict)-> dict:
    nuevoDic = {
    'nombre':str(informacion['nombre']),
    'edad':int(informacion['edad']),
    'atraccion':'',
    'apto':bool,
    'primer_ingreso':bool(informacion['primer_ingreso']),
    'total_boleta':0
    }
    
    xTreme = int(20000)
    carrosChocones = int(5000)
    sillasVoladoras = int(10000)
    
    if informacion['edad'] >= int(15) and informacion['edad'] <= int(18):
        total_boleta = carrosChocones - (carrosChocones*7)/100
        nuevoDic.update({'atraccion':'Carros chocones'})
        nuevoDic.update({'apto':True})
        if informacion['primer_ingreso'] == bool(True): 
            nuevoDic.update({'total_boleta':total_boleta})
        else:
            nuevoDic.update({'total_boleta':carrosChocones})
    else:
        if informacion['edad'] >= int(7) and informacion['edad'] < int(15):
            total_boleta = sillasVoladoras - (sillasVoladoras*5)/100
            nuevoDic.update({'atraccion':'Sillas voladoras'})
            nuevoDic.update({'apto':True})
            if informacion['primer_ingreso'] == bool(True):
                nuevoDic.update({'total_boleta':total_boleta})
            else:
                nuevoDic.update({'total_boleta':sillasVoladoras}) 
        else:
            if informacion['edad'] > int(18): 
                total_boleta = xTreme - (xTreme*5)/100
                nuevoDic.update({'atraccion':'X-Treme'})
                nuevoDic.update({'apto':True})
                if informacion['primer_ingreso'] == bool(True):
                    nuevoDic.update({'total_boleta':total_boleta})
                else:
                    nuevoDic.update({'total_boleta':xTreme})
            else:
                nuevoDic.update({'atraccion':'N/A'})
                nuevoDic.update({'total_boleta':'N/A'})
                nuevoDic.update({'apto':False})
    return nuevoDic

print(cliente(informacion))