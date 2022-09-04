from display import *
import winsound
def cocktailSort(draw_info,ascending=False):
    a = draw_info.lst 
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i] > a[i + 1] and  ascending) or (a[i] < a[i + 1] and not ascending):
                tmp = abs(a[i] - a[i + 1])
                # winsound.Beep((37 + (tmp%100)), 1)
                a[i], a[i + 1] = a[i + 1], a[i]
                draw_list(draw_info,{i:(0,255,0),i+1:(255,0,0)},True)   
                
                
                swapped = True
                yield True
                
 
        # if nothing moved, then array is sorted.
        if (swapped == False):
            break
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1] and ascending) or (a[i] < a[i + 1] and not ascending):
                
                tmp = abs(a[i] - a[i + 1])
                a[i], a[i + 1] = a[i + 1], a[i]
                winsound.Beep(2500, tmp%10)
                
                draw_list(draw_info,{i:(0,255,0),i+1:(255,0,0)},True)
                swapped = True
                yield True
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1
        
    return a  