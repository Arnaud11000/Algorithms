def left(i):
    return 2*i


def right(i):
    return 2*i + 1


def parent(i):
    return i//2


def max_heapify(a, heap_size, i):
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and a[l] > a[i]:
        largest = l
    
    if r < heap_size and a[r] > a[largest]:
        largest = r 
    
    if largest != i:
        # swap elements
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def build_max_heap(a):
    heap_size = len(a)

    for i in range(heap_size//2, 0, -1):
        max_heapify(a, heap_size, i)


def heap_sort(a):
    build_max_heap(a)

    # len(a) inclut le None
    heap_size = len(a)

    # Dernier véritable élément : len(a) - 1
    for i in range(len(a) - 1, 1, -1):

        # Le maximum a[1] va à sa position définitive
        a[1], a[i] = a[i], a[1]

        # La position i est désormais exclue du heap actif
        heap_size -= 1

        # Réparer le heap à partir de la racine
        max_heapify(a, heap_size, 1)

    return a[1:]

heap_sort([1,7,4,7,3,8,7,6,3,7,8,4,2,1,0,0,6])
