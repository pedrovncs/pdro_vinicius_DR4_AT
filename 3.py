def check_words(chars, word):
    list_word =  list(word)
    
    for letter in list_word:
        if letter not in chars:
            return False
    return True
    
chars = 'aophtynlkm'
word = 'python'

print(f'{chars} contém as letras de {word}? {check_words(chars, word)}')