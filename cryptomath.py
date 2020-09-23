# @method Euclid; update val every time
# no matter with a greater than b or not


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# print(gcd(24, 30))

# print(gcd(409119243, 87780243))


# @refer: Euclid Extend
# @Link: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# @description: ax == 1 (mod m)
# a * Sk + m * Tk = 1(gcd(a,m)) (mod m)
# 1 new 0 old
# @return x(inverse)
def get_mod_inverse(a, module):
    # 整除证明
    m = module
    if gcd(a, m) != 1:
        return None
    r0, s0, t0 = a, 1, 0
    r1, s1, t1 = m, 0, 1
    while r1 != 0:
        # q(uotient)

        # remove dots; r_old > r_new
        q = r0 // r1
        r1, r0 = r0 - q * r1, r1
        s1, s0 = s0 - q * s1, s1
        t1, t0 = t0 - q * t1, t1

    return s0 % m

    # TEST print(f'7 Inverse Mod 26 == {get_mod_inverse(7, 26)}')
