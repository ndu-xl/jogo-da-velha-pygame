def MenuPage():
    import pygame
    from sys import exit

    pygame.init()

    largura = 1000
    altura = 650

    def atualizarNomes(p1= " ", p2 = " "): #Atualizando nomes para um valor atual
        with open("nomes.txt", "w") as arquivo:
            arquivo.write(p1 + "\n")
            arquivo.write(p2)
            print(p1,"o", p2,"x")

    def lendoNomesPvP(): #le os nomes ja salvos
        with open("nomes.txt", "r") as arquivo:
            nome1 = arquivo.readline().strip()
            nome2 = arquivo.readline().strip()
        return nome1, nome2
    tela = pygame.display.set_mode((largura, altura))

    def lendoNomesPvE(): #le os nomes ja salvos
        with open("nomes.txt", "r") as arquivo:
            nome1 = arquivo.readline().strip()
        return nome1
    pygame.display.set_caption("Jogo da Velha")

    #fontes criadas
    fonte = pygame.font.SysFont("arial", 40, True)
    fonteTitulo = pygame.font.SysFont("arial", 70, True)
    fonteSub = pygame.font.SysFont("arial", 24)

    # BOTÕES MENU
    botaoPvP = pygame.Rect(350, 275, 300, 100)
    botaoPvE = pygame.Rect(350, 400, 300, 100)

    modo = "menu" #modo, indica qual tela esta selecionada e q deve ser desenhada no loop

    # INPUT PvP
    NomePlayer1 = pygame.Rect(200, 250, 600, 50)
    NomePlayer2 = pygame.Rect(200, 350, 600, 50)
    Voltar = pygame.Rect(20,500,100,50)
    Play = pygame.Rect(400,500,200,80)

    #Esse state indica que a caixa de texto n esta selecionada para digitar
    NomePlayer1State = False
    NomePlayer2State = False

    NomePlayer1Texto, NomePlayer2Texto = lendoNomesPvP() #Essa parte e usada para q os nomes ja salvos sejam escritos novamente

    #INPUT PvE
    NomePlayer = pygame.Rect(200,300,600,50)

    NomePlayerState = False
    NomePlayerTexto = lendoNomesPvE()
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #  MENU 
            if modo == "menu":

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if botaoPvP.collidepoint(event.pos): #altera o modo para pvp, redesenhando a tela
                        modo = "pvp"

                    elif botaoPvE.collidepoint(event.pos): #altera o modo para pve, redesenhando a tela
                        modo = "pve"

            # PvP INPUT 
            elif modo == "pvp":

                # clique nas caixas
                if (event.type == pygame.MOUSEBUTTONDOWN):

                    if (NomePlayer1.collidepoint(event.pos)): #altera o state para o user digitar e alterar o texto
                        NomePlayer1State = True
                        NomePlayer1Texto = ""
                        NomePlayer2State = False

                    elif (NomePlayer2.collidepoint(event.pos)): #altera o state para o user digitar e alterar o texto
                        NomePlayer2State = True
                        NomePlayer2Texto = ""
                        NomePlayer1State = False

                    elif(Voltar.collidepoint(event.pos)): #retorna para o menu
                        modo = "menu"
                    elif(Play.collidepoint(event.pos)):
                        atualizarNomes(NomePlayer1Texto, NomePlayer2Texto) #retorna pvp, fazendo mudar de tela no arquivo main
                        return "pvp"

                # digitação logica
                if event.type == pygame.KEYDOWN:

                    if NomePlayer1State:

                        if event.key == pygame.K_BACKSPACE:
                            NomePlayer1Texto = NomePlayer1Texto[:-1]
                        else:
                            NomePlayer1Texto += event.unicode
                    elif NomePlayer2State:

                        if event.key == pygame.K_BACKSPACE:
                            NomePlayer2Texto = NomePlayer2Texto[:-1]
                        else:
                            NomePlayer2Texto += event.unicode
                    
            elif modo == "pve":
                
                if (event.type == pygame.MOUSEBUTTONDOWN):

                    if(Voltar.collidepoint(event.pos)): #retorna para o menu
                        modo = "menu"
                    elif(Play.collidepoint(event.pos)): #retorna pve, fazendo mudar de tela no arquivo main
                        atualizarNomes(NomePlayerTexto) 
                        return "pve"
                    elif(NomePlayer.collidepoint(event.pos)):
                        NomePlayerState = True

                #digitacao
                if(event.type == pygame.KEYDOWN):
                    
                    if(NomePlayer):
                        if event.key == pygame.K_BACKSPACE:
                            NomePlayerTexto = NomePlayerTexto[:-1]
                        else:
                            NomePlayerTexto += event.unicode

        # DESENHO DA TELA
        tela.fill((240, 240, 240))

        # MENU
        if modo == "menu":

            #Desenho da tela MENU
            tituloMenu = fonteTitulo.render("Jogo da Velha", True, (40, 40, 40))
            tela.blit(tituloMenu, (270, 90))

            subtitulo = fonteSub.render(
                "Escolha um modo para iniciar",
                True,
                (80, 80, 80)
            )
            tela.blit(subtitulo, (350, 190))

            
            pygame.draw.rect(tela, (52, 152, 219), botaoPvP, border_radius=12)
            pygame.draw.rect(tela, (231, 76, 60), botaoPvE, border_radius=12)

            pygame.draw.rect(tela, (30, 30, 30), botaoPvP, 3, border_radius=12)
            pygame.draw.rect(tela, (30, 30, 30), botaoPvE, 3, border_radius=12)

            textoPvP = fonte.render("PvP", True, (255, 255, 255))
            textoPvE = fonte.render("PvE", True, (255, 255, 255))

            tela.blit(textoPvP, textoPvP.get_rect(center=botaoPvP.center))
            tela.blit(textoPvE, textoPvE.get_rect(center=botaoPvE.center))

        # PVP
        elif modo == "pvp":

            #Desenho da tela pvp
            tituloPvP = fonteTitulo.render("Digite os nomes", True, (0, 0, 0))
            tela.blit(tituloPvP, (230, 90))

            # caixas
            pygame.draw.rect(tela, ((240, 240, 240)), NomePlayer1)
            pygame.draw.rect(tela, (52, 152, 219), NomePlayer1, 3, border_radius=10)

            pygame.draw.rect(tela, ((240, 240, 240)), NomePlayer2)
            pygame.draw.rect(tela, (231, 76, 60), NomePlayer2, 3, border_radius=10)

            pygame.draw.rect(tela, (52, 152, 219), Voltar, border_radius=10)
            pygame.draw.rect(tela,(30,30,30), Voltar, 3, border_radius=10)

            pygame.draw.rect(tela,(60,225,141), Play,border_radius=10)
            pygame.draw.rect(tela, (30,30,30), Play,3, border_radius=10)



            # textos
            render1 = fonteSub.render(NomePlayer1Texto, True, (0, 0, 0))
            render2 = fonteSub.render(NomePlayer2Texto, True, (0, 0, 0))
            render3 = fonteSub.render("Voltar", True, (255,255,255))
            render4 = fonte.render("Play", True, (255,255,255))

            tela.blit(render1, (NomePlayer1.x + 10, NomePlayer1.y + 10))
            tela.blit(render2, (NomePlayer2.x + 10, NomePlayer2.y + 10))
            tela.blit(render3, (Voltar.x +20, Voltar.y + 10))
            tela.blit(render4, (Play.x+60,Play.y+15))

        elif modo == "pve":

            #Desenho da tela pve
            #Titulo
            render5 = fonteTitulo.render("Nome player", True,(0,0,0))
            
            tela.blit(render5,(300,160))

            #Caixas
            pygame.draw.rect(tela, ((240, 240, 240)), NomePlayer)
            pygame.draw.rect(tela, (52, 152, 219), NomePlayer, 3, border_radius=10)

            #Botao de voltar
            pygame.draw.rect(tela, (52, 152, 219), Voltar, border_radius=10)
            pygame.draw.rect(tela,(30,30,30), Voltar, 3, border_radius=10)

            render6 = fonteSub.render("Voltar", True, (255,255,255))
            tela.blit(render6, (Voltar.x +20, Voltar.y + 10))

            #Botao de play
            pygame.draw.rect(tela,(60,225,141), Play,border_radius=10)
            pygame.draw.rect(tela, (30,30,30), Play,3, border_radius=10)

            render4 = fonte.render("Play", True, (255,255,255))
            tela.blit(render4, (Play.x+60,Play.y+15))

            #caixa de input, nome do player
            render7 = fonteSub.render(NomePlayerTexto, True, (0,0,0))
            tela.blit(render7,(NomePlayer.x +10, NomePlayer.y +10))
        pygame.display.update() #atualiza a tela no loop
