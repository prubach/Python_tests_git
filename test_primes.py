from primes import is_prime

PRIMES = [5, 7, 11, 13, 17, 19]
NON_PRIMES = [4, 8, 9, 15, 20]


def test_primes():
    for p in PRIMES:
        assert is_prime(p)
    for p in NON_PRIMES:
        assert not is_prime(p)
