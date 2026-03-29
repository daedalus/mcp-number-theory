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


class TestPAdicValuation:
    def test_p_adic_basic(self):
        assert nt.p_adic_valuation(100, 2) == 2

    def test_p_adic_prime(self):
        assert nt.p_adic_valuation(243, 3) == 5

    def test_p_adic_coprime(self):
        assert nt.p_adic_valuation(30, 7) == 0

    def test_p_adic_negative(self):
        assert nt.p_adic_valuation(-36, 3) == 2

    def test_p_adic_large_power(self):
        assert nt.p_adic_valuation(2**20, 2) == 20

    def test_p_adic_one(self):
        assert nt.p_adic_valuation(1, 5) == 0

    def test_p_adic_powers_of_three(self):
        assert nt.p_adic_valuation(3**7, 3) == 7

    def test_p_adic_invalid_zero(self):
        import pytest

        with pytest.raises(ValueError):
            nt.p_adic_valuation(0, 5)

    def test_p_adic_invalid_prime_zero(self):
        import pytest

        with pytest.raises(ValueError):
            nt.p_adic_valuation(10, 0)


class TestHenselLiftSquare:
    def test_hensel_lift_square_simple(self):
        result = nt.hensel_lift_square(2, 7, 2)
        assert pow(result, 2, 49) == 2

    def test_hensel_lift_square_high_power(self):
        result = nt.hensel_lift_square(4, 5, 4)
        assert pow(result, 2, 625) == 4

    def test_hensel_lift_square_non_residue(self):
        assert nt.hensel_lift_square(3, 7, 3) is None

    def test_hensel_lift_square_k1(self):
        result = nt.hensel_lift_square(2, 7, 1)
        assert result == 3 or result == 4

    def test_hensel_lift_square_larger_prime(self):
        result = nt.hensel_lift_square(3, 13, 3)
        assert pow(result, 2, 2197) == 3

    def test_hensel_lift_square_high_power_large(self):
        result = nt.hensel_lift_square(3, 13, 5)
        assert pow(result, 2, 371293) == 3

    def test_hensel_lift_square_both_roots(self):
        r1 = nt.hensel_lift_square(2, 7, 3)
        r2 = (7**3 - r1) % (7**3)
        assert pow(r1, 2, 343) == 2
        assert pow(r2, 2, 343) == 2


class TestHenselLift:
    def test_hensel_lift_polynomial(self):
        def f(x: int) -> int:
            return x * x - 2

        def df(x: int) -> int:
            return 2 * x

        result = nt.hensel_lift(f, df, 3, 7, 3)
        assert pow(result, 2, 343) == 2

    def test_hensel_lift_cubic(self):
        def f(x: int) -> int:
            return x**3 - 2

        def df(x: int) -> int:
            return 3 * x**2

        result = nt.hensel_lift(f, df, 3, 5, 2)
        assert pow(result, 3, 25) == 2

    def test_hensel_lift_k1(self):
        def f(x: int) -> int:
            return x * x - 3

        def df(x: int) -> int:
            return 2 * x

        result = nt.hensel_lift(f, df, 5, 11, 1)
        assert result == 5

    def test_hensel_lift_quartic(self):
        def f(x: int) -> int:
            return x**4 - 2

        def df(x: int) -> int:
            return 4 * x**3

        result = nt.hensel_lift(f, df, 2, 7, 2)
        assert pow(result, 4, 49) == 2

    def test_hensel_lift_linear(self):
        def f(x: int) -> int:
            return 3 * x - 5

        def df(_x: int) -> int:
            return 3

        result = nt.hensel_lift(f, df, 4, 11, 3)
        assert (3 * result - 5) % (11**3) == 0

    def test_hensel_lift_invalid_derivative(self):
        import pytest

        def f(x: int) -> int:
            return x * x - 2

        def df(x: int) -> int:
            return 2 * x

        with pytest.raises(ValueError):
            nt.hensel_lift(f, df, 0, 5, 3)


class TestHenselLiftQuadratic:
    def test_hensel_lift_quadratic_simple(self):
        result = nt.hensel_lift_quadratic(1, 0, -2, 3, 7, 3)
        assert pow(result, 2, 343) == 2

    def test_hensel_lift_quadratic_x2_plus_1(self):
        result = nt.hensel_lift_quadratic(1, 0, -5, 4, 11, 2)
        assert pow(result, 2, 121) == 5

    def test_hensel_lift_quadratic_k1(self):
        result = nt.hensel_lift_quadratic(1, 0, -3, 5, 11, 1)
        assert result == 5

    def test_hensel_lift_quadratic_invalid_derivative(self):
        import pytest

        with pytest.raises(ValueError):
            nt.hensel_lift_quadratic(1, 0, -2, 0, 5, 3)


class TestHenselLiftCubic:
    def test_hensel_lift_cubic_simple(self):
        result = nt.hensel_lift_cubic(1, 0, 0, -2, 3, 5, 2)
        assert pow(result, 3, 25) == 2

    def test_hensel_lift_cubic_x3_minus_2(self):
        result = nt.hensel_lift_cubic(1, 0, 0, -2, 3, 5, 2)
        assert pow(result, 3, 25) == 2

    def test_hensel_lift_cubic_k1(self):
        result = nt.hensel_lift_cubic(1, 0, 0, -2, 3, 5, 1)
        assert result == 3

    def test_hensel_lift_cubic_invalid_derivative(self):
        import pytest

        with pytest.raises(ValueError):
            nt.hensel_lift_cubic(1, 0, 0, -2, 0, 5, 3)


class TestPrimitiveRoot:
    def test_primitive_root_3(self):
        result = nt.primitive_root(3)
        assert result == 2

    def test_primitive_root_5(self):
        result = nt.primitive_root(5)
        assert result == 2 or result == 3

    def test_primitive_root_7(self):
        result = nt.primitive_root(7)
        assert result == 3

    def test_primitive_root_composite(self):
        assert nt.primitive_root(8) is None

    def test_is_primitive_root(self):
        assert nt.is_primitive_root(2, 5) is True
        assert nt.is_primitive_root(3, 5) is True
        assert nt.is_primitive_root(4, 5) is False

    def test_is_primitive_root_composite(self):
        assert nt.is_primitive_root(2, 8) is False


class TestLucasLehmer:
    def test_lucas_lehmer_2(self):
        assert nt.lucas_lehmer(2) is True

    def test_lucas_lehmer_3(self):
        assert nt.lucas_lehmer(3) is True

    def test_lucas_lehmer_5(self):
        assert nt.lucas_lehmer(5) is True

    def test_lucas_lehmer_7(self):
        assert nt.lucas_lehmer(7) is True

    def test_lucas_lehmer_11(self):
        assert nt.lucas_lehmer(11) is False

    def test_lucas_lehmer_composite(self):
        assert nt.lucas_lehmer(15) is False


class TestSolveLinearDiophantine:
    def test_simple_solution(self):
        result = nt.solve_linear_diophantine(2, 3, 5)
        assert result is not None
        x, y = result
        assert 2 * x + 3 * y == 5

    def test_no_solution(self):
        assert nt.solve_linear_diophantine(2, 4, 5) is None

    def test_zero_a(self):
        result = nt.solve_linear_diophantine(0, 3, 6)
        assert result == (0, 2)

    def test_zero_b(self):
        result = nt.solve_linear_diophantine(4, 0, 8)
        assert result == (2, 0)

    def test_both_zero_c(self):
        result = nt.solve_linear_diophantine(0, 0, 0)
        assert result == (0, 0)

    def test_both_zero_non_zero_c(self):
        assert nt.solve_linear_diophantine(0, 0, 5) is None

    def test_gcd_case(self):
        result = nt.solve_linear_diophantine(12, 18, 30)
        assert result is not None
        x, y = result
        assert 12 * x + 18 * y == 30
