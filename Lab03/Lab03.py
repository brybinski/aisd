


def numbers(n: int) -> None:
    if n == 0:
        print(0)
        return
    print(n)
    return numbers(n-1)


def fib(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)


def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    return number * power(number, n-1)


def reverse(txt: str) -> str:
    if len(txt) == 0:
        return ""
    return txt[len(txt)-1] + reverse(txt[0: len(txt)-1])


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)


def prime(n: int, div=-1) -> bool:
    if n <= 1:
        return False
    if div == 2 or n == 2:
        return True

    sqrt: float = math.sqrt(n)

    if div == -1:
        return prime(n, math.ceil(sqrt))

    if n % div == 0:
        return False

    return prime(n, div-1)


print(prime(4))
