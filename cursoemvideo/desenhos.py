import pygame

pygame.init()

# Configuração da tela
size = (700, 500)
screen = pygame.display.set_mode(size)

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Loop principal
done = False
clock = pygame.time.Clock()

while not done:
    # Lógica do jogo
    # ...

    # Limpa a tela
    screen.fill(WHITE)

    # Desenha algo na tela
    # ...

    # Atualiza a tela
    pygame.display.flip()

    # Espera um pouco para manter uma taxa constante de frames
    clock.tick(60)

# Finaliza o pygame
pygame.quit()
