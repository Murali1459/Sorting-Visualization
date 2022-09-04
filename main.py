import pygame 
from display import *
import time
from Algorithms.bubble_sort import bubble_sort
from Algorithms.insertion_sort import insertion_sort
from Algorithms.cocktailshaker_sort import cocktailSort
from Algorithms.comb_sort import comb_sort

if __name__ == "__main__":
    clock = pygame.time.Clock()
    arr_size = 100
    min_val = 0
    max_val = 500
    lst = gen_list(arr_size,min_val,max_val)
    draw_info = Display(800,600,lst)
    done = True 
    sorting = False
    Line  = False
    sorting_algorithm_generator = None
    ascending = True
    while done:
        clock.tick(60)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info,ascending,Line=draw_info.LINE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r and not sorting:
                lst = gen_list(arr_size,min_val,max_val)
                draw_info.set_list(lst)
            elif event.key == pygame.K_b and not sorting:
                sorting = True
                sorting_algorithm_generator = bubble_sort(draw_info,ascending)
            elif event.key == pygame.K_i and not sorting:
                sorting = True
                sorting_algorithm_generator = insertion_sort(draw_info,ascending)
            elif event.key == pygame.K_c and not sorting:
                sorting = True
                sorting_algorithm_generator = cocktailSort(draw_info,ascending)
            elif event.key == pygame.K_o and not sorting:
                sorting = True
                sorting_algorithm_generator = comb_sort(draw_info,ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_l and not sorting:
                draw_info.LINE  = True
            elif event.key == pygame.K_p and not sorting:
                draw_info.LINE  = False
            elif event.key == pygame.K_s and sorting:
                sorting = False
            pygame.display.update()