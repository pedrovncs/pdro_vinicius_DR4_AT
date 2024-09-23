#Escreva uma função que recebe um dicionário de sinônimos e duas palavras. A função deve retornar true se as palavras forem sinônimos e false caso contrário.
def is_synonym(words_dict, word1, word2):
    list_synonyms = []
    
    for key,values in words_dict.items():
        aux_list = [key] + values
        list_synonyms.append(aux_list)
    
    for synonyms in list_synonyms:
        if word1 in synonyms and word2 in synonyms:
            return True
        else:
            return False
    
    

dict_synonyms = {
    'bravo': ['irritado', 'zangado'],
    'carro': ['automóvel', 'veículo'],
    'casa': ['residência', 'lar']
}

word1 = 'irritado'
word2 = 'bravo'

word3 = 'banana'
word4 = 'automóvel'

word5 = 'zangado'
word6 = 'zangado'

print(f'{word1} e {word2} são sinônios? {is_synonym(dict_synonyms, word1, word2)}') 

print(f'{word3} e {word4} são sinônimos? {is_synonym(dict_synonyms, word3, word4)}') 

print(f'{word5} e {word6} são sinônimos? {is_synonym(dict_synonyms, word5, word6)}')
