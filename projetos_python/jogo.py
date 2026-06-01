import pygame
import red
import mapear

def main():
    pygame.init()

    largura = 800
    altura = 600
    
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Meu jogo")

    jogador = {
        "x": largura//2,
        "y": altura//2,
        "i": 0,
        "passo_contador": 0,
        "velocidade": 2
    }
    
    frame_contador = 0
    frame_atual = 1

    spritesheet = pygame.image.load("red_leaf_sprites.png")
    
    trainer, sprites = red.matriz_sprites_trainer(spritesheet)

    relogio = pygame.time.Clock()

    rodando = True
   
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill((0, 0, 0))

        teclas = pygame.key.get_pressed()
        
        #MOVIMENTAÇÃO:
        jogador["x"], jogador["y"] = coordenadas(jogador, trainer, largura, altura, teclas)
        
        mapear.desenhar_mapa(tela)

        #ANIMAÇÃO:
        sprite, frame_contador, frame_atual, jogador["i"] = animar(teclas, sprites, frame_contador, frame_atual, jogador["i"])
        
        tela.blit(sprite, (jogador["x"], jogador["y"]))
        
        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()

def coordenadas(jogador, trainer, largura, altura, teclas):
    i = jogador["i"]
    if teclas[pygame.K_w]:
        if jogador["y"] >= jogador["velocidade"]:
            jogador["y"] -= jogador["velocidade"]
    if teclas[pygame.K_s]:
        if jogador["y"] <= altura - trainer[i][0][1] - jogador["velocidade"]:    
            jogador["y"] += jogador["velocidade"]
    if teclas[pygame.K_a]:
        if jogador["x"] >= jogador["velocidade"]:
            jogador["x"] -= jogador["velocidade"]
    if teclas[pygame.K_d]:
        if jogador["x"] <= largura - trainer[i][0][0] - jogador["velocidade"]:
            jogador["x"] += jogador["velocidade"]
    return jogador["x"], jogador["y"]

def atualizar_frame(frame_contador, frame_atual):
    frame_contador += 1
    if frame_contador >= 20:
        frame_contador = 0
        if frame_atual == 1:
            frame_atual = 2
        else:
            frame_atual = 1
    return frame_contador, frame_atual

def animar(teclas, sprites, frame_contador, frame_atual, i):
    if teclas[pygame.K_s]:
        i = 0
        frame_contador, frame_atual = atualizar_frame(frame_contador, frame_atual)
        sprite = sprites[i][frame_atual]
    elif teclas[pygame.K_w]:
        i = 1
        frame_contador, frame_atual = atualizar_frame(frame_contador, frame_atual)
        sprite = sprites[i][frame_atual]
    elif teclas[pygame.K_a]:
        i = 2
        frame_contador, frame_atual = atualizar_frame(frame_contador, frame_atual)
        sprite = sprites[i][frame_atual]
    elif teclas[pygame.K_d]:
        i = 3
        frame_contador, frame_atual = atualizar_frame(frame_contador, frame_atual)
        sprite = sprites[i][frame_atual]
    else:
        sprite = sprites[i][0]
    return sprite, frame_contador, frame_atual, i


if __name__ == "__main__":
    main()