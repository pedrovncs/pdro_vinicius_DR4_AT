#4 Defina uma tupla para representar um produto no estoque, contendo o nome do produto (string), o preço (float) e a quantidade disponível (inteiro). 
# Em seguida, crie uma lista contendo pelo menos três produtos.

produto1 = ('O Senhor dos Anéis: A Sociedade do Anel', 33.99, 765)
produto2 = ('O Senhor dos Anéis: As Duas Torres', 52.43, 225)
produto3 = ('O Senhor dos Anéis: O Retorno do Rei', 69.99, 33)

lista_produtos = [produto1, produto2, produto3]

print(f'\nQuestão 4:')
print(lista_produtos)

#5 Escreva uma função que adiciona um novo produto ao estoque:
# adicionar_produtos_via_json(estoque: list[Produto], arquivo_json: str), 
# onde estoque é a lista onde os produtos serão adicionados e arquivo_json é o caminho para o arquivo json contendo os produtos a serem adicionados. 
# Cada objeto dentro do array principal json contém três pares chave-valor: nome, preço e quantidade. 
# Caso haja algum erro durante o processo (como arquivo inválido ou valores incorretos), a função deve lidar com o erro e exibir uma mensagem apropriada.
import pandas as pd
import json

def adicionar_produtos_via_json(estoque, arquivo_json):
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            produtos = json.load(f)
            
            for produto in produtos:
                if type(produto['nome']) == str and type(produto['preco']) == float and type(produto['quantidade']) == int:
                    estoque.append((produto['nome'], produto['preco'], produto['quantidade']))
                else:
                    raise ValueError
            return estoque
    except FileNotFoundError:
        print('erro, arquivo json nao encontrado')
        return
    except json.JSONDecodeError:
        print('erro, arquivo json invalido')
        return
    except ValueError:
        print('erro, tipos incorretos no json')
        return

lista_produtos_atualizada = adicionar_produtos_via_json(lista_produtos, 'produtos_5.json')

print(f'\nQuestão 5:\n')
print(lista_produtos_atualizada)

#6 Implemente a seguinte função: calcular_valor_total_estoque(estoque: list[Produto]):
# Essa função deve calcular e retornar o valor total de todos os produtos no estoque. (total += preço * quantidade).
def calcular_valor_total_estoque(estoque):
    dict_estoque = {}
    for produto in estoque:
        dict_estoque[produto[0]] = produto[1] * produto[2]
    return dict_estoque

print(f'\nQuestão 6:\n')
dict_estoque = calcular_valor_total_estoque(lista_produtos_atualizada)
total_produtos = sum(dict_estoque.values())
for key, value in dict_estoque.items():
    print(f'{key}: R${round(value,2)}')

print(f'\nO valor total do estoque é: R${round(total_produtos,2)}')       

#7 Escreva uma função para vender produtos do estoque: vender_produto(estoque: list[Produto], nome: str, quantidade_vendida: int):
#Essa função deve encontrar o produto pelo nome e, se houver quantidade suficiente no estoque, deve subtrair a quantidade vendida. 
# Caso a quantidade no estoque seja insuficiente, a função deve exibir uma mensagem de erro.

def vender_produto(estoque, nome, quantidade_vendida):
    try:
        for index,produto in enumerate(estoque):
            if produto[0] == nome:
                if produto[2] >= quantidade_vendida:
                    estoque.remove(produto)
                    qtd_restante = produto[2] - quantidade_vendida
                    estoque.insert(index, (produto[0], produto[1], qtd_restante))
                    print(f'{quantidade_vendida} unidades de {nome} vendidas com sucesso! Restam {qtd_restante} unidades no estoque')
                    return estoque
                else:
                    raise ValueError
        print(f'erro, produto {nome} nao encontrado')
    except ValueError:
        print(f'erro, quantidade insuficiente no estoque: solicitado {quantidade_vendida}, em estoque: {produto[2]}')
        return
    
    
print(f'\nQuestão 7:\n')
estoque_atualizado = vender_produto(lista_produtos_atualizada, 'O Senhor dos Anéis: A Sociedade do Anel', 10)

print(f'Estoque atualizado: \n{estoque_atualizado}')


#8 Crie uma função que exibe todos os produtos em um estoque e salve essas informações em um arquivo csv, com tratamento de erros durante a escrita.
import pandas as pd

def salvar_estoque_csv(estoque, arquivo_csv):
    try:
        df = pd.DataFrame(estoque, columns=['Nome', 'Preço', 'Quantidade'])
        print(df)
        df.to_csv(arquivo_csv, index=False)
        print(f'arquivo {arquivo_csv} salvo com sucesso')
    except:
        print('erro ao salvar arquivo csv')
        return
    
print(f'\nQuestão 8:\n')
salvar_estoque_csv(estoque_atualizado, 'estoque_tolkien.csv')
