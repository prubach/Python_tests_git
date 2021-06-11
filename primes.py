n = 1000000


def is_prime(i):
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            return False
    return True


def run(n=n):
    for i in range(2, n):
        if is_prime(i):
            print(' ' + str(i), end='')


if __name__ == "__main__":
    run(100)