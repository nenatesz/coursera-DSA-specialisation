#  if b !== 0 find gcd(b, a')
def gcd(a, b):
    #current_gcd = 1
    if b == 0:
        return a
    a_prime = a % b
    ecludian_gcd = gcd(b, a_prime)
    return ecludian_gcd

    # for d in range(2, min(a, b) + 1):
    #     if a % d == 0 and b % d == 0:
    #         if d > current_gcd:
    #             current_gcd = d

    # return current_gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))