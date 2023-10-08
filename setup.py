import pygame.image

        #ยัดภาพตัวละครล background
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

Knight_sheet = pygame.image.load("assets/images/Knight/sprites/Knight.png").convert_alpha()
Ronin = pygame.image.load("assets/images/Roin/sprites/Ronin.png").convert_alpha()

            #กำหนดให้เริ่มใช้ท่าทางเคลื่อนไหวในช่องไหน
KNIGHT_ANIMATION_STEP = [10, 8, 1, 7, 7, 3, 7]
RONIN_ANIMATION_STEP = [8, 8, 1, 8, 8, 3, 7]

         ## กำหนดระยะห่างตัวละคร
fighter_1 = Fighter(200, 310, Knight_sheet, KNIGHT_ANIMATION_STEP)
fighter_2 = Fighter(700, 310, Ronin_sheet, RONIN_ANIMATION_STEP)
