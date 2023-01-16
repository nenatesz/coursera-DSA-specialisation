def fibonacci_number(n):
    fibArray = []
    # if n == 0:
    fibArray.append(0)
    # if n == 1:
    fibArray.append(1)
    for i in range(2, n):
        w = fibArray[i-1] + fibArray[i-2]
        fibArray.append(w) 
    return fibArray[n-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n + 1))