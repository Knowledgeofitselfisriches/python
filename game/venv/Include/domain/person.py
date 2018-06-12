import clip,gun,clip
class Person:
    def __init__(self,name):
        self.name = name
        self.hp   = 100
    def get_gun(self,gun,clip):
        self.gun = gun
        self.clip = clip
        
        print(f'{self.name} 得到了枪')
    def install_clip(self):
        if self.gun and self.clip:
            self.gun.unin_clip(self.clip)
    def install_bullet(self,bullet):
        if self.clip :
            self.clip.save_bullet(bullet)
    def shoot(self,enemy):
        if self.gun:
            self.gun.launch_bullet()
            
if __name__ == '__main__':
    from  gun import Gun
    from clip import Clip
    from bullet import Bullet
    gun = Gun()
    clip = Clip()
    b1 = Bullet()
    b2 = Bullet()
    b3 = Bullet()
    # clip.save_bullet()
    p = Person('老外')
    p.get_gun(gun,clip)
    p.install_bullet(b1)
    p.install_bullet( b2)
    p.install_bullet( b3)
    p.install_clip()
    # p.shoot()
    
    