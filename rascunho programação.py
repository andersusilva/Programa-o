#EstruturaDeDecisao
#questão 1 (Compilou)
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
if n1 > n2:
  print (n1, 'é o maior número digitado')
else:
    print (n2, 'é o maior número digitado');
	
#questão 2 (Compilou)
a = int(input('Digite um número: '))
if a < 0:
 print (a, 'é negativo')
else:
 print (a, 'é zero ou positivo')
 
#questão 3 (Compilou)
sexo = input('Digite o seu sexo! Sendo f para Feminino ou m para Masculino')
if sexo == 'm': 
	print('Masculino') 
elif sexo == 'f': 
	print('Feminino') 
else: 
	print('Sexo Inválido')
	
#questão 4 (Compilou)
letra = input('Digite uma letra (em minúsculo) : ')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print 'A letra digitada é uma vogal'
else:
    print 'A letra digitada é uma consoante'

#questão 5 (Compilou)
nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua 2ª nota: '))
notafinal = (nota1 + nota2) / 2
if notafinal >= 7 and notafinal < 10:
    print ('Você foi Aprovado!')
elif notafinal >= 10:
    print ('Você foi aprovado com Louvor!')
else:
    print ('Infelizmente você foi Reprovado!')

#questão 6 (compilou)
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))
if n1 > n2 and n3:
	print (n1, 'é o maior número digitado');
elif n2 > n1 and n2:
	print (n2, 'é o maior número digitado');
else:
	print (n3, 'é o maior número digitado');

#questão7 (não to acertando o n3)

n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
n3 = int(input('Digite o 3° numero: '))

def maior():
    if n1 > n2 and n3 and n1:
        print n1, 'é o maior numero!!'
    elif n2 > n1 and n3:
        print n2,'é o maior numero!!'
    elif n3 > n1 and n2:
        print n3,'é o maior numero!!'

    #Se somente numeros forem iguais

    elif n1 == n2 and n1 and n2 > n3:
        print n1,'é','o maior!!'
    elif n1 == n3 and n1 and n3 > n2:
        print n1,'é','o maior!!'
    elif n2 == n3 and n2 and n3 > n1:
        print n2,'é','o maior!!'
    #todos os forem numeros iguais
    elif n1 == n2 and n3:
        print 'todos o numeros são iguais'

def menor():
    if n1 < n2 and n3 and n1:
        print n1, 'é o menor numero!!'
    elif n2 < n1 and n3:
        print n2,'é o menor numero!!'
    # elif n3 < n1 and n2:
        print n3,'é o menor numero!!'

    #Se somente alguns numeros forem iguais

    elif n1 == n2 and n1 and n2 < n3:
        print n1,'é','o menor!!'
    elif n1 == n3 and n1 and n3 < n2:
        print n1,'é','o menor!!'
    elif n2 == n3 and n2 and n3 < n1:
        print n2,'é','o menor!!'

maior()   #método usado para descubrir o maior número
menor()   #método usado para descubrir o menor número

#questão 8 (Compilou)
p1 = input("Digite o 1° preço: ")
p2 = input("Digite o 2° preço: ")
p3 = input("Digite o 3° preço: ")

def menor():
    if p1 < p2 and p3 and p1:
        print ('O produto 1 é o mais barato!!')
    elif p2 < p1 and p3:
        print ('O produto 2 é o mais barato!!')
    elif p3 < p1 and p2:
        print ('O produto 3 é o mais barato!!')

    #Se alguns numeros forem iguais

    elif p1 == p2 and p1 and p2 < p3:
        print ('O produto 1 e 2 são os mais baratos!')
    elif p1 == p3 and p1 and p3 < p2:
        print ('O produto 1 e 3 são os mais baratos!')
    elif p2 == p3 and p2 and p3 < p1:
        print ('O produto 1 e 2 são os mais baratos!')

    #Se todos os numeros forem iguais

    else:
        print ('Todos os preços são iguais!')

menor() #função menor!

#questão 10 (Compilou)
turno = input('Digite em que turno você estuda: M para matutino ou V para Vespertino ou N para Noturno (em maiúsculo): ')

if turno == 'M':    #estuda de manha?
    print ('Bom Dia !!')
elif turno == 'V':  #estuda a tarde? 
    print ('Boa Tarde!!')
elif turno == 'N':  #estuda de noite?
    print ('Boa Noite!!')
else:    
    print ('Valor Inválido')
	
