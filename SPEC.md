# SPEC.md — mcp-number-theory

## Purpose
An MCP server that exposes number theory functions and factorization algorithms from RsaCtfTool, allowing LLMs to perform mathematical operations like primality testing, integer factorization, modular arithmetic, and various cryptographic math operations.

## Scope
- **In scope**: All pure number theory functions from `number_theory.py` and factorization algorithms from `algos.py`
- **Not in scope**: RSA attacks that require key files or network access (those remain in RsaCtfTool)

## Public API / Interface

### MCP Tools

#### Number Theory Functions
- `gcd(a, b)` - Greatest common divisor
- `isqrt(n)` - Integer square root
- `introot(n, r)` - Integer r-th root
- `invmod(a, m)` - Modular inverse
- `gcdext(a, b)` - Extended GCD
- `is_square(n)` - Check if perfect square
- `is_cube(n)` - Check if perfect cube
- `next_prime(n)` - Next prime after n
- `is_prime(n)` - Primality test
- `fib(n)` - n-th Fibonacci number
- `primes(n)` - List of first n primes
- `lcm(x, y)` - Least common multiple
- `invert(a, b)` - Modular inverse
- `powmod(b, e, m)` - Modular exponentiation
- `ilog2(n)`, `ilog(n)`, `ilog10(n)` - Integer logarithms
- `phi(n, factors)` - Euler totient function
- `chinese_remainder(m, a)` - CRT solver
- `legendre(a, p)` - Legendre symbol
- `tonelli(n, p)` - Tonelli-Shanks sqrt
- `p_adic_valuation(n, p)` - p-adic valuation (exponent of p dividing n)
- `hensel_lift_square(a, p, k)` - Lift square root from mod p to mod p^k
- `dlp_bruteforce(g, h, p)` - Discrete log brute force
- `fac(n)` - Factorial
- `lucas(n)` - Lucas number
- `is_lucas(n)` - Check if Lucas number
- `find_period(n)` - Find period
- `trivial_factorization_with_n_phi(n, phi)` - Factor given phi

#### Factorization Algorithms
- `brent(n)` - Brent's factorization
- `carmichael(n)` - Carmichael factorization
- `fermat(n)` - Fermat factorization
- `pollard_rho(n)` - Pollard's rho
- `pollard_P_1(n)` - Pollard P-1
- `williams_pp1(n)` - Williams P+1
- `shor(n)` - Shor's algorithm (classical part)
- `SQUFOF(n)` - Square Forms Factorization
- `hart(n)` - Hart's one-line factorization
- `kraitchik(n)` - Kraitchik factorization
- `lehman(n)` - Lehman factorization
- `euler(n)` - Euler factorization
- `dixon(n)` - Dixon factorization
- `wiener(n, e)` - Wiener's attack
- `pollard_strassen(n)` - Pollard-Strassen
- `factor_XYXZ(n, base)` - Factor x^y*x^z form
- `factor_2PN(n, P)` - Factor with P prime

## Edge Cases
- Handle 0 and 1 in prime-related functions
- Handle negative numbers gracefully
- Handle non-integer inputs
- Handle very large integers
- Handle modular inverse when inverse doesn't exist (gcd != 1)

## Performance & Constraints
- Use gmpy2 when available for performance
- Fall back to pure Python implementations
- Factorization algorithms may be slow for large inputs

## MCP Configuration
- Transport: stdio
- Package: fastmcp
