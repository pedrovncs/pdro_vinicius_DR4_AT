#10  Desenvolva um programa para identificar medições climáticas inconsistentes e salvar os resultados (medições que precisam de revisão e motivo) em um novo arquivo Excel. 
#Colunas: {Data de Medição, Temperatura, Umidade, Nível UV, Luminosidade, ml_Chuva}
#Regra 1: Umidade abaixo de 30% e temperatura acima de 35ºC com chuva (ml_Chuva > 0).  Motivo: Umidade baixa para alta temperatura e chuva.
#Regra 2: Nível UV maior que 3 fora do horário entre 8h e 17h. Motivo: Nível UV alto fora do horário de pico.
#Regra 3: Luminosidade acima de 1000 entre 18h e 6h. Motivo: Luminosidade elevada fora do horário diurno.

import pandas as pd
from datetime import datetime

try:
    df = pd.read_excel('medicoes_10.xlsx')
    print(f'Dataframe criado:\n {df} \n')
except FileNotFoundError:
    print('arquivo não encontrado')
except Exception as err:
    print(f'erro, {err}')

regras = {
    'Umidade baixa para alta temperatura': (df['Umidade'] < 30) & (df['Temperatura'] > 35) & (df['ml_Chuva'] > 0),
    'Nível UV alto fora do horário de pico': (df['Nível UV'] > 3) & ((df['Data de Medição'].dt.hour < 8) | (df['Data de Medição'].dt.hour > 17)),
    'Luminosidade elevada fora do horário diurno': (df['Luminosidade'] > 1000) & ((df['Data de Medição'].dt.hour < 6) | (df['Data de Medição'].dt.hour > 18))
}

df_inconsistentes = pd.DataFrame()

for motivo, condicao in regras.items():
    aux_df = df[condicao].copy()
    aux_df['Motivo'] = motivo
    df_inconsistentes = pd.concat([df_inconsistentes, aux_df])

df_inconsistentes['Data de Medição'] = df_inconsistentes['Data de Medição'].dt.strftime('%Y-%m-%d %H:%M:%S')

print(df_inconsistentes)

try	:
    with pd.ExcelWriter('medicoes_inconsistentes_10.xlsx', engine='openpyxl') as writer:
        df_inconsistentes.to_excel(writer, sheet_name='Inconsistentes', index=False)
        print(f'foram encontradas {len(df_inconsistentes)} medições inconsistentes e salvas em medicoes_inconsistentes_10.xlsx')
except Exception as err:
    print(f'erro, {err}')