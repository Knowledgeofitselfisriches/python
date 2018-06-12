class Bullet:
    damage = 1
    def attack(self,person):
        person.hp = person.hp-Bullet.damage
        print(f'打中了{person.name},还剩{person.hp}')
if __name__ == '__main__':
    from person import Person
    per = Person('老王')
    b = Bullet()
    b.attack(per)
        
        