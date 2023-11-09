'''
----------------------------------------------------------
1. Considere a seguinte lista = [10, 20, 35, 37, 39, 21, 22, 26, 24, 28, 29].
Utilize o laço de repetição for para percorrer está lista e imprima apenas os números pares.


lista = [10, 20, 35, 37, 39, 21, 22, 26, 24, 28, 29]
par = []
for item in lista:
    if item % 2 == 0:
       par.append(item)
print(par)
'''

'''
2. Considere a seguinte lista de velocidades = [46, 32, 48, 62, 63, 33, 45, 36, 45, 68], 
utilize o for para imprimir apenas as velocidades acima do limite (limite = 60)


velocidades = [46, 32, 48, 62, 63, 33, 45, 36, 45, 68]
maior = []
for i in velocidades:
    if i > 60:
        maior.append(i)
print(maior)
'''

'''
3. Utilize a mesma lista da questão 1 para contar a 
quantidade de pares dentro da lista, e informe essa quantidade no final do programa.


lista = [10, 20, 35, 37, 39, 21, 22, 26, 24, 28, 29]
quantidade = 0
for i in lista:
    if i % 2 == 0:
        quantidade += 1

print(quantidade)
'''


'''
4. Considere a lista do exercicio 2, 
e imprima o maior número da lista, para isso você precisa utilizar o laço de repetição for


velocidades = [46, 32, 48, 62, 63, 33, 45, 36, 45, 68]
maior = 0
for i in velocidades:
    if i > maior:
      maior = i
print(maior)
'''


carrinho = []
while True:
    print('''--- bem- vindo ao menu ----
1 - adicionar produto
2 - Editar produto
3 - Remover produto
4 - Listar todos os produtos
5 - Sair''')
  

    opcao = input('selecione a opcao: ')

    if opcao == '1':
        produto = input('adicione o produto:')
        carrinho.append(produto)
        print('produto adicionado com sucesso!')
    elif opcao == '2':
        produto = input('qual produto do carrinho deseja editar: ')
        if produto in carrinho:
            indece = carrinho.index(produto)
            carrinho[indece] = input('digite o novo nome do produto:')
            print('produto adicionado com sucesso!')
        else:
            print('produto nao encontrado!')
    elif opcao == '3':
        produto = input('digite o  produto que queira REMOVER')
        if produto in carrinho:
            carrinho.remove(produto)
            print('Produto removido com sucesso!')
    elif opcao == '4':
        for produto in carrinho:
            print('--- Seu Carrinho ---')
            print(f'Nome do produto: {produto}')
    elif opcao == '5':
        print('voce saio do programa')
        break
    else:
        print('opcao invalida')
