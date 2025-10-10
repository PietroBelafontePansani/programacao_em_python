import pygame

pygame.init()

largura =  700
altura = 450

tela =  pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Movimentando o quadrado')


branco = 46, 2, 25, 1
azul = (0,0,255)

x,y  = largura // 2, altura//2
tamanho  =  20
velocidade = 5

x_circulo, y_circulo = 150,200


# tela.fill(('red'))
pygame.display.flip()
run =  True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    teclas = pygame.key.get_pressed()      
    if teclas[pygame.K_a]:
          x  -= velocidade
    if teclas[pygame.K_d]:
          x  += velocidade
    if teclas[pygame.K_w]:
          y  -= velocidade
    if teclas[pygame.K_s]:
          y  = y + velocidade  


    # teclas = pygame.key.get_pressed()      
    if teclas[pygame.K_LEFT]:
          x_circulo  -= velocidade
    if teclas[pygame.K_RIGHT]:
          x_circulo  += velocidade
    if teclas[pygame.K_UP]:
          y_circulo  -= velocidade
    if teclas[pygame.K_DOWN]:
          y_circulo  = y + velocidade        

    tela.fill(branco)

    pygame.draw.rect(tela, azul,(x,y, tamanho, tamanho))
    pygame.draw.circle(tela,"red",(x_circulo, y_circulo),30)
    pygame.draw.ellipse(tela, azul,(x_circulo, y_circulo, 150, 70))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()             


