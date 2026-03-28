"""Number theory functions implemented using gmpy2 for performance."""

import math
import random
from functools import cache, reduce

try:
    import gmpy2 as gmpy

    gmpy_version = 2
except ImportError:
    import gmpy

    gmpy_version = 1


def list_prod(list_: list) -> int:
    """Compute the product of a list of integers."""
    if not list_:
        return 1
    return reduce(lambda x, y: x * y, list_, 1)


def digit_sum(n: int) -> int:
    """Compute sum of digits efficiently without string conversion."""
    if n == 0:
        return 0
    total = 0
    n = abs(n)
    while n:
        total += n % 10
        n //= 10
    return total


def A007814(n: int) -> int:
    """Return the exponent of the highest power of 2 dividing n."""
    return (~n & n - 1).bit_length()


def A135481(n: int) -> int:
    """Return n with trailing zeros stripped."""
    return ~n & n - 1


def A000265(n: int) -> int:
    """Return n divided by the largest power of 2 that divides n."""
    return n // (A135481(n) + 1)


@cache
def mulmod(a: int, b: int, m: int) -> int:
    """Modular multiplication using recursive doubling."""
    if b == 0:
        return 0
    if b == 1:
        return a % m
    if b & 1 == 0:
        return mulmod((a << 1) % m, b >> 1, m)
    else:
        return (a + mulmod(a, b - 1, m)) % m


def getpubkeysz(n: int) -> int:
    """Get public key size in bits."""
    if (size := n.bit_length()) & 1 != 0:
        size += 1
    return size


def is_pow2(n: int) -> bool:
    """Check if n is a power of 2."""
    return n & (n - 1) == 0


def _gcdext(a: int, b: int) -> list[int]:
    """Extended GCD."""
    if a == 0:
        return [b, 0, 1]
    d, r = divmod(b, a)
    g, y, x = _gcdext(r, a)
    return [g, x - d * y, y]


def _isqrt(n: int) -> int:
    """Integer square root using Newton's method."""
    if n == 0:
        return 0
    x, y = n, (n + 1) >> 1
    while y < x:
        x, y = y, (y + n // y) >> 1
    return x


def _isqrt_rem(n: int) -> tuple[int, int]:
    """Integer square root with remainder."""
    i2 = _isqrt(n)
    return i2, n - (i2 * i2)


def _gcd(a: int, b: int) -> int:
    """Greatest common divisor."""
    while b:
        a, b = b, a % b
    return abs(a)


def _remove(n: int, p: int) -> tuple[int, int]:
    """Remove all factors of p from n, return (result, count)."""
    r = n
    c = 0
    while r % p == 0:
        r //= p
        c += 1
    return r, c


def _introot(n: int, r: int = 2) -> int | None:
    """Integer r-th root."""
    if n < 0:
        return None if r & 1 == 0 else -_introot(-n, r)
    if n < 2:
        return n
    if r == 2:
        return _isqrt(n)
    lower, upper = 0, n
    while lower != upper - 1:
        mid = lower + ((upper - lower) >> 1)
        m = pow(mid, r)
        if m == n:
            return mid
        lower = mid * (m < n) + lower * (m >= n)
        upper = mid * (m > n) + upper * (m <= n)
    return lower


def _iroot(n: int, p: int) -> tuple[int, bool]:
    """Integer root with existence check."""
    b = introot(n, p)
    if b is None:
        return 0, False
    return b, b**p == n


def _introot_gmpy(n: int, r: int = 2) -> int | None:
    """Integer r-th root using gmpy2."""
    if n < 0:
        return None if r & 1 == 0 else -_introot_gmpy(-n, r)
    return gmpy.root(n, r)[0]


def _introot_gmpy2(n: int, r: int = 2) -> int | None:
    """Integer r-th root using gmpy2 iroot."""
    if n < 0:
        return None if r & 1 == 0 else -_introot_gmpy2(-n, r)
    return gmpy.iroot(n, r)[0]


def _invmod(a: int, m: int) -> int:
    """Modular inverse using extended Euclidean algorithm."""
    a, x, u = a % m, 0, 1
    while a:
        x, u, m, a = u, x - (m // a) * u, a, m % a
    return x


def _is_square(n: int) -> bool:
    """Check if n is a perfect square."""
    if (h := n & 0xF) > 9 or h in [2, 3, 5, 6, 7, 8]:
        return False
    t = _isqrt(n)
    return t * t == n


def _powmod_base_list(base_lst: list[int], exp: int, mod: int) -> list[int]:
    """Compute powmod for a list of bases."""
    return [powmod(i, exp, mod) for i in base_lst]


def _powmod_exp_list(base: int, exp_lst: list[int], mod: int) -> list[int]:
    """Compute powmod for a list of exponents."""
    return [powmod(base, i, mod) for i in exp_lst]


def _miller_rabin(n: int, k: int = 40) -> bool:
    """Miller-Rabin primality test."""
    if n == 2:
        return True
    if (n & 1 == 0) or (digit_sum(n) % 9 in [0, 3, 6]):
        return False

    r, s = 0, n - 1
    while s & 1 == 0:
        r += 1
        s >>= 1
    for _ in range(0, k):
        a = random.randrange(2, n - 1)
        if (x := pow(a, s, n)) in [1, n - 1]:
            continue
        j = 0
        while j <= r - 1:
            if (x := pow(x, 2, n)) == (n - 1):
                break
            j += 1
        else:
            return False
    return True


def _fermat_prime_criterion(n: int, b: int = 2) -> bool:
    """Fermat's prime criterion."""
    return pow(b, n - 1, n) == 1


def _is_prime(n: int) -> bool:
    """Primality test using Fermat and Miller-Rabin."""
    if all(
        (
            _fermat_prime_criterion(n),
            _fermat_prime_criterion(n, b=3),
            _fermat_prime_criterion(n, b=5),
        )
    ):
        return _miller_rabin(n)
    return False


def _next_prime(n: int) -> int:
    """Find the next prime after n."""
    while True:
        if _is_prime(n):
            return n
        n += 1


def _erathostenes_sieve(n: int) -> list[int]:
    """Returns a list of primes < n."""
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i :: (i << 1)] = [False] * ((n - i * i - 1) // (i << 1) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def _primes_yield(n: int):
    """Generate first n primes."""
    p = i = 1
    while i <= n:
        p = _next_prime(p)
        yield p
        i += 1


def _primes_yield_gmpy(n: int):
    """Generate first n primes using gmpy2."""
    p = i = 1
    while i <= n:
        p = gmpy.next_prime(p)
        yield p
        i += 1


def _fib(n: int) -> int:
    """n-th Fibonacci number."""
    a, b = 0, 1
    i = 0
    while i <= n:
        a, b = b, a + b
        i += 1
    return a


def ilogb(x: int, b: int) -> int:
    """Greatest integer l such that b**l <= x."""
    log_count = 0
    while x >= b:
        x //= b
        log_count += 1
    return log_count


def _primes_gmpy(n: int) -> list[int]:
    """Return first n primes using gmpy2."""
    return list(_primes_yield_gmpy(n))


def _isqrt_gmpy(n: int) -> int:
    """Integer square root using gmpy2."""
    return int(gmpy.sqrt(n))


def _invert(a: int, b: int) -> int:
    """Modular inverse using Fermat's little theorem."""
    return pow(a, b - 2, b)


def _lcm(x: int, y: int) -> int:
    """Least common multiple."""
    return (x * y) // _gcd(x, y)


def _ilog2_gmpy(n: int) -> int:
    """Integer log2 using gmpy2."""
    return int(gmpy.log2(n))


def _ilog_gmpy(n: int) -> int:
    """Integer log using gmpy2."""
    return int(gmpy.log(n))


def _ilog2_math(n: int) -> int:
    """Integer log2 using math."""
    return int(math.log2(n))


def _ilog_math(n: int) -> int:
    """Integer log using math."""
    return int(math.log(n))


def _ilog10_math(n: int) -> int:
    """Integer log10 using math."""
    return int(math.log10(n))


def _ilog10_gmpy(n: int) -> int:
    """Integer log10 using gmpy2."""
    return int(gmpy.log10(n))


def _mod(a: int, b: int) -> int:
    """Modulo operation."""
    return a % b


def _mul(a: int, b: int) -> int:
    """Multiplication."""
    return a * b


def _is_divisible(n: int, p: int) -> bool:
    """Check if n is divisible by p."""
    return n % p == 0


def _is_congruent(a: int, b: int, m: int) -> bool:
    """Check if a ≡ b (mod m)."""
    return (a - b) % m == 0


def _powmod(b: int, e: int, m: int) -> int:
    """Modular exponentiation (pure Python)."""
    r = 1
    b %= m
    while e > 0:
        r = ((r * b) % m) * (e & 1) + r * ((e + 1) & 1)
        e >>= 1
        b = (b * b) % m
    return r


def _fac(n: int) -> int:
    """Factorial."""
    tmp = 1
    for m in range(n, 1, -1):
        tmp *= m
    return tmp


@cache
def _lucas(n: int) -> int:
    """n-th Lucas number."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return _lucas(n - 1) + _lucas(n - 2)


# Use gmpy2 functions when available
if gmpy_version >= 1:
    gcd = gmpy.gcd
    gcdext = gmpy.gcdext
    is_square = gmpy.is_square
    next_prime = gmpy.next_prime
    is_prime = gmpy.is_prime
    fib = gmpy.fib
    primes = _primes_gmpy
    lcm = gmpy.lcm
    invert = gmpy.invert
    invmod = gmpy.invert
    remove = gmpy.remove
    fac = gmpy.fac
    if gmpy_version == 2:
        iroot = gmpy.iroot
        ilog = _ilog_gmpy
        ilog2 = _ilog2_gmpy
        ilog10 = _ilog10_gmpy
        log = gmpy.log
        log2 = gmpy.log2
        log10 = gmpy.log10
        mod = gmpy.f_mod
        mul = gmpy.mul
        powmod = gmpy.powmod
        isqrt_rem = gmpy.isqrt_rem
        introot = _introot_gmpy2
        is_divisible = gmpy.is_divisible
        is_congruent = gmpy.is_congruent
        fdivmod = gmpy.f_divmod
        lucas = gmpy.lucas
        powmod_base_list = gmpy.powmod_base_list
        powmod_exp_list = gmpy.powmod_exp_list
    else:
        iroot = gmpy.root
        ilog = _ilog_math
        ilog2 = _ilog2_math
        ilog10 = _ilog10_math
        log = math.log
        log2 = math.log2
        log10 = math.log10
        mul = _mul
        mod = _mod
        powmod = pow
        isqrt_rem = gmpy.sqrtrem
        introot = _introot_gmpy
        is_divisible = _is_divisible
        is_congruent = _is_congruent
        fdivmod = gmpy.fdivmod
        lucas = _lucas
        powmod_base_list = _powmod_base_list
        powmod_exp_list = _powmod_exp_list

    isqrt = gmpy.isqrt
else:
    remove = _remove
    iroot = _iroot
    gcd = _gcd
    isqrt = _isqrt
    isqrt_rem = _isqrt_rem
    introot = _introot
    invmod = _invmod
    gcdext = _gcdext
    is_square = _is_square
    next_prime = _next_prime
    fib = _fib
    is_prime = _is_prime
    lcm = _lcm
    invert = _invmod
    powmod = _powmod
    ilog = _ilog_math
    ilog2 = _ilog2_math
    ilog10 = _ilog10_math
    log = math.log
    log2 = math.log2
    log10 = math.log10
    mod = _mod
    mul = _mul
    is_divisible = _is_divisible
    is_congruent = _is_congruent
    fac = _fac
    fdivmod = divmod
    lucas = _lucas
    powmod_base_list = _powmod_base_list
    powmod_exp_list = _powmod_exp_list


def legendre(a: int, p: int) -> int:
    """Legendre symbol (a/p)."""
    return powmod(a, (p - 1) >> 1, p)


def cuberoot(n: int) -> int | None:
    """Integer cube root."""
    return introot(n, 3)


def is_cube(n: int) -> bool:
    """Check if n is a perfect cube."""
    b = False
    if (n % 9) in [0, 1, 8]:
        a, b = iroot(n, 3)
    return b


def neg_pow(a: int, b: int, n: int) -> int:
    """Calculate a^b mod n when b is negative."""
    assert b < 0
    assert gcd(a, n) == 1
    res = int(invert(a, n))
    return powmod(res, b * (-1), n)


def phi(n: int, factors: list[int]) -> int:
    """Euler totient function."""
    if is_prime(n):
        return n - 1
    elif is_square(n):
        i2 = isqrt(n)
        return phi(i2, factors) * i2
    else:
        y = n
        for p in factors:
            if n % p == 0:
                y //= p
                y *= p - 1
                n, _ = remove(n, p)
        if n > 1:
            y //= n
            y *= n - 1
        return y


def chinese_remainder(m: list[int], a: list[int]) -> int:
    """Solve CRT given moduli m and remainders a."""
    S = 0
    N = list_prod(m)
    for mi, ai in zip(m, a):
        Ni = N // mi
        S += Ni * invert(Ni, mi) * ai
    return S % N


def tonelli(n: int, p: int) -> int:
    """Tonelli-Shanks modular square root algorithm."""
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    q >>= (s := A007814(q))
    if s == 1:
        return powmod(n, (p + 1) >> 2, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c, r, t, m = powmod(z, q, p), powmod(n, (q + 1) >> 1, p), powmod(n, q, p), s
    while (t - 1) % p != 0:
        t2 = powmod(t, 2, p)
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = powmod(t2, 2, p)
        b = powmod(c, 1 << (m - i - 1), p)
        r = mulmod(r, b, p)
        c = powmod(b, 2, p)
        t = mulmod(t, c, p)
        m = i
    return r


def dlp_bruteforce(g: int, h: int, p: int) -> int | None:
    """Solve discrete logarithm problem by brute force: find x such that g^x ≡ h (mod p)."""
    for x in range(1, p):
        if h == powmod(g, x, p):
            return x
    return None


def rational_to_contfrac(x: int, y: int) -> list[int]:
    """Convert rational number x/y to continued fraction."""
    a = x // y
    if a * y == x:
        return [a]
    pquotients = rational_to_contfrac(y, x - a * y)
    pquotients.insert(0, a)
    return pquotients


def contfrac_to_rational(frac: list[int]) -> tuple[int, int]:
    """Convert continued fraction to rational number."""
    if len(frac) == 0:
        return (0, 1)
    elif len(frac) == 1:
        return (frac[0], 1)
    else:
        remainder = frac[1:]
        num, denom = contfrac_to_rational(remainder)
        return (frac[0] * num + denom, num)


def convergents_from_contfrac(frac: list[int]) -> list[tuple[int, int]]:
    """Generate convergents from continued fraction."""
    return [contfrac_to_rational(frac[:i]) for i in range(0, len(frac))]


def inv_mod_pow_of_2(factor: int, bit_count: int) -> int:
    """Fast modular inverse for powers of 2."""
    rest = factor & -2
    acc = 1
    for i in range(bit_count):
        acc -= (acc & (1 << i)) * (rest << i)
    mask = (1 << bit_count) - 1
    return acc & mask


def mlucas(v: int, a: int, n: int) -> int:
    """Multiplies along a Lucas sequence modulo n."""
    v1, v2 = v, (v * v - 2) % n
    while a > 0:
        v1, v2 = (
            ((v1 * v1 - 2) % n, (v1 * v2 - v) % n)
            if a & 1 == 0
            else ((v1 * v2 - v) % n, (v2 * v2 - 2) % n)
        )
        a >>= 1
    return v1


def is_lucas(n: int) -> bool:
    """Check if n is a Lucas number (A000032)."""

    def sign(n: int) -> int:
        return 1 if n > 0 else -1

    u1, u2 = 1, 3
    if n <= 2:
        return sign(n) == n
    while n > u2:
        old_u1, u1 = u1, u2
        u2 = old_u1 + u2
    return u2 == n


def find_period(n: int) -> int:
    """Find the period of n in binary representation."""
    shifted = n
    num_bits = n.bit_length()
    mask = (1 << num_bits) - 1
    for period in range(1, num_bits):
        shifted >>= 1
        mask >>= 1
        if ((n ^ shifted) & mask) == 0:
            return period
    return -1


def trivial_factorization_with_n_phi(n: int, phi: int) -> tuple[int, int] | None:
    """Factor n given phi(n)."""
    return trivial_factorization_with_n_b(n, n - phi + 1)


def trivial_factorization_with_n_b(n: int, b: int) -> tuple[int, int] | None:
    """Factor n given b where n = a*b and a <= b."""
    if (b2n4 := (b * b) - (n << 2)) > 0:
        i = isqrt(b2n4)
        p, q = int((b - i) >> 1), int((b + i) >> 1)
        if p * q == n:
            return p, q
    return None
