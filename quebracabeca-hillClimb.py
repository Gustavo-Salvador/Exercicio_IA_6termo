from random import randint
import matplotlib.pyplot as plt
import copy

qntLinhas = 5
qntColunas = 5
quebraCabecaAleatorio = False

limiteTentativas = 100000

def criaQuebraCabeca(y, x, embaralhado = False):
    resultado = []
    
    if embaralhado:
        pecas = list(range(1, y * x + 1))
        
    for i in range(y):
        resultado.append([])
        for j in range(x):
            if not embaralhado:
                resultado[i].append([(j + 1) + (x * i), randint(0, 3)])
                
            else:
                resultado[i].append([pecas.pop(randint(0, len(pecas) - 1)), randint(0, 3)])
            
    return resultado

def imprimeQuebraCabeca(forma):
    for i in range(len(forma)):
        for j in range(len(forma[i])):
            print(forma[i][j], end = '\t')
        print()        


def contaPecasCertas(formaCorreta, formaAtual):
    pontuacao = 0
    for i in range(len(formaAtual)):
        for j in range(len(formaAtual[i])):
            if formaAtual[i][j][0] == formaCorreta[i][j][0]:
                pontuacao += 1        
                if formaAtual[i][j][1] == formaCorreta[i][j][1]:
                    pontuacao += 1
                
    return pontuacao

def movePeca(formaAtual):
    pecaY = randint(0, len(formaAtual) - 1)
    pecaX = randint(0, len(formaAtual[pecaY]) - 1)
    
    peca2Y = randint(0, len(formaAtual) - 1)
    peca2X = randint(0, len(formaAtual[pecaY]) - 1)
    
    formaAtual[pecaY][pecaX][0], formaAtual[pecaY][pecaX][1], formaAtual[peca2Y][peca2X][0], formaAtual[peca2Y][peca2X][1] = formaAtual[peca2Y][peca2X][0], formaAtual[peca2Y][peca2X][1], formaAtual[pecaY][pecaX][0], formaAtual[pecaY][pecaX][1]
    
    return formaAtual
    
def giraPeca(formaAtual):
    pecaY = randint(0, len(formaAtual) - 1)
    pecaX = randint(0, len(formaAtual[pecaY]) - 1)
    
    formaAtual[pecaY][pecaX][1] = randint(0, 3)
    
    return formaAtual

def montaQuebraCabeca():
    quebraCabecaCerto = criaQuebraCabeca(qntColunas, qntLinhas, quebraCabecaAleatorio)
    
    print('Quebra-Cabeca Certo:')
    imprimeQuebraCabeca(quebraCabecaCerto)
    print()
    
    quebraCabeca = criaQuebraCabeca(qntColunas, qntLinhas, True)
    
    pontuacao = contaPecasCertas(quebraCabecaCerto, quebraCabeca)
    
    c = 0
    pecasCertas = []
    while True:      
        moveOuGira = randint(0, 1)
        if moveOuGira == 0:
            quebraCabecaAtual = movePeca(copy.deepcopy(quebraCabeca))
        else:
            quebraCabecaAtual = giraPeca(copy.deepcopy(quebraCabeca))
        
        pontuacaoAtual = contaPecasCertas(quebraCabecaCerto, quebraCabecaAtual)
        
        if pontuacaoAtual > pontuacao:
            pontuacao = pontuacaoAtual
            quebraCabeca = copy.deepcopy(quebraCabecaAtual)
            
        pecasCertas.append(pontuacao)
            
        if pontuacao == (qntColunas * qntLinhas) * 2:
            result = 'Exito!!!'
            break
            
        if c >= limiteTentativas:
            result = 'Falha'
            break            
        
        c += 1
    
    return result, quebraCabeca, pontuacao, pecasCertas

res, qbrCbc, pnt, pcsCrt = montaQuebraCabeca()
print(f'{res}, pontuação = {pnt}')
imprimeQuebraCabeca(qbrCbc)
x = range(len(pcsCrt))
plt.plot(x, pcsCrt)
plt.xlabel("Tentativas")
plt.ylabel("Peças corretas")
plt.title("Variação da Pontuação")
#plt.legend(loc="lower right")
plt.show()