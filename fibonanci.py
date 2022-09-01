def fibonacci(n):
    data = []
    if n == 1:
        data = [0]
    else:
        data = [0,1]
        for i in range(1, n-1):
            data.append(data[i-1] + data[i])
    return data

print(fibonacci(20))