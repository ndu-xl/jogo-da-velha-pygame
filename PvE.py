import pygame 
from pygame.locals import* 
from sys import exit
from time import sleep
from random import randint
def PvEPage():

    pygame.init() # inicia o programa pygame

    vitoria_som = pygame.mixer.Sound('Vitoria Som.wav') 
    velha_som = pygame.mixer.Sound('Empate Som.wav')

    largura = 1000
    altura = 650

    VelhaText = False
    VitoriaText = False
    Vitoria = False
    VitoriaX = False
    VitoriaO = False

    fonteVitoriaVelha = pygame.font.SysFont("arial", 140, True, False)# Fontes
    fonteSub = pygame.font.SysFont("arial", 24)

    tam = 600

    Tabuleiro = [["","",""],["","",""],["","",""]]
    Jogada = 1

    Resetar = pygame.Rect(20,440,100,50)

    Voltar = pygame.Rect(20,500,100,50)
    fonteSub = pygame.font.SysFont("arial", 24)

    def PlayerXVictoryListen(vencedor):#verifica se o x ganhou e muda a pontuação e a cor do vitoria
        nonlocal pontuacaoX, VitoriaX
        Velha = pontuacaoX
        if(vencedor == "X"):
            VitoriaX = True
            vitoria_som.play()
            pontuacaoX += 1
            return pontuacaoX
        elif(vencedor == False):
            return Velha
        else:
            return Velha
        

    def PlayerOVictoryListen(vencedor):#verifica se o O ganhou e muda a pontuação e a cor do vitoria
        nonlocal pontuacaoO, VitoriaO
        Velha = pontuacaoO
        if(vencedor == "O"):
            VitoriaO = True
            vitoria_som.play()
            pontuacaoO += 1
            return pontuacaoO
        elif(vencedor == False):
            return Velha
        else:
            return Velha

    def lendoNomes(): #Lendo nomes para o placar que já foi guardada de partidas anteriormente para o placar atualizar a variável
            with open("nomes.txt", "r") as arquivo:
                nome1 = arquivo.readline().strip()
                nome2 = arquivo.readline().strip()
                if nome1 == "":
                    nome1 = "Player 1"
                return nome2, nome1

    def lendoPontos(): #Lendo pontuação que já foi guardada de partidas anteriormente para o placar atualizar a variável
        nonlocal pontuacaoX, pontuacaoO
        try:
            with open("dados.txt", "r") as arquivo:
                txtpontuacaoX = arquivo.readline().strip()
                txtpontuacaoO = arquivo.readline().strip()
                pontuacaoX = int(txtpontuacaoX)
                pontuacaoO = int(txtpontuacaoO)
                return pontuacaoX, pontuacaoO
        except FileNotFoundError:
            atualizarPontos(False, 0, 0)
            return 0, 0
        except ValueError:
            atualizarPontos(False, 0, 0)
            return 0, 0

    def atualizarPontos(VitoriaState,p1, p2): #Atualizando pontuação para um valor atual
        nonlocal Tabuleiro
        if(VitoriaState == True):
            with open("dados.txt", "w") as arquivo:
                arquivo.write(str(p1) + "\n")
                arquivo.write(str(p2))
            VitoriaState = False
            Tabuleiro = [["","",""],["","",""],["","",""]]
        return VitoriaState
    
    def resetarPontos(): # Auto-explicativo, ele reinicia os valores
        nonlocal pontuacaoO, pontuacaoX
        pontuacaoX = 0
        pontuacaoO = 0
        return pontuacaoX, pontuacaoO
        

    nome1, nome2 = lendoNomes()
    pontuacaoX, pontuacaoO = lendoPontos()


    x = (largura - tam) // 2
    y = (altura - tam) // 2

    def VarrerColuna(y): #Autoexplicativo, varre a linha e retorna qual linha foi clicado
        if(25<= y <= 225):
            CasaSelectLinha = 0
        elif(225<= y <= 425):
            CasaSelectLinha = 1
        elif(425<= y <= 625):
            CasaSelectLinha = 2
        return CasaSelectLinha

    def VitoriaListen(): #Logica de Vitoria
        nonlocal Vitoria
        nonlocal Tabuleiro
        nonlocal VelhaText
        nonlocal VitoriaText
        for i in range(3):
            if(Tabuleiro[i][0] != ""): #Vitoria por linha
                if(Tabuleiro[i][0] == Tabuleiro[i][1] == Tabuleiro[i][2]  ):
                    print("VITORIA")
                    Vitoria = True
                    VitoriaText = True
                    Vitoria = atualizarPontos(Vitoria,PlayerXVictoryListen(Tabuleiro[i][0]),PlayerOVictoryListen(Tabuleiro[i][0])) # Atualizando pontos pós partida
            if(Tabuleiro[0][i] != ""): #Vitoria por coluna
                if(Tabuleiro[0][i] == Tabuleiro[1][i] == Tabuleiro[2][i]):
                    print("VITORIA")
                    VitoriaText = True
                    Vitoria = True
                    Vitoria = atualizarPontos(Vitoria,PlayerXVictoryListen(Tabuleiro[0][i]),PlayerOVictoryListen(Tabuleiro[0][i])) 

            if(Tabuleiro[1][1] != ""): #Vitoria por diagonal
                if(Tabuleiro[1][1] == Tabuleiro[0][0] == Tabuleiro[2][2]):
                    print("VITORIA")
                    VitoriaText = True                
                    Vitoria = True
                    Vitoria = atualizarPontos(Vitoria,PlayerXVictoryListen(Tabuleiro[1][1]),PlayerOVictoryListen(Tabuleiro[1][1]))
                elif(Tabuleiro[1][1] == Tabuleiro[0][2] == Tabuleiro[2][0]):
                    print("VITORIA")
                    VitoriaText = True                
                    Vitoria = True
                    Vitoria = atualizarPontos(Vitoria,PlayerXVictoryListen(Tabuleiro[1][1]),PlayerOVictoryListen(Tabuleiro[1][1]))
                
            CasasPreenchidas = 0 #Analisa se deu velha, ou seja, nenhuma casa vazia e ngm venceu, resetando o tabuleiro
            for j in range(3):
                for l in range(3):
                    if(Tabuleiro[j][l] != ""):
                        CasasPreenchidas += 1
            if(CasasPreenchidas == 9):
                VelhaText = True
                Tabuleiro = [["","",""],["","",""],["","",""]]
                velha_som.play()
                
    tela = pygame.display.set_mode((largura,altura))

    pygame.display.set_caption("Jogo da Velha") # Altera o nome do jogo

    while True:
        if(Jogada%2 == 0): # verifica se a jogada é a do bot
            while True:
                jogadaBotX = randint(200, 800)
                jogadaBotY = randint(25, 625)
                if(200<=jogadaBotX<=400): #coluna 1
                    CasaSelectColuna = 0
                    CasaSelectLinha = VarrerColuna(jogadaBotY)
                elif(400<= jogadaBotX <= 600): #coluna 2
                    CasaSelectColuna = 1
                    CasaSelectLinha = VarrerColuna(jogadaBotY)
                elif(600<= jogadaBotX <= 800): #coluna 3
                    CasaSelectColuna = 2
                    CasaSelectLinha = VarrerColuna(jogadaBotY)
                if(Tabuleiro[CasaSelectLinha][CasaSelectColuna] == ""): # se já tiver algo naquela casa o bot vai escolher outra
                    Tabuleiro[CasaSelectLinha][CasaSelectColuna] = "X"
                    Jogada += 1
                    break
        mensagemPontuacaoO = f'Bot X:{pontuacaoX}' # Vai criar mensagem de pontuação
        mensagemPontuacaoX = f'{nome2} O:{pontuacaoO}'
        mensagemVitoria = "VITORIA" 
        mensagemVelha = "VELHA"
        colorText = 0,0,0
        if VitoriaO: # ele verifica se o O ganhou e muda a cor do vitoria
           colorText = 52,152,209
        if VitoriaX: # a mesma coisa só que com o X
            colorText = 231,76,60
        #Vai formatar os textos
        formatacaoFinalVitoria = fonteVitoriaVelha.render(mensagemVitoria, False, (colorText))
        formatacaoFinalVelha = fonteVitoriaVelha.render(mensagemVelha, False, (60, 60, 60))
        formatacaoFinalPontuacaoO = fonteSub.render(mensagemPontuacaoO, True, (231,76,60))
        formatacaoFinalPontuacaoX = fonteSub.render(mensagemPontuacaoX, True, (52,152,209))
        for event in pygame.event.get():
            if event.type == QUIT: #funcao para fechar o jogo
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                #detecta botoes
                if(Voltar.collidepoint(event.pos)):
                    return  "menu"
                if(Resetar.collidepoint(event.pos)):
                    pontuacaoO, pontuacaoX = resetarPontos()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if(200<=mouse_x<=800 and 25 <= mouse_y <= 625): #Ve se o clique foi fora ou dentro do tabuleiro com dimensoes: X = 200-800 / Y = 25-625
                    print("clique dentro do tabuleiro")
                    if(200<=mouse_x<=400): #coluna 1
                        CasaSelectColuna = 0
                        CasaSelectLinha = VarrerColuna(mouse_y)
                    elif(400<= mouse_x <= 600): #coluna 2
                        CasaSelectColuna = 1
                        CasaSelectLinha = VarrerColuna(mouse_y)
                    elif(600<= mouse_x <= 800): #coluna 3
                        CasaSelectColuna = 2
                        CasaSelectLinha = VarrerColuna(mouse_y)
                    if(Tabuleiro[CasaSelectLinha][CasaSelectColuna] == ""): #não deixa selecionar a casa já selecionada
                        if(Jogada%2 != 0):
                            Tabuleiro[CasaSelectLinha][CasaSelectColuna] = "O"
                            Jogada += 1
                    else:
                        print("Casa ja selecionada")

                    #Variaveis para acompanhar o fluxo do processo
                    print(CasaSelectColuna,CasaSelectLinha)
                    for i in range(len(Tabuleiro)):
                        print(Tabuleiro[i])
        if VitoriaText:# Adiciona texto de vitoria se houver vitoria
            tela.blit(formatacaoFinalVitoria, (250, 250)) 
        # Adicionando texto da pontuacao na tela
        tela.blit(formatacaoFinalPontuacaoO, (20, 20)) 
        tela.blit(formatacaoFinalPontuacaoX, (20, 70))
        if VelhaText:
            tela.blit(formatacaoFinalVelha, (250, 250))
        
        pygame.display.update() #funcao para atualizar as mudancas da tela
        #cooldown a cada fim de partida para o usuario entender que ganhou ou deu velha
        if VitoriaText:
            sleep(1)
            VitoriaText = False
            VitoriaX = False
            VitoriaO = False
        if VelhaText:
            sleep(1)
            VelhaText = False

        tela.fill((240, 240, 240)) #define a tela como branca

            # verticais
        pygame.draw.line(tela, (0,0,0), (400, 25), (400, 625), 5)
        pygame.draw.line(tela, (0,0,0), (600, 25), (600, 625), 5)

        # horizontais
        pygame.draw.line(tela, (0,0,0), (200, 225), (800, 225), 5)
        pygame.draw.line(tela, (0,0,0), (200, 425), (800, 425), 5)

         #Botao de voltar
        pygame.draw.rect(tela, (52,152,209), Voltar, border_radius=10)
        pygame.draw.rect(tela,(30,30,30), Voltar, 3, border_radius=10)

        #Botao de resetar
        pygame.draw.rect(tela, (231,76,60), Resetar, border_radius=10)
        pygame.draw.rect(tela,(30,30,30), Resetar, 3, border_radius=10)

        #nomes dos botoes
        render7 = fonteSub.render("Reset", True, (255,255,255))
        render6 = fonteSub.render("Voltar", True, (255,255,255))
        #colocando eles na tela
        tela.blit(render7, (Resetar.x +20, Resetar.y + 10))
        tela.blit(render6, (Voltar.x +20, Voltar.y + 10))

        for linha in range(3): #Desenha as figuras dentro de cada casa ja selecionada
            for coluna in range(3):

                if(Tabuleiro[linha][coluna] == "X"):
                    if(linha == 0):
                        Desenho_X = 25
                    elif(linha == 1):
                        Desenho_X = 225
                    elif(linha == 2):
                        Desenho_X = 425
                    if(coluna == 0):
                        Desenho_Y = 200
                    elif(coluna == 1):
                        Desenho_Y = 400
                    elif(coluna == 2):
                        Desenho_Y = 600
                    pygame.draw.line(tela,(231,76,60),(Desenho_Y+30,Desenho_X+30),(Desenho_Y+170,Desenho_X+170), 10)
                    pygame.draw.line(tela,(231,76,60),(Desenho_Y+170,Desenho_X+30),(Desenho_Y+30,Desenho_X+170), 10)
                elif(Tabuleiro[linha][coluna] == "O"):
                    if(linha == 0):
                        Desenho_X = 25
                    elif(linha == 1):
                        Desenho_X = 225
                    elif(linha == 2):
                        Desenho_X = 425
                    if(coluna == 0):
                        Desenho_Y = 200
                    elif(coluna == 1):
                        Desenho_Y = 400
                    elif(coluna == 2):
                        Desenho_Y = 600
                    pygame.draw.circle(tela,(52,152,209),(Desenho_Y+100,Desenho_X+100),80,6)
        VitoriaListen() #verifica até alguem ganhar