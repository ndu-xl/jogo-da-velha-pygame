import pygame 
from pygame.locals import* 
from sys import exit
from time import sleep
def PvPPage():

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

    #fontes criadas
    fonteVitoriaVelha = pygame.font.SysFont("arial", 140, True, False)
    fonteSub = pygame.font.SysFont("arial", 24, True, False)
    fonteSub = pygame.font.SysFont("arial", 24)

    tam = 600

    Tabuleiro = [["","",""],["","",""],["","",""]]
    Jogada = 1

    Resetar = pygame.Rect(20,440,100,50)

    Voltar = pygame.Rect(20,500,100,50)


    def PlayerXVictoryListen(vencedor): #ve se o vencedor foi o X para mudar a pontuacao
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
        

    def PlayerOVictoryListen(vencedor): #ve se o vencedor foi o O para mudar a pontuacao
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

    def lendoNomes(): #Lendo pontuação que já foi guardada de partidas anteriormente para atualizar a variável
            with open("nomes.txt", "r") as arquivo:
                nome1 = arquivo.readline().strip()
                nome2 = arquivo.readline().strip()
                if nome1 == "":
                    nome1 = "Player 1"
                if nome2 == "":
                    nome2 = "Player 2"
                return nome1, nome2

    def lendoPontos(): #Lendo pontuação que já foi guardada de partidas anteriormente para atualizar a variável
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
    
    def resetarPontos(): #reseta todos os pontos no arquivo
        nonlocal pontuacaoO, pontuacaoX
        pontuacaoX = 0
        pontuacaoO = 0
        return pontuacaoX, pontuacaoO
        
    player1, player2 = lendoNomes()
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
                    print("VITORIA") #Loop provisorio(Tudo que vier pos vitoria tem q vir aqui)
                    Vitoria = True
                    VitoriaText = True
                    Vitoria = atualizarPontos(Vitoria,PlayerXVictoryListen(Tabuleiro[i][0]),PlayerOVictoryListen(Tabuleiro[i][0])) # Atualizando pós partida
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
        mensagemPontuacaoO = f'{player1} X:{pontuacaoX}'
        mensagemPontuacaoX = f'{player2} O:{pontuacaoO}' # Vai criar a mensagem do placar
        mensagemVitoria = "VITORIA" # vai criar a mensagem vitoria
        mensagemVelha = "VELHA"

        #altera a cor do texto de vitoria dependendo do vencedor
        colorText = 0,0,0
        if VitoriaO:
           colorText = 231,76,60
        if VitoriaX:
            colorText = 52,152,209

        #criacao de textos, mensagem de vitoria/velha/pontuacoes
        formatacaoFinalVitoria = fonteVitoriaVelha.render(mensagemVitoria, False, (colorText))
        formatacaoFinalVelha = fonteVitoriaVelha.render(mensagemVelha, False, (60, 60, 60))
        formatacaoFinalPontuacaoO = fonteSub.render(mensagemPontuacaoO, True, (52,152,209)) # Vai formatar a fonte e renderizar o placar
        formatacaoFinalPontuacaoX = fonteSub.render(mensagemPontuacaoX, True, (231,76,60))
        
        
        for event in pygame.event.get():
            if event.type == QUIT: #funcao para fechar o jogo
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN: # ve se teve clique do mouse

                if(Voltar.collidepoint(event.pos)): #analisa se o clique foi em Voltar
                    return  "menu"
                if(Resetar.collidepoint(event.pos)): #analisa se o clique foi em Resetar
                    pontuacaoO, pontuacaoX = resetarPontos()

                mouse_x, mouse_y = pygame.mouse.get_pos() #pega a posicao do clique do mouse
                
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
                    if(Tabuleiro[CasaSelectLinha][CasaSelectColuna] == ""):
                        if(Jogada%2 == 0):
                            Tabuleiro[CasaSelectLinha][CasaSelectColuna] = "X"
                            Jogada += 1
                        else:
                            Tabuleiro[CasaSelectLinha][CasaSelectColuna] = "O"
                            Jogada += 1
                    else:
                        print("Casa ja selecionada") 

                    #Variaveis para acompanhar o fluxo do processo no terminal
                    print(CasaSelectColuna,CasaSelectLinha)
                    for i in range(len(Tabuleiro)):
                        print(Tabuleiro[i])

            
        if VitoriaText:
            tela.blit(formatacaoFinalVitoria, (250, 250)) # Adiciona texto de vitoria  
        tela.blit(formatacaoFinalPontuacaoO, (20, 20)) # Adicionando texto da pontuacao na tela
        tela.blit(formatacaoFinalPontuacaoX, (20, 70))
        if VelhaText:
            tela.blit(formatacaoFinalVelha, (250, 250))
        
        pygame.display.update() #funcao para atualizar as mudancas da tela
        if VitoriaText:
            sleep(1)
            VitoriaText = False
            VitoriaX = False #reseta a variavel 
            VitoriaO = False #reseta a variavel 
        if VelhaText:
            sleep(1)
            VelhaText = False
        tela.fill((240, 240, 240)) #define a tela como branca

        #linhas verticais
        pygame.draw.line(tela, (0,0,0), (400, 25), (400, 625), 5)
        pygame.draw.line(tela, (0,0,0), (600, 25), (600, 625), 5)

        #linhas horizontais
        pygame.draw.line(tela, (0,0,0), (200, 225), (800, 225), 5)
        pygame.draw.line(tela, (0,0,0), (200, 425), (800, 425), 5)

         #Botao de voltar
        pygame.draw.rect(tela, (52,152,209), Voltar, border_radius=10)
        pygame.draw.rect(tela,(30,30,30), Voltar, 3, border_radius=10)

        #Botao de resetar
        pygame.draw.rect(tela, (231,76,60), Resetar, border_radius=10)
        pygame.draw.rect(tela,(30,30,30), Resetar, 3, border_radius=10)

        #texto de cada botao
        render7 = fonteSub.render("Reset", True, (255,255,255))
        render6 = fonteSub.render("Voltar", True, (255,255,255))
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
                    pygame.draw.line(tela,(52,152,209),(Desenho_Y+30,Desenho_X+30),(Desenho_Y+170,Desenho_X+170), 10)
                    pygame.draw.line(tela,(52,152,209),(Desenho_Y+170,Desenho_X+30),(Desenho_Y+30,Desenho_X+170), 10)
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
                    pygame.draw.circle(tela,(231,76,60),(Desenho_Y+100,Desenho_X+100),80,6)
        VitoriaListen() #por fim, analisa se houve vencedores na rodada/loop
