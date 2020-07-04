# Aqui será uma sequencia de exercicios propostos no site:
# https://wiki.python.org.br/EstruturaSequencial
# Por opção propria decidi criar uma classe sendo que cada
# método desta classe é um dos exercicios propostos em que
# depois chamo todos eles em um menu mais personalizado em
# que eu posso chamar cada exercicio desta classe nele:
import os
import time

class Exercicio:
    ########################### Funções auxiliares: ############################
    #Função para limpar a tela
    def limpaEsseTrem(self):
        os.system('cls||clear')
    #Função que faz o sistema aguardar
    def pera(self,tempo):
        print('Aguarde por favor...')
        time.sleep(tempo)
    #Função que verifica se o valor e numerico ou nao
    def eNumIsso(self,n):
        try:
            int(n)
            return True
        except:
            return False
    ######################## Fim de Funções auxiliares: ########################

    ######################### Inicio dos Exercicios ! ##########################
    # Exercicio 1:
    #Faça um Programa que mostre a mensagem "Alo mundo" na tela.
    def olaMundo(self):
        print('------------------------Exercicio 1:-----------------------')
        print('Faça um Programa que mostre a mensagem "Alo mundo" na tela.')
        print('Ola Mundo!!!!')
        print('-----------------------------------------------------------')

    # Exercicio 2:
    #Faça um Programa que peça um número e então mostre a mensagem O número
    #informado foi [número].
    def exibeNumero(self):
        print('------------------------Exercicio 2:-----------------------')
        print('Faça um Programa que peça um número e então mostre a mensagem Numero informado foi X:')
        exercicio.pera(4)
        exercicio.limpaEsseTrem()
        print('-----------------------------------------------------------')
        valor = input('Digite um Numero valido:')
        if exercicio.eNumIsso(valor):
            print(f'O valor digitado {valor} e um valor NUMERICO')
        else:
            print(f"O valor digitado {valor} não é um numerico!!!!")

        exercicio.pera(5)
        print('-----------------------------------------------------------')
    #################### Fim dos Exercicios! ########################

#################### Começo da parte principal do programa ####################
exercicio = Exercicio() # Cria a classe para ser usada
i = True
while(i):
    exercicio.limpaEsseTrem()
    print('-----------------------------------------------------------')
    print('Lista de exercicios já feitos:')
    print('1 : OlaMundo')
    print('2 : Exibe Numero')
    print('0 : Finaliza o Programa')
    print('-----------------------------------------------------------')
    ex = input('Escolha qual exercicio você quer executar:')

    if ex == '0':
        print('Exercicios retirados de: https://wiki.python.org.br/ListaDeExercicios')
        print('Finalizando programa...')
        exercicio.pera(3)
        i = False
    else:
        if ex == '1':
            exercicio.olaMundo()
            #time.sleep(5)
            exercicio.pera(5)
        elif ex == '2':
            exercicio.exibeNumero()
