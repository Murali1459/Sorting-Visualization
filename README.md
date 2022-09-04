
## The Algorithms  

**Bubble Sort** - is one of the simpler sorting algorithms as it repeatedly steps through the list comparing adjacent elements and swapping them in case they are not in ascending order. Worst case performance will be met when the array is entirely reversed so we would get O(n^2) comparisons and swaps. Best case would be if the array would be already sorted and it would amount to O(n) comparisons and O(1) swaps.

**Insertion Sort** - is also a pretty simple sorting algorithm that builds the sorted array one element at a time by removing the probed element and inserting it in the place it needs to be in the final sorted array. It performs well on small lists but it is not efficient on large lists and has much lower performance than more advanced algorithms such as quicksort, heapsort or merge sort. Worst case performance is just like Bubble Sort, having O(n^2) comparisons and swaps when the array is completely reversed and also a best case performance of O(n) comparisons and O(1) swaps.

**Cocktail Sort** - Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always traverses elements from left and moves the largest element to its correct position in the first iteration and second-largest in the second iteration and so on. Cocktail Sort traverses through a given array in both directions alternatively. Cocktail sort does not go through the unnecessary iteration making it efficient for large arrays.Cocktail sorts break down barriers that limit bubble sorts from being efficient enough on large arrays by not allowing them to go through unnecessary iterations on one specific region (or cluster) before moving onto another section of an array.The best-case time complexity of cocktail sort is O(n). Average Case Complexity - It occurs when the array elements are in jumbled order that is not properly ascending and not properly descending. The average case time complexity of cocktail sort is O(n^2).

**Comb Sort** - Comb Sort is mainly an improvement over Bubble Sort. Bubble sort always compares adjacent values. So all inversions are removed one by one. Comb Sort improves on Bubble Sort by using a gap of the size of more than 1. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches the value 1. Thus Comb Sort removes more than one inversion count with one swap and performs better than Bubble Sort.Average case time complexity of the algorithm is Ω(N^2/2^p), where p is the number of increments. The worst-case complexity of this algorithm is O(n^2) and the Best Case complexity is O(nlogn).

**Keyboard Shortcuts**

For ascending order(By default)

    a

For Descending order

    d

For Bubble Sort

    b

For Insertion Sort

    i

For Cocktail Sort

    c

For Comb Sort

    o

To stop Sorting

    s