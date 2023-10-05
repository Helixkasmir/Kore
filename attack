#เพิ่มไปที่class fighter
self.attacking = False

#เพิ่มไปที่ def move
self.attack_type = 0

#สามารถทำได้ถ้าไม่ได้attack
if self.attcking == False :
    #ส่วนของplayer 1
    if self.player == 1:
        #ต่อจากjump
        #กำหนดว่าจะใช้ปุ่มไหนattack
        if key[pygame.K_z] or key[pygame.K_x]:
            self.attck()
            #พิจารณาว่าจะใช้การโจมตีอะไร
            if key[pygame.K_z]:
                self.attack_type = 1
            if key[pygame.K_x]:
                self.attack_type = 2

#ส่วนของplayer 2
if self.player == 2:
#ต่อจากjump
#กำหนดว่าจะใช้ปุ่มไหนattack
    if key[pygame.K_k] or key[pygame.K_l]:
        self.attck()
    #พิจารณาว่าจะใช้การโจมตีอะไร
    if key[pygame.K_k]:
        self.attack_type = 1
    if key[pygame.K_l]:
        self.attack_type = 2


#ต่อจากupdate player position
def attack(self, target):
    self.attacking = True
    #ระยะการโจมตี
    attackking_rect = pygame.Rect(self.rect.centerx, self.rect.y,2 * self.rect.width, self.rect.height)
    if attackking_rect.collidedict(target.rect):
        #อันนี้จะเป็นส่วนของเลือด
