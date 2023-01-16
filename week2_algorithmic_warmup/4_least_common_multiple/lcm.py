# def lcm(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     assert False


# if __name__ == '__main__':
#     a, b = map(int, input().split())
#     print(lcm(a, b))

def gcd(a, b):
    #current_gcd = 1
    if b == 0:
        return a
    a_prime = a % b
    ecludian_gcd = gcd(b, a_prime)
    return ecludian_gcd

def lcm(a, b):
    lcm = (a // gcd(a, b)) * b
    return lcm


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))