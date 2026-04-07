import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()

branco = (255, 255, 255)

abc = True
while abc:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            abc = False
            
        if event.type == pygame.KEYDOWN:
            l = event.unicode
            print(f"Letra: {l}")

            fonte = pygame.font.SysFont('Arial', 400)

            if event.key == pygame.K_a:
                print("Essa é a letra A")
                screen.fill((255, 0, 0))
                letra = fonte.render('A', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_b:
                print("Essa é a letra B")
                screen.fill((255, 140, 0))
                letra = fonte.render('B', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_c:
                print("Essa é a letra C")
                screen.fill((255, 215, 0))
                letra = fonte.render('C', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_d:
                print("Essa é a letra D")
                screen.fill((255, 255, 0))
                letra = fonte.render('D', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_e:
                print("Essa é a letra E")
                screen.fill((173, 255, 47))
                letra = fonte.render('E', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_f:
                print("Essa é a letra F")
                screen.fill((50, 205, 50))
                letra = fonte.render('F', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_g:
                print("Essa é a letra G")
                screen.fill((0, 128, 0))
                letra = fonte.render('G', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_h:
                print("Essa é a letra H")
                screen.fill((0, 100, 0))
                letra = fonte.render('H', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_i:
                print("Essa é a letra I")
                screen.fill((0, 250, 154))
                letra = fonte.render('I', True, branco)
                screen.blit(letra, (750, 200))

            elif event.key == pygame.K_j:
                print("Essa é a letra J")
                screen.fill((72, 209, 204))
                letra = fonte.render('J', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_k:
                print("Essa é a letra K")
                screen.fill((0, 255, 255))
                letra = fonte.render('K', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_l:
                print("Essa é a letra L")
                screen.fill((70, 130, 180))
                letra = fonte.render('L', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_m:
                print("Essa é a letra M")
                screen.fill((0, 191, 255))
                letra = fonte.render('M', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_n:
                print("Essa é a letra N")
                screen.fill((0, 0, 255))
                letra = fonte.render('N', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_o:
                print("Essa é a letra O")
                screen.fill((131, 111, 255))
                letra = fonte.render('O', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_p:
                print("Essa é a letra P")
                screen.fill((128, 0, 128))
                letra = fonte.render('P', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_q:
                print("Essa é a letra Q")
                screen.fill((139, 0, 139))
                letra = fonte.render('Q', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_r:
                print("Essa é a letra R")
                screen.fill((255, 0, 255))
                letra = fonte.render('R', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_s:
                print("Essa é a letra S")
                screen.fill((255, 20, 147))
                letra = fonte.render('S', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_t:
                print("Essa é a letra T")
                screen.fill((220, 20, 60))
                letra = fonte.render('T', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_u:
                print("Essa é a letra U")
                screen.fill((165, 42, 42))
                letra = fonte.render('U', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_v:
                print("Essa é a letra V")
                screen.fill((250, 128, 114))
                letra = fonte.render('V', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_w:
                print("Essa é a letra W")
                screen.fill((245, 245, 220))
                letra = fonte.render('W', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_x:
                print("Essa é a letra X")
                screen.fill((230, 230, 250))
                letra = fonte.render('X', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_y:
                print("Essa é a letra Y")
                screen.fill((128, 128, 0))
                letra = fonte.render('Y', True, branco)
                screen.blit(letra, (650, 200))

            elif event.key == pygame.K_z:
                print("Essa é a letra Z")
                screen.fill((216, 191, 216))
                letra = fonte.render('Z', True, branco)
                screen.blit(letra, (650, 200))
                
            elif event.key == pygame.K_ESCAPE:
                abc = False

            else:
                screen.fill((0, 0, 0))
                fonte = pygame.font.SysFont('Arial', 70)
                letra = fonte.render('Essa tecla não é uma letra válida!', True, branco)
                screen.blit(letra, (330, 400))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
