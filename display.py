import numpy
import pygame
import math
import random
pygame.init()

class Display:
    BACKGROUND_COLOR = (255,255,255)
    PAD = 100
    LINE = False
    TOP_PAD  = 15
    # FONT = pygame.font.SysFont('comicsans', 30)
    # LARGE_FONT = pygame.font.SysFont('comicsans', 40)
    GRADIENTS = [
        (160,160,160),
        (192,192,192),
        (128,128,128) 
    ]
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    def __init__(self,width,height,lst):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting visualisation")
        self.set_list(lst)
    
    def set_list(self,lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        self.block_width = round((self.width - self.PAD)/len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD)/(self.max_val - self.min_val)) 
        self.start_x = self.PAD//2

def gen_list(n,mi,ma):
    tmp = []
    for _ in range(n):
        v = random.randint(mi,ma)
        tmp.append(v)
    return tmp
def draw(draw_info,ascending,Line=False):
    draw_info.screen.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()
def draw_list(draw_info,color_position={},clear_bg=False):
    if clear_bg:
        clear_rect = (draw_info.PAD//2, draw_info.TOP_PAD, 
                        draw_info.width - draw_info.PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.screen, draw_info.BACKGROUND_COLOR, clear_rect)
    for i,val in enumerate(draw_info.lst):
        x = draw_info.start_x + i*draw_info.block_width
        y = draw_info.height - (val-draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i%3]
        if i in color_position:
            color = color_position[i]
        if(draw_info.LINE):
            pygame.draw.line(draw_info.screen,color,(x,y),(x,draw_info.height))
        else:
            pygame.draw.rect(draw_info.screen,color,(x,y,draw_info.block_width,draw_info.height))
    if clear_bg:
            pygame.display.update()
        
        
        
        