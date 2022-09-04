from display import *
import winsound
def bubble_sort(draw_info,ascending=False):
    lst = draw_info.lst
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if (lst[j+1] > lst[j] and not ascending) or (lst[j+1] < lst[j] and ascending): 
                tmp = abs(lst[j+1] - lst[j])
                lst[j],lst[j+1] =lst[j+1],lst[j]
                # winsound.Beep(2500, tmp%10)
                draw_list(draw_info,{j:(0,255,0),j+1:(255,0,0)},True)
                yield True
    return lst 