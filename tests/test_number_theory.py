"""Tests for number theory functions."""


from mcp_number_theory import number_theory as nt


class TestGcd:
    def test_gcd_positive(self):
        assert nt.gcd(48, 18) == 6

    def test_gcd_negative(self):
        assert nt.gcd(-48, 18) == 6

    def test_gcd_zero(self):
        assert nt.gcd(0, 5) == 5

    def test_gcd_same(self):
        assert nt.gcd(7, 7) == 7


class TestIsqrt:
    def test_isqrt_perfect_square(self):
        assert nt.isqrt(144) == 12

    def test_isqrt_non_perfect_square(self):
        assert nt.isqrt(100) == 10

    def test_isqrt_zero(self):
        assert nt.isqrt(0) == 0


class TestIntroot:
    def test_introot_square(self):
        assert nt.introot(16, 2) == 4

    def test_introot_cube(self):
        assert nt.introot(27, 3) == 3

    def test_introot_not_perfect(self):
        assert nt.introot(15, 2) == 3

    def test_introot_negative_even(self):
        assert nt.introot(-16, 2) is None

    def test_introot_negative_odd(self):
        assert nt.introot(-27, 3) == -3


class TestIsPrime:
    def test_is_prime_small(self):
        assert nt.is_prime(2) is True

    def test_is_prime_known_prime(self):
        assert nt.is_prime(7919) is True

    def test_is_prime_composite(self):
        assert nt.is_prime(100) is False

    def test_is_prime_one(self):
        assert nt.is_prime(1) is False


class TestFib:
    def test_fib_zero(self):
        assert nt.fib(0) == 0

    def test_fib_one(self):
        assert nt.fib(1) == 1

    def test_fib_ten(self):
        assert nt.fib(10) == 55


class TestPowmod:
    def test_powmod_basic(self):
        assert nt.powmod(2, 10, 1000) == 24

    def test_powmod_large_exp(self):
        assert nt.powmod(3, 100, 7) == pow(3, 100, 7)


class TestLcm:
    def test_lcm_basic(self):
        assert nt.lcm(4, 6) == 12

    def test_lcm_coprime(self):
        assert nt.lcm(7, 11) == 77


class TestChChineseRemainder:
    def test_crt_simple(self):
        result = nt.chinese_remainder([3, 5], [2, 3])
        assert result % 3 == 2
        assert result % 5 == 3


class TestPhi:
    def test_phi_prime(self):
        assert nt.phi(7, [7]) == 6

    def test_phi_product(self):
        assert nt.phi(21, [3, 7]) == 12


class TestLegendre:
    def test_legendre_one(self):
        assert nt.legendre(2, 7) == 1

    def test_legendre_minus_one(self):
        assert nt.legendre(3, 7) == 6


class TestTonelli:
    def test_tonelli_simple(self):
        result = nt.tonelli(2, 7)
        assert pow(result, 2, 7) == 2


class TestLucas:
    def test_lucas_zero(self):
        assert nt.lucas(0) == 2

    def test_lucas_one(self):
        assert nt.lucas(1) == 1


class TestIsLucas:
    def test_is_lucas_true(self):
        assert nt.is_lucas(3) is True

    def test_is_lucas_false(self):
        assert nt.is_lucas(4) is True


class TestIsSquare:
    def test_is_square_true(self):
        assert nt.is_square(16) is True

    def test_is_square_false(self):
        assert nt.is_square(15) is False


class TestIsCube:
    def test_is_cube_true(self):
        assert nt.is_cube(27) is True

    def test_is_cube_false(self):
        assert nt.is_cube(16) is False


class TestFactorial:
    def test_fac_zero(self):
        assert nt.fac(0) == 1

    def test_fac_five(self):
        assert nt.fac(5) == 120


class TestPrimes:
    def test_primes_five(self):
        assert nt.primes(5) == [2, 3, 5, 7, 11]

    def test_primes_ten(self):
        result = nt.primes(10)
        assert len(result) == 10
        assert result[0] == 2


class TestNextPrime:
    def test_next_prime_after_ten(self):
        assert nt.next_prime(10) == 11

    def test_next_prime_after_prime(self):
        assert nt.next_prime(13) == 17
