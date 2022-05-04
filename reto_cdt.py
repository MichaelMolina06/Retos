def CDT(usuario, capital, tiempo):
    cant=capital
    pi=0
    if tiempo>2:
        pi=0.03

    vi=(cant*pi*tiempo)/12
    vt=vi + cant

    print(usuario,vi)
    print(vt)

def run():
    
    print("Bienvenido a su CDT")

    print("A continuacion ingrese los siguientes datos:")
    u=input(str(("Nombre de Usuario:  ")))
    c=input(float(("Monto o capital:  ")))
    t=input(int(("Tiempo transcurrido en meses:  ")))

    CDT(u,c,t)

if __name__ == '__main__':
    run()