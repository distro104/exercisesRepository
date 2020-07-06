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
    #Função que imprime uma linha tracejada na tela e caso tenha um texto
    #imprime a linha com o texto centralizado:
    def daLinha(self,txt = '',tamanhoDoTrem = 0):
        texto = '' # Variavel que guarda o texto completo que sera impresso
        if tamanhoDoTrem == 0:
            tamanhoDoTrem = 70
        if len(txt) == 0:
            for i in range(tamanhoDoTrem):
                texto = texto + '-'
        else:
            j = (tamanhoDoTrem - len(txt)) // 2
            for i in range(j):
                texto = texto + '-'
            texto = texto + txt
            for i in range (j):
                texto = texto + '-'
            if len(texto) < tamanhoDoTrem:
                texto = texto + '-'
        print(texto,'\n')

    ######################## Fim de Funções auxiliares: ########################

    ######################### Inicio dos Exercicios ! ##########################
    # Exercicio 1:
    #Faça um Programa que mostre a mensagem "Alo mundo" na tela.
    def olaMundo(self):
        self.limpaEsseTrem()
        self.daLinha('Exercicio 1:')
        print('Faça um Programa que mostre a mensagem "Alo mundo" na tela.')
        print('Ola Mundo!!!!')
        self.daLinha()
        self.pera(3)
    # Exercicio 2:
    #Faça um Programa que peça um número e então mostre a mensagem O número
    #informado foi [número].
    def exibeNumero(self):
        self.limpaEsseTrem()
        self.daLinha('Exercicio 2:')
        print('Faça um Programa que peça um número e então mostre a mensagem Numero informado foi X:')
        self.daLinha()
        valor = input('Digite um Numero valido:')
        if self.eNumIsso(valor):
            print(f'O valor digitado {valor} e um valor NUMERICO')
        else:
            print(f"O valor digitado {valor} não é um numerico!!!!")
        self.pera(5)
        self.daLinha()
    # Exercicio 3
    # Faça um Programa que peça doisou mais números e imprima a soma.
    def somaNumeros(self):
        repetir = False
        valores = []
        texto = ''
        while(repetir == False):
            self.limpaEsseTrem()
            self.daLinha('Exercicio 3:')
            print('Faça um Programa que  peça dois ou mais  números e imprima a soma.')
            print('Lembrando que caso seja  digitado letras somente sera  adicionado ')
            print('a listagem mas  o valor  não será somado! E caso não seja digitado')
            print('valor o programa efetuara a somatoria SOMENTE dos valores numericos')
            print('e voltara ao menu principal.')
            self.daLinha()
            i = 0
            print('Numeros: ')
            print(valores)
            self.daLinha()

            valor = input('Digite o valor que deseja adicionar a soma:')
            if (self.eNumIsso(valor)):
                valores.append(valor)
            elif len(valor) == 0:
                repetir = True

                self.daLinha('Somatoria:')
                total = 0
                for j in valores:
                    total = total + int(j)
                print('Os valores foram:')
                print(valores)
                print(f'Valor total: {total}')

            else:
                print('Não foi digitado um valor valido!!')
            self.pera(3)

    # Exercicio 4
    # Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    def calculaNota(self):
        repetir = False
        notas = []
        media = 0
        while repetir == False:
            self.limpaEsseTrem()
            self.daLinha('Exercicio 3')
            print('Faça um programa que peça as 4 notas bimestrais e mostre a media.')
            self.daLinha()
            print('Valores digitados:')
            print(notas)

            if len(notas) < 4:
                valor = input('Digite um valor valido: ')
                if self.eNumIsso(valor) == True:
                    notas.append(valor)
                else:
                    print('O valor digitado não é um valor valido! Digite um valor valido.')
            else:
                for i in notas:
                    media = media + int(i)
                    media = media / len(notas)
                print('O média das notas é:')
                print(media)
                repetir = True
            self.pera(3)
    ########################## Fim dos Exercicios! #############################

#################### Começo da parte principal do programa ####################
exercicio = Exercicio() # Cria a classe para ser usada
i = True
while(i):
    exercicio.limpaEsseTrem()
    exercicio.daLinha()
    print('Lista de exercicios já feitos:')
    print('1 : OlaMundo')
    print('2 : Exibe Numero')
    print('3 : Soma Numeros')
    print('4 : Calcula Media das notas')
    print('0 : Finaliza o Programa')
    exercicio.daLinha()
    ex = input('Escolha qual exercicio você quer executar:')

    if ex == '0':
        print('Exercicios retirados do site: https://wiki.python.org.br/ListaDeExercicios')
        print('Finalizando programa...')
        exercicio.pera(3)
        i = False
    else:
        if ex == '1':
            exercicio.olaMundo()
        elif ex == '2':
            exercicio.exibeNumero()
        elif ex == '3':
            exercicio.somaNumeros()
        elif ex == '4':
            exercicio.calculaNota()
