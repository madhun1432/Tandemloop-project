def generate_odd_series(a: int):
    result = [2*i - 1 for i in range(1, a+1)]
    return result

a = int(input("Enter a single integer a: "))
output = generate_odd_series(a)
print(", ".join(map(str, output)))