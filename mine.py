import pygame
from fighter import Fighter

pygame.init()

#สร้างหน้าจอ window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set fps
clock = pygame.time.Clock()
FPS = 60

#สี
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

# game varibles
#(นับถอยหลัง)
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores[P1,P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000


# fighter variables
WARRIOP_SIZE = 162
WARRIOP_SCALE = 4
WARRIOP_OFFSET = [72, 56]
WARRIOP_DATA = [WARRIOP_SIZE, WARRIOP_SCALE, WARRIOP_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#ใส่ภาพพื้นหลัง
bg_image = pygame.image.load("assets/background/background.jpg").convert_alpha()

#lood spritesheets
warrio_sheet = pygame.image.load("assets/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/wizard/Sprites/wizard.png").convert_alpha()

#define number of steps in each animation
#(กำหนดจำนวนขั้นตอนในแต่ละภาพเคลื่อนไหว)
WARRIOR_ANIMAION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]


#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 80)

#ฟังก์ชั่นสำหรับวาดข้อความ
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#ฟังก์ชั่นสำหรับวาดพื้นหลัง
def draw_bg():
    scaled_bg  = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

#ฟั่งก์ชั่นสำหรับวาดหลอดเลือด
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))#ตอนตีจะขึ้นเป็นสีแดง
    pygame.draw.rect(screen, YELLOW,(x,y, 400 * ratio, 30))



#สร้างตัวเอามาต่อยกัน
fighter_1 = Fighter(1, 200, 310, False, WARRIOP_DATA, warrio_sheet, WARRIOR_ANIMAION_STEPS)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)



#game loop
run = True
while run:

    clock.tick(FPS)

    #วาดพื้นหลัง
    draw_bg()

    #showe player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    #update countdown
    if intro_count <= 0:
        #move fighters
        # Move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)

    else :
        #display count timer
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_WIDTH / 3)        
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
        

    #update fighters
    fighter_1.update()
    fighter_2.update()


    #วาดตัวต่อยกัน
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()
