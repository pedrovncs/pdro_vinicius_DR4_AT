#9 Desenvolva um programa que combine dados de funcionários e suas avaliações a partir de dois arquivos Excel, com base na coluna ID, e salve o resultado em um novo arquivo Excel. 
# É preciso garantir que apenas IDs presentes em ambos os arquivos sejam combinados.

import pandas as pd

def criar_xlsx():
    path_xlsx = 'funcionarios_9.xlsx'
    
    dados_funcionarios = {
        'ID': [1, 2, 3, 4],
        'Nome': ['Pedro', 'Vinicius', 'Araujo', 'Paiva'],
        'Idade': [23, 33, 25, 27],
        'Cargo': ['Analista', 'Estágiario', 'Desenvolvedor', 'Estagiário']
    }

    avaliacoes_funcionarios = {
        'ID': [2,3,1,5],
        'Avaliacao': ['Bom', 'Regular', 'Ruim', 'Bom'],
    }

    df1 = pd.DataFrame(dados_funcionarios)
    df2 = pd.DataFrame(avaliacoes_funcionarios)

    with pd.ExcelWriter(path_xlsx, engine= 'openpyxl') as writer:
        try:
            df1.to_excel(writer, sheet_name='Funcionários', index=False)
            df2.to_excel(writer, sheet_name='Avaliações', index=False)
            print("Arquivo  criado com sucesso!")
        except Exception as err:
            print(f"Erro criando arquivo {path_xlsx}: {err}")
        

criar_xlsx()

try:
    df_funcionarios = pd.read_excel('funcionarios_9.xlsx', sheet_name='Funcionários')
    df_avaliacoes = pd.read_excel('funcionarios_9.xlsx', sheet_name='Avaliações')

    merged_funcionarios_avaliacoes = pd.merge(df_funcionarios, df_avaliacoes, on='ID', how='inner')
    merged_funcionarios_avaliacoes.to_excel('merged_funcionarios_9.xlsx', index=False)
    print("Arquivo merged_funcionarios_9.xlsx criado com sucesso!")
except FileNotFoundError as err:
    print(f"Erro, arquivo não encontrado: {err}")
except Exception as err:
    print(f"Erro: {err}")