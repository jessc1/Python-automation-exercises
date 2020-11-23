def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]

numbers = [3,2,0,4]
bubble_sort(numbers)
print(numbers)
