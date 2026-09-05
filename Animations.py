import pygame
import time
class animation:
    def __init__(self,framenum,framerate,sheet,height,width):
        self.framenum=framenum
        self.framerate=framerate
        self.time=0
        self.frame=0
        self.sheet=pygame.transform.scale(sheet,(width*framenum,height))
        self.height=height
        self.width=width
    def animate(self):
        surface=pygame.Surface((self.width,self.height), pygame.SRCALPHA)
        surface.blit(self.sheet,(0-self.width*self.frame,0))
        if time.time()-self.time>self.framerate:
            self.time=time.time()
            if self.frame>=self.framenum-1:
                self.frame=0
            else:
                self.frame+=1
        return surface
    def animateonce(self):
        surface=pygame.Surface((self.width,self.height), pygame.SRCALPHA)
        
        if time.time()-self.time>self.framerate:
            self.time=time.time()
            if (self.frame>=self.framenum)==False:
                
                self.frame+=1
        if (self.frame>=self.framenum)==False:
            surface.blit(self.sheet,(0-self.width*self.frame,0))
        return surface