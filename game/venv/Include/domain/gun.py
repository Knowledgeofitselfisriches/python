import sys
from clip import Clip

sys.path.insert(1, r'E:\python\python\game\venv\Include\decorator')
from singleton import Singleton


class Gun(object, metaclass=Singleton):
    clip = None
    
    def unin_clip(self, clip):
        
        if not Gun.clip:
            Gun.clip = clip
            print('装弹夹')
    
    def launch_bullet(self):
        if Gun.clip:
            clip.pop_bullet()
            print('开枪了')
        else:
            print('没有弹夹')


if __name__ == '__main__':
    from bullet import Bullet
    gun = Gun()
    clip = Clip()
    clip.save_bullet(Bullet())
    gun.unin_clip(clip)
    gun.launch_bullet()
