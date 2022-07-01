import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
data = pd.read_csv("023-ACQUE-SUPERFICIALI-DATI-Laghi-ridotto.csv")

#converto virgole decimali in punti
data['Profondità'] = data['Profondità'].str.replace(',', '.')
data['VALORE'] = data['VALORE'].str.replace(',', '.')

#sostituisco spazi in colonna Descrizione Profondità
data['Descrizione Profondità'] = data['Descrizione Profondità'].replace(' ', '-', regex=True)
#sostituisco anche underscore con dash
data['Descrizione Profondità'] = data['Descrizione Profondità'].replace('_', '-', regex=True)
#sostituisco apostrofo con dash
data['Descrizione Profondità'] = data['Descrizione Profondità'].replace("'", '-', regex=True)

#sostituisco spazi in colonna  Profondità
data['Profondità'] = data['Profondità'].replace(' ', '', regex=True)

#sostituisco spazi in colonna Comune
data['COMUNE'] = data['COMUNE'].replace(' ', '-', regex=True)

#date
data['DATA CAMPIONAMENTO']=pd.to_datetime(data['DATA CAMPIONAMENTO'], utc=False)
data['DATA CAMPIONAMENTO'] = data['DATA CAMPIONAMENTO'].dt.date

# coordinate
data['COORD X']= data['COORD X'].astype(int)
data['COORD Y']= data['COORD Y'].astype(int)

#maggiore e minore
data['VALORE'] = data['VALORE'].replace('<', 'lt-', regex=True)
data['VALORE'] = data['VALORE'].replace('>', 'gt-', regex=True)


#CAS: togliere WISE dal nome e aggiungerlo in altra colonna
data.loc[data['CAS'].str.contains('WISE'), 'ParameterIdentificationSystem'] = 'WISE'
data['CAS'] = data['CAS'].map(lambda x: x.lstrip(' WISE '))

#faccio lo stesso per CASID
data.loc[data['CAS'].str.contains('CASID'), 'ParameterIdentificationSystem'] = 'CAS'
data['CAS'] = data['CAS'].map(lambda x: x.lstrip('CASID'))

#Metto CAS nei restanti
data['ParameterIdentificationSystem'].fillna('CAS', inplace=True)

#unità di misura: slash diventa trattino
data['UM'] = data['UM'].str.replace('/', '-', regex=False)
data['UM'] = data['UM'].str.replace(' ', '-', regex=False) #per le UM che contengono spazi, sostanze chimiche

data = data.drop("Column 16", 1)
print(data.head())

data.to_csv('Monitoraggio_laghi_dati_puliti.csv')
