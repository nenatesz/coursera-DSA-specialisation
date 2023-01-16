def fibonacci(fibArray, n):
    # if n == 0:
    fibArray.append(0)
    # if n == 1:
    fibArray.append(1)
    for i in range(2, n + 1):
        w = (fibArray[i-1] + fibArray[i-2]) % 10
        #fibArray[i] = (fibArray[i - 1] + fibArray[i - 2]) % 10
        fibArray.append(w) 
    return fibArray


def fibonacci_last_digit(n):
    arr = []
    fib = fibonacci(arr, 60)
    x = n % 60

    return fib[x]

    # if n <= 1:
    #     return n

    # fibArray = []
    # fibArray.append(0)
    # fibArray.append(1)

    # # for _ in range(n - 1):
    # #     previous, current = current, previous + current

    # for i in range(2, n):
    #     w = fibArray[i-1] + fibArray[i-2]
    #     fibArray.append(w) 
    # return fibArray[n-1] 


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))