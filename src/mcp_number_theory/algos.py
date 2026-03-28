"""Factorization algorithms."""

import sys
from itertools import count
from random import randint

from .number_theory import (
    A000265,
    convergents_from_contfrac,
    cuberoot,
    fdivmod,
    find_period,
    gcd,
    ilogb,
    introot,
    inv_mod_pow_of_2,
    invmod,
    iroot,
    is_congruent,
    is_divisible,
    is_square,
    isqrt,
    isqrt_rem,
    log,
    mlucas,
    next_prime,
    powmod,
    primes,
    rational_to_contfrac,
    trivial_factorization_with_n_phi,
)

sys.setrecursionlimit(100000)


def brent(N: int) -> int | None:
    """Pollard rho with Brent optimizations."""
    if N & 1 == 0:
        return 2
    g = N
    while g == N:
        y, c, m = randint(1, N - 1), randint(1, N - 1), randint(1, N - 1)
        g, r, q = 1, 1, 1
        while g == 1:
            x = y
            i = 0
            while i <= r:
                y = (powmod(y, 2, N) + c) % N
                i += 1
            k = 0
            while k < r and g == 1:
                ys = y
                i = 0
                while i <= min(m, r - k):
                    y = (powmod(y, 2, N) + c) % N
                    q = q * (abs(x - y)) % N
                    i += 1
                g, k = gcd(q, N), k + m
                if N > g > 1:
                    return g
            r <<= 1
        if g == N:
            while True:
                ys = (powmod(ys, 2, N) + c) % N
                g = gcd(abs(x - ys), N)
                if N > g > 1:
                    return g
    return None


def carmichael(N: int) -> list[tuple[int, int]]:
    """Carmichael factorization method."""
    f = N1 = N - 1
    f = A000265(f)
    a = 2
    while a <= N1:
        if powmod(a, f << 1, N) == 1:
            r = powmod(a, f, N)
            p = gcd(r - 1, N)
            q = gcd(r + 1, N)
            if q > p > 1:
                return [(p, q)]
        a = next_prime(a)
    return []


def fermat(n: int) -> tuple[int, int]:
    """Fermat factorization method."""
    if (n - 2) & 3 == 0:
        raise ValueError("n ≡ 2 (mod 4) not supported")
    a, rem = isqrt_rem(n)
    b2 = -rem
    c0 = (a << 1) + 1
    c = c0
    while not is_square(b2):
        b2 += c
        c += 2
    a = (c - 1) >> 1
    b = isqrt(b2)
    return a - b, a + b


def pollard_rho(n: int) -> int:
    """Pollard's rho factorization."""
    d, x, y = 1, 2, 2

    def g(val: int) -> int:
        return powmod(val, 2, n) - 1

    while d == 1:
        x, y = g(x), g(g(y))
        d = gcd(abs(y - x), n)
    return d


def close_factor(n: int, b: int) -> tuple[int, int] | None:
    """Close factor algorithm."""
    phi_approx = n - 2 * isqrt(n) + 1
    look_up: dict[int, int] = {}
    z = 1
    parity = phi_approx & 1
    for i in range(0, b + 1):
        if i & 1 == parity:
            look_up[z] = i
        z <<= 1
        z -= (z >= n) * n

    mu = invmod(powmod(2, phi_approx, n), n)
    fac = powmod(2, b, n)

    for i in range(0, (b * b) + 1):
        if mu in look_up:
            phi = phi_approx + look_up[mu] - (i * b)
            r = trivial_factorization_with_n_phi(n, phi)
            if r is not None:
                return r
        mu = (mu * fac) % n
    return None


def InverseInverseSqrt2exp(n: int, k: int) -> int:
    """Computes an approximation to the modular inverse square root of n with k bits."""
    a = 1
    t = 3
    while t < k:
        t = min(k, (t << 1) - 2)
        a = (a * (3 - (a * a) * n) >> 1) & ((1 << t) - 1)
    return inv_mod_pow_of_2(a, k)


def pollard_P_1(n: int) -> tuple[int, int] | None:
    """Pollard P-1 factorization."""
    logn = log(isqrt(n))
    prime_list = primes(997)

    z: list[int] = []
    for pj in prime_list:
        logp = log(pj)
        z.extend(pj for _ in range(1, int(logn / logp) + 1))

    for pp in prime_list:
        for i in range(len(z)):
            pp = powmod(pp, z[i], n)
            p = gcd(n, pp - 1)
            if n > p > 1:
                return p, n // p
    return None


def williams_pp1(n: int) -> tuple[int, int] | None:
    """Williams P+1 factorization."""
    p, i2 = 2, isqrt(n)
    for v in count(1):
        while True:
            e = ilogb(i2, p)
            if e == 0:
                break
            for _ in range(e):
                v = mlucas(v, p, n)
            g = gcd(v - 2, n)
            if 1 < g < n:
                return g, n // g
            if g == n:
                break
            p = next_prime(p)
    return None


def shor(n: int) -> tuple[int, int] | None:
    """Shor's algorithm (classical part only)."""
    for a in range(2, n):
        if (g := gcd(n, a)) != 1:
            return g, n // g
        for r in range(2, n, 2):
            if powmod(a, r, n) == 1:
                if (ar2 := powmod(a, r >> 1, n)) != -1:
                    g1, g2 = gcd(ar2 - 1, n), gcd(ar2 + 1, n)
                    if (n > g1 > 1) or (n > g2 > 1):
                        p = max(max(min(n, g1), 1), max(min(n, g2), 1))
                        return (p, n // p)
    return None


def SQUFOF(N: int) -> tuple[int, int] | None:
    """Shanks' Square Forms Factorization."""
    multiplier = [
        1,
        3,
        5,
        7,
        11,
        3 * 5,
        3 * 7,
        3 * 11,
        5 * 7,
        5 * 11,
        7 * 11,
        3 * 5 * 7,
        3 * 5 * 11,
        3 * 7 * 11,
        5 * 7 * 11,
        3 * 5 * 7 * 11,
    ]

    if (N - 2) & 3 == 0:
        raise ValueError("n ≡ 2 (mod 4) not supported")

    s = isqrt(N)
    L = isqrt(s << 1) << 1
    B = 3 * L

    for k in range(len(multiplier)):
        D = multiplier[k] * N
        Po = Pprev = P = isqrt(D)
        Qprev = 1
        Q = D - (Po * Po)
        for i in range(2, B + 1):
            b = (Po + P) // Q
            P = b * Q - P
            q = Q
            Q = Qprev + b * (Pprev - P)
            r = isqrt(Q)
            if not (i & 1) and (r * r) == Q:
                break
            Pprev, Qprev = P, q
        b = (Po - P) // r
        Pprev = P = b * r + P
        Qprev = r
        Q = (D - (Pprev * Pprev)) // Qprev
        c1 = True
        while c1:
            b = (Po + P) // Q
            Pprev = P
            P = b * Q - P
            q = Q
            Q = Qprev + b * (Pprev - P)
            Qprev = q
            c1 = P != Pprev
        r = gcd(N, Qprev)
        if 1 < r < N:
            return r, N // r
    return None


def hart(n: int) -> tuple[int, int]:
    """Hart's one line factorization."""
    m = 2
    i = 1
    while not is_square(m):
        s = isqrt(n * i) + 1
        m = pow(s, 2, n)
        i += 1
    t = isqrt(m)
    g = gcd(s - t, n)
    return g, n // g


def kraitchik(n: int) -> tuple[int, int]:
    """Kraitchik factorization."""
    x = isqrt(n)
    while True:
        x2 = x * x
        y2 = x2 - n
        while y2 >= 0:
            if is_square(y2):
                y = isqrt(y2)
                z, w = x + y, x - y
                if z % n != 0 and w % n != 0:
                    return gcd(z, n), gcd(w, n)
            y2 -= n
        x += 1


def lehman(n: int) -> tuple[int, int] | None:
    """Lehman's factorization algorithm."""
    if is_congruent(n, 2, 4):
        raise ValueError("n ≡ 2 (mod 4) not supported")

    for k in range(1, cuberoot(n)):
        nk4 = n * k << 2
        ki4 = isqrt(k) << 2
        ink4 = isqrt(nk4) + 1
        i6 = introot(n, 6)
        ink4i6ki4 = ink4 + (i6 // (ki4)) + 1
        for a in range(ink4, ink4i6ki4):
            b2 = (a * a) - nk4
            if is_square(b2):
                b = isqrt(b2)
                p = gcd(a + b, n)
                q = gcd(a - b, n)
                return p, q
    return None


def euler(n: int) -> tuple[int, int] | None:
    """Euler factorization method."""
    end, a, b, solutionsFound, firstb, lf = isqrt(n), 0, 0, [], -1, 0

    while a < end:
        b, f = isqrt_rem(n - a * a)
        if f == 0 and (a != firstb) and (b != firstb):
            solutionsFound.append([b, a])
            firstb = b
            lf = len(solutionsFound)
            if lf == 2:
                break
        a += 1

    if lf < 2:
        return None

    a = solutionsFound[0][0]
    b = solutionsFound[0][1]
    c = solutionsFound[1][0]
    d = solutionsFound[1][1]

    k = pow(gcd(a - c, d - b), 2)
    h = pow(gcd(a + c, d + b), 2)
    m = pow(gcd(a + c, d - b), 2)
    lev = pow(gcd(a - c, d + b), 2)

    return gcd(k + h, n), gcd(lev + m, n)


def dixon(n: int) -> tuple[int, int] | None:
    """Dixon's factorization method."""
    start, basej2N, base = isqrt(n), [4 % n], [2]
    while True:
        lp = base[-1]
        for i in range(start, n):
            i2N = pow(i, 2, n)
            if i2N == basej2N[-1]:
                p = gcd(i - lp, n)
                if 1 < p < n:
                    return p, n // p
        base.append(next_prime(lp))
        basej2N.append(pow(base[-1], 2, n))


def wiener(n: int, e: int) -> tuple[int, int] | None:
    """Wiener's attack on RSA with small d."""
    convergents = convergents_from_contfrac(rational_to_contfrac(e, n))

    for k, d in convergents:
        if k != 0:
            phi, q = fdivmod((e * d) - 1, k)
            if (phi & 1 == 0) and (q == 0):
                s = n - phi + 1
                discr = (s * s) - (n << 2)
                t = 0
                if discr > 0 and is_square(discr):
                    t = isqrt(discr)
                if (s + t) & 1 == 0:
                    pq = trivial_factorization_with_n_phi(n, phi)
                    if pq is not None:
                        return pq
    return None


def pollard_strassen(n: int) -> tuple[int, int] | None:
    """Pollard-Strassen algorithm."""
    f = []
    c = iroot(n, 4)[0]
    for i in range(c):
        f.append(1)
        jmin = i * c + 1
        jmax = jmin + c - 1
        for j in range(jmin, jmax + 1):
            f[i] = (f[i] * j) % n
            if (g := gcd(f[i], n)) > 1:
                return g, n // g
    return None


def factor_XYXZ(n: int, base: int = 3) -> tuple[int, int] | None:
    """Factor integer of form x^y * x^z."""
    power = 1
    max_power = (int(log(n) / log(base)) + 1) >> 1
    while power <= max_power:
        p = next_prime(base**power)
        if is_divisible(n, p):
            return p, n // p
        power += 1
    return None


def factor_2PN(n: int, P: int = 3) -> tuple[int, int] | None:
    """Factor with P prime > 2."""
    P2N = (P * n) << 1
    A, remainder = isqrt_rem(P2N)
    A += int(remainder != 0)

    c = -(A * A) + A + P2N
    disc = 1 - (c << 2)

    if disc >= 0:
        isqrtdisc = isqrt(disc)

        for x in [(-1 + isqrtdisc) >> 1, (-1 - isqrtdisc) >> 1]:
            if x < 0:
                continue

            p = (A + x) // P
            q = (A - x - 1) >> 1
            if p * q == n:
                return p, q

            p = (A - x - 1) // P
            q = (A + x) >> 1
            if p * q == n:
                return p, q

    return None


def lehmer_machine(n: int) -> tuple[int, int]:
    """Lehmer's machine (fermat-based)."""
    if (n - 2) & 3 == 0:
        raise ValueError("n ≡ 2 (mod 4) not supported")
    y = 1
    while not is_square(n + y * y):
        y += 1
    x = isqrt(n + y * y)
    return x - y, x + y


def factor_high_and_low_bits_equal(
    n: int, max_middle_bits: int = 24
) -> tuple[int, int] | None:
    """Factor when high and low bits are equal."""
    if ((n_size := n.bit_length()) < 6) or (n & 7 != 1):
        return None
    k = (n_size + 1) >> 1
    a = isqrt(n - 1) + 1
    k_shift = 1 << k

    for middle_bits in range(1, max_middle_bits + 1):
        for r in [1, k_shift - 1]:
            s = a
            for i in range(k):
                if ((s ^ r) >> i) & 1:
                    m = min(middle_bits, i)
                    shift_val = 1 << (i - m)
                    for _ in range(1 << m):
                        s += shift_val
                        d = (s * s) - n
                        if is_square(d):
                            d_sqrt = isqrt(d)
                            return (s - d_sqrt, s + d_sqrt)
    return None


def difference_of_powers_factor(n: int) -> list[int]:
    """Factor using difference of powers."""
    F = set()
    for a in range(2, isqrt(n) + 1):
        a_k = a
        for k in range(1, int(log(n) / log(a)) + 1):
            if (1 << k) > n:
                break
            a_k *= a
            if a_k > n:
                break
            for sign in [-1, 1]:
                if (b_k := a_k + sign * n) > 0:
                    b, e = iroot(b_k, k)
                    if e and b > 1:
                        if 1 < (f1 := gcd(a - b, n)) < n:
                            F.add(f1)
                        if 1 < (f2 := gcd(a + b, n)) < n:
                            F.add(f2)
    return sorted(F)


def repunit_factor(n: int) -> tuple[int, int] | None:
    """Factor using repunit properties."""
    z = find_period(n)
    if z == -1:
        return None
    num_bits = n.bit_length()
    k = num_bits // z
    R = (1 << (k * z)) - 1
    R //= (1 << z) - 1
    p = gcd(n, R)
    if p > 1:
        return p, n // p
    return None
