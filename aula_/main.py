# import pygame

# pygame.init()

# largura = 700
# altura = 450
# tela = pygame.display.set_mode((largura,altura))
# pygame.display.set_caption('Movimentando o quadrado')

# branco = (255,255,255)
# azul = (0,0,255)

# x,y = largura // 2, altura//2
# tamanho = 20
# velocidade = 2.5

# tela.fill((255,0,0))
# pygame.display.flip()
# run = True

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_a]:
#         x -= velocidade
#     if teclas[pygame.K_d]:
#         x += velocidade
#     if teclas[pygame.K_w]:
#         y -= velocidade
#     if teclas[pygame.K_s]:
#         y += velocidade

#     tela.fill(branco)

#     pygame.draw.rect(tela, azul,(x, y, tamanho, tamanho))

#     pygame.display.flip()

#     pygame.time.Clock().tick(30)

# pygame.quit    


import pygame

pygame.init()

h = 800
w = 600

tela = pygame.display.set_mode((h,w))
pygame.display.set_caption('movimento do circulo')

branco =(255,255,255)
azul = (0,0,255)

ball_x = 400 //2
ball_y = 300 //2

velocidade = 5

tela.fill((255,0,0))
pygame.display.flip()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        ball_x -= velocidade
    if teclas[pygame.K_d]:
        ball_x += velocidade
    if teclas[pygame.K_w]:
        ball_y -= velocidade
    if teclas[pygame.K_s]:
        ball_y += velocidade 

    tela.fill(branco)

    pygame.draw.circle(tela, azul,(800,600,30))
    
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit    
