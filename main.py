import pygame
import random
import sayac

zaman = sayac.zaman

# Paketleri başlatma
pygame.init()

# Ekranı ayarlama
WIDTH = 1280
HEIGHT = 960
SPEED = 7
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Karakterleri ekleme
monster = pygame.image.load("icons/monster.png")
monster_loc = monster.get_rect()
monster_loc.topleft = (WIDTH/2, HEIGHT/2)
monster_2 = pygame.image.load("icons/monster2.png")
monster_2_loc = monster_2.get_rect()
monster_2_loc.topleft = (50, 50)

# Renkler
WHITE = (255, 255, 255)

# Fps ayarı
FPS = 60
sure = pygame.time.Clock()

# Skor
Score = 0

# Font
FONT = pygame.font.SysFont('consolas', 40)

start = True
while start:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            start = False
    tus = pygame.key.get_pressed()

    if tus[pygame.K_LEFT] and monster_loc.left > 0:
        monster_loc.x -= SPEED

    elif tus[pygame.K_RIGHT] and monster_loc.right < 1280:
        monster_loc.x += SPEED

    elif tus[pygame.K_UP] and monster_loc.top > 40:
        monster_loc.y -= SPEED

    elif tus[pygame.K_DOWN] and monster_loc.bottom < 960:
        monster_loc.y += SPEED
    window.fill((0, 100, 0))
    pygame.draw.rect(window, (255, 0, 0), monster_loc, 1)
    pygame.draw.rect(window, (255, 0, 0), monster_2_loc, 1)
    if monster_loc.colliderect(monster_2_loc):
        monster_2_loc.x = random.randint(20, 1260)
        monster_2_loc.y = random.randint(20, 895)
        Score += 1
        zaman += 5
    if zaman == 0:
        bitti = FONT.render("Süre Doldu. Skor: " + str(Score), True, (255, 0, 0))

    print("Skor: " + str(Score))
    window.blit(monster, monster_loc)
    window.blit(monster_2, monster_2_loc)
    YAZI = FONT.render("Skor: " + str(Score), True, WHITE, (255, 0, 0))
    YAZI_LOC = YAZI.get_rect()
    YAZI_LOC.topleft = (0, 0)
    window.blit(YAZI, YAZI_LOC)
    SAAT = FONT.render("SÜRE: " + str(zaman), True, WHITE, (0, 0, 255))
    SAAT_LOC = SAAT.get_rect()
    SAAT_LOC.topleft = (640, 0)
    window.blit(SAAT, SAAT_LOC)
    pygame.draw.line(window, WHITE, (0, 40), (1280, 40), 5)
    pygame.display.update()
    sure.tick(FPS)

pygame.quit()