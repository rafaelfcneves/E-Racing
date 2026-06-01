import pygame

RED_STATS = [
    [(14, 19), (15, 19), (15, 19)],
    [(14, 19), (14, 19), (14, 19)],
    [(14, 19), (14, 18), (14, 18)],
    [(14, 19), (14, 18), (14, 18)],
]

RED_PIXEIS = [
    [(26, 54), (8, 55), (43, 55)],
    [(26, 87), (9, 88), (43, 87)],
    [(25, 120), (8, 121), (42, 121)],
    [(27, 153), (10, 154), (44, 154)],

]

def escalar(stats, i):
    escalado_length = 3*stats[i][0]
    escalado_height = 3*stats[i][1]
    escalados = [escalado_length, escalado_height]
    return escalados

def recortar_sprite(stats, pixeis, i, spritesheet):
    sprite = spritesheet.subsurface(pixeis[i][0], pixeis[i][1], stats[i][0], stats[i][1])
    return sprite

def remover_fundo(sprite, cor):
    sprite.set_colorkey(cor)
    return sprite

def matriz_sprites_trainer(spritesheet):
    spritesheet = pygame.image.load("red_leaf_sprites.png")
    sprites = []
    trainer = []
    for i in range(4):
        s_temporario = []
        t_temporario = []
        for j in range(3):
            sprite = recortar_sprite(RED_STATS[i], RED_PIXEIS[i], j, spritesheet)
            escalados = escalar(RED_STATS[i], j)
            sprite = pygame.transform.scale(sprite, (escalados[0], escalados[1]))
            sprite = remover_fundo(sprite, (255, 127, 39))
            s_temporario.append(sprite)
            t_temporario.append(escalados)
        sprites.append(s_temporario)
        trainer.append(t_temporario)
    return trainer, sprites