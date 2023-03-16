nascimento = 1997
nome = 'caio'
anoAtual = 2023
nascimentojovem = 2006

def calculoidade(nascimento,anoAtual):
    idade = anoAtual - nascimento
    idadejovem = anoAtual - nascimentojovem
    return idade
idade = calculoidade (nascimento, anoAtual)
idadejovem = calculoidade (nascimentojovem, anoAtual)
print ('A idade de Caio é ' + str(idade))
print ('A idade do jovem é ' + str(idadejovem))