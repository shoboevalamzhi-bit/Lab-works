def bubble_sort_with_steps(arr):
    arr = arr.copy()
    n = len(arr)
    
    print(f"Исходный массив: {arr}\n")
    
    for i in range(n - 1):
        print(f"Проход {i + 1}:")
        
        for j in range(n - 1 - i):
            print(f"Сравнение ({arr[j]} {arr[j + 1]}): ", end="")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"{arr[j + 1]} ↔ {arr[j]} -> {arr}")
            else:
                print(f"обмен нет")
        print(f"Результат прохода {i + 1}: {arr}\n")
    print(f"Отсортированный массив: {arr}")

user_input = input("Введите числа через пробел: ")
numbers = [int(x) for x in user_input.split()]
bubble_sort_with_steps(numbers)