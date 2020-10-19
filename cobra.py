import pygame
from random import randint

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


pygame.init()

janela = pygame.display.set_mode((600, 600))
titulo = pygame.display.set_caption("SNAKE")


largura = 600
altura = 600
tamanho = 10

relogio = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    janela.blit(texto1, [largura/4, altura/2])


def cobra(CobraXY):
    # desenhar o retangulo na tela, o primeiro argumento é aonde vai ser desenhado
    # o segundo é a cor do objeto
    # entre chaves, vai ser no local onde ira ser criado e seu tamnho de altura e largura
    for XY in CobraXY:
        pygame.draw.rect(janela, black, [XY[0], XY[1], tamanho, tamanho])


def maca(posXMaca, posYMaca):
    pygame.draw.rect(janela, red, [posXMaca, posYMaca, tamanho, tamanho])


def jogo():
    posX = randint(0, (largura - tamanho) / 10) * 10
    posY = randint(0, (altura - tamanho) / 10) * 10
    posXMaca = randint(0, (largura - tamanho) / 10) * 10
    posYMaca = randint(0, (altura - tamanho) / 10) * 10
    velX = 0
    velY = 0
    sair = True
    gameover = False
    # criar uma lista cobra
    CobraXY = []
    # comprimento d acobra
    Cobracomp = 1

    # Laço infinito para o jogo rodar
    while sair:
        while gameover:
            # trocar a cor de fundo
            janela.fill(white)
            # mensagem e cor da fonte para o fim de jogo
            texto("C para continuar, S para sair ", black)
            # uptade da tela
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()
                    if event.key == pygame.K_s:
                        sair = False
                        gameover = False

        # vai pegar o tipo de evento para fechar a janela do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            # movivmentaçao da cobra, se o evento for o pressionar de uma tecla:
            if event.type == pygame.KEYDOWN:
                # se o evento for apertar a tecla esquerda
                if event.key == pygame.K_LEFT and velX != tamanho:
                    velX = -tamanho
                    velY = 0
                    # se o evento for apertar a tecla direita:
                if event.key == pygame.K_RIGHT and velX != -tamanho:
                    velX = tamanho
                    velY = 0
                    # se o evento for apertar a tecla pra cima
                if event.key == pygame.K_UP and velY != tamanho:
                    velX = 0
                    velY = -tamanho
                    # se o evento for apertar a tecla pra baixo
                if event.key == pygame.K_DOWN and velY != -tamanho:
                    velX = 0
                    velY = tamanho

        # preenche o fundo da tela
        janela.fill(white)

        # a posição mais a velocidade do objeto
        posX += velX
        posY += velY

        # cabeça da cobra
        CobraInicio = []
        # colocando os valores de x e y dentro da lista cabeça da cobra
        CobraInicio.append(posX)
        CobraInicio.append(posY)
        # colocando a lista inicio dentro da lista cobra xy
        CobraXY.append(CobraInicio)
        # manter o comprimento da cobra
        if len(CobraXY) > Cobracomp:
            del CobraXY[0]

        # verificar na lista kd bloco da cobra para o gamer over
        if any(bloco == CobraInicio for bloco in CobraXY[:-1]):
            gameover = True

        # chamar a funçao cobra
        cobra(CobraXY)

        # chamar a função maçã
        maca(posXMaca, posYMaca)

        # regra de comer a maçã e aumentar
        if posX == posXMaca and posY == posYMaca:
            posXMaca = randint(0, (largura - tamanho) / 10) * 10
            posYMaca = randint(0, (altura - tamanho) / 10) * 10
            Cobracomp += 1

        # atualização dos frames da tela
        pygame.display.update()

        #  fps do jogo
        relogio.tick(15)

        # REGRA PARA A COBRA PASSAR PARA O OUTRO LADO DA TELA
        # se o objeto chegar na borda da tela
        if posX > largura:
            # retorna a posição a 0
            posX = 0
        if posX < 0:
            posX = largura - tamanho
        if posY > altura:
            posY = 0
        if posY < 0:
            posY = altura - tamanho

        # REGRA PARA O JOGO PARAR QND ATIGINR A BORDA
        # if posX >= largura:
        #     sair = False
        # if posX <= 0:
        #     sair = False
        # if posY > altura:
        #     sair = False
        # if posY < 0:
        #     sair = False

    pygame.quit()


jogo()
