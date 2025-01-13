def square(n):
    return n*n
numbers = [1,2,3,4,5,6]
result = map(square, numbers)
print(list(result))