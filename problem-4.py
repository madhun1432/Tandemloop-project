def count_multiples(numbers):
    multiples_count = {}
    for i in range(1, 10):
        count = sum(1 for num in numbers if num % i == 0)
        multiples_count[i] = count
    return multiples_count


input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = count_multiples(input_list)
print(result)