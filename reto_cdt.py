
def CDT(usuario, capital, tiempo):
    pass

def run():
    
    print("Bienvenido a su CDT")

    print("A continuacion ingrese los siguientes datos:")
    u=input(str(("Nombre de Usuario")))
    c=input(int(("Monto o capital")))
    t=input(int(("Tiempo transcurrido en meses")))

    CDT(u,c,t)

if __name__ == '__main__':
    run()