import pandas as pd

rutaFileCsv="https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

def listaPeliculas(rutaFileCsv: str):
    if '.csv' in rutaFileCsv or '.CSV' in rutaFileCsv:
        try:
            dataFrame = pd.read_csv(rutaFileCsv)
            dataFrame2 = dataFrame[["Country","Language","Gross Earnings"]]
            pivot = pd.pivot_table(dataFrame2,index=['Country', 'Language'], values=['Gross Earnings'])
            filtro = pivot.head(n=10)
        except:
            print("Error al leer el archivo de datos.")
    else: print("Extensión inválida.")
    return filtro

def run ():
    pass

if __name__ == '__main__':
    run()