import sys
sys.path.insert(1,r'E:\python\python\game\venv\Include\decorator')
from singleton import Singleton
from bullet import Bullet
class Clip(object,metaclass=Singleton):
    size = 20
    def __init__(self):
        self.remainder = []
    def save_bullet(self,bullet):
        
        if len( self.remainder)  < self.size:
            self.remainder.append(bullet)
            print(f'保存一颗子弹，弹夹里有{len(self.remainder)}颗子弹')
        else:
            print('弹夹已满！！！')
    def pop_bullet(self):
        if len( self.remainder)  >0:
            bullet = self.remainder.pop()
           
            print(f'弹出一颗子弹，弹夹里有{len(self.remainder)}颗子弹')
            return bullet
        else:
            print('没子弹了')
if __name__ == '__main__':
    # print(sys.path)
    bullet = Bullet()
    bullet1 = Bullet()
    clip = Clip()
    clip.save_bullet(bullet)
    clip.save_bullet(bullet)
    clip.pop_bullet()
    # clip.save_bullet()
    clip = Clip()
    clip.pop_bullet()
 