def CDT(usuario:str, capital:int, tiempo:int):
    
    cant = capital
    pi = 0.03
    pp = 0.02

    vi= (cant*pi*tiempo)/12
    vp= cant * pp

    if tiempo > 2:
        vt= vi + cant
        #result= print("Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, segun el monto inicial " + str(cant) + " para un tiempo de " + str(tiempo) + " meses es: " + str(vt))
    else:
        vt= cant - vp
        #result=print("Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, segun el monto inicial " + str(cant) + " para un tiempo de " + str(tiempo) + " meses es: " + str(vt))

    result="Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,cant,tiempo,vt)
    return result


def run():
    
    print("Bienvenido a su CDT")

    print("A continuacion ingrese los siguientes datos:")
    u=str(input("Nombre de Usuario:  "))
    c=int(input("Monto o capital:  "))
    t=int(input("Tiempo del CDT transcurrido en meses:  "))

    print(CDT(u,c,t))


if __name__ == '__main__':
    run()