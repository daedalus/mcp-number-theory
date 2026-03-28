"""Tests for factorization algorithms."""


from mcp_number_theory import algos


class TestBrent:
    def test_brent_small(self):
        result = algos.brent(91)
        assert result in [7, 13]


class TestPollardRho:
    def test_pollard_rho_small(self):
        result = algos.pollard_rho(91)
        assert result in [7, 13]


class TestFermat:
    def test_fermat_near_squares(self):
        p, q = algos.fermat(15 * 31)
        assert p * q == 15 * 31


class TestHart:
    def test_hart_small(self):
        p, q = algos.hart(91)
        assert p * q == 91


class TestKraitchik:
    def test_kraitchik_small(self):
        p, q = algos.kraitchik(91)
        assert p * q == 91


class TestSQUFOF:
    def test_squfof_small(self):
        result = algos.SQUFOF(91)
        assert result is not None
        p, q = result
        assert p * q == 91


class TestLehmerMachine:
    def test_lehmer_machine(self):
        p, q = algos.lehmer_machine(15 * 31)
        assert p * q == 15 * 31
