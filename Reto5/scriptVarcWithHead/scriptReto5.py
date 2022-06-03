import pandas as pd
def listaPeliculas(rutaFileCsv: str):
    if '.csv' in rutaFileCsv or '.CSV' in rutaFileCsv:
        try:
            dF = pd.read_csv(rutaFileCsv)
            dF2 = dF[["Country","Language","Gross Earnings"]]
            tPvot = pd.pivot_table(dF2,index=['Country', 'Language'], values=['Gross Earnings'])
            fl = tPvot.head(n=10)
        except:
            print("Error al leer el archivo de datos.")
    else: print("Extensión inválida.")
    return fl