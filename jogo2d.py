import pygame
from sys import exit

def display_score():
    current_time  =  int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f'Score: {current_time}', False, 'Gray')
    score_rect = score_surf.get_rect(center=(330, 50))
    display.blit(score_surf,score_rect)


pygame.init()
display = pygame.display.set_mode((677, 375))
pygame.display.set_caption('mario da deep web')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 30)
game_active = True
start_time = 0

ground = pygame.image.load('img/ground.png').convert()
# score_surf = text_font.render('Score: ', False, 'Gray').convert()
# score_rect = score_surf.get_rect(center=(330, 50))


player_surf = pygame.image.load('img/mario.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(50, 348))
player_gravity = 0
player_stand = pygame.image.load('img/gameOver.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (330,180))


inimigo_surf = pygame.image.load('img/inimigo.png').convert_alpha()
inimigo_rect = inimigo_surf.get_rect(bottomright=(730, 347))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20 
        else:
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                inimigo_rect.left = 730
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        display.blit(ground, (0, 0))
        # pygame.draw.rect(display, "#6e98ee", score_rect)
        # pygame.draw.rect(display, '#6e98ee', score_rect, 10)
        # display.blit(score_surf, score_rect)
        display_score()
        inimigo_rect.x -= 4
        if inimigo_rect.right <= 0:
            inimigo_rect.left = 730
        display.blit(inimigo_surf, inimigo_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 347: player_rect.bottom = 347
        display.blit(player_surf, player_rect)

        if inimigo_rect.colliderect(player_rect):
            game_active = False
    else:
        display.fill('#6e98ee')
        display.blit(player_stand,player_stand_rect)

    pygame.display.update()
    clock.tick(30)
