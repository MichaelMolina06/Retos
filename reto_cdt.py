def CDT(usuario, capital, tiempo):
    
    cant = capital
    pi = 0.03
    pp = 0.02

    vi= (cant*pi*tiempo)/12
    vp= cant * pp

    if tiempo > 2:
        vt= vi + cant
        print("Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, segun el monto inicial " + str(cant) + " para un tiempo de " + str(tiempo) + " meses es: " + str(vt))
    else:
        vt= cant - vp
        print("Para el usuario " + str(usuario) + " La cantidad de dinero a recibir, segun el monto inicial " + str(cant) + " para un tiempo de " + str(tiempo) + " meses es: " + str(vt))

def run():
    
    print("Bienvenido a su CDT")

    print("A continuacion ingrese los siguientes datos:")
    u=str(input("Nombre de Usuario:  "))
    c=int(input("Monto o capital:  "))
    t=int(input("Tiempo del CDT transcurrido en meses:  "))

    CDT(u,c,t)

if __name__ == '__main__':
    run()