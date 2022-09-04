from display import *
def getNextGap(gap):
     
    # Shrink gap by Shrink factor
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
def comb_sort(draw_info,ascending=False):
    a = draw_info.lst 
    n = len(a)
    # Initialize gap
    gap = n
    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True
    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap !=1 or swapped == 1:
        # Find next gap
        gap = getNextGap(gap)
        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False
        for i in range(0, n-gap):
            if (a[i] > a[i + gap] and ascending) or (a[i] < a[i + gap] and not ascending):
                a[i], a[i + gap]=a[i + gap], a[i]
                draw_list(draw_info,{i:(0,255,0),i+1:(255,0,0)},True)
                swapped = True
                yield True
    return a