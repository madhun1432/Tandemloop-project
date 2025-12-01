def generate_series(a: int):
    count = a if a % 2 != 0 else a - 1
    result = [2*i - 1 for i in range(1, count + 1)]
    return result

a = int(input("Enter a single integer a: "))
output = generate_series(a)
print(", ".join(map(str, output)))