"""MCP server exposing number theory functions and factorization algorithms."""

import fastmcp

from . import algos
from . import number_theory as nt

mcp = fastmcp.FastMCP("mcp-number-theory")


@mcp.tool()
def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b."""
    return nt.gcd(a, b)


@mcp.tool()
def isqrt(n: int) -> int:
    """Compute the integer square root of n."""
    return nt.isqrt(n)


@mcp.tool()
def introot(n: int, r: int = 2) -> int | None:
    """Compute the integer r-th root of n. Returns None if not a perfect r-th power."""
    return nt.introot(n, r)


@mcp.tool()
def invmod(a: int, m: int) -> int:
    """Compute the modular inverse of a modulo m."""
    return nt.invmod(a, m)


@mcp.tool()
def gcdext(a: int, b: int) -> dict[str, int]:
    """Compute the extended GCD of a and b. Returns dict with g, x, y where g = ax + by."""
    result = nt.gcdext(a, b)
    return {"g": result[0], "x": result[1], "y": result[2]}


@mcp.tool()
def is_square(n: int) -> bool:
    """Check if n is a perfect square."""
    return nt.is_square(n)


@mcp.tool()
def is_cube(n: int) -> bool:
    """Check if n is a perfect cube."""
    return nt.is_cube(n)


@mcp.tool()
def next_prime(n: int) -> int:
    """Find the next prime after n."""
    return nt.next_prime(n)


@mcp.tool()
def is_prime(n: int) -> bool:
    """Test if n is prime using probabilistic methods."""
    return nt.is_prime(n)


@mcp.tool()
def fib(n: int) -> int:
    """Compute the n-th Fibonacci number."""
    return nt.fib(n)


@mcp.tool()
def primes(n: int) -> list[int]:
    """Return a list of the first n primes."""
    return nt.primes(n)


@mcp.tool()
def lcm(x: int, y: int) -> int:
    """Compute the least common multiple of x and y."""
    return nt.lcm(x, y)


@mcp.tool()
def invert(a: int, b: int) -> int:
    """Compute the modular inverse of a modulo b using Fermat's little theorem."""
    return nt.invert(a, b)


@mcp.tool()
def powmod(b: int, e: int, m: int) -> int:
    """Compute b^e mod m using modular exponentiation."""
    return nt.powmod(b, e, m)


@mcp.tool()
def ilog2(n: int) -> int:
    """Compute the integer log base 2 of n."""
    return nt.ilog2(n)


@mcp.tool()
def ilog(n: int) -> int:
    """Compute the integer log of n (natural log)."""
    return nt.ilog(n)


@mcp.tool()
def ilog10(n: int) -> int:
    """Compute the integer log base 10 of n."""
    return nt.ilog10(n)


@mcp.tool()
def phi(n: int, factors: list[int]) -> int:
    """Compute Euler's totient function phi(n) given the prime factors of n."""
    return nt.phi(n, factors)


@mcp.tool()
def chinese_remainder(m: list[int], a: list[int]) -> int:
    """Solve the Chinese Remainder Theorem. Given moduli m and remainders a, find x such that x ≡ a[i] (mod m[i])."""
    return nt.chinese_remainder(m, a)


@mcp.tool()
def legendre(a: int, p: int) -> int:
    """Compute the Legendre symbol (a/p)."""
    return nt.legendre(a, p)


@mcp.tool()
def tonelli(n: int, p: int) -> int:
    """Compute the modular square root using Tonelli-Shanks algorithm. Returns x such that x^2 ≡ n (mod p)."""
    return nt.tonelli(n, p)


@mcp.tool()
def p_adic_valuation(n: int, p: int) -> int:
    """Return the exponent of the highest power of p dividing n."""
    return nt.p_adic_valuation(n, p)


@mcp.tool()
def hensel_lift_square(a: int, p: int, k: int) -> int | None:
    """Lift quadratic residue from mod p to mod p^k using Hensel's method."""
    return nt.hensel_lift_square(a, p, k)


@mcp.tool()
def hensel_lift_quadratic(a: int, b: int, c: int, x0: int, p: int, k: int) -> int:
    """Lift root of ax^2 + bx + c ≡ 0 from mod p to mod p^k."""
    return nt.hensel_lift_quadratic(a, b, c, x0, p, k)


@mcp.tool()
def hensel_lift_cubic(a: int, b: int, c: int, d: int, x0: int, p: int, k: int) -> int:
    """Lift root of ax^3 + bx^2 + cx + d ≡ 0 from mod p to mod p^k."""
    return nt.hensel_lift_cubic(a, b, c, d, x0, p, k)


@mcp.tool()
def dlp_bruteforce(g: int, h: int, p: int) -> int | None:
    """Solve discrete logarithm by brute force: find x such that g^x ≡ h (mod p)."""
    return nt.dlp_bruteforce(g, h, p)


@mcp.tool()
def fac(n: int) -> int:
    """Compute the factorial of n."""
    return nt.fac(n)


@mcp.tool()
def lucas(n: int) -> int:
    """Compute the n-th Lucas number."""
    return nt.lucas(n)


@mcp.tool()
def is_lucas(n: int) -> bool:
    """Check if n is a Lucas number."""
    return nt.is_lucas(n)


@mcp.tool()
def find_period(n: int) -> int:
    """Find the period of n in binary representation."""
    return nt.find_period(n)


@mcp.tool()
def trivial_factorization_with_n_phi(n: int, phi: int) -> tuple[int, int] | None:
    """Factor n given phi(n). Returns (p, q) if found, None otherwise."""
    return nt.trivial_factorization_with_n_phi(n, phi)


@mcp.tool()
def brent(n: int) -> int:
    """Factor n using Brent's algorithm (Pollard rho with optimizations). Returns a factor."""
    return algos.brent(n)


@mcp.tool()
def carmichael(n: int) -> list[tuple[int, int]]:
    """Factor n using Carmichael's method. Returns list of factor pairs."""
    return algos.carmichael(n)


@mcp.tool()
def fermat(n: int) -> tuple[int, int]:
    """Factor n using Fermat's factorization method. Returns (p, q)."""
    return algos.fermat(n)


@mcp.tool()
def pollard_rho(n: int) -> int:
    """Factor n using Pollard's rho algorithm. Returns a factor."""
    return algos.pollard_rho(n)


@mcp.tool()
def pollard_P_1(n: int) -> tuple[int, int] | None:
    """Factor n using Pollard's P-1 algorithm. Returns (p, q) if found."""
    return algos.pollard_P_1(n)


@mcp.tool()
def williams_pp1(n: int) -> tuple[int, int] | None:
    """Factor n using Williams' P+1 algorithm. Returns (p, q) if found."""
    return algos.williams_pp1(n)


@mcp.tool()
def shor(n: int) -> tuple[int, int] | None:
    """Factor n using Shor's algorithm (classical part). Returns (p, q) if found."""
    return algos.shor(n)


@mcp.tool()
def SQUFOF(n: int) -> tuple[int, int] | None:
    """Factor n using Shanks' Square Forms Factorization. Returns (p, q) if found."""
    return algos.SQUFOF(n)


@mcp.tool()
def hart(n: int) -> tuple[int, int]:
    """Factor n using Hart's one-line factorization. Returns (p, q)."""
    return algos.hart(n)


@mcp.tool()
def kraitchik(n: int) -> tuple[int, int]:
    """Factor n using Kraitchik factorization. Returns (p, q)."""
    return algos.kraitchik(n)


@mcp.tool()
def lehman(n: int) -> tuple[int, int] | None:
    """Factor n using Lehman's factorization algorithm. Returns (p, q) if found."""
    return algos.lehman(n)


@mcp.tool()
def euler_factorization(n: int) -> tuple[int, int] | None:
    """Factor n using Euler's factorization method. Returns (p, q) if found."""
    return algos.euler(n)


@mcp.tool()
def dixon(n: int) -> tuple[int, int] | None:
    """Factor n using Dixon's factorization method. Returns (p, q) if found."""
    return algos.dixon(n)


@mcp.tool()
def wiener(n: int, e: int) -> tuple[int, int] | None:
    """Attack RSA using Wiener's method given modulus n and public exponent e. Returns (p, q) if vulnerable."""
    return algos.wiener(n, e)


@mcp.tool()
def pollard_strassen(n: int) -> tuple[int, int] | None:
    """Factor n using Pollard-Strassen algorithm. Returns (p, q) if found."""
    return algos.pollard_strassen(n)


@mcp.tool()
def factor_XYXZ(n: int, base: int = 3) -> tuple[int, int] | None:
    """Factor integer of form x^y * x^z. Returns (p, q) if found."""
    return algos.factor_XYXZ(n, base)


@mcp.tool()
def factor_2PN(n: int, p_val: int = 3) -> tuple[int, int] | None:
    """Factor n with P prime > 2. Returns (p, q) if found."""
    return algos.factor_2PN(n, p_val)


@mcp.tool()
def lehmer_machine(n: int) -> tuple[int, int]:
    """Factor n using Lehmer's machine (fermat-based). Returns (p, q)."""
    return algos.lehmer_machine(n)


@mcp.tool()
def repunit_factor(n: int) -> tuple[int, int] | None:
    """Factor n using repunit properties. Returns (p, q) if found."""
    return algos.repunit_factor(n)


@mcp.tool()
def factor_high_and_low_bits_equal(
    n: int, max_middle_bits: int = 24
) -> tuple[int, int] | None:
    """Factor when high and low bits are equal. Returns (p, q) if found."""
    return algos.factor_high_and_low_bits_equal(n, max_middle_bits)


@mcp.tool()
def difference_of_powers_factor(n: int) -> list[int]:
    """Factor using difference of powers method. Returns list of factors."""
    return algos.difference_of_powers_factor(n)


@mcp.tool()
def getpubkeysz(n: int) -> int:
    """Get public key size in bits."""
    return nt.getpubkeysz(n)


@mcp.tool()
def neg_pow(a: int, b: int, n: int) -> int:
    """Calculate a^b mod n when b is negative."""
    return nt.neg_pow(a, b, n)


@mcp.tool()
def contfrac_to_rational(frac: list[int]) -> tuple[int, int]:
    """Convert continued fraction to rational number."""
    return nt.contfrac_to_rational(frac)


@mcp.tool()
def powmod_base_list(base_lst: list[int], exp: int, mod: int) -> list[int]:
    """Compute powmod for a list of bases."""
    return nt.powmod_base_list(base_lst, exp, mod)


@mcp.tool()
def powmod_exp_list(base: int, exp_lst: list[int], mod: int) -> list[int]:
    """Compute powmod for a list of exponents."""
    return nt.powmod_exp_list(base, exp_lst, mod)


@mcp.tool()
def close_factor(n: int, b: int) -> tuple[int, int] | None:
    """Factor n using close factor algorithm. Returns (p, q) if found."""
    return algos.close_factor(n, b)


@mcp.tool()
def inverseinversesqrt2exp(n: int, k: int) -> int:
    """Compute modular inverse square root approximation with k bits."""
    return algos.InverseInverseSqrt2exp(n, k)


# =============================================================================
# Multiplicative Number Theory
# =============================================================================


@mcp.tool()
def jacobi(a: int, n: int) -> int:
    """Compute Jacobi symbol (a/n). Returns -1, 0, or 1."""
    return nt.jacobi(a, n)


@mcp.tool()
def mobius(n: int) -> int:
    """Compute Möbius function. Returns 0 if n has squared prime factor."""
    return nt.mobius(n)


@mcp.tool()
def is_square_free(n: int) -> bool:
    """Check if n is square-free."""
    return nt.is_square_free(n)


@mcp.tool()
def carmichael_lambda(n: int) -> int:
    """Compute Carmichael function (exponent of multiplicative group mod n)."""
    return nt.carmichael_lambda(n)


@mcp.tool()
def prime_factors(n: int) -> list[int]:
    """Return list of distinct prime factors of n."""
    return nt.prime_factors(n)


# =============================================================================
# Divisor Functions
# =============================================================================


@mcp.tool()
def divisors(n: int) -> list[int]:
    """Return all positive divisors of n in ascending order."""
    return nt.divisors(n)


@mcp.tool()
def num_divisors(n: int) -> int:
    """Count number of positive divisors of n (tau function)."""
    return nt.num_divisors(n)


@mcp.tool()
def sum_divisors(n: int) -> int:
    """Compute sum of all positive divisors of n (sigma function)."""
    return nt.sum_divisors(n)


@mcp.tool()
def aliquot_sum(n: int) -> int:
    """Compute sum of proper divisors (excluding n)."""
    return nt.aliquot_sum(n)


# =============================================================================
# Prime Functions
# =============================================================================


@mcp.tool()
def is_sophie_germain(p: int) -> bool:
    """Check if p is a Sophie Germain prime (p and 2p+1 are both prime)."""
    return nt.is_sophie_germain(p)


@mcp.tool()
def is_safe_prime(p: int) -> bool:
    """Check if p is a safe prime (p = 2q + 1 where q is prime)."""
    return nt.is_safe_prime(p)


@mcp.tool()
def prime_counting(x: int) -> int:
    """Count primes <= x."""
    return nt.prime_counting(x)


@mcp.tool()
def nth_prime(n: int) -> int:
    """Return the nth prime (1-indexed)."""
    return nt.nth_prime(n)


@mcp.tool()
def is_prime_power(n: int) -> tuple[int, int] | None:
    """Check if n = p^k for some prime p. Returns (p, k) if true."""
    return nt.is_prime_power(n)


# =============================================================================
# Modular Functions
# =============================================================================


@mcp.tool()
def multiplicative_order(a: int, n: int) -> int | None:
    """Find multiplicative order of a modulo n."""
    return nt.multiplicative_order(a, n)


@mcp.tool()
def discrete_log(g: int, h: int, p: int) -> int | None:
    """Solve g^x ≡ h (mod p) using baby-step giant-step."""
    return nt.discrete_log_baby_step_giant_step(g, h, p)


@mcp.tool()
def kronecker_symbol(a: int, n: int) -> int:
    """Compute Kronecker symbol (a/n)."""
    return nt.kronecker_symbol(a, n)


# =============================================================================
# Rational Approximation
# =============================================================================


@mcp.tool()
def best_rational_approximation(x: float, max_denom: int) -> tuple[int, int]:
    """Find best rational approximation to x with denominator <= max_denom."""
    return nt.best_rational_approximation(x, max_denom)


# =============================================================================
# Primitive Roots
# =============================================================================


@mcp.tool()
def primitive_root(p: int) -> int | None:
    """Find a primitive root modulo p. Returns None if p is not prime."""
    return nt.primitive_root(p)


@mcp.tool()
def is_primitive_root(g: int, p: int) -> bool:
    """Check if g is a primitive root modulo p."""
    return nt.is_primitive_root(g, p)


# =============================================================================
# Lucas-Lehmer Test
# =============================================================================


@mcp.tool()
def lucas_lehmer(p: int) -> bool:
    """Test if 2^p - 1 is a Mersenne prime using Lucas-Lehmer test."""
    return nt.lucas_lehmer(p)


# =============================================================================
# Diophantine Equations
# =============================================================================


@mcp.tool()
def solve_linear_diophantine(a: int, b: int, c: int) -> tuple[int, int] | None:
    """Solve ax + by = c for integers x, y. Returns (x, y) or None if no solution."""
    return nt.solve_linear_diophantine(a, b, c)
